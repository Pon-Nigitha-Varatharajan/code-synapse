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

recommender_code = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
Auto-generated Product Recommender
\"\"\"

# ------------------------------
# 1. Association Rules
# ------------------------------
apriori_rules = {}
""".format(json.dumps(apriori_rules, indent=2))

recommender_code += """
def recommend_products(basket, top_n=5):
    \"""
    Recommend products for a given basket using Apriori rules.
    \"""
    basket_set = set(basket)
    recs = []
    for rule in apriori_rules:
        if set(rule['if']).issubset(basket_set) and rule['then'] not in basket_set:
            recs.append(rule['then'])
    # Remove duplicates
    recs = list(dict.fromkeys(recs))
    return recs[:top_n]

# ------------------------------
# CLI Test
# ------------------------------
if __name__ == "__main__":
    sample_basket = ["whole milk", "rolls/buns"]
    print("Sample Basket:", sample_basket)
    print("Recommended Products:", recommend_products(sample_basket))
"""

with open(OUTPUT_RECOMMENDER, "w") as f:
    f.write(recommender_code)
print(f"✅ Generated {OUTPUT_RECOMMENDER}")

# ------------------------------
# 2. Generate segment_classifier.py
# ------------------------------
# Read decision tree rules as text
with open(DTREE_FILE, "r") as f:
    dtree_lines = f.readlines()

classifier_code = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
Auto-generated Segment Classifier from Decision Tree
\"\"\"

def classify_segment(features):
    \"\"\"
    features: dict of feature_name -> value
    Returns predicted segment/class
    \"\"\"
"""

indent = "    "
for line in dtree_lines:
    if line.strip() == "":
        continue
    level = line.count("  ")  # detect tree depth by indentation (2 spaces)
    content = line.strip()
    if content.startswith("Leaf:"):
        # Leaf node → return class
        cls = content.replace("Leaf:", "").strip()
        classifier_code += indent*level + f"return {cls}\n"
    else:
        # Split condition
        classifier_code += indent*level + f"if features['{content.split('<=')[0].strip()}'] <= {content.split('<=')[1].strip()}:\n"

# CLI Test
classifier_code += """
# ------------------------------
# CLI Test
# ------------------------------
if __name__ == "__main__":
    sample_features = {"top_1_presence": 0}
    print("Predicted Segment:", classify_segment(sample_features))
"""

with open(OUTPUT_CLASSIFIER, "w") as f:
    f.write(classifier_code)
print(f"✅ Generated {OUTPUT_CLASSIFIER}")