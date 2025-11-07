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
import csv

# Custom modules
import data_processing
import feature_engineering
import eda
from rule_miner import run_miner
import decission_tree
from decission_tree import run_evaluation
from apriori import run_apriori, find_optimal_thresholds

# Configure page
st.set_page_config(
    page_title="Code-Synapse",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #A23B72;
        border-bottom: 2px solid #F18F01;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 0.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .info-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2E86AB;
        margin: 1rem 0;
    }
    .success-card {
        background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .warning-card {
        background: linear-gradient(135deg, #f46b45 0%, #eea849 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2E86AB 0%, #A23B72 100%);
    }
    .sidebar .sidebar-content .sidebar-title {
        color: white !important;
        font-weight: 700;
    }
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .tab-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🛒 Code-Synapse</h1>', unsafe_allow_html=True)
st.markdown("---")

# -------------------------------
# Sidebar Navigation
# -------------------------------
with st.sidebar:
    st.markdown('<h2 class="sidebar-title">📊 Navigation</h2>', unsafe_allow_html=True)
    st.markdown("---")
    
    tabs = [
        "📂 Data Preprocessing", 
        "⚙️ Feature Engineering", 
        "📊 EDA", 
        "📈 Association Rules", 
        "🌳 Decision Tree", 
        "🔮 Product Recommender",
        "🔄 Self-Evolving Engine"
    ]
    selected_tab = st.radio("Select Module", tabs)
    
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.info("""
    - Start with Data Preprocessing
    - Run modules sequentially
    - Use optimal thresholds for best results
    """)
    
    # Status indicator
    st.markdown("### 🟢 System Status")
    status_cols = st.columns(2)
    with status_cols[0]:
        data_exists = os.path.exists("clean/groceries_baskets.json")
        st.metric("Data", "✅" if data_exists else "❌")
    with status_cols[1]:
        features_exists = os.path.exists("features/train_baskets_features.json")
        st.metric("Features", "✅" if features_exists else "❌")

# -------------------------------
# TAB 1: Data Preprocessing
# -------------------------------
if selected_tab == "📂 Data Preprocessing":
    st.markdown('<div class="tab-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">📂 Data Preprocessing</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        uploaded_file = st.file_uploader("Upload your groceries CSV file", type=["csv"], 
                                       help="Upload a CSV file where each row represents a transaction with comma-separated items")
    with col2:
        st.markdown("""
        <div class="info-card">
        <strong>Expected Format:</strong><br>
        Each row: item1,item2,item3,...<br>
        Example: milk,bread,eggs,butter
        </div>
        """, unsafe_allow_html=True)
    
    if uploaded_file:
        with st.spinner("🔄 Processing uploaded data..."):
            transactions = [line.decode("utf-8").strip().split(",") for line in uploaded_file.readlines()]
        
        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Transactions", len(transactions))
        with col2:
            total_items = sum(len([item for item in b if item != ""]) for b in transactions)
            st.metric("Total Items", total_items)
        with col3:
            avg_basket_size = total_items / len(transactions)
            st.metric("Avg Basket Size", f"{avg_basket_size:.1f}")
        with col4:
            unique_items = len(set(item for basket in transactions for item in basket if item != ""))
            st.metric("Unique Items", unique_items)
        
        # Sample Data
        with st.expander("📋 Sample Transactions (First 5)", expanded=True):
            sample_df = pd.DataFrame(transactions[:5]).fillna("")
            st.dataframe(sample_df, use_container_width=True)
        
        # Basket Size Analysis
        st.markdown("#### 📊 Basket Size Distribution")
        basket_sizes = [len([item for item in b if item != ""]) for b in transactions]
        
        fig_col1, fig_col2 = st.columns([2, 1])
        with fig_col1:
            fig, ax = plt.subplots(figsize=(10, 6))
            pd.Series(basket_sizes).hist(bins=30, ax=ax, color="#2E86AB", alpha=0.7, edgecolor='white')
            ax.set_title("Distribution of Basket Sizes", fontsize=14, fontweight='bold')
            ax.set_xlabel("Number of Products per Basket")
            ax.set_ylabel("Frequency")
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)
        
        with fig_col2:
            size_stats = pd.Series(basket_sizes).describe()
            st.dataframe(size_stats, use_container_width=True)
        
        # Data Saving
        st.markdown("#### 💾 Save Processed Data")
        if st.button("💾 Save Cleaned Data", use_container_width=True):
            with st.spinner("Saving cleaned data..."):
                os.makedirs("clean", exist_ok=True)
                with open("clean/groceries_baskets.json", "w") as f:
                    json.dump(transactions, f)

                from sklearn.model_selection import train_test_split
                train_tx, test_tx = train_test_split(transactions, test_size=0.3, random_state=42)
                with open("clean/groceries_train.json", "w") as f:
                    json.dump(train_tx, f)
                with open("clean/groceries_test.json", "w") as f:
                    json.dump(test_tx, f)
                
                groceries_df = pd.DataFrame(transactions).fillna("")
                groceries_df.to_csv("clean/groceries_clean.csv", index=False)
                
                st.success("✅ Cleaned datasets successfully saved in 'clean/' folder")
                st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# TAB 2: Feature Engineering
# -------------------------------
elif selected_tab == "⚙️ Feature Engineering":
    st.markdown('<div class="tab-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">⚙️ Feature Engineering</h2>', unsafe_allow_html=True)
    
    if os.path.exists("clean/groceries_train.json") and os.path.exists("clean/groceries_test.json"):
        with open("clean/groceries_train.json") as f:
            train_tx = json.load(f)
        with open("clean/groceries_test.json") as f:
            test_tx = json.load(f)
        
        # Dataset Info
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Train Dataset</h3>
                <h2>{len(train_tx):,}</h2>
                <p>Transactions</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Test Dataset</h3>
                <h2>{len(test_tx):,}</h2>
                <p>Transactions</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Item Analysis
        all_train_items = [item for basket in train_tx for item in basket if item != ""]
        item_counts = Counter(all_train_items)
        top_items = [item for item, _ in item_counts.most_common(500)]
        
        st.markdown("#### 🏆 Top Items Analysis")
        col1, col2 = st.columns([2, 1])
        with col1:
            top_10_df = pd.DataFrame(item_counts.most_common(10), columns=["Item", "Count"])
            st.dataframe(top_10_df.style.background_gradient(subset=['Count'], cmap='Blues'), 
                        use_container_width=True)
        with col2:
            st.markdown(f"""
            <div class="info-card">
            <strong>Feature Engineering</strong><br>
            Using top <strong>500</strong> items<br>
            Creating binary features<br>
            Basket size features
            </div>
            """, unsafe_allow_html=True)
        
        # Feature Building
        st.markdown("#### 🛠️ Build Feature Matrices")
        if st.button("💾 Build & Save Feature Matrices", use_container_width=True):
            with st.spinner("Building feature matrices..."):
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
                
                st.success("✅ Feature files successfully saved in 'features/' folder")
                
                # Show feature preview
                st.markdown("#### 🔍 Feature Matrix Preview")
                st.dataframe(train_item_matrix.head(10), use_container_width=True)
    else:
        st.markdown("""
        <div class="warning-card">
            <h3>⚠️ Data Required</h3>
            <p>Please run Data Preprocessing first to generate train/test datasets.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# TAB 3: EDA
# -------------------------------
elif selected_tab == "📊 EDA":
    st.markdown('<div class="tab-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">📊 Exploratory Data Analysis</h2>', unsafe_allow_html=True)
    
    if os.path.exists("clean/groceries_baskets.json"):
        with open("clean/groceries_baskets.json") as f:
            transactions = json.load(f)

        all_items = [item for basket in transactions for item in basket if item != ""]
        item_counts = Counter(all_items)
        items_df = pd.DataFrame(item_counts.items(), columns=["Item", "Frequency"]).sort_values(by="Frequency", ascending=False)

        # Summary Metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Transactions", len(transactions))
        with col2:
            st.metric("Total Items", len(all_items))
        with col3:
            st.metric("Unique Items", len(item_counts))
        with col4:
            st.metric("Avg Items/Basket", f"{len(all_items)/len(transactions):.1f}")

        # Top Items Table
        st.markdown("#### 🏆 Top 20 Most Frequent Items")
        st.dataframe(items_df.head(20).style.background_gradient(subset=['Frequency'], cmap='Greens'), 
                    use_container_width=True)

        # Visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📦 Basket Size Distribution")
            basket_sizes = [len([item for item in basket if item != ""]) for basket in transactions]
            fig, ax = plt.subplots(figsize=(10, 6))
            pd.Series(basket_sizes).hist(bins=30, ax=ax, color="#F18F01", alpha=0.7, edgecolor='white')
            ax.set_title("Basket Size Distribution", fontweight='bold')
            ax.set_xlabel("Number of Items per Basket")
            ax.set_ylabel("Frequency")
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)

        with col2:
            st.markdown("#### 🥇 Top 15 Items")
            top_items = item_counts.most_common(15)
            items, counts = zip(*top_items)
            fig, ax = plt.subplots(figsize=(10, 8))
            ax.barh(items[::-1], counts[::-1], color="#A23B72", alpha=0.7)
            ax.set_title("Top 15 Most Frequent Items", fontweight='bold')
            ax.set_xlabel("Number of Purchases")
            ax.set_ylabel("Item")
            ax.grid(True, alpha=0.3)
            st.pyplot(fig)

        # Co-occurrence Heatmap
        st.markdown("#### 🔗 Item Co-occurrence Heatmap (Top 20 Items)")
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
        
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(co_matrix, annot=True, fmt=".0f", cmap="YlGnBu", ax=ax, 
                   cbar_kws={'label': 'Co-occurrence Count'})
        ax.set_title("Co-occurrence of Top 20 Items", fontweight='bold', pad=20)
        st.pyplot(fig)
        
    else:
        st.markdown("""
        <div class="warning-card">
            <h3>⚠️ Data Required</h3>
            <p>Please run Data Preprocessing first to generate cleaned baskets.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# TAB 4: Association Rule Mining
# -------------------------------
elif selected_tab == "📈 Association Rules":
    st.markdown('<div class="tab-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">📈 Association Rule Mining</h2>', unsafe_allow_html=True)
    
    if os.path.exists("clean/groceries_baskets.json"):
        with open("clean/groceries_baskets.json") as f:
            baskets = json.load(f)

        # Manual Threshold Section
        st.markdown("#### ⚙️ Manual Rule Mining")
        col1, col2 = st.columns([1, 1])
        
        with col1:
            algo = st.radio("Select Algorithm", ["Apriori", "FP-Growth"], horizontal=True,
                          help="Apriori: Better for small datasets | FP-Growth: More efficient for large datasets")
            
        with col2:
            st.markdown("""
            <div class="info-card">
            <strong>Parameter Guide:</strong><br>
            • Support: Frequency of itemset<br>
            • Confidence: Rule accuracy<br>
            • Lift: Rule interestingness
            </div>
            """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            min_support = st.slider("Minimum Support", 0.001, 0.5, 0.02, 0.001,
                                  help="Minimum frequency of itemset in the dataset")
        with col2:
            min_confidence = st.slider("Minimum Confidence", 0.1, 1.0, 0.5, 0.01,
                                     help="Minimum accuracy for the rule")
        with col3:
            min_lift = st.slider("Minimum Lift", 0.1, 10.0, 1.0, 0.1,
                               help="Minimum interestingness measure")

        if st.button("🔎 Mine Association Rules", use_container_width=True):
            with st.spinner("Mining association rules..."):
                algo_key = "apriori" if algo == "Apriori" else "fp"
                rules = run_miner(algo_key, baskets, min_support, min_confidence, min_lift)
            
            if rules:
                rules_df = pd.DataFrame(rules)
                st.success(f"✅ Found {len(rules)} rules")
                
                # Rules Summary
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Rules", len(rules))
                with col2:
                    avg_conf = rules_df['confidence'].mean()
                    st.metric("Avg Confidence", f"{avg_conf:.3f}")
                with col3:
                    avg_lift = rules_df['lift'].mean()
                    st.metric("Avg Lift", f"{avg_lift:.3f}")
                
                # Display Rules
                st.markdown("#### 📋 Discovered Rules")
                st.dataframe(rules_df.style.background_gradient(subset=['confidence', 'lift'], 
                                                              cmap='YlOrBr'), 
                           use_container_width=True)
                
                # Download
                csv_data = rules_df.to_csv(index=False).encode('utf-8')
                st.download_button("💾 Download Rules as CSV", data=csv_data, 
                                 file_name="association_rules.csv", 
                                 mime="text/csv", use_container_width=True)
            else:
                st.warning("❌ No rules found with current thresholds. Try lowering the minimum support or confidence.")

        # Automatic Threshold Finder
        st.markdown("---")
        st.markdown("#### 🤖 Automatic Optimal Threshold Finder")
        
        if os.path.exists("clean/groceries_train.json") and os.path.exists("clean/groceries_test.json"):
            with open("clean/groceries_train.json") as f:
                train_baskets = json.load(f)
            with open("clean/groceries_test.json") as f:
                test_baskets = json.load(f)

            if st.button("🧠 Find Optimal Thresholds", use_container_width=True):
                with st.spinner("Searching for optimal thresholds... This may take a few minutes."):
                    results = find_optimal_thresholds(
                        train_baskets,
                        test_baskets,
                        support_values=[0.01, 0.02, 0.03, 0.05],
                        confidence_values=[0.3, 0.4, 0.5, 0.6],
                        lift_values=[0.5, 1.0, 1.2, 1.5]
                    )
                
                st.success("✅ Optimal thresholds found!")
                
                # Display Results
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Optimal Support", f"{results['optimal_support']:.3f}")
                with col2:
                    st.metric("Optimal Confidence", f"{results['optimal_confidence']:.3f}")
                with col3:
                    st.metric("Optimal Lift", f"{results['optimal_lift']:.3f}")
                with col4:
                    st.metric("Test Coverage", f"{results['coverage']*100:.1f}%")
                
                # Additional Metrics
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Number of Rules", len(results['rules']))
                with col2:
                    st.metric("Avg Confidence", f"{results['avg_confidence']:.3f}")
                
                if results['rules']:
                    st.markdown("#### 📋 Optimal Rules")
                    optimal_rules_df = pd.DataFrame(results['rules'])
                    st.dataframe(optimal_rules_df.style.background_gradient(subset=['confidence', 'lift'], 
                                                                          cmap='YlOrBr'), 
                               use_container_width=True)
                    
                    # Download optimal rules
                    optimal_csv = optimal_rules_df.to_csv(index=False).encode('utf-8')
                    st.download_button("💾 Download Optimal Rules", data=optimal_csv, 
                                     file_name="optimal_association_rules.csv", 
                                     mime="text/csv", use_container_width=True)
        else:
            st.warning("⚠️ Please run Data Preprocessing first to generate train/test datasets.")
    else:
        st.markdown("""
        <div class="warning-card">
            <h3>⚠️ Data Required</h3>
            <p>Please run Data Preprocessing first to load the baskets data.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# TAB 5: Decision Tree
# -------------------------------
elif selected_tab == "🌳 Decision Tree":
    st.markdown('<div class="tab-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">🌳 Decision Tree for Basket Segmentation</h2>', unsafe_allow_html=True)
    
    feature_file = "features/train_baskets_features.json"
    if os.path.exists(feature_file):
        with open(feature_file, "r") as f:
            X_data = [json.loads(line) for line in f]

        st.success(f"✅ Loaded {len(X_data)} feature entries for decision tree modeling.")

        # Model Configuration
        st.markdown("#### ⚙️ Model Configuration")
        max_depth = st.slider("Maximum Tree Depth", 2, 5, 3, 
                            help="Controls the complexity of the decision tree")
        
        if st.button("🌳 Build Decision Tree", use_container_width=True):
            with st.spinner("Building decision tree model..."):
                X = [decission_tree.extract_features(d) for d in X_data]
                y = [decission_tree.label_basket(d) for d in X_data]
                features = list(X[0].keys())
                tree_model = decission_tree.build_tree(X, y, features, max_depth=max_depth)

            # Display Results
            st.markdown("#### 📜 Decision Tree Rules")
            with st.expander("View Tree Rules", expanded=True):
                rules_text = decission_tree.tree_to_rules(tree_model)
                st.code(rules_text, language='text')
            
            st.markdown("#### 🌳 Decision Tree Visualization")
            dot = decission_tree.tree_to_graphviz(tree_model)
            st.graphviz_chart(dot.source)

            # Interactive Prediction
            st.markdown("#### 📊 Model Evaluation")
            acc, report, cm = run_evaluation(max_depth=max_depth)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Accuracy", f"{acc*100:.2f}%")
            with col2:
                st.metric("Training Samples", len(X_data))
            
            st.markdown("##### 📈 Classification Report")
            report_df = pd.DataFrame(report).transpose()
            st.dataframe(report_df.style.background_gradient(cmap="Blues", axis=0), 
                        use_container_width=True)
            
            st.markdown("##### 🎯 Confusion Matrix")
            fig, ax = plt.subplots(figsize=(8, 6))
            labels = ["Small Basket", "Medium Basket", "Big Basket"]
            sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", 
                       xticklabels=labels, yticklabels=labels, ax=ax,
                       cbar_kws={'label': 'Number of Predictions'})
            ax.set_xlabel("Predicted Label", fontweight='bold')
            ax.set_ylabel("True Label", fontweight='bold')
            ax.set_title("Confusion Matrix", fontweight='bold', pad=20)
            st.pyplot(fig)
    else:
        st.markdown("""
        <div class="warning-card">
            <h3>⚠️ Feature Data Required</h3>
            <p>Please run Feature Engineering first to generate feature matrices.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# TAB 6: Product Recommender
# -------------------------------
elif selected_tab == "🔮 Product Recommender":
    st.markdown('<div class="tab-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">🔮 Product Recommender</h2>', unsafe_allow_html=True)
    
    BASE_DIR = "/Users/ponnigithav/Desktop/code-synapse"
    NEW_BASKETS_FILE = os.path.join(BASE_DIR, "data", "new_baskets.json")

    if os.path.exists("clean/groceries_baskets.json"):
        with open("clean/groceries_baskets.json", "r") as f:
            baskets = json.load(f)
    else:
        st.warning("⚠️ No baskets available. Please upload and process data first.")
        baskets = []

    if baskets:
        # Load rules from both CSV files
        fp_rules_file = "fp_growth_rules.csv"
        apriori_rules_file = "all_apriori_rules.csv"
        
        # Function to load rules from CSV
        def load_rules_from_csv(filename):
            rules = []
            try:
                with open(filename, 'r', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        # Handle different CSV formats
                        if 'antecedent' in row and 'consequent' in row:
                            rules.append({
                                'if': row['antecedent'].split(';') if row['antecedent'] else [],
                                'then': row['consequent'].split(';') if row['consequent'] else [],
                                'support': float(row['support']),
                                'confidence': float(row['confidence']),
                                'lift': float(row['lift'])
                            })
                        elif 'if' in row and 'then' in row:
                            # Handle the format with 'if' and 'then' columns
                            rules.append({
                                'if': eval(row['if']) if row['if'] else [],
                                'then': eval(row['then']) if row['then'] else [],
                                'support': float(row['support']),
                                'confidence': float(row['confidence']),
                                'lift': float(row['lift'])
                            })
                st.success(f"✅ Loaded {len(rules)} rules from {filename}")
                return rules
            except FileNotFoundError:
                st.warning(f"⚠️ File {filename} not found. Please generate rules first.")
                return []
            except Exception as e:
                st.error(f"❌ Error loading rules from {filename}: {str(e)}")
                return []
        
        # Load both rule sets
        fp_rules = []
        apriori_rules = []
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Load FP-Growth Rules", use_container_width=True):
                fp_rules = load_rules_from_csv(fp_rules_file)
                st.session_state.fp_rules = fp_rules
                
        with col2:
            if st.button("🔄 Load Apriori Rules", use_container_width=True):
                apriori_rules = load_rules_from_csv(apriori_rules_file)
                st.session_state.apriori_rules = apriori_rules
        
        # Initialize session state for rules if not exists
        if "fp_rules" not in st.session_state:
            st.session_state.fp_rules = []
        if "apriori_rules" not in st.session_state:
            st.session_state.apriori_rules = []
        
        # Use session state rules
        fp_rules = st.session_state.fp_rules
        apriori_rules = st.session_state.apriori_rules
        
        # Algorithm Selection
        st.markdown("#### 🎯 Choose Recommendation Algorithm")
        
        # Show available rules status
        col1, col2 = st.columns(2)
        with col1:
            fp_status = "✅ Loaded" if fp_rules else "❌ Not Loaded"
        with col2:
            apriori_status = "✅ Loaded" if apriori_rules else "❌ Not Loaded"
        
        # Only show algorithm selection if both rule sets are available
        if fp_rules and apriori_rules:
            algorithm = st.radio(
                "Select algorithm:",
                ["FP-Growth", "Apriori"],
                horizontal=True,
                help="FP-Growth: Faster for large datasets | Apriori: Traditional association rules"
            )
        elif fp_rules:
            algorithm = "FP-Growth"
            st.info("📊 Using FP-Growth rules (Apriori rules not available)")
        elif apriori_rules:
            algorithm = "Apriori"
            st.info("📊 Using Apriori rules (FP-Growth rules not available)")
        else:
            st.error("❌ No rules available. Please generate and load rules first.")
            st.stop()
        
        # Select rules based on algorithm
        if algorithm == "FP-Growth":
            rules = fp_rules
        else:
            rules = apriori_rules

        # ✅ Load unique products from grocery_item_frequency.csv
        freq_file = os.path.join(BASE_DIR, "clean", "grocery_item_frequency.csv")

        if os.path.exists(freq_file):
            try:
                import pandas as pd
                df_freq = pd.read_csv(freq_file)
                
                # Assume the first column holds item names
                first_col = df_freq.columns[0]
                all_unique_products = sorted(df_freq[first_col].dropna().unique().tolist())
                st.success(f"✅ Loaded {len(all_unique_products)} unique products from grocery_item_frequency.csv")
            except Exception as e:
                st.error(f"❌ Error reading {freq_file}: {str(e)}")
                all_unique_products = []
        else:
            all_unique_products = sorted(set(item for basket in baskets for item in basket if item))
                
        # Also get products from rules for comparison
        rule_products = set()
        for r in rules:
            rule_products.update(r["if"])
            if isinstance(r["then"], list):
                rule_products.update(r["then"])
            else:
                rule_products.add(r["then"])
        rule_products = sorted(rule_products)

        st.info(f"**{algorithm} Stats:**  rules loaded | {len(all_unique_products)} unique products available")

        # Initialize session state for basket and algorithm
        if "basket" not in st.session_state:
            st.session_state.basket = []
        if "current_algorithm" not in st.session_state:
            st.session_state.current_algorithm = algorithm

        # Clear basket if algorithm changed
        if st.session_state.current_algorithm != algorithm:
            st.session_state.basket = []
            st.session_state.current_algorithm = algorithm
            st.rerun()

        # Basket Management
        st.markdown("#### 🛍️ Build Your Basket")
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            product_choice = st.selectbox(
                "Select a product to add:", 
                all_unique_products,
                help=f"Choose from {len(all_unique_products)} available products in the dataset"
            )
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("➕ Add", use_container_width=True, help="Add selected product to basket"):
                if product_choice not in st.session_state.basket:
                    st.session_state.basket.append(product_choice)
                    st.rerun()
                else:
                    st.warning(f"'{product_choice}' is already in your basket!")
        
        with col3:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🗑️ Clear All", use_container_width=True, help="Clear entire basket"):
                st.session_state.basket = []
                st.rerun()

        # Display Current Basket
        st.markdown("#### 📦 Your Current Basket")
        if st.session_state.basket:
            # Show basket items with remove buttons
            basket_cols = st.columns(4)
            for i, item in enumerate(st.session_state.basket):
                col_idx = i % 4
                with basket_cols[col_idx]:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"""
                        <div style="background: #e3f2fd; padding: 0.5rem; border-radius: 8px; text-align: center; margin: 0.2rem;">
                            {item}
                        </div>
                        """, unsafe_allow_html=True)
                    with col2:
                        if st.button("❌", key=f"remove_{i}", help=f"Remove {item}"):
                            st.session_state.basket.remove(item)
                            st.rerun()
            
            # Basket summary
            st.metric("Items in Basket", len(st.session_state.basket))
        else:
            st.info("🎯 Your basket is empty. Add some products to get recommendations!")

        # Recommendations Section
        if st.session_state.basket:
            st.markdown("#### ✨ Product Recommendations")
            
            # Recommendation settings
            col1, col2 = st.columns(2)
            with col1:
                top_n = st.slider(
                    "Number of recommendations", 
                    1, 15, 5,
                    help="Adjust how many recommendations you want to see"
                )
            with col2:
                score_method = st.selectbox(
                    "Scoring method",
                    ["Confidence", "Lift", "Confidence × Lift"],
                    help="How to rank recommendations"
                )
            
            # Generate recommendations
            recs = []
            basket_set = set(st.session_state.basket)
            
            for rule in rules:
                if set(rule["if"]).issubset(basket_set):
                    rec_items = rule["then"] if isinstance(rule["then"], list) else [rule["then"]]
                    for item in rec_items:
                        if item not in basket_set:
                            # Calculate score based on selected method
                            if score_method == "Confidence":
                                score = rule["confidence"]
                            elif score_method == "Lift":
                                score = rule["lift"]
                            else:  # Confidence × Lift
                                score = rule["confidence"] * rule["lift"]
                            
                            recs.append((item, score, rule["confidence"], rule["lift"], rule["support"]))
            
            # Remove duplicates and keep highest score
            rec_dict = {}
            for item, score, conf, lift, supp in recs:
                if item not in rec_dict or score > rec_dict[item][0]:
                    rec_dict[item] = (score, conf, lift, supp)
            
            # Sort by selected score method
            sorted_recs = sorted(rec_dict.items(), key=lambda x: x[1][0], reverse=True)[:top_n]
            
            if sorted_recs:
                st.success(f"🎉 **{algorithm} found {len(sorted_recs)} recommendations based on your basket:**")
                
                # Display recommendations in a grid
                cols = st.columns(2)
                for i, (item, (score, conf, lift, supp)) in enumerate(sorted_recs):
                    with cols[i % 2]:
                        # Color code based on score
                        if score >= 0.7:
                            color_gradient = "linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%)"
                            emoji = "🔥"
                        elif score >= 0.4:
                            color_gradient = "linear-gradient(135deg, #2196F3 0%, #64b5f6 100%)"
                            emoji = "⭐"
                        else:
                            color_gradient = "linear-gradient(135deg, #ff9800 0%, #ffcc80 100%)"
                            emoji = "💡"
                        
                        st.markdown(f"""
                        <div style="background: {color_gradient}; 
                                    padding: 1rem; border-radius: 10px; color: white; margin: 0.5rem 0;
                                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                            <h4>{emoji} {item}</h4>
                            <p><strong>Score:</strong> {score:.3f}</p>
                            <p><small>Confidence: {conf:.3f} | Lift: {lift:.3f} | Support: {supp:.3f}</small></p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Add to basket button for recommended items
                        if st.button(f"Add {item}", key=f"add_rec_{i}", use_container_width=True):
                            if item not in st.session_state.basket:
                                st.session_state.basket.append(item)
                                st.success(f"Added {item} to basket!")
                                st.rerun()
                
                # Algorithm comparison suggestion (only if both algorithms are available)
                if fp_rules and apriori_rules:
                    st.markdown("---")
                    other_algo = "Apriori" if algorithm == "FP-Growth" else "FP-Growth"
                    if st.button(f"🔍 Compare with {other_algo} algorithm", use_container_width=True):
                        st.session_state.current_algorithm = other_algo
                        st.rerun()
                        
            else:
                st.warning("""
                """)
                
                # Show popular items that work well with current basket
                if len(st.session_state.basket) > 0:
                    st.markdown("#### 💡 Popular Combinations")
                    # Find items that frequently co-occur with basket items
                    co_occurrence = {}
                    for basket in baskets:
                        basket_set_full = set(basket)
                        if any(item in basket_set_full for item in st.session_state.basket):
                            for item in basket_set_full:
                                if item not in st.session_state.basket:
                                    co_occurrence[item] = co_occurrence.get(item, 0) + 1
                    
                    if co_occurrence:
                        popular_items = sorted(co_occurrence.items(), key=lambda x: x[1], reverse=True)[:5]
                        st.write("Frequently purchased together with your items:")
                        for item, count in popular_items:
                            col1, col2 = st.columns([3, 1])
                            with col1:
                                st.write(f"**{item}** ({count} occurrences)")
                            with col2:
                                if st.button(f"Add", key=f"pop_{item}"):
                                    if item not in st.session_state.basket:
                                        st.session_state.basket.append(item)
                                        st.rerun()
                    else:
                        st.info("Try adding some common items like 'whole milk', 'rolls/buns', or 'soda' to get better recommendations.")
        
        # Rules Preview Section
        st.markdown("---")
        st.markdown("#### 📋 Rules Preview")
        
        if rules:
            # Show top rules
            top_rules = sorted(rules, key=lambda x: x['confidence'], reverse=True)[:10]
            rules_df = pd.DataFrame(top_rules)
            
            # Format the rules for better display
            rules_display = []
            for rule in top_rules:
                rules_display.append({
                    'Rule': f"If {', '.join(rule['if'])} → Then {', '.join(rule['then'])}",
                    'Support': rule['support'],
                    'Confidence': rule['confidence'],
                    'Lift': rule['lift']
                })
            
            rules_display_df = pd.DataFrame(rules_display)
            st.dataframe(rules_display_df, use_container_width=True)
            
            # Download current rules
            csv_data = pd.DataFrame(rules).to_csv(index=False).encode('utf-8')
            st.download_button(
                label=f"💾 Download {algorithm} Rules as CSV",
                data=csv_data,
                file_name=f"{algorithm.lower()}_rules.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.info("No rules to display. Please load rules first.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# TAB 7: Self-Evolving Engine
# -------------------------------
elif selected_tab == "🔄 Self-Evolving Engine":
    st.markdown('<div class="tab-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">🔄 Self-Evolving Recommendation Engine</h2>', unsafe_allow_html=True)
    
    BASE_DIR = "/Users/ponnigithav/Desktop/code-synapse"
    NEW_BASKETS_FILE = os.path.join(BASE_DIR, "data", "new_baskets.json")
    OUTPUT_RECOMMENDER = os.path.join(BASE_DIR, "product_recommender.py")

    st.markdown("""
    <div class="info-card">
        <strong>🔄 Self-Evolving Engine</strong><br>
        This module allows you to add new transaction data and automatically update 
        the recommendation engine with new patterns and rules.
    </div>
    """, unsafe_allow_html=True)

    # Manual Basket Input
    st.markdown("#### 📝 Add New Baskets Manually")
    st.write("Enter products separated by commas for each new basket:")

    if "new_baskets" not in st.session_state:
        st.session_state.new_baskets = []

    col1, col2 = st.columns([3, 1])
    with col1:
        new_basket_input = st.text_input("New Basket (comma-separated items)", "",
                                       placeholder="e.g., milk, bread, eggs, butter")
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("➕ Add Basket", use_container_width=True):
            if new_basket_input.strip():
                basket_items = [item.strip() for item in new_basket_input.split(",") if item.strip()]
                st.session_state.new_baskets.append(basket_items)
                st.success(f"✅ Added basket: {basket_items}")
                st.rerun()

    # Display Pending Baskets
    if st.session_state.new_baskets:
        st.markdown("#### 📋 New Baskets Pending Integration")
        for i, basket in enumerate(st.session_state.new_baskets, 1):
            st.write(f"**Basket {i}:** {', '.join(basket)}")
        
        if st.button("🗑️ Clear All Pending Baskets", use_container_width=True):
            st.session_state.new_baskets = []
            st.rerun()

    # File Upload Option
    st.markdown("---")
    st.markdown("#### 📁 Upload New Baskets File")
    uploaded_file = st.file_uploader("Upload JSON or CSV file with new transactions", 
                                   type=["json", "csv"],
                                   help="JSON: Array of arrays | CSV: Comma-separated items per row")
    
    if uploaded_file:
        try:
            if uploaded_file.type == "application/json":
                file_baskets = json.load(uploaded_file)
            else:
                file_baskets = [line.decode("utf-8").strip().split(",") for line in uploaded_file.readlines()]
            
            st.session_state.new_baskets.extend(file_baskets)
            st.success(f"✅ Loaded {len(file_baskets)} baskets from file.")
            st.rerun()
        except Exception as e:
            st.error(f"❌ Error reading file: {str(e)}")

    # Engine Execution
    st.markdown("---")
    st.markdown("#### 🚀 Execute Self-Evolving Engine")
    
    if st.session_state.new_baskets:
        st.info(f"Ready to process {len(st.session_state.new_baskets)} new baskets")
        
        if st.button("🤖 Run Self-Evolving Engine", use_container_width=True, type="primary"):
            with st.spinner("Processing new baskets and updating recommendation engine..."):
                # Save new baskets
                os.makedirs(os.path.dirname(NEW_BASKETS_FILE), exist_ok=True)
                with open(NEW_BASKETS_FILE, "w") as f:
                    json.dump(st.session_state.new_baskets, f)

                # Run evolving engine
                try:
                    import self_evolving_engine
                    self_evolving_engine.run_self_evolving_engine_once(st.session_state.new_baskets)
                    
                    st.success("✅ Engine successfully updated with new patterns!")
                    st.balloons()
                    
                    # Show summary
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Baskets Processed", len(st.session_state.new_baskets))
                    with col2:
                        st.metric("Engine Updated", "✅")
                    
                    st.session_state.new_baskets = []
                    
                except Exception as e:
                    st.error(f"❌ Error updating engine: {str(e)}")
    else:
        st.info("ℹ️ Add some new baskets manually or upload a file to start the self-evolving process.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
