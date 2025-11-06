#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Decision Tree on Groceries Dataset — Enhanced Visualization Version
Includes:
✅ Advanced labeling (dominant category)
✅ Category count features
✅ Improved Graphviz visualization (vertical + compact)
✅ Model evaluation
✅ Streamlit compatibility
"""

import os
import math
import json
import pandas as pd
import numpy as np
from graphviz import Digraph
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -----------------------------------------------------
# 1️⃣ Category Mapping
# -----------------------------------------------------
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

# -----------------------------------------------------
# 2️⃣ Improved Basket Labeling (Dominant Category)
# -----------------------------------------------------
def label_basket(basket_entry):
    """Label basket by its dominant category."""
    basket = basket_entry.get("basket", [])
    category_counts = {cat: sum(i in basket for i in items) for cat, items in CATEGORY_MAP.items()}
    dominant_category = max(category_counts, key=category_counts.get)
    return f"{dominant_category}_shopper"

# -----------------------------------------------------
# 3️⃣ Feature Extraction
# -----------------------------------------------------
def extract_features(basket_entry):
    basket = basket_entry["basket"]
    features = {}
    for category, items in CATEGORY_MAP.items():
        features[f"count_{category}"] = sum(i in basket for i in items)

    total_items = sum(features[f"count_{cat}"] for cat in CATEGORY_MAP.keys())
    num_categories = sum(features[f"count_{cat}"] > 0 for cat in CATEGORY_MAP.keys())

    features["total_items"] = total_items
    features["num_categories"] = num_categories
    features["diversity"] = num_categories / (total_items + 1e-5)
    return features

# -----------------------------------------------------
# 4️⃣ Custom ID3 Decision Tree Implementation
# -----------------------------------------------------
def entropy(labels):
    total = len(labels)
    counts = {l: labels.count(l) for l in set(labels)}
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

def build_tree(X, y, features, depth=0, max_depth=4):
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
        remaining = [f for f in features if f != best_feature]
        tree["children"][v] = build_tree(subset_X, subset_y, remaining, depth + 1, max_depth)
    return tree

# -----------------------------------------------------
# 5️⃣ Enhanced Graphviz Visualization (Compact & Vertical)
# -----------------------------------------------------
def tree_to_graphviz(tree, dot=None, parent=None, edge_label=None):
    if dot is None:
        dot = Digraph(comment="Decision Tree", format="png")
        dot.attr(rankdir="TB")  # 🔁 Vertical layout (Top to Bottom)
        dot.attr("node", shape="ellipse", fontname="Helvetica", fontsize="10")

    node_id = str(id(tree))
    if "label" in tree:
        dot.node(node_id, label=f"🎯 {tree['label']}", shape="box", color="#A7C7E7", style="filled")
        if parent:
            dot.edge(parent, node_id, label=edge_label or "")
        return dot

    feature = tree["feature"]
    dot.node(node_id, label=f"{feature}", shape="ellipse", color="#90EE90", style="filled")
    if parent:
        dot.edge(parent, node_id, label=edge_label or "")

    for val, subtree in tree["children"].items():
        edge_lbl = f"= {val}"
        tree_to_graphviz(subtree, dot, node_id, edge_lbl)
    return dot

# -----------------------------------------------------
# 6️⃣ Classification Function
# -----------------------------------------------------
def classify_segment(features, tree):
    if "label" in tree:
        return tree["label"]
    feature = tree["feature"]
    value = features.get(feature, 0)
    if value in tree["children"]:
        return classify_segment(features, tree["children"][value])
    else:
        return "Unknown"

# -----------------------------------------------------
# 7️⃣ Build, Evaluate, and Save
# -----------------------------------------------------
def build_decision_tree(max_depth=4):
    with open("features/groceries_baskets_features.json", "r") as f:
        data = [json.loads(line) for line in f]

    X = [extract_features(d) for d in data]
    y = [label_basket(d) for d in data]
    features = list(X[0].keys())

    tree_model = build_tree(X, y, features, max_depth=max_depth)
    os.makedirs("rules", exist_ok=True)
    with open("rules/basket_decision_tree_rules.txt", "w") as f:
        f.write(tree_to_rules(tree_model))

    return tree_model

def tree_to_rules(tree, indent=""):
    if "label" in tree:
        return indent + f"→ Leaf: {tree['label']}\n"
    rules = ""
    feature = tree["feature"]
    for val, subtree in tree["children"].items():
        rules += indent + f"if {feature} == {val}:\n"
        rules += tree_to_rules(subtree, indent + "  ")
    return rules

def evaluate_tree(tree, X, y):
    preds = [classify_segment(x, tree) for x in X]
    acc = accuracy_score(y, preds)
    report = classification_report(y, preds, output_dict=True)
    cm = confusion_matrix(y, preds)
    return acc, report, cm

def run_evaluation(max_depth=4):
    with open("features/groceries_baskets_features.json", "r") as f:
        data = [json.loads(line) for line in f]

    X_all = [extract_features(d) for d in data]
    y_all = [label_basket(d) for d in data]

    X_train, X_test, y_train, y_test = train_test_split(
        X_all, y_all, test_size=0.3, stratify=y_all, random_state=42
    )

    features = list(X_train[0].keys())
    tree_model = build_tree(X_train, y_train, features, max_depth=max_depth)

    acc, report, cm = evaluate_tree(tree_model, X_test, y_test)

    # 🖼 Save better visualization
    dot = tree_to_graphviz(tree_model)
    os.makedirs("rules", exist_ok=True)
    dot.render("rules/decision_tree_visualization", format="png", cleanup=True)

    return acc, report, cm

# -----------------------------------------------------
# 8️⃣ Run Directly (Testing)
# -----------------------------------------------------x
if __name__ == "__main__":
    tree_model = build_decision_tree(max_depth=4)
    dot = tree_to_graphviz(tree_model)
    dot.render("rules/decision_tree_visualization", format="png", cleanup=True)
    print("✅ Tree visualization saved as rules/decision_tree_visualization.png")

    acc, report, cm, _ = run_evaluation(max_depth=4)
    print(f"\nAccuracy: {acc:.3f}")
    print("Confusion Matrix:\n", cm)