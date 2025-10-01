#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto-generated Product Recommender
"""

# ------------------------------
# 1. Association Rules
# ------------------------------
apriori_rules = [
  {
    "if": [
      "curd"
    ],
    "then": [
      "beef"
    ],
    "support": 1.0,
    "confidence": 1.0,
    "lift": 1.0
  },
  {
    "if": [
      "beef"
    ],
    "then": [
      "curd"
    ],
    "support": 1.0,
    "confidence": 1.0,
    "lift": 1.0
  },
  {
    "if": [
      "butter"
    ],
    "then": [
      "curd"
    ],
    "support": 1.0,
    "confidence": 1.0,
    "lift": 1.0
  },
  {
    "if": [
      "curd"
    ],
    "then": [
      "butter"
    ],
    "support": 1.0,
    "confidence": 1.0,
    "lift": 1.0
  },
  {
    "if": [
      "butter"
    ],
    "then": [
      "beef"
    ],
    "support": 1.0,
    "confidence": 1.0,
    "lift": 1.0
  },
  {
    "if": [
      "beef"
    ],
    "then": [
      "butter"
    ],
    "support": 1.0,
    "confidence": 1.0,
    "lift": 1.0
  },
  {
    "if": [
      "butter"
    ],
    "then": [
      "curd",
      "beef"
    ],
    "support": 1.0,
    "confidence": 1.0,
    "lift": 1.0
  },
  {
    "if": [
      "curd"
    ],
    "then": [
      "butter",
      "beef"
    ],
    "support": 1.0,
    "confidence": 1.0,
    "lift": 1.0
  },
  {
    "if": [
      "beef"
    ],
    "then": [
      "butter",
      "curd"
    ],
    "support": 1.0,
    "confidence": 1.0,
    "lift": 1.0
  },
  {
    "if": [
      "butter",
      "curd"
    ],
    "then": [
      "beef"
    ],
    "support": 1.0,
    "confidence": 1.0,
    "lift": 1.0
  },
  {
    "if": [
      "butter",
      "beef"
    ],
    "then": [
      "curd"
    ],
    "support": 1.0,
    "confidence": 1.0,
    "lift": 1.0
  },
  {
    "if": [
      "curd",
      "beef"
    ],
    "then": [
      "butter"
    ],
    "support": 1.0,
    "confidence": 1.0,
    "lift": 1.0
  }
]

def recommend_products(basket, top_n=5):
    basket_set = set(basket)
    recs = []
    for rule in apriori_rules:
        if set(rule["if"]).issubset(basket_set):
            if isinstance(rule["then"], list):
                for item in rule["then"]:
                    if item not in basket_set:
                        recs.append(item)
            else:
                if rule["then"] not in basket_set:
                    recs.append(rule["then"])
    recs = list(dict.fromkeys(recs))
    return recs[:top_n]

if __name__ == "__main__":
    sample_basket = ["whole milk", "rolls/buns"]
    print("Sample Basket:", sample_basket)
    print("Recommended Products:", recommend_products(sample_basket))
