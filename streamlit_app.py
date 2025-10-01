# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json
from itertools import combinations
from collections import Counter, defaultdict
import itertools

# Custom modules
import data_processing
import feature_engineering
import eda
from rule_miner import run_miner
import decission_tree
from decission_tree import run_evaluation
from apriori import run_apriori, find_optimal_thresholds

sns.set(style="whitegrid", palette="muted")
st.set_page_config(page_title="Groceries Analytics Platform", layout="wide")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🛒 Groceries Analytics Platform</h1>", unsafe_allow_html=True)
st.markdown("---")

# -------------------------------
# Sidebar Navigation
# -------------------------------
tabs = [
    "Data Preprocessing", 
    "Feature Engineering", 
    "EDA", 
    "Association Rule Mining", 
    "Decision Tree", 
    "Product Recommender",
    "New Basket & Self-Evolving"
]
selected_tab = st.sidebar.radio("Select Module", tabs)
st.sidebar.markdown("💡 **Navigate through the modules to explore your data and recommendations.**")

# -------------------------------
# TAB 1: Data Preprocessing
# -------------------------------
if selected_tab == "Data Preprocessing":
    st.header("📂 Data Preprocessing")
    uploaded_file = st.file_uploader("Upload your groceries CSV file", type=["csv"])
    if uploaded_file:
        transactions = [line.decode("utf-8").strip().split(",") for line in uploaded_file.readlines()]
        st.success(f"✅ {len(transactions)} transactions loaded")

        with st.expander("📋 Sample Baskets", expanded=True):
            for i, basket in enumerate(transactions[:3]):
                st.write(f"Transaction {i+1}: {basket}")

        groceries_df = pd.DataFrame(transactions).fillna("")

        st.subheader("Basket Size Summary")
        basket_sizes = [len([item for item in b if item != ""]) for b in transactions]
        st.dataframe(pd.Series(basket_sizes).describe())

        fig, ax = plt.subplots(figsize=(8,5))
        pd.Series(basket_sizes).hist(bins=30, ax=ax, color="#4CAF50", edgecolor='black')
        ax.set_title("Distribution of Basket Sizes")
        ax.set_xlabel("Number of Products per Basket")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

        if st.button("💾 Save Cleaned Data"):
            os.makedirs("clean", exist_ok=True)
            with open("clean/groceries_baskets.json", "w") as f:
                json.dump(transactions, f)

            from sklearn.model_selection import train_test_split
            train_tx, test_tx = train_test_split(transactions, test_size=0.3, random_state=42)
            with open("clean/groceries_train.json", "w") as f:
                json.dump(train_tx, f)
            with open("clean/groceries_test.json", "w") as f:
                json.dump(test_tx, f)
            groceries_df.to_csv("clean/groceries_clean.csv", index=False)
            st.success("✅ Cleaned datasets saved in 'clean/' folder")

# -------------------------------
# TAB 2: Feature Engineering
# -------------------------------
elif selected_tab == "Feature Engineering":
    st.header("⚙️ Feature Engineering")
    if os.path.exists("clean/groceries_train.json") and os.path.exists("clean/groceries_test.json"):
        with open("clean/groceries_train.json") as f:
            train_tx = json.load(f)
        with open("clean/groceries_test.json") as f:
            test_tx = json.load(f)

        st.info(f"Train: {len(train_tx)} baskets | Test: {len(test_tx)} baskets")

        all_train_items = [item for basket in train_tx for item in basket if item != ""]
        top_items = [item for item, _ in Counter(all_train_items).most_common(500)]
        st.markdown(f"**Top 10 Items:** {top_items[:10]}")

        if st.button("💾 Build & Save Feature Matrices"):
            def build_features(transactions, top_items):
                basket_df = pd.DataFrame({"basket": transactions})
                basket_df["basket_size"] = basket_df["basket"].apply(lambda x: len([i for i in x if i != ""]))
                basket_df["basket_top_items"] = basket_df["basket"].apply(lambda x: [i for i in x if i in top_items])
                top_item_df = pd.DataFrame([{item: int(item in basket) for item in top_items} for basket in basket_df["basket_top_items"]])
                return basket_df, top_item_df

            train_basket_df, train_item_matrix = build_features(train_tx, top_items)
            test_basket_df, test_item_matrix = build_features(test_tx, top_items)

            os.makedirs("features", exist_ok=True)
            train_basket_df.to_json("features/train_baskets_features.json", orient="records", lines=True)
            train_item_matrix.to_csv("features/train_top_items_matrix.csv", index=False)
            test_basket_df.to_json("features/test_baskets_features.json", orient="records", lines=True)
            test_item_matrix.to_csv("features/test_top_items_matrix.csv", index=False)
            st.success("✅ Feature files saved in 'features/' folder")
    else:
        st.warning("Please run Data Preprocessing first to generate train/test datasets.")

