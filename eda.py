#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🛒 Groceries Market Basket Analysis - EDA
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

sns.set(style="whitegrid", palette="muted")

# ------------------------------
# 1. Load Cleaned Data
# ------------------------------
import json

with open("clean/groceries_baskets.json", "r") as f:
    transactions = json.load(f)

print(f"✅ Loaded {len(transactions)} transactions")

# ------------------------------
# 2. Flatten Transactions for Item-level Analysis
# ------------------------------
all_items = [item for basket in transactions for item in basket if item != ""]
item_counts = Counter(all_items)

# ------------------------------
# 3. Univariate Analysis
# ------------------------------

# 3a. Basket Size Distribution
basket_sizes = [len([item for item in basket if item != ""]) for basket in transactions]

plt.figure(figsize=(8,5))
plt.hist(basket_sizes, bins=30, color='skyblue', edgecolor='black')
plt.title("Basket Size Distribution")
plt.xlabel("Number of Items per Basket")
plt.ylabel("Frequency")
plt.show()

# 3b. Most Popular Items
top_items = item_counts.most_common(15)
items, counts = zip(*top_items)

plt.figure(figsize=(10,6))
plt.barh(items[::-1], counts[::-1], color='salmon')
plt.title("Top 15 Most Frequent Items")
plt.xlabel("Number of Purchases")
plt.ylabel("Item")
plt.show()

# ------------------------------
# 4. Bivariate Analysis
# ------------------------------
# Example: Basket size vs top item presence
import numpy as np

top_item_name = items[0]  # most frequent item
basket_has_top_item = [top_item_name in basket for basket in transactions]

plt.figure(figsize=(8,5))
plt.scatter(basket_sizes, basket_has_top_item, alpha=0.3)
plt.title(f"Basket Size vs Presence of '{top_item_name}'")
plt.xlabel("Basket Size")
plt.ylabel(f"Contains '{top_item_name}' (0/1)")
plt.show()

# ------------------------------
# 5. Item Co-occurrence Analysis (Multivariate)
# ------------------------------
from itertools import combinations
from collections import defaultdict

co_occurrence = defaultdict(int)

# Count pairwise co-occurrences for top 20 items
top_20_items = [item for item, _ in item_counts.most_common(20)]

for basket in transactions:
    basket_items = [item for item in basket if item in top_20_items]
    for pair in combinations(basket_items, 2):
        co_occurrence[tuple(sorted(pair))] += 1

# Convert to DataFrame for heatmap
import numpy as np

co_matrix = pd.DataFrame(np.zeros((20,20)), index=top_20_items, columns=top_20_items)

for (i,j), count in co_occurrence.items():
    co_matrix.loc[i,j] = count
    co_matrix.loc[j,i] = count

plt.figure(figsize=(12,10))
sns.heatmap(co_matrix, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Co-occurrence of Top 20 Items")
plt.show()

print("\n✅ Groceries EDA Completed Successfully!")