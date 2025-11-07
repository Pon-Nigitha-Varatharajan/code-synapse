#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Milestone 7 (Optimized): Self-Evolving Engine using FP-Growth
Automatically updates association rules and regenerates product_recommender.py
Much faster than Apriori-based version.
"""

import os
import json
import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
from generator_code import generate_recommender_from_rules

# ------------------------------
# Paths
# ------------------------------
BASE_DIR = "/Users/ponnigithav/Desktop/code-synapse"
RULES_FILE = os.path.join(BASE_DIR, "rules", "association_rules.json")
OUTPUT_RECOMMENDER = os.path.join(BASE_DIR, "product_recommender.py")
NEW_BASKETS_FILE = os.path.join(BASE_DIR, "data", "new_baskets.json")

# ------------------------------
# Parameters
# ------------------------------
MIN_SUPPORT = 0.03
MIN_CONFIDENCE = 0.5
MIN_LIFT = 1.0
PRUNE_LIFT_THRESHOLD = 1.0

# ------------------------------
# Utility: Load baskets
# ------------------------------
def load_baskets(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []

# ------------------------------
# FP-Growth Rule Mining
# ------------------------------
def run_fpgrowth(baskets):
    """Run FP-Growth and generate association rules."""
    # Convert baskets to one-hot encoded DataFrame
    unique_items = sorted({item for basket in baskets for item in basket})
    df = pd.DataFrame([{item: (item in basket) for item in unique_items} for basket in baskets])
    
    # Frequent itemsets
    frequent_itemsets = fpgrowth(df, min_support=MIN_SUPPORT, use_colnames=True)
    if frequent_itemsets.empty:
        print("⚠️ No frequent itemsets found — check support threshold or dataset size.")
        return []
    
    # Association rules
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=MIN_CONFIDENCE)
    
    # Filter and format
    rules = rules[rules['lift'] >= MIN_LIFT].sort_values(by='lift', ascending=False)
    
    # Convert to list of dicts for saving
    formatted_rules = []
    for _, row in rules.iterrows():
        formatted_rules.append({
            "if": list(row['antecedents']),
            "then": list(row['consequents']),
            "support": float(row['support']),
            "confidence": float(row['confidence']),
            "lift": float(row['lift']),
            "itemset_size": len(row['antecedents']) + len(row['consequents'])
        })
    
    return formatted_rules

# ------------------------------
# Self-Evolving Engine (One Run)
# ------------------------------
def run_self_evolving_engine_once(new_baskets):
    print("🚀 Running FP-Growth-based Self-Evolving Engine...")
    
    # Run FP-Growth
    rules = run_fpgrowth(new_baskets)
    print(f"✅ Generated {len(rules)} association rules")
    
    # Save rules
    os.makedirs(os.path.dirname(RULES_FILE), exist_ok=True)
    with open(RULES_FILE, "w") as f:
        json.dump(rules, f, indent=2)
    print(f"💾 Rules saved to: {RULES_FILE}")

    # Regenerate recommender
    generate_recommender_from_rules(rules, OUTPUT_RECOMMENDER)
    print(f"🤖 Recommender file updated at: {OUTPUT_RECOMMENDER}")

if __name__ == "__main__":
    new_baskets = load_baskets(NEW_BASKETS_FILE)
    if new_baskets:
        run_self_evolving_engine_once(new_baskets)
    else:
        print("⚠️ No new baskets found. Add transactions to data/new_baskets.json.")