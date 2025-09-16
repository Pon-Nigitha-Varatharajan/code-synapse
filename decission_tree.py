#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hybrid Product Recommender
- Uses Apriori rules if available
- Computes co-occurrence from baskets
- Modular, human-readable
"""

import json
import os
from itertools import combinations
from collections import defaultdict, Counter
import numpy as np

# ------------------------------
# 1. Paths and Config
# ------------------------------
BASE_DIR = "/Users/ponnigithav/Desktop/code-synapse"
BASKETS_FILE = os.path.join(BASE_DIR, "features", "groceries_baskets_features.json")
RULES_FILE = os.path.join(BASE_DIR, "rules", "association_rules.json")
RECOMMENDATIONS_DIR = os.path.join(BASE_DIR, "recommendations")

MIN_SUPPORT = 0.01
MIN_CONFIDENCE = 0.2
MIN_LIFT = 1.0

# ------------------------------
# 2. Load Baskets
# ------------------------------
with open(BASKETS_FILE, "r") as f:
    baskets = [json.loads(line)["basket"] for line in f]
print(f"✅ Loaded {len(baskets)} baskets")

# ------------------------------
# 3. Apriori Rule Functions
# ------------------------------
def get_support(itemset, baskets):
    return sum(1 for basket in baskets if set(itemset).issubset(basket)) / len(baskets)

def apriori(baskets, min_support=0.01, min_confidence=0.2, min_lift=1.0):
    # Frequent 1-itemsets
    item_counts = Counter(item for basket in baskets for item in basket)
    total_baskets = len(baskets)
    freq_itemsets = {frozenset([item]): count/total_baskets
                     for item, count in item_counts.items() if count/total_baskets >= min_support}

    all_freq_itemsets = dict(freq_itemsets)
    k = 2
    while freq_itemsets:
        candidates = set(i.union(j) for i in freq_itemsets for j in freq_itemsets if len(i.union(j)) == k)
        candidate_counts = defaultdict(int)
        for basket in baskets:
            basket_set = set(basket)
            for cand in candidates:
                if cand.issubset(basket_set):
                    candidate_counts[cand] += 1
        freq_itemsets = {cand: count/total_baskets for cand, count in candidate_counts.items()
                         if count/total_baskets >= min_support}
        all_freq_itemsets.update(freq_itemsets)
        k += 1

    # Generate rules
    rules = []
    for itemset, support in all_freq_itemsets.items():
        if len(itemset) < 2:
            continue
        for i in range(1, len(itemset)):
            for lhs in combinations(itemset, i):
                rhs = itemset.difference(lhs)
                lhs = frozenset(lhs)
                lhs_support = all_freq_itemsets.get(lhs, get_support(lhs, baskets))
                confidence = support / lhs_support if lhs_support > 0 else 0
                rhs_support = all_freq_itemsets.get(rhs, get_support(rhs, baskets))
                lift = confidence / rhs_support if rhs_support > 0 else 0
                if confidence >= min_confidence and lift >= min_lift:
                    rules.append({
                        "if": list(lhs),
                        "then": list(rhs)[0],
                        "support": round(support, 4),
                        "confidence": round(confidence, 4),
                        "lift": round(lift, 4)
                    })
    return rules

# ------------------------------
# 4. Load or Generate Rules
# ------------------------------
if os.path.exists(RULES_FILE):
    with open(RULES_FILE, "r") as f:
        apriori_rules = json.load(f)
    print(f"✅ Loaded {len(apriori_rules)} precomputed Apriori rules")
else:
    apriori_rules = apriori(baskets, MIN_SUPPORT, MIN_CONFIDENCE, MIN_LIFT)
    os.makedirs(os.path.dirname(RULES_FILE), exist_ok=True)
    with open(RULES_FILE, "w") as f:
        json.dump(apriori_rules, f, indent=2)
    print(f"✅ Generated {len(apriori_rules)} Apriori rules")

# ------------------------------
# 5. Compute Co-occurrence Matrix
# ------------------------------
item_counts = Counter()
co_counts = Counter()
for basket in baskets:
    for item in basket:
        item_counts[item] += 1
    for i, j in combinations(set(basket), 2):
        co_counts[(i,j)] += 1
        co_counts[(j,i)] += 1  # symmetric

items = list(item_counts.keys())
item_index = {item: idx for idx, item in enumerate(items)}

matrix = np.zeros((len(items), len(items)))
for (i,j), count in co_counts.items():
    matrix[item_index[i], item_index[j]] = count

freq = np.array([item_counts[item] for item in items])
similarity = matrix / freq[:, None]

# ------------------------------
# 6. Recommendation Function
# ------------------------------
def recommend(basket, top_n=5):
    """
    Recommend products for a given basket
    using Apriori rules and co-occurrence scoring.
    """
    # 1️⃣ Co-occurrence recommendations
    scores = np.zeros(len(items))
    for item in basket:
        if item in item_index:
            scores += similarity[item_index[item]]
    for item in basket:
        if item in item_index:
            scores[item_index[item]] = -1
    co_recs = [items[idx] for idx in scores.argsort()[-top_n:][::-1]]

    # 2️⃣ Apriori recommendations
    apriori_recs = []
    basket_set = set(basket)
    for rule in apriori_rules:
        if set(rule["if"]).issubset(basket_set) and rule["then"] not in basket_set:
            apriori_recs.append(rule["then"])
    apriori_recs = list(dict.fromkeys(apriori_recs))

    # Combine
    combined = apriori_recs + [r for r in co_recs if r not in apriori_recs]
    return combined[:top_n]

# ------------------------------
# 7. Test Recommendations
# ------------------------------
if __name__ == "__main__":
    example_basket = ["whole milk", "brown bread"]
    print("\nExample Basket:", example_basket)
    print("Recommended Items:", recommend(example_basket, top_n=5))

    # Save sample recommendations
    os.makedirs(RECOMMENDATIONS_DIR, exist_ok=True)
    sample_recs = {str(basket): recommend(basket, top_n=5) for basket in baskets[:100]}
    with open(os.path.join(RECOMMENDATIONS_DIR, "basket_recommendations.json"), "w") as f:
        json.dump(sample_recs, f, indent=2)
    print(f"📁 Sample recommendations saved: {RECOMMENDATIONS_DIR}/basket_recommendations.json")