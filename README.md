# code-synapse
Here’s a clean, professional README.md you can directly use for your GitHub repo 👇

⸻

🛒 Self-Evolving Grocery Recommendation System

A smart, self-evolving grocery recommendation system built using Machine Learning and Interactive Analytics to discover purchasing patterns and generate actionable product insights.

This project leverages association rule mining and customer segmentation to help retailers improve cross-selling, upselling, and personalized recommendations.

⸻

🚀 Features

🔍 Association Rule Mining
	•	Uses Apriori and FP-Growth algorithms
	•	Identifies frequently purchased itemsets
	•	Generates strong rules using:
	•	Support
	•	Confidence
	•	Lift

⸻

⚙️ Threshold Optimization
	•	Performs grid search over:
	•	Support
	•	Confidence
	•	Lift
	•	Automatically selects optimal thresholds for best rule generation

⸻

👥 Customer Segmentation
	•	Uses ID3 Decision Tree
	•	Classifies transactions into:
	•	Small Basket
	•	Medium Basket
	•	Big Basket
	•	Visualized using Graphviz

⸻

🔄 Self-Evolving Engine
	•	Automatically updates rules when new data is added
	•	Adapts to changing customer behavior over time

⸻

🤖 Hybrid Recommendation System
	•	Combines:
	•	Rule-based recommendations
	•	Co-occurrence matrix
	•	Produces more accurate and reliable suggestions

⸻

📊 Interactive Dashboard (Streamlit)

Includes 7 modules:
	1.	Preprocessing
	2.	Feature Engineering
	3.	Exploratory Data Analysis (EDA)
	4.	Rule Mining
	5.	Decision Tree Modeling
	6.	Recommendation Engine
	7.	Self-Evolution Module

⸻

🧠 Applications
	•	🛍️ Retail stores
	•	🛒 E-commerce platforms
	•	📈 Marketing analytics
	•	🧾 Customer behavior analysis

Also extensible to:
	•	💊 Pharmaceuticals
	•	🎬 Entertainment
	•	🛒 Online retail ecosystems

⸻

🛠️ Tech Stack
	•	Programming Language: Python
	•	Frontend: Streamlit
	•	Libraries & Tools:
	•	Pandas
	•	NumPy
	•	Matplotlib
	•	Seaborn
	•	Scikit-learn
	•	Graphviz
	•	Data Formats: CSV, JSON

⸻

⚡ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/Pon-Nigitha-Varatharajan/code-synapse.git
cd code-synapse

2️⃣ Create Virtual Environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Application

streamlit run main.py


⸻

📈 How It Works (Workflow)
	1.	Load transaction dataset
	2.	Preprocess & clean data
	3.	Generate frequent itemsets (Apriori / FP-Growth)
	4.	Optimize thresholds using grid search
	5.	Build association rules
	6.	Segment customers using decision tree
	7.	Generate recommendations
	8.	Continuously update model with new data

⸻

🌟 Key Highlights
	•	🔁 Dynamic system that evolves with data
	•	📊 End-to-end analytics pipeline
	•	🧩 Modular architecture for easy extension
	•	🧠 Combines ML + Rule Mining + Visualization

