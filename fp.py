#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FP-Growth with optional threshold optimization and CSV export for product recommendations
"""

from collections import Counter, defaultdict
from itertools import combinations
import itertools
import csv
import os

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
            # Sort items by frequency in descending order
            ordered = [i for i in sorted(trans, 
                                       key=lambda x: self.frequent_items.get(x, 0), 
                                       reverse=True)
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
    """Get the path from node to root (excluding root)"""
    path = []
    while node and node.parent and node.parent.item is not None:
        node = node.parent
        path.append(node.item)
    return path[::-1]  # Reverse to get correct order

def find_prefix_paths(base_item, header_node):
    """Find all prefix paths for a given item"""
    cond_pats = []
    counts = []
    node = header_node
    while node:
        path = ascend_fpnode(node)
        if path:
            cond_pats.append(path)
            counts.append(node.count)
        node = node.link
    return cond_pats, counts

def mine_tree(tree, min_support, prefix, freq_itemsets):
    """Mine the FP-tree recursively"""
    # Sort by frequency in DESCENDING order (FIXED)
    sorted_items = sorted(tree.frequent_items.items(), 
                         key=lambda x: x[1], 
                         reverse=True)  # Changed to reverse=True
    
    for base_item, count in sorted_items:
        new_freq_set = prefix.copy()
        new_freq_set.add(base_item)
        freq_itemsets[frozenset(new_freq_set)] = count
        
        # Get conditional pattern base
        cond_pats, counts = find_prefix_paths(base_item, tree.headers[base_item])
        
        if cond_pats:
            # Build conditional transactions with counts
            cond_transactions = []
            for path, path_count in zip(cond_pats, counts):
                cond_transactions.extend([path] * path_count)
            
            # Build conditional FP-tree
            cond_tree = FPTree(cond_transactions, min_support)
            if cond_tree.frequent_items:
                mine_tree(cond_tree, min_support, new_freq_set, freq_itemsets)

def fp_growth(transactions, min_support_ratio):
    """Run FP-Growth algorithm"""
    min_support_count = max(1, int(min_support_ratio * len(transactions)))
    tree = FPTree(transactions, min_support_count)
    freq_itemsets = {}
    mine_tree(tree, min_support_count, set(), freq_itemsets)
    
    # Convert counts to support ratios
    return {itemset: count / len(transactions) for itemset, count in freq_itemsets.items()}

# ------------------------------
# Rule Generation
# ------------------------------
def get_support(itemset, baskets):
    return sum(1 for basket in baskets if set(itemset).issubset(basket)) / len(baskets)

def generate_rules(freq_itemsets, baskets, min_confidence, min_lift):
    """Generate association rules from frequent itemsets"""
    rules = []
    for itemset, support in freq_itemsets.items():
        if len(itemset) < 2:
            continue
        
        # Generate all possible rules
        for i in range(1, len(itemset)):
            for lhs in combinations(itemset, i):
                lhs_set = frozenset(lhs)
                rhs_set = itemset - lhs_set
                
                # Get supports
                lhs_support = freq_itemsets.get(lhs_set, get_support(lhs_set, baskets))
                rhs_support = freq_itemsets.get(rhs_set, get_support(rhs_set, baskets))
                
                # Calculate metrics
                confidence = support / lhs_support if lhs_support > 0 else 0
                lift = confidence / rhs_support if rhs_support > 0 else 0
                
                if confidence >= min_confidence and lift >= min_lift:
                    rules.append({
                        "if": list(lhs_set),
                        "then": list(rhs_set),
                        "support": round(support, 4),
                        "confidence": round(confidence, 4),
                        "lift": round(lift, 4),
                        "itemset_size": len(itemset)
                    })
    return rules

# ------------------------------
# Run Single FP-Growth
# ------------------------------
def run_fp_growth(baskets, min_support, min_confidence, min_lift):
    """Run FP-Growth and generate rules"""
    print(f"Running FP-Growth with {len(baskets)} baskets, min_support={min_support}")
    freq_itemsets = fp_growth(baskets, min_support)
    print(f"Found {len(freq_itemsets)} frequent itemsets")
    rules = generate_rules(freq_itemsets, baskets, min_confidence, min_lift)
    print(f"Generated {len(rules)} rules")
    return rules

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
# CSV Export for Product Recommendations
# ------------------------------
def save_rules_to_csv(rules, filename="fp_growth_rules.csv", include_params=False, params=None):
    """Save FP-Growth rules to CSV file"""
    if not rules:
        print("No rules to save.")
        return
    
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        if include_params and params:
            fieldnames = ['antecedent', 'consequent', 'support', 'confidence', 'lift', 
                         'itemset_size', 'min_support', 'min_confidence', 'min_lift', 'rule_id']
        else:
            fieldnames = ['antecedent', 'consequent', 'support', 'confidence', 'lift', 'itemset_size', 'rule_id']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i, rule in enumerate(rules):
            row_data = {
                'antecedent': ';'.join(map(str, rule['if'])),
                'consequent': ';'.join(map(str, rule['then'])),
                'support': rule['support'],
                'confidence': rule['confidence'],
                'lift': rule['lift'],
                'itemset_size': rule.get('itemset_size', len(rule['if']) + len(rule['then'])),
                'rule_id': f"rule_{i+1:04d}"
            }
            
            if include_params and params:
                row_data['min_support'] = params[0]
                row_data['min_confidence'] = params[1]
                row_data['min_lift'] = params[2]
            
            writer.writerow(row_data)
    
    print(f"Successfully saved {len(rules)} rules to {filename}")

def save_all_rules_to_csv(all_rules_data, filename="all_fp_growth_rules.csv"):
    """Save all rules from all parameter combinations to a single CSV file"""
    if not all_rules_data:
        print("No rules data to save.")
        return
    
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['antecedent', 'consequent', 'support', 'confidence', 'lift', 
                     'itemset_size', 'min_support', 'min_confidence', 'min_lift', 
                     'parameter_set', 'rule_id']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        rule_counter = 1
        for param_set, rules in all_rules_data:
            s, c, l = param_set
            for rule in rules:
                writer.writerow({
                    'antecedent': ';'.join(map(str, rule['if'])),
                    'consequent': ';'.join(map(str, rule['then'])),
                    'support': rule['support'],
                    'confidence': rule['confidence'],
                    'lift': rule['lift'],
                    'itemset_size': rule.get('itemset_size', len(rule['if']) + len(rule['then'])),
                    'min_support': s,
                    'min_confidence': c,
                    'min_lift': l,
                    'parameter_set': f"s{s}_c{c}_l{l}",
                    'rule_id': f"rule_{rule_counter:06d}"
                })
                rule_counter += 1
    
    print(f"Successfully saved {rule_counter-1} total rules from all parameter combinations to {filename}")

def load_rules_from_csv(filename="fp_growth_rules.csv"):
    """Load FP-Growth rules from CSV file"""
    rules = []
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rule_data = {
                    'if': row['antecedent'].split(';') if row['antecedent'] else [],
                    'then': row['consequent'].split(';') if row['consequent'] else [],
                    'support': float(row['support']),
                    'confidence': float(row['confidence']),
                    'lift': float(row['lift'])
                }
                if 'itemset_size' in row:
                    rule_data['itemset_size'] = int(row['itemset_size'])
                rules.append(rule_data)
        print(f"Successfully loaded {len(rules)} rules from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error loading rules from {filename}: {e}")
    
    return rules

# ------------------------------
# Product Recommendation Functions
# ------------------------------
def recommend_products(rules, user_basket, max_recommendations=5):
    """Generate product recommendations based on FP-Growth rules"""
    recommendations = {}
    
    for rule in rules:
        antecedent = set(rule['if'])
        consequent = set(rule['then'])
        
        if antecedent.issubset(set(user_basket)):
            score = rule['confidence'] * rule['lift']
            
            for product in consequent:
                if product not in user_basket:
                    if product in recommendations:
                        recommendations[product] = max(recommendations[product], score)
                    else:
                        recommendations[product] = score
    
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations[:max_recommendations]

# ------------------------------
# Grid Search for Optimal Thresholds
# ------------------------------
def find_optimal_thresholds(train_baskets, test_baskets,
                            support_values=[0.01,0.02,0.03,0.05],
                            confidence_values=[0.3,0.4,0.5,0.6],
                            lift_values=[0.5,1.0,1.2,1.5],
                            output_csv="fp_growth_rules.csv",
                            save_all_rules=True):
    """Find optimal thresholds using grid search and save all rules"""
    best_score = -1
    best_params = None
    best_rules = []
    all_rules_data = []  # Store all rules from all parameter combinations
    
    print(f"Testing {len(support_values)} x {len(confidence_values)} x {len(lift_values)} = {len(support_values)*len(confidence_values)*len(lift_values)} parameter combinations")
    
    for s, c, l in itertools.product(support_values, confidence_values, lift_values):
        print(f"Testing support={s}, confidence={c}, lift={l}")
        rules = run_fp_growth(train_baskets, min_support=s, min_confidence=c, min_lift=l)
        
        # Store all rules with their parameters
        if rules:
            all_rules_data.append(((s, c, l), rules))
        
        coverage, avg_conf, avg_lift = evaluate_rules(rules, test_baskets)
        score = coverage * avg_conf * avg_lift
        print(f"  Rules: {len(rules)}, Coverage: {coverage:.3f}, Score: {score:.3f}")
        
        if score > best_score and len(rules) > 0:
            best_score = score
            best_params = (s, c, l)
            best_rules = rules

    # Save all rules from all parameter combinations
    if save_all_rules and all_rules_data:
        all_rules_filename = "fp_growth_rules.csv"
        save_all_rules_to_csv(all_rules_data, all_rules_filename)
        
        # Also save summary of parameter combinations
        save_parameter_summary(all_rules_data, "parameter_summary.csv")

    if best_rules:
        coverage, avg_conf, avg_lift = evaluate_rules(best_rules, test_baskets)
        
        # Save optimal rules with parameter info
        save_rules_to_csv(best_rules, output_csv, include_params=True, params=best_params)
        
        return {
            "optimal_support": best_params[0],
            "optimal_confidence": best_params[1],
            "optimal_lift": best_params[2],
            "coverage": coverage,
            "avg_confidence": avg_conf,
            "avg_lift": avg_lift,
            "rules": best_rules,
            "rules_file": output_csv,
            "all_rules_file": "fp_growth_rules.csv" if save_all_rules and all_rules_data else None,
            "total_parameter_combinations": len(list(itertools.product(support_values, confidence_values, lift_values))),
            "successful_combinations": len(all_rules_data)
        }
    else:
        return {"error": "No valid rules found with given parameters"}

def save_parameter_summary(all_rules_data, filename="parameter_summary.csv"):
    """Save summary of rules generated for each parameter combination"""
    if not all_rules_data:
        return
    
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['min_support', 'min_confidence', 'min_lift', 'num_rules', 
                     'avg_confidence', 'avg_lift', 'avg_support']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for params, rules in all_rules_data:
            s, c, l = params
            if rules:
                avg_conf = sum(rule['confidence'] for rule in rules) / len(rules)
                avg_lift = sum(rule['lift'] for rule in rules) / len(rules)
                avg_supp = sum(rule['support'] for rule in rules) / len(rules)
                
                writer.writerow({
                    'min_support': s,
                    'min_confidence': c,
                    'min_lift': l,
                    'num_rules': len(rules),
                    'avg_confidence': round(avg_conf, 4),
                    'avg_lift': round(avg_lift, 4),
                    'avg_support': round(avg_supp, 4)
                })
    
    print(f"Saved parameter summary to {filename}")

# ------------------------------
# Example Usage
# ------------------------------
def example_usage():
    """Example demonstrating FP-Growth with the fix"""
    transactions = [
        ['milk', 'bread', 'butter'],
        ['milk', 'bread'],
        ['milk', 'eggs'],
        ['bread', 'butter', 'eggs'],
        ['milk', 'bread', 'eggs', 'butter'],
        ['bread', 'eggs'],
        ['milk', 'eggs'],
        ['milk', 'bread', 'eggs'],
        ['milk', 'bread', 'butter'],
        ['bread', 'butter']
    ]
    
    train_data = transactions[:7]
    test_data = transactions[7:]
    
    print("Running FP-Growth with threshold optimization...")
    results = find_optimal_thresholds(
        train_baskets=train_data,
        test_baskets=test_data,
        support_values=[0.1, 0.2],
        confidence_values=[0.3, 0.5],
        lift_values=[1.0, 1.5],
        output_csv="optimal_rules.csv",
        save_all_rules=True
    )
    
    if "error" not in results:
        print(f"\n=== OPTIMAL PARAMETERS ===")
        print(f"Support: {results['optimal_support']}")
        print(f"Confidence: {results['optimal_confidence']}")
        print(f"Lift: {results['optimal_lift']}")
        print(f"Number of optimal rules: {len(results['rules'])}")
        print(f"Optimal rules saved to: {results['rules_file']}")
        
        if results.get('all_rules_file'):
            print(f"All rules saved to: {results['all_rules_file']}")
        
        print(f"Parameter combinations tested: {results['total_parameter_combinations']}")
        print(f"Successful combinations: {results['successful_combinations']}")
        
        # Test recommendations with optimal rules
        loaded_rules = load_rules_from_csv("optimal_rules.csv")
        sample_basket = ['milk', 'bread']
        recommendations = recommend_products(loaded_rules, sample_basket)
        
        print(f"\n=== RECOMMENDATIONS ===")
        print(f"User basket: {sample_basket}")
        print("Recommended products:")
        for product, score in recommendations:
            print(f"  - {product}: {score:.4f}")
            
        # Show rules from all parameters
        try:
            all_rules = load_rules_from_csv("all_parameter_rules.csv")
            print(f"\n=== ALL RULES SUMMARY ===")
            print(f"Total rules from all parameters: {len(all_rules)}")
        except:
            print("\nCould not load all rules file")
            
    else:
        print(results["error"])

if __name__ == "__main__":
    example_usage()