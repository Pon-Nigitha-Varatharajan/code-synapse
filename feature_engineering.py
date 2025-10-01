#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Feature Engineering for Groceries Dataset (Train/Test)
"""

import os
import json
import pandas as pd
from collections import Counter

# ------------------------------
# 1. Load Train/Test Data
# ------------------------------
with open("clean/groceries_train.json", "r") as f:
    train_tx = json.load(f)

with open("clean/groceries_test.json", "r") as f:
    test_tx = json.load(f)

print(f"✅ Train: {len(train_tx)} baskets, Test: {len(test_tx)} baskets")

# ------------------------------
# 2. Build Top Items from Train
# ------------------------------
all_train_items = [item for basket in train_tx for item in basket if item != ""]
train_item_counts = Counter(all_train_items)
top_items = [item for item, _ in train_item_counts.most_common(500)]  # top 500 items
print(f"✅ Top 500 items selected from Train set")

# ------------------------------
# 3. Feature Engineering Function
# ------------------------------
def build_features(transactions, top_items):
    basket_df = pd.DataFrame({"basket": transactions})
    # Basket size
    basket_df["basket_size"] = basket_df["basket"].apply(lambda x: len([i for i in x if i != ""]))
    # Keep only top items
    basket_df["basket_top_items"] = basket_df["basket"].apply(lambda x: [i for i in x if i in top_items])
    # Presence matrix (sparse)
    top_item_df = pd.DataFrame([{item: int(item in basket) for item in top_items} for basket in basket_df["basket_top_items"]])
    return basket_df, top_item_df

# ------------------------------
# 4. Build Features for Train and Test
# ------------------------------
train_basket_df, train_item_matrix = build_features(train_tx, top_items)
test_basket_df, test_item_matrix = build_features(test_tx, top_items)

print(f"\n🔎 Train matrix shape: {train_item_matrix.shape}")
print(f"🔎 Test matrix shape : {test_item_matrix.shape}")

# ------------------------------
# 5. Save Features
# ------------------------------
os.makedirs("features", exist_ok=True)

train_basket_df.to_json("features/train_baskets_features.json", orient="records", lines=True)
train_item_matrix.to_csv("features/train_top_items_matrix.csv", index=False)

test_basket_df.to_json("features/test_baskets_features.json", orient="records", lines=True)
test_item_matrix.to_csv("features/test_top_items_matrix.csv", index=False)

print("\n✅ Feature files saved in 'features/' folder")