# -------------------------------
# TAB 3: EDA
# -------------------------------
elif selected_tab == "EDA":
    st.header("📊 Exploratory Data Analysis")
    if os.path.exists("clean/groceries_baskets.json"):
        with open("clean/groceries_baskets.json") as f:
            transactions = json.load(f)

        all_items = [item for basket in transactions for item in basket if item != ""]
        item_counts = Counter(all_items)
        items_df = pd.DataFrame(item_counts.items(), columns=["Item", "Frequency"]).sort_values(by="Frequency", ascending=False)

        st.subheader("🏆 Top Items")
        st.dataframe(items_df.head(20))

        basket_sizes = [len([item for item in basket if item != ""]) for basket in transactions]
        fig, ax = plt.subplots(figsize=(8,5))
        pd.Series(basket_sizes).hist(bins=30, ax=ax, color="#FF9800", edgecolor='black')
        ax.set_title("Basket Size Distribution")
        ax.set_xlabel("Number of Items per Basket")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

        top_items = item_counts.most_common(15)
        items, counts = zip(*top_items)
        fig2, ax2 = plt.subplots(figsize=(10,6))
        ax2.barh(items[::-1], counts[::-1], color="#4CAF50")
        ax2.set_title("Top 15 Most Frequent Items")
        ax2.set_xlabel("Number of Purchases")
        ax2.set_ylabel("Item")
        st.pyplot(fig2)

        st.subheader("📈 Item Co-occurrence Heatmap")
        top_20_items = [item for item, _ in item_counts.most_common(20)]
        co_occurrence = defaultdict(int)
        for basket in transactions:
            basket_items = [item for item in basket if item in top_20_items]
            for pair in combinations(basket_items, 2):
                co_occurrence[tuple(sorted(pair))] += 1
        co_matrix = pd.DataFrame(0, index=top_20_items, columns=top_20_items)
        for (i,j), count in co_occurrence.items():
            co_matrix.loc[i,j] = count
            co_matrix.loc[j,i] = count
        fig3, ax3 = plt.subplots(figsize=(12,10))
        sns.heatmap(co_matrix, annot=True, fmt=".0f", cmap="YlGnBu", ax=ax3)
        ax3.set_title("Co-occurrence of Top 20 Items")
        st.pyplot(fig3)
    else:
        st.warning("Please run Data Preprocessing first to generate cleaned baskets.")

