# 🛒 Instacart Market Basket Analysis - EDA

# =======================
# 1. Import Libraries
# =======================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# =======================
# 2. Load Data
# =======================
orders = pd.read_csv("archive/orders.csv")
order_products = pd.read_csv("archive/order_products__prior.csv")
products = pd.read_csv("archive/products.csv")
aisles = pd.read_csv("archive/aisles.csv")
departments = pd.read_csv("archive/departments.csv")

# Merge product details into order_products
order_products = order_products.merge(products, on="product_id", how="left")
order_products = order_products.merge(aisles, on="aisle_id", how="left")
order_products = order_products.merge(departments, on="department_id", how="left")

print("✅ Data Loaded Successfully")

# =======================
# 3. Univariate Analysis
# =======================

# Orders per user
orders_per_user = orders.groupby("user_id")["order_id"].count()
plt.figure(figsize=(8,5))
sns.histplot(orders_per_user, bins=30, kde=False)
plt.title("Orders per User")
plt.xlabel("Number of Orders")
plt.ylabel("Users")
plt.show()

# Days since prior order
plt.figure(figsize=(8,5))
sns.histplot(orders["days_since_prior_order"].dropna(), bins=30, kde=False)
plt.title("Days Since Prior Order")
plt.xlabel("Days")
plt.ylabel("Frequency")
plt.show()

# Basket size distribution
basket_size = order_products.groupby("order_id")["product_id"].count()
plt.figure(figsize=(8,5))
sns.histplot(basket_size, bins=30, kde=False)
plt.title("Basket Size Distribution")
plt.xlabel("Products per Order")
plt.ylabel("Frequency")
plt.show()

# Most popular products
plt.figure(figsize=(10,6))
order_products["product_name"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Most Popular Products")
plt.ylabel("Count")
plt.show()

# =======================
# 4. Bivariate Analysis
# =======================

# Relationship between order_number and reorder ratio
orders_with_reorder = order_products.groupby("order_id")["reordered"].mean().reset_index()
merged_orders = orders.merge(orders_with_reorder, on="order_id", how="left")

plt.figure(figsize=(8,5))
sns.lineplot(x="order_number", y="reordered", data=merged_orders, errorbar=None)
plt.title("Reorder Ratio vs. Order Number")
plt.xlabel("Order Number")
plt.ylabel("Reorder Ratio")
plt.show()

# Basket size vs reorder ratio
basket_reorder = order_products.groupby("order_id")["reordered"].mean()
plt.figure(figsize=(8,5))
sns.scatterplot(x=basket_size, y=basket_reorder)
plt.title("Basket Size vs. Reorder Ratio")
plt.xlabel("Basket Size")
plt.ylabel("Reorder Ratio")
plt.show()

# Department vs Number of Products
plt.figure(figsize=(12,6))
sns.countplot(y="department", data=order_products, order=order_products["department"].value_counts().index)
plt.title("Products Bought by Department")
plt.show()

# =======================
# 5. Multivariate Analysis
# =======================

# Correlation Heatmap
features = orders[["order_number", "days_since_prior_order"]].dropna()
plt.figure(figsize=(6,4))
sns.heatmap(features.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Top 5 aisles across top 5 departments
top_aisles = order_products["aisle"].value_counts().head(5).index
top_depts = order_products["department"].value_counts().head(5).index

subset = order_products[(order_products["aisle"].isin(top_aisles)) & 
                        (order_products["department"].isin(top_depts))]

plt.figure(figsize=(12,6))
sns.countplot(x="aisle", hue="department", data=subset)
plt.title("Top Aisles within Top Departments")
plt.show()

# Pairplot (sampled for performance)
sample_orders = orders.sample(5000, random_state=42)
sns.pairplot(sample_orders[["order_number","days_since_prior_order","eval_set"]], hue="eval_set")
plt.show()