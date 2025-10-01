#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Preprocessing for Groceries Dataset with Train/Test Split
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import json

# ------------------------------
# 1. Load Data
# ------------------------------
with open("archive/groceries.csv", "r") as f:
    transactions = [line.strip().split(",") for line in f.readlines()]

print(f"✅ Groceries Data Loaded: {len(transactions)} transactions")
print("\n🔎 Example baskets:")
for i in range(3):
    print(f"Transaction {i+1}: {transactions[i]}")

# ------------------------------
# 2. Convert to DataFrame (ragged)
# ------------------------------
groceries = pd.DataFrame(transactions)
print("\n✅ Data converted to DataFrame (ragged format)")
print(groceries.head())

# ------------------------------
# 3. Null Value Check & Handling
# ------------------------------
print("\n🔎 Null Value Check (from ragged baskets):")
print(groceries.isnull().sum())  # only sample output

# Fill NaN with empty string
groceries = groceries.fillna("")
print("✅ Missing values handled")

# ------------------------------
# 4. Train/Test Split
# ------------------------------
train_tx, test_tx = train_test_split(transactions, test_size=0.3, random_state=42)

print(f"\n✅ Train/Test Split Complete")
print(f"   Train set: {len(train_tx)} baskets")
print(f"   Test set : {len(test_tx)} baskets")

# ------------------------------
# 5. Basket Size Summary
# ------------------------------
basket_sizes = [len([item for item in basket if item != ""]) for basket in transactions]

print("\n🔎 Basket Size Summary:")
print(pd.Series(basket_sizes).describe())

plt.figure(figsize=(8, 5))
pd.Series(basket_sizes).hist(bins=30)
plt.title("Distribution of Basket Sizes")
plt.xlabel("Number of Products per Basket")
plt.ylabel("Frequency")
plt.show()

# ------------------------------
# 6. Save Cleaned Data
# ------------------------------
os.makedirs("clean", exist_ok=True)

# Save full baskets
with open("clean/groceries_baskets.json", "w") as f:
    json.dump(transactions, f)

# Save train/test separately
with open("clean/groceries_train.json", "w") as f:
    json.dump(train_tx, f)

with open("clean/groceries_test.json", "w") as f:
    json.dump(test_tx, f)

# Save ragged DataFrame as CSV
groceries.to_csv("clean/groceries_clean.csv", index=False)

print("\n✅ Cleaned datasets (full/train/test) saved in 'clean/' folder")