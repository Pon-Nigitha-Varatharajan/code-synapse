#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Feature Engineering for Groceries Dataset
"""

import pandas as pd
import os
import json
from collections import Counter

# ------------------------------
# 1. Load Cleaned Data
# ------------------------------
with open("clean/groceries_baskets.json", "r") as f:
    transactions = json.load(f)

print(f"✅ Loaded {len(transactions)} transactions")

# ------------------------------
# 2. Basket-Level Features
# ------------------------------

# Create basket DataFrame
basket_df = pd.DataFrame({"basket": transactions})

# Basket size
basket_df["basket_size"] = basket_df["basket"].apply(lambda x: len([i for i in x if i != ""]))

print("\n🔎 Example Basket Features:")
print(basket_df.head(3))

# ------------------------------
# 3. Item-Level Popularity Features
# ------------------------------

# Flatten items and count frequency
all_items = [item for basket in transactions for item in basket if item != ""]
item_counts = Counter(all_items)
top_items = [item for item, count in item_counts.most_common(500)]  # top 500 items

# Keep only top items in baskets
basket_df["basket_top_items"] = basket_df["basket"].apply(lambda x: [i for i in x if i in top_items])

print("\n✅ Top items filtered in baskets")

# ------------------------------
# 4. Transaction-Level Features
# ------------------------------

# Presence matrix for top items (sparse)
top_item_df = pd.DataFrame(
    [{item: int(item in basket) for item in top_items} for basket in basket_df["basket_top_items"]]
)

print(f"\n🔎 Top item presence matrix shape: {top_item_df.shape}")

# ------------------------------
# 5. Save Feature Files
# ------------------------------
os.makedirs("features", exist_ok=True)

# Save baskets with features
basket_df.to_json("features/groceries_baskets_features.json", orient="records", lines=True)
top_item_df.to_csv("features/groceries_top_items_matrix.csv", index=False)

print("\n✅ Features saved:")
print(" - 'features/groceries_baskets_features.json'")
print(" - 'features/groceries_top_items_matrix.csv'")