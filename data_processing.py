#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Preprocessing for Groceries Dataset
"""

import pandas as pd
import os
import matplotlib.pyplot as plt

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
print(groceries.isnull().sum().head())  # only sample output

# Fill NaN with empty string
groceries = groceries.fillna("")

print("✅ Missing values handled")

# ------------------------------
# 4. Duplicate Check & Removal
# ------------------------------
before = len(groceries)
groceries = groceries.drop_duplicates()
after = len(groceries)

print(f"\n🔎 Duplicate Check: {before - after} duplicate rows removed")
print("✅ Duplicates removed")

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

# Save baskets as JSON (better for variable-length)
import json
with open("clean/groceries_baskets.json", "w") as f:
    json.dump(transactions, f)

# Save ragged DataFrame as CSV
groceries.to_csv("clean/groceries_clean.csv", index=False)

print("\n✅ Cleaned datasets saved in 'clean/' folder")