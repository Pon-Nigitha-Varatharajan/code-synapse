#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 20:27:20 2025

@author: ponnigithav
"""

import pandas as pd

# ------------------------------
# 1. Load Cleaned Data
# ------------------------------
orders = pd.read_csv("clean/orders_clean.csv")
order_products_prior = pd.read_csv("clean/order_products_prior_clean.csv")
products = pd.read_csv("clean/products_clean.csv")
departments = pd.read_csv("clean/departments_clean.csv")
aisles = pd.read_csv("clean/aisles_clean.csv")

print("✅ Cleaned Data Loaded")

# Merge product info into prior orders
order_products_prior = order_products_prior.merge(products, on="product_id", how="left")
order_products_prior = order_products_prior.merge(departments, on="department_id", how="left")
order_products_prior = order_products_prior.merge(aisles, on="aisle_id", how="left")

# ------------------------------
# 2. Basket-Level Features
# ------------------------------
basket_df = order_products_prior.groupby("order_id")["product_name"].apply(list).reset_index()
basket_df.rename(columns={"product_name": "basket"}, inplace=True)

print("\n🔎 Example Basket:")
print(basket_df.head(3))

# ------------------------------
# 3. User-Level Features
# ------------------------------

# Total orders per user
user_orders = orders.groupby("user_id")["order_id"].count().reset_index()
user_orders.rename(columns={"order_id": "total_orders"}, inplace=True)

# Average basket size
basket_size = order_products_prior.groupby("order_id")["product_id"].count().reset_index()
basket_size.rename(columns={"product_id": "basket_size"}, inplace=True)
user_avg_basket = orders.merge(basket_size, on="order_id").groupby("user_id")["basket_size"].mean().reset_index()
user_avg_basket.rename(columns={"basket_size": "avg_basket_size"}, inplace=True)

# Recency (days since last order)
user_recency = orders.groupby("user_id")["days_since_prior_order"].max().reset_index()
user_recency.rename(columns={"days_since_prior_order": "recency"}, inplace=True)

# Reorder ratio  ✅ FIX: Merge orders to bring user_id
merged = order_products_prior.merge(orders[["order_id", "user_id"]], on="order_id", how="left")
user_reorder = merged.groupby("user_id")["reordered"].mean().reset_index()
user_reorder.rename(columns={"reordered": "reorder_ratio"}, inplace=True)

# Top department per user
top_department = merged.groupby(["user_id", "department"]).size().reset_index(name="count")
top_department = top_department.loc[top_department.groupby("user_id")["count"].idxmax()]
top_department = top_department[["user_id", "department"]].rename(columns={"department": "top_department"})

# ------------------------------
# 4. Combine User Features
# ------------------------------
user_features = user_orders.merge(user_avg_basket, on="user_id", how="left")
user_features = user_features.merge(user_recency, on="user_id", how="left")
user_features = user_features.merge(user_reorder, on="user_id", how="left")
user_features = user_features.merge(top_department, on="user_id", how="left")

print("\n✅ User-Level Features (sample):")
print(user_features.head(5))

# ------------------------------
# 5. Save Feature Files
# ------------------------------
import os
os.makedirs("features", exist_ok=True)

basket_df.to_json("features/baskets.json", orient="records", lines=True)
user_features.to_csv("features/user_profiles.csv", index=False)
print("\n✅ Features saved: 'features/baskets.json' & 'features/user_profiles.csv'")










