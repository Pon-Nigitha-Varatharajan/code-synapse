import streamlit as st
from graphviz import Digraph
import os

st.set_page_config(page_title="Rule Flow", layout="wide", page_icon="🛒")
st.title("🛒 Basket Decision Tree (Rule Flow)")

# ------------------------------
# Load Rules
# ------------------------------
RULES_FILE = "rules/basket_decision_tree_rules.txt"

def parse_rules(file_path):
    edges = []
    stack = []
    nodes_info = {}
    with open(file_path, "r") as f:
        for line in f:
            stripped = line.rstrip()
            if not stripped:
                continue
            indent_level = len(line) - len(line.lstrip())
            node = stripped.replace("if ", "").replace("Leaf: ", "").strip().strip("'").strip(":")
            nodes_info[node] = stripped.strip()
            while stack and stack[-1][1] >= indent_level:
                stack.pop()
            if stack:
                edges.append((stack[-1][0], node))
            stack.append((node, indent_level))
    return edges, nodes_info

edges, nodes_info = parse_rules(RULES_FILE)

# ------------------------------
# Build Graphviz Tree
# ------------------------------
dot = Digraph(comment='Basket Decision Tree')
dot.attr('node', shape='box', style='filled,rounded', fontname='Helvetica', fontsize='12')

nodes = set([n for e in edges for n in e])
for n in nodes:
    color = 'lightgreen' if "Basket" in n else 'lightblue'
    dot.node(n, n, color=color, tooltip=nodes_info.get(n, ""))

for parent, child in edges:
    dot.edge(parent, child, color='gray')

dot.attr(rankdir='LR')

# ------------------------------
# Display
# ------------------------------
st.graphviz_chart(dot)
st.markdown("""
- Leaf nodes (green) = final basket segments  
- Internal nodes (blue) = feature splits  
- Hover over nodes to see rule conditions
""")