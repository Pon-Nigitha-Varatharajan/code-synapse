# generator_code.py
import json
import os

BASE_DIR = "/Users/ponnigithav/Desktop/code-synapse"
RULES_FILE = os.path.join(BASE_DIR, "rules", "association_rules.json")
OUTPUT_RECOMMENDER = os.path.join(BASE_DIR, "product_recommender.py")

def generate_recommender_from_rules(rules=None, output_file=OUTPUT_RECOMMENDER):
    """
    Generates product_recommender.py from rules.
    If `rules` is None, loads from RULES_FILE.
    """
    if rules is None:
        with open(RULES_FILE, "r") as f:
            rules = json.load(f)

    recommender_code = f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
Auto-generated Product Recommender
\"\"\"

# ------------------------------
# 1. Association Rules
# ------------------------------
apriori_rules = {json.dumps(rules, indent=2)}

def recommend_products(basket, top_n=5):
    basket_set = set(basket)
    recs = []
    for rule in apriori_rules:
        if set(rule["if"]).issubset(basket_set):
            if isinstance(rule["then"], list):
                for item in rule["then"]:
                    if item not in basket_set:
                        recs.append(item)
            else:
                if rule["then"] not in basket_set:
                    recs.append(rule["then"])
    recs = list(dict.fromkeys(recs))
    return recs[:top_n]

if __name__ == "__main__":
    sample_basket = ["whole milk", "rolls/buns"]
    print("Sample Basket:", sample_basket)
    print("Recommended Products:", recommend_products(sample_basket))
"""

    with open(output_file, "w") as f:
        f.write(recommender_code)
    print(f"✅ Generated {output_file}")