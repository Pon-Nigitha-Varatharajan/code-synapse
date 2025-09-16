#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Milestone 4: Python Code Generator
Generates product_recommender.py & segment_classifier.py
from your JSON/Decision Tree rules
"""

import json
import os

# ------------------------------
# Paths
# ------------------------------
BASE_DIR = "/Users/ponnigithav/Desktop/code-synapse"
RULES_FILE = os.path.join(BASE_DIR, "rules", "association_rules.json")
DTREE_FILE = os.path.join(BASE_DIR, "rules", "basket_decision_tree_rules.txt")

OUTPUT_RECOMMENDER = os.path.join(BASE_DIR, "product_recommender.py")
OUTPUT_CLASSIFIER = os.path.join(BASE_DIR, "segment_classifier.py")

# ------------------------------
# 1. Generate product_recommender.py
# ------------------------------
with open(RULES_FILE, "r") as f:
    apriori_rules = json.load(f)

recommender_code = f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
Auto-generated Product Recommender
\"\"\"

# ------------------------------
# 1. Association Rules
# ------------------------------
apriori_rules = {json.dumps(apriori_rules, indent=2)}

def recommend_products(basket, top_n=5):
    \"\"\"
    Recommend products for a given basket using Apriori rules.
    \"\"\"
    basket_set = set(basket)
    recs = []
    for rule in apriori_rules:
        if set(rule['if']).issubset(basket_set) and rule['then'] not in basket_set:
            recs.append(rule['then'])
    recs = list(dict.fromkeys(recs))  # remove duplicates
    return recs[:top_n]

if __name__ == "__main__":
    sample_basket = ["whole milk", "rolls/buns"]
    print("Sample Basket:", sample_basket)
    print("Recommended Products:", recommend_products(sample_basket))
"""

with open(OUTPUT_RECOMMENDER, "w") as f:
    f.write(recommender_code)
print(f"✅ Generated {OUTPUT_RECOMMENDER}")