# -------------------------------
# TAB 4: Association Rule Mining
# -------------------------------
elif selected_tab == "Association Rule Mining":
    st.header("📈 Association Rule Mining")
    if os.path.exists("clean/groceries_baskets.json"):
        with open("clean/groceries_baskets.json") as f:
            baskets = json.load(f)

        st.subheader("⚙️ Manual Thresholds")
        algo = st.radio("Select Algorithm", ["Apriori", "FP-Growth"], horizontal=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            min_support = st.slider("Minimum Support", 0.01, 1.0, 0.05, 0.01)
        with col2:
            min_confidence = st.slider("Minimum Confidence", 0.1, 1.0, 0.5, 0.01)
        with col3:
            min_lift = st.slider("Minimum Lift", 0.1, 10.0, 1.0, 0.1)

        if st.button("🔎 Run Mining"):
            with st.spinner("Mining association rules..."):
                algo_key = "apriori" if algo == "Apriori" else "fp"
                rules = run_miner(algo_key, baskets, min_support, min_confidence, min_lift)
            st.success(f"✅ Found {len(rules)} rules")
            if rules:
                rules_df = pd.DataFrame(rules)
                st.dataframe(rules_df)
                st.download_button("💾 Download Rules as CSV", data=rules_df.to_csv(index=False).encode('utf-8'), file_name="association_rules.csv")

        st.subheader("🤖 Automatic Optimal Threshold Finder")
        if os.path.exists("clean/groceries_train.json") and os.path.exists("clean/groceries_test.json"):
            with open("clean/groceries_train.json") as f:
                train_baskets = json.load(f)
            with open("clean/groceries_test.json") as f:
                test_baskets = json.load(f)

            if st.button("🧠 Find Optimal Thresholds"):
                with st.spinner("Searching optimal thresholds..."):
                    results = find_optimal_thresholds(
                        train_baskets,
                        test_baskets,
                        support_values=[0.01,0.02,0.03,0.05],
                        confidence_values=[0.3,0.4,0.5,0.6],
                        lift_values=[0.5,1.0,1.2,1.5]
                    )
                st.success("✅ Optimal thresholds found!")
                st.metric("Optimal Support", results['optimal_support'])
                st.metric("Optimal Confidence", results['optimal_confidence'])
                st.metric("Optimal Lift", results['optimal_lift'])
                st.write(f"**Coverage on test set:** {results['coverage']*100:.2f}%")
                st.write(f"**Average Confidence:** {results['avg_confidence']:.2f}")
                st.write(f"**Average Lift:** {results['avg_lift']:.2f}")
                st.write(f"**Number of Rules:** {len(results['rules'])}")
                if results['rules']:
                    st.dataframe(pd.DataFrame(results['rules']))
                    st.download_button("💾 Download Optimal Rules as CSV", data=pd.DataFrame(results['rules']).to_csv(index=False).encode('utf-8'), file_name="optimal_association_rules.csv")
        else:
            st.warning("Please run Data Preprocessing first to generate train/test datasets.")

# -------------------------------
# TAB 5: Decision Tree
# -------------------------------
elif selected_tab == "Decision Tree":
    st.header("🌳 Decision Tree for Basket Segmentation")
    feature_file = "features/train_baskets_features.json"
    if os.path.exists(feature_file):
        with open(feature_file, "r") as f:
            X_data = [json.loads(line) for line in f]

        st.success(f"✅ Loaded {len(X_data)} feature entries for decision tree.")

        X = [decission_tree.extract_features(d) for d in X_data]
        y = [decission_tree.label_basket(d) for d in X_data]
        features = list(X[0].keys())
        tree_model = decission_tree.build_tree(X, y, features, max_depth=3)

        st.subheader("📜 Decision Tree Rules")
        with st.expander("View Tree Rules", expanded=True):
            st.text(decission_tree.tree_to_rules(tree_model))

        st.subheader("🌳 Decision Tree Visualization")
        dot = decission_tree.tree_to_graphviz(tree_model)
        st.graphviz_chart(dot.source)

        st.subheader("🛒 Classify a Sample Basket")
        sample_input = {f: st.checkbox(f"Has {f}", value=False) for f in features}
        if st.button("Predict Segment"):
            predicted_segment = decission_tree.classify_segment(sample_input, tree_model)
            st.success(f"Predicted Basket Segment: {predicted_segment}")

        st.subheader("📊 Model Evaluation")
        acc, report, cm = run_evaluation(max_depth=3)
        st.metric("Accuracy", f"{acc*100:.2f}%")
        st.write("**Classification Report:**")
        st.dataframe(pd.DataFrame(report).transpose().style.background_gradient(cmap="Blues"))

        st.write("**Confusion Matrix:**")
        fig, ax = plt.subplots()
        labels = ["Small Basket", "Medium Basket", "Big Basket"]
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels, ax=ax)
        ax.set_xlabel("Predicted")
        ax.set_ylabel("Actual")
        st.pyplot(fig)
    else:
        st.warning("⚠️ Please run Feature Engineering first to generate feature matrices.")

