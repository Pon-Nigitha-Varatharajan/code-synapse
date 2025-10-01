#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FP-Growth with optional threshold optimization
"""

from collections import Counter
from itertools import combinations
import itertools

# ------------------------------
# FP-Growth Core
# ------------------------------
class FPNode:
    def __init__(self, item, count, parent):
        self.item = item
        self.count = count
        self.parent = parent
        self.children = {}
        self.link = None

    def increment(self, count):
        self.count += count

class FPTree:
    def __init__(self, transactions, min_support):
        self.min_support = min_support
        self.frequent_items = self.find_frequent_items(transactions)
        self.headers = {}
        self.root = self.build_tree(transactions)

    def find_frequent_items(self, transactions):
        counts = Counter()
        for trans in transactions:
            counts.update(trans)
        return {item: cnt for item, cnt in counts.items() if cnt >= self.min_support}

    def build_tree(self, transactions):
        root = FPNode(None, 1, None)
        for trans in transactions:
            ordered = [i for i in sorted(trans, key=lambda x: self.frequent_items.get(x, 0), reverse=True)
                       if i in self.frequent_items]
            self.insert_tree(ordered, root)
        return root

    def insert_tree(self, items, node):
        if not items:
            return
        first = items[0]
        if first in node.children:
            node.children[first].increment(1)
        else:
            child = FPNode(first, 1, node)
            node.children[first] = child
            if first not in self.headers:
                self.headers[first] = child
            else:
                current = self.headers[first]
                while current.link:
                    current = current.link
                current.link = child
        self.insert_tree(items[1:], node.children[first])

def ascend_fpnode(node):
    path = []
    while node and node.parent and node.parent.item is not None:
        node = node.parent
        path.append(node.item)
    return path

def find_prefix_paths(base_item, node):
    cond_pats = []
    while node:
        prefix_path = ascend_fpnode(node)
        if prefix_path:
            cond_pats.append(prefix_path)
        node = node.link
    return cond_pats

def mine_tree(tree, min_support, prefix, freq_itemsets):
    sorted_items = sorted(tree.frequent_items.items(), key=lambda x: x[1])
    for base_item, count in sorted_items:
        new_freq_set = prefix.copy()
        new_freq_set.add(base_item)
        freq_itemsets[frozenset(new_freq_set)] = count
        cond_pats = find_prefix_paths(base_item, tree.headers[base_item])
        cond_tree = FPTree(cond_pats, min_support)
        if cond_tree.frequent_items:
            mine_tree(cond_tree, min_support, new_freq_set, freq_itemsets)

def fp_growth(transactions, min_support_ratio):
    min_support = max(1, int(min_support_ratio * len(transactions)))
    tree = FPTree(transactions, min_support)
    freq_itemsets = {}
    mine_tree(tree, min_support, set(), freq_itemsets)
    return {itemset: count / len(transactions) for itemset, count in freq_itemsets.items()}

# ------------------------------
# Rule Generation
# ------------------------------
def get_support(itemset, baskets):
    return sum(1 for basket in baskets if set(itemset).issubset(basket)) / len(baskets)

def generate_rules(freq_itemsets, baskets, min_confidence, min_lift):
    rules = []
    for itemset, support in freq_itemsets.items():
        if len(itemset) < 2:
            continue
        for i in range(1, len(itemset)):
            for lhs in combinations(itemset, i):
                lhs_set = frozenset(lhs)
                rhs_set = itemset - lhs_set
                lhs_support = freq_itemsets.get(lhs_set, get_support(lhs_set, baskets))
                rhs_support = freq_itemsets.get(rhs_set, get_support(rhs_set, baskets))
                confidence = support / lhs_support if lhs_support > 0 else 0
                lift = confidence / rhs_support if rhs_support > 0 else 0
                if confidence >= min_confidence and lift >= min_lift:
                    rules.append({
                        "if": list(lhs_set),
                        "then": list(rhs_set),
                        "support": round(support, 4),
                        "confidence": round(confidence, 4),
                        "lift": round(lift, 4)
                    })
    return rules

# ------------------------------
# Run Single FP-Growth
# ------------------------------
def run_fp_growth(baskets, min_support, min_confidence, min_lift):
    freq_itemsets = fp_growth(baskets, min_support)
    return generate_rules(freq_itemsets, baskets, min_confidence, min_lift)

# ------------------------------
# Evaluate Rules
# ------------------------------
def evaluate_rules(rules, test_baskets):
    covered = 0
    total_confidence = 0
    total_lift = 0
    for basket in test_baskets:
        for rule in rules:
            if set(rule['if']).issubset(basket):
                covered += 1
                total_confidence += rule['confidence']
                total_lift += rule['lift']
                break
    coverage = covered / len(test_baskets) if len(test_baskets) > 0 else 0
    avg_confidence = total_confidence / covered if covered > 0 else 0
    avg_lift = total_lift / covered if covered > 0 else 0
    return coverage, avg_confidence, avg_lift

# ------------------------------
# Grid Search for Optimal Thresholds
# ------------------------------
def find_optimal_thresholds(train_baskets, test_baskets,
                            support_values=[0.01,0.02,0.03,0.05],
                            confidence_values=[0.3,0.4,0.5,0.6],
                            lift_values=[0.5,1.0,1.2,1.5]):
    best_score = -1
    best_params = None
    best_rules = []

    for s, c, l in itertools.product(support_values, confidence_values, lift_values):
        rules = run_fp_growth(train_baskets, min_support=s, min_confidence=c, min_lift=l)
        coverage, avg_conf, avg_lift = evaluate_rules(rules, test_baskets)
        score = coverage * avg_conf * avg_lift
        if score > best_score:
            best_score = score
            best_params = (s, c, l)
            best_rules = rules

    coverage, avg_conf, avg_lift = evaluate_rules(best_rules, test_baskets)
    return {
        "optimal_support": best_params[0],
        "optimal_confidence": best_params[1],
        "optimal_lift": best_params[2],
        "coverage": coverage,
        "avg_confidence": avg_conf,
        "avg_lift": avg_lift,
        "rules": best_rules
    }