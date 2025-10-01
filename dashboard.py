#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Groceries Recommendation Dashboard
Combines Apriori rules and co-occurrence visualizations
"""

import json
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style="whitegrid", palette="muted")

# ------------------------------
# 1. Set Absolute Paths
# ------------------------------
BASE_DIR = "/Users/ponnigithav/Desktop/code-synapse"
BASKETS_FILE = f"{BASE_DIR}/features/groceries_baskets_features.json"
RULES_FILE = f"{BASE_DIR}/rules/association_rules.json"

# ------------------------------
# 2. Load Baskets and Rules
# ------------------------------
with open(BASKETS_FILE, "r") as f:
    baskets = [json.loads(line)["basket"] for line in f]

with open(RULES_FILE, "r") as f:
    rules = json.load(f)

print(f"✅ Loaded {len(baskets)} baskets and {len(rules)} Apriori rules")

# ------------------------------
# 3. Prepare Data for Visuals
# ------------------------------
all_items = [item for basket in baskets for item in basket]

# Top 10 items
top_items = Counter(all_items).most_common(10)
items, counts = zip(*top_items)

# Top Apriori rules by confidence
if rules:
    df_rules = pd.DataFrame(rules)
    top_conf = df_rules.nlargest(10, "confidence")

# Co-occurrence matrix (top 15 items)
item_counts = Counter(all_items)
top_15_items = [item for item, _ in item_counts.most_common(15)]
item_index = {item: idx for idx, item in enumerate(top_15_items)}
matrix = np.zeros((15, 15))
for basket in baskets:
    for i, j in [(x, y) for x in basket for y in basket if x in top_15_items and y in top_15_items]:
        matrix[item_index[i], item_index[j]] += 1

# Normalize for similarity
freq = np.array([matrix[i, i] for i in range(15)])
similarity = matrix / freq[:, None]

# ------------------------------
# 4. Create Dashboard
# ------------------------------
fig = plt.figure(constrained_layout=True, figsize=(18,12))
gs = fig.add_gridspec(2, 2)

# --- Top Items Bar ---
ax0 = fig.add_subplot(gs[0, 0])
ax0.bar(items, counts, color='skyblue')
ax0.set_title("Top 10 Most Frequent Items")
ax0.set_ylabel("Number of Occurrences")
ax0.set_xticklabels(items, rotation=45, ha='right')

# --- Top Apriori Rules by Confidence ---
ax1 = fig.add_subplot(gs[0, 1])
sns.barplot(x="confidence", y="then", data=top_conf, palette="viridis", ax=ax1)
ax1.set_title("Top 10 Consequents by Confidence (Apriori Rules)")

# --- Support vs Confidence Bubble ---
ax2 = fig.add_subplot(gs[1, 0])
sns.scatterplot(x="support", y="confidence", size="lift", data=df_rules, alpha=0.6, ax=ax2)
ax2.set_title("Support vs Confidence (Bubble = Lift)")
ax2.set_xlabel("Support")
ax2.set_ylabel("Confidence")

# --- Co-occurrence Heatmap ---
ax3 = fig.add_subplot(gs[1, 1])
sns.heatmap(similarity, xticklabels=top_15_items, yticklabels=top_15_items,
            cmap="YlGnBu", annot=True, fmt=".2f", ax=ax3)
ax3.set_title("Item Co-occurrence Heatmap (Top 15 Items)")

plt.suptitle("🛒 Groceries Recommendation Dashboard", fontsize=18)
plt.show()

# ------------------------------
# 5. Sample Recommendations Table
# ------------------------------
def recommend(basket, top_n=5):
    # Co-occurrence scoring
    scores = np.zeros(len(top_15_items))
    for item in basket:
        if item in item_index:
            scores += similarity[item_index[item]]
    for item in basket:
        if item in item_index:
            scores[item_index[item]] = -1
    co_recs = [top_15_items[idx] for idx in scores.argsort()[-top_n:][::-1]]

    # Apriori rules
    apriori_recs = []
    basket_set = set(basket)
    for rule in rules:
        if set(rule["if"]).issubset(basket_set) and rule["then"] not in basket_set:
            apriori_recs.append(rule["then"])
    apriori_recs = list(dict.fromkeys(apriori_recs))

    # Combine
    combined = apriori_recs + [r for r in co_recs if r not in apriori_recs]
    return combined[:top_n]

# Show recommendations for first 5 baskets
print("\n🔹 Sample Basket Recommendations:")
for i, basket in enumerate(baskets[:5], 1):
    recs = recommend(basket)
    print(f"\nBasket {i}: {basket}")
    print(f"Recommended Items: {recs}")