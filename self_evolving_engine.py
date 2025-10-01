#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 16:19:46 2025

@author: ponnigithav
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Milestone 7: Self-Evolving Engine
Automatically updates rules and regenerates product_recommender.py
"""

import os
import json
import time
from collections import defaultdict
from apriori import run_apriori, evaluate_rules
from generator_code import generate_recommender_from_rules

# ------------------------------
# Paths
# ------------------------------
BASE_DIR = "/Users/ponnigithav/Desktop/code-synapse"
RULES_FILE = os.path.join(BASE_DIR, "rules", "association_rules.json")
OUTPUT_RECOMMENDER = os.path.join(BASE_DIR, "product_recommender.py")
NEW_BASKETS_FILE = os.path.join(BASE_DIR, "data", "new_baskets.json")  # simulated new data

# ------------------------------
# Parameters
# ------------------------------
MIN_SUPPORT = 0.03
MIN_CONFIDENCE = 0.5
MIN_LIFT = 1.0
PRUNE_LIFT_THRESHOLD = 1.0   # rules below this lift are pruned
CHECK_INTERVAL = 30          # seconds between checks for new baskets

# ------------------------------
# Utility: Load baskets
# ------------------------------
def load_baskets(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []

# ------------------------------
# Utility: Rank rules by lift
# ------------------------------
def rank_rules(rules):
    return sorted(rules, key=lambda x: x['lift'], reverse=True)

# ------------------------------
# Main loop
# ------------------------------
def run_self_evolving_engine_once(new_baskets):
    
    # Existing logic from run_self_evolving_engine, but no infinite loop
    # Combine old + new baskets
    all_baskets = new_baskets

    # Run Apriori
    rules = run_apriori(all_baskets, min_support=MIN_SUPPORT,
                        min_confidence=MIN_CONFIDENCE, min_lift=MIN_LIFT)
    # Prune and rank
    pruned_rules = [r for r in rules if r['lift'] >= PRUNE_LIFT_THRESHOLD]
    ranked_rules = sorted(pruned_rules, key=lambda x: x['lift'], reverse=True)

    # Save rules
    os.makedirs(os.path.dirname(RULES_FILE), exist_ok=True)
    with open(RULES_FILE, "w") as f:
        json.dump(ranked_rules, f, indent=2)

    # Regenerate product_recommender.py
    generate_recommender_from_rules(ranked_rules, OUTPUT_RECOMMENDER)

if __name__ == "__main__":
    run_self_evolving_engine()