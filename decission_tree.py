#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Decision Tree on Groceries dataset (categories: fruits, vegetables, dairy, frozen, etc.)
Refactored for Streamlit integration.
"""

import json
import math
import os
from graphviz import Digraph

# ------------------------------
# 1. Define Categories
# ------------------------------
CATEGORY_MAP = {
    "fruits": ["citrus fruit","tropical fruit","pip fruit","grapes","berries","other fruits","apples","pears","bananas"],
    "vegetables": ["root vegetables","onions","potato products","cabbages","carrots","herbs","other vegetables","fresh vegetables"],
    "dairy": ["yogurt","milk","cream","butter","curd","whipped/sour cream","cheese"],
    "frozen": ["frozen foods","frozen dessert","ice cream"],
    "bakery": ["bread","rolls/buns","pastry","cake bar","specialty bar"],
    "meat": ["beef","pork","poultry","ham","sausage","meat spreads"],
    "seafood": ["fish","seafood"],
    "beverages": ["coffee","instant coffee","tea","soda","mineral water","juices","alcoholic drinks","soft drinks","bottled water"],
    "snacks": ["chocolate","candy","sugar","waffles","chips","popcorn","nuts","snack products","biscuits"],
    "household": ["detergent","cleaner","soap","hygiene articles","kitchen towels"],
    "canned": ["canned vegetables","canned fruit","canned fish","canned products"],
    "misc": ["spices","seasonings","sauces","condiments","mustard","vinegar","oils","salt"]
}

# ------------------------------
# 2. Basket Label Function
# ------------------------------
def label_basket(b):
    size = b["basket_size"]
    if size <= 2:
        return "Small Basket"
    elif size >= 5:
        return "Big Basket"
    else:
        return "Medium Basket"

# ------------------------------
# 3. Extract Features by Category
# ------------------------------
def extract_features(basket_entry):
    basket = basket_entry["basket"]
    features = {}
    for category, items in CATEGORY_MAP.items():
        features[f"has_{category}"] = int(any(i in basket for i in items))
    return features

# ------------------------------
# 4. ID3 Decision Tree Functions
# ------------------------------
def entropy(labels):
    total = len(labels)
    counts = {}
    for l in labels:
        counts[l] = counts.get(l, 0) + 1
    return -sum((c/total) * math.log2(c/total) for c in counts.values() if c > 0)

def information_gain(X, y, feature):
    total_entropy = entropy(y)
    values = set(x[feature] for x in X)
    weighted_entropy = 0
    for v in values:
        subset_y = [y[i] for i in range(len(y)) if X[i][feature] == v]
        weighted_entropy += (len(subset_y)/len(y)) * entropy(subset_y)
    return total_entropy - weighted_entropy

def majority_class(y):
    return max(set(y), key=y.count)

def build_tree(X, y, features, depth=0, max_depth=3):
    if len(set(y)) == 1:
        return {"label": y[0]}
    if not features or depth == max_depth:
        return {"label": majority_class(y)}

    gains = [(information_gain(X, y, f), f) for f in features]
    best_gain, best_feature = max(gains, key=lambda x: x[0])
    if best_gain == 0:
        return {"label": majority_class(y)}

    tree = {"feature": best_feature, "children": {}}
    values = set(x[best_feature] for x in X)
    for v in values:
        subset_X = [X[i] for i in range(len(X)) if X[i][best_feature] == v]
        subset_y = [y[i] for i in range(len(X)) if X[i][best_feature] == v]
        if not subset_X:
            tree["children"][v] = {"label": majority_class(y)}
        else:
            remaining = [f for f in features if f != best_feature]
            tree["children"][v] = build_tree(subset_X, subset_y, remaining, depth+1, max_depth)
    return tree

# ------------------------------
# 5. Convert tree to textual rules
# ------------------------------
def tree_to_rules(tree, indent=""):
    if "label" in tree:
        return indent + f"Leaf: '{tree['label']}'\n"
    rules = ""
    feature = tree["feature"]
    for val, subtree in tree["children"].items():
        rules += indent + f"if {feature} == {val}:\n"
        rules += tree_to_rules(subtree, indent + "  ")
    return rules

# ------------------------------
# 6. Graphviz Visualization
# ------------------------------
def tree_to_graphviz(tree, dot=None, parent=None, edge_label=None):
    if dot is None:
        dot = Digraph(comment="Decision Tree")
    if "label" in tree:
        node_id = str(id(tree))
        dot.node(node_id, label=str(tree["label"]), shape="box", style="filled", color="lightblue")
        if parent:
            dot.edge(parent, node_id, label=edge_label)
        return dot
    node_id = str(id(tree))
    dot.node(node_id, label=tree["feature"], shape="ellipse", style="filled", color="lightgreen")
    if parent:
        dot.edge(parent, node_id, label=edge_label)
    for val, subtree in tree["children"].items():
        tree_to_graphviz(subtree, dot, node_id, str(val))
    return dot

# ------------------------------
# 7. Classify a sample
# ------------------------------
def classify_segment(features, tree):
    if "label" in tree:
        return tree["label"]
    feature = tree["feature"]
    value = features.get(feature, 0)
    if value in tree["children"]:
        return classify_segment(features, tree["children"][value])
    return "Unknown"

# ------------------------------
# 8. Build tree from file
# ------------------------------
def build_decision_tree(max_depth=3, save_rules=True):
    with open("features/groceries_baskets_features.json", "r") as f:
        data = [json.loads(line) for line in f]

    X = [extract_features(d) for d in data]
    y = [label_basket(d) for d in data]

    features = list(X[0].keys())
    tree_built = build_tree(X, y, features, max_depth=max_depth)

    if save_rules:
        rules_text = tree_to_rules(tree_built)
        os.makedirs("rules", exist_ok=True)
        with open("rules/basket_decision_tree_rules.txt", "w") as f:
            f.write(rules_text)
    else:
        rules_text = ""

    return tree_built, rules_text

# ------------------------------
# 10. Model Evaluation (Train/Test Split)
# ------------------------------
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd

def evaluate_tree(tree, X, y):
    preds = [classify_segment(x, tree) for x in X]
    acc = accuracy_score(y, preds)
    report = classification_report(y, preds, output_dict=True)
    cm = confusion_matrix(y, preds, labels=["Small Basket","Medium Basket","Big Basket"])
    return acc, report, cm

def run_evaluation(max_depth=3):
    # Load data
    with open("features/groceries_baskets_features.json", "r") as f:
        data = [json.loads(line) for line in f]

    X_all = [extract_features(d) for d in data]
    y_all = [label_basket(d) for d in data]

    # Train/test split
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=0.3, random_state=42)

    # Build tree on train data
    features = list(X_train[0].keys())
    tree_model = build_tree(X_train, y_train, features, max_depth=max_depth)

    # Evaluate on test data
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
    preds = [classify_segment(x, tree_model) for x in X_test]
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds, output_dict=True)
    cm = confusion_matrix(y_test, preds, labels=["Small Basket","Medium Basket","Big Basket"])

    return acc, report, cm

# ------------------------------
# Run evaluation if executed directly
# ------------------------------
if __name__ == "__main__":
    tree_built, rules_text = build_decision_tree()
    print(rules_text)

    # Example classification
    sample = {f"has_{cat}": 0 for cat in CATEGORY_MAP.keys()}
    sample["has_fruits"] = 1
    sample["has_dairy"] = 1
    print("Sample Features:", sample)
    print("Predicted Segment:", classify_segment(sample, tree_built))

    # Run evaluation
    run_evaluation(max_depth=3)