# -------------------------------
# TAB 6: Product Recommender
# -------------------------------
elif selected_tab == "Product Recommender":
    st.header("🔮 Product Recommender")

    BASE_DIR = "/Users/ponnigithav/Desktop/code-synapse"
    NEW_BASKETS_FILE = os.path.join(BASE_DIR, "data", "new_baskets.json")

    if os.path.exists("clean/groceries_baskets.json"):
        with open("clean/groceries_baskets.json", "r") as f:
            baskets = json.load(f)
    else:
        st.warning("⚠️ No baskets available. Upload data first.")
        baskets = []

    if baskets:
        from apriori import run_apriori
        min_support = 0.02
        min_confidence = 0.3
        min_lift = 1.0
        rules = run_apriori(baskets, min_support, min_confidence, min_lift)

        all_items = sorted(
            set(
                itertools.chain.from_iterable(
                    r["if"] + (r["then"] if isinstance(r["then"], list) else [r["then"]])
                    for r in rules
                )
            )
        )

        if "basket" not in st.session_state:
            st.session_state.basket = []

        product_choice = st.selectbox("Select a product to add:", all_items)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ Add to Basket"):
                if product_choice not in st.session_state.basket:
                    st.session_state.basket.append(product_choice)
        with col2:
            if st.button("🗑️ Clear Basket"):
                st.session_state.basket = []

        st.markdown("**Your Basket:**")
        st.info(st.session_state.basket if st.session_state.basket else "Empty")

        if st.session_state.basket:
            top_n = st.slider("Number of recommendations", 1, 10, 5)
            recs = []
            basket_set = set(st.session_state.basket)
            for rule in rules:
                if set(rule["if"]).issubset(basket_set):
                    rec_items = rule["then"] if isinstance(rule["then"], list) else [rule["then"]]
                    for item in rec_items:
                        if item not in basket_set:
                            recs.append(item)
            recs = list(dict.fromkeys(recs))[:top_n]

            st.subheader("✨ Recommended Products")
            if recs:
                for r in recs:
                    st.success(f"✅ {r}")
            else:
                st.info("No recommendations found for this basket.")

# -------------------------------
# TAB 7: New Basket & Self-Evolving
# -------------------------------
elif selected_tab == "New Basket & Self-Evolving":
    st.header("🆕 Add New Baskets & Update Engine")

    BASE_DIR = "/Users/ponnigithav/Desktop/code-synapse"
    NEW_BASKETS_FILE = os.path.join(BASE_DIR, "data", "new_baskets.json")
    OUTPUT_RECOMMENDER = os.path.join(BASE_DIR, "product_recommender.py")

    st.subheader("Enter New Baskets Manually")
    st.write("Add products separated by commas for each basket:")

    if "new_baskets" not in st.session_state:
        st.session_state.new_baskets = []

    new_basket_input = st.text_input("New Basket (comma-separated)", "")
    if st.button("➕ Add Basket"):
        if new_basket_input.strip():
            basket_items = [item.strip() for item in new_basket_input.split(",") if item.strip()]
            st.session_state.new_baskets.append(basket_items)
            st.success(f"Added basket: {basket_items}")

    if st.session_state.new_baskets:
        st.markdown("**New Baskets Pending:**")
        for i, b in enumerate(st.session_state.new_baskets, 1):
            st.write(f"{i}: {b}")

    st.subheader("Or Upload New Baskets File")
    uploaded_file = st.file_uploader("Upload JSON or CSV file", type=["json", "csv"])
    if uploaded_file:
        if uploaded_file.type == "application/json":
            file_baskets = json.load(uploaded_file)
        else:
            file_baskets = [line.decode("utf-8").strip().split(",") for line in uploaded_file.readlines()]
        st.session_state.new_baskets.extend(file_baskets)
        st.success(f"Loaded {len(file_baskets)} baskets from file.")

    if st.button("🤖 Run Self-Evolving Engine on New Baskets"):
        if st.session_state.new_baskets:
            os.makedirs(os.path.dirname(NEW_BASKETS_FILE), exist_ok=True)
            with open(NEW_BASKETS_FILE, "w") as f:
                json.dump(st.session_state.new_baskets, f)

            import self_evolving_engine
            self_evolving_engine.run_self_evolving_engine_once(st.session_state.new_baskets)
            st.success(f"✅ Engine updated rules & regenerated {OUTPUT_RECOMMENDER}!")
            st.session_state.new_baskets = []
        else:
            st.warning("⚠️ No new baskets to process.")