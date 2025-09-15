import pandas as pd
import os
import matplotlib.pyplot as plt

# ------------------------------
# 1. Load Data
# ------------------------------
orders = pd.read_csv("archive/orders.csv")
order_products_prior = pd.read_csv("archive/order_products__prior.csv")
order_products_train = pd.read_csv("archive/order_products__train.csv")
products = pd.read_csv("archive/products.csv")
aisles = pd.read_csv("archive/aisles.csv")
departments = pd.read_csv("archive/departments.csv")

print("✅ Data Loaded Successfully")

# ------------------------------
# 2. Null Value Check & Handling
# ------------------------------
print("\n🔎 Null Value Check:")
print("Orders:\n", orders.isnull().sum())
print("\nOrder Products Prior:\n", order_products_prior.isnull().sum())
print("\nOrder Products Train:\n", order_products_train.isnull().sum())
print("\nProducts:\n", products.isnull().sum())
print("\nAisles:\n", aisles.isnull().sum())
print("\nDepartments:\n", departments.isnull().sum())

# Fill missing values in days_since_prior_order with median
orders["days_since_prior_order"] = orders["days_since_prior_order"].fillna(
    orders["days_since_prior_order"].median()
)

print("\n✅ Missing values handled")

# ------------------------------
# 3. Duplicate Check & Removal
# ------------------------------
print("\n🔎 Duplicate Check:")
print("Orders:", orders.duplicated().sum())
print("Order Products Prior:", order_products_prior.duplicated().sum())
print("Order Products Train:", order_products_train.duplicated().sum())
print("Products:", products.duplicated().sum())
print("Aisles:", aisles.duplicated().sum())
print("Departments:", departments.duplicated().sum())

# Drop duplicates if any
orders = orders.drop_duplicates()
order_products_prior = order_products_prior.drop_duplicates()
order_products_train = order_products_train.drop_duplicates()
products = products.drop_duplicates()
aisles = aisles.drop_duplicates()
departments = departments.drop_duplicates()

print("✅ Duplicates removed")

# ------------------------------
# 4. Data Type Fixes
# ------------------------------
orders["order_id"] = orders["order_id"].astype(int)
orders["user_id"] = orders["user_id"].astype(int)
orders["order_number"] = orders["order_number"].astype(int)
orders["order_dow"] = orders["order_dow"].astype(int)
orders["order_hour_of_day"] = orders["order_hour_of_day"].astype(int)
orders["days_since_prior_order"] = orders["days_since_prior_order"].astype(int)

print("✅ Data types fixed")

# ------------------------------
# 5. Basket Size Summary
# ------------------------------
basket_size = order_products_prior.groupby("order_id")["product_id"].count()
print("\n🔎 Basket Size Summary:\n", basket_size.describe())

plt.figure(figsize=(8, 5))
basket_size.hist(bins=30)
plt.title("Distribution of Basket Sizes")
plt.xlabel("Number of Products per Order")
plt.ylabel("Frequency")
plt.show()

# ------------------------------
# 6. Save Cleaned Data
# ------------------------------
os.makedirs("clean", exist_ok=True)

orders.to_csv("clean/orders_clean.csv", index=False)
order_products_prior.to_csv("clean/order_products_prior_clean.csv", index=False)
order_products_train.to_csv("clean/order_products_train_clean.csv", index=False)
products.to_csv("clean/products_clean.csv", index=False)
aisles.to_csv("clean/aisles_clean.csv", index=False)
departments.to_csv("clean/departments_clean.csv", index=False)

print("\n✅ Cleaned datasets saved in 'clean/' folder")