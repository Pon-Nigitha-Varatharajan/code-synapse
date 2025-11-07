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
      "other vegetables",
      "root vegetables"
    ],
    "then": [
      "bottled water"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "other vegetables",
      "chicken"
    ],
    "then": [
      "bottled water",
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "root vegetables"
    ],
    "then": [
      "other vegetables",
      "bottled water",
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "chicken"
    ],
    "then": [
      "other vegetables",
      "bottled water",
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "bottled water"
    ],
    "then": [
      "other vegetables",
      "chicken",
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "other vegetables"
    ],
    "then": [
      "bottled water",
      "chicken",
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "chocolate"
    ],
    "then": [
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "chips"
    ],
    "then": [
      "chocolate"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "chocolate"
    ],
    "then": [
      "soda"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "soda"
    ],
    "then": [
      "chocolate"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "soda"
    ],
    "then": [
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "chips"
    ],
    "then": [
      "soda"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "chocolate",
      "soda"
    ],
    "then": [
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chocolate",
      "chips"
    ],
    "then": [
      "soda"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "soda",
      "chips"
    ],
    "then": [
      "chocolate"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chocolate"
    ],
    "then": [
      "soda",
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "soda"
    ],
    "then": [
      "chocolate",
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chips"
    ],
    "then": [
      "chocolate",
      "soda"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "waffles"
    ],
    "then": [
      "soda"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "bottled water",
      "other vegetables"
    ],
    "then": [
      "chicken",
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "bottled water",
      "chicken"
    ],
    "then": [
      "other vegetables",
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "chocolate"
    ],
    "then": [
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "other vegetables",
      "root vegetables"
    ],
    "then": [
      "bottled water",
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "bottled water",
      "root vegetables"
    ],
    "then": [
      "other vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "bottled water",
      "other vegetables"
    ],
    "then": [
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "root vegetables"
    ],
    "then": [
      "bottled water",
      "other vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "bottled water"
    ],
    "then": [
      "other vegetables",
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "other vegetables"
    ],
    "then": [
      "bottled water",
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "bottled water",
      "chicken"
    ],
    "then": [
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "bottled water",
      "root vegetables"
    ],
    "then": [
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "root vegetables",
      "chicken"
    ],
    "then": [
      "bottled water"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "bottled water"
    ],
    "then": [
      "root vegetables",
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chicken"
    ],
    "then": [
      "bottled water",
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "root vegetables"
    ],
    "then": [
      "bottled water",
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "bottled water",
      "chicken",
      "root vegetables"
    ],
    "then": [
      "other vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "other vegetables",
      "chicken",
      "root vegetables"
    ],
    "then": [
      "bottled water"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "other vegetables",
      "bottled water",
      "root vegetables"
    ],
    "then": [
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "other vegetables",
      "bottled water",
      "chicken"
    ],
    "then": [
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "chicken",
      "root vegetables"
    ],
    "then": [
      "bottled water",
      "other vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "bottled water",
      "root vegetables"
    ],
    "then": [
      "other vegetables",
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "soda"
    ],
    "then": [
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "waffles"
    ],
    "then": [
      "chocolate"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "chicken"
    ],
    "then": [
      "other vegetables",
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "soda",
      "chocolate",
      "waffles"
    ],
    "then": [
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "soda",
      "waffles",
      "chips"
    ],
    "then": [
      "chocolate"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "chocolate",
      "soda",
      "chips"
    ],
    "then": [
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "chocolate",
      "waffles"
    ],
    "then": [
      "soda",
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "soda",
      "waffles"
    ],
    "then": [
      "chocolate",
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "waffles",
      "chips"
    ],
    "then": [
      "chocolate",
      "soda"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "chocolate",
      "soda"
    ],
    "then": [
      "waffles",
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "chocolate",
      "chips"
    ],
    "then": [
      "soda",
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "soda",
      "chips"
    ],
    "then": [
      "chocolate",
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "waffles"
    ],
    "then": [
      "chocolate",
      "soda",
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "chocolate"
    ],
    "then": [
      "soda",
      "waffles",
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "soda"
    ],
    "then": [
      "chocolate",
      "waffles",
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "chips"
    ],
    "then": [
      "soda",
      "chocolate",
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "frozen dessert"
    ],
    "then": [
      "beef"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "beef"
    ],
    "then": [
      "frozen dessert"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "frozen dessert",
      "whole milk"
    ],
    "then": [
      "beef"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "whole milk",
      "beef"
    ],
    "then": [
      "frozen dessert"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "frozen dessert"
    ],
    "then": [
      "whole milk",
      "beef"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chocolate",
      "waffles",
      "chips"
    ],
    "then": [
      "soda"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "chips"
    ],
    "then": [
      "chocolate",
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "waffles"
    ],
    "then": [
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "waffles"
    ],
    "then": [
      "chocolate",
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chips"
    ],
    "then": [
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "chocolate",
      "waffles"
    ],
    "then": [
      "soda"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "soda",
      "waffles"
    ],
    "then": [
      "chocolate"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chocolate",
      "soda"
    ],
    "then": [
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "waffles"
    ],
    "then": [
      "chocolate",
      "soda"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chocolate"
    ],
    "then": [
      "soda",
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "soda"
    ],
    "then": [
      "chocolate",
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "soda",
      "waffles"
    ],
    "then": [
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "waffles",
      "chips"
    ],
    "then": [
      "soda"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "soda",
      "chips"
    ],
    "then": [
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "waffles"
    ],
    "then": [
      "soda",
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "soda"
    ],
    "then": [
      "waffles",
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chips"
    ],
    "then": [
      "soda",
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chocolate",
      "waffles"
    ],
    "then": [
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chocolate",
      "chips"
    ],
    "then": [
      "waffles"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "waffles",
      "chips"
    ],
    "then": [
      "chocolate"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chocolate"
    ],
    "then": [
      "waffles",
      "chips"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "other vegetables"
    ],
    "then": [
      "chicken",
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "beef"
    ],
    "then": [
      "frozen dessert",
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "root vegetables"
    ],
    "then": [
      "other vegetables",
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "tropical fruit"
    ],
    "then": [
      "yogurt",
      "whole milk",
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "tropical fruit"
    ],
    "then": [
      "whole milk",
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "cereal"
    ],
    "then": [
      "tropical fruit",
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "yogurt",
      "whole milk"
    ],
    "then": [
      "tropical fruit"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "tropical fruit",
      "whole milk"
    ],
    "then": [
      "yogurt"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "yogurt"
    ],
    "then": [
      "tropical fruit",
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "tropical fruit"
    ],
    "then": [
      "yogurt",
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "yogurt",
      "tropical fruit",
      "whole milk"
    ],
    "then": [
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "yogurt",
      "whole milk",
      "cereal"
    ],
    "then": [
      "tropical fruit"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "other vegetables",
      "chicken"
    ],
    "then": [
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "yogurt",
      "tropical fruit"
    ],
    "then": [
      "whole milk",
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "yogurt",
      "whole milk"
    ],
    "then": [
      "tropical fruit",
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "yogurt",
      "cereal"
    ],
    "then": [
      "tropical fruit",
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "tropical fruit",
      "whole milk"
    ],
    "then": [
      "yogurt",
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "tropical fruit",
      "cereal"
    ],
    "then": [
      "yogurt",
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "whole milk",
      "cereal"
    ],
    "then": [
      "yogurt",
      "tropical fruit"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "whole milk",
      "cereal"
    ],
    "then": [
      "tropical fruit"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "tropical fruit",
      "whole milk"
    ],
    "then": [
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "cereal"
    ],
    "then": [
      "yogurt",
      "tropical fruit"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "tropical fruit"
    ],
    "then": [
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "yogurt"
    ],
    "then": [
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "cereal"
    ],
    "then": [
      "yogurt"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "yogurt",
      "whole milk"
    ],
    "then": [
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "whole milk",
      "cereal"
    ],
    "then": [
      "yogurt"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "yogurt"
    ],
    "then": [
      "whole milk",
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "cereal"
    ],
    "then": [
      "yogurt",
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "cereal"
    ],
    "then": [
      "tropical fruit"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "tropical fruit"
    ],
    "then": [
      "yogurt",
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "yogurt"
    ],
    "then": [
      "tropical fruit"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "tropical fruit"
    ],
    "then": [
      "yogurt"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "yogurt",
      "tropical fruit"
    ],
    "then": [
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "yogurt",
      "cereal"
    ],
    "then": [
      "tropical fruit"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "tropical fruit",
      "cereal"
    ],
    "then": [
      "yogurt"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "yogurt"
    ],
    "then": [
      "tropical fruit",
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "yogurt"
    ],
    "then": [
      "tropical fruit",
      "whole milk",
      "cereal"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "tropical fruit",
      "whole milk",
      "cereal"
    ],
    "then": [
      "yogurt"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "bottled water",
      "other vegetables"
    ],
    "then": [
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chicken"
    ],
    "then": [
      "bottled water",
      "other vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "bottled water"
    ],
    "then": [
      "other vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "other vegetables"
    ],
    "then": [
      "bottled water"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "bottled water",
      "chicken"
    ],
    "then": [
      "other vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "cereal"
    ],
    "then": [
      "yogurt",
      "tropical fruit",
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 4
  },
  {
    "if": [
      "other vegetables",
      "chicken"
    ],
    "then": [
      "bottled water"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "bottled water"
    ],
    "then": [
      "other vegetables",
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "other vegetables"
    ],
    "then": [
      "bottled water",
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chicken"
    ],
    "then": [
      "bottled water"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "root vegetables"
    ],
    "then": [
      "other vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "other vegetables"
    ],
    "then": [
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "chicken"
    ],
    "then": [
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "root vegetables"
    ],
    "then": [
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "bottled water"
    ],
    "then": [
      "root vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "root vegetables"
    ],
    "then": [
      "bottled water"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "other vegetables"
    ],
    "then": [
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "chicken"
    ],
    "then": [
      "other vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "butter",
      "rolls/buns"
    ],
    "then": [
      "jam"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "jam",
      "rolls/buns"
    ],
    "then": [
      "butter"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "butter"
    ],
    "then": [
      "jam"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "jam"
    ],
    "then": [
      "butter"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "jam"
    ],
    "then": [
      "rolls/buns"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "rolls/buns"
    ],
    "then": [
      "jam"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "butter"
    ],
    "then": [
      "rolls/buns"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "rolls/buns"
    ],
    "then": [
      "butter"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "butter",
      "jam"
    ],
    "then": [
      "rolls/buns"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "chicken",
      "root vegetables"
    ],
    "then": [
      "other vegetables"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "other vegetables",
      "root vegetables"
    ],
    "then": [
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "butter"
    ],
    "then": [
      "jam",
      "rolls/buns"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "jam"
    ],
    "then": [
      "butter",
      "rolls/buns"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "rolls/buns"
    ],
    "then": [
      "butter",
      "jam"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 3
  },
  {
    "if": [
      "bottled water"
    ],
    "then": [
      "chicken"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 5.0,
    "itemset_size": 2
  },
  {
    "if": [
      "whole milk"
    ],
    "then": [
      "frozen dessert",
      "beef"
    ],
    "support": 0.2,
    "confidence": 0.5,
    "lift": 2.5,
    "itemset_size": 3
  },
  {
    "if": [
      "frozen dessert",
      "beef"
    ],
    "then": [
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 2.5,
    "itemset_size": 3
  },
  {
    "if": [
      "beef"
    ],
    "then": [
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 2.5,
    "itemset_size": 2
  },
  {
    "if": [
      "whole milk"
    ],
    "then": [
      "beef"
    ],
    "support": 0.2,
    "confidence": 0.5,
    "lift": 2.5,
    "itemset_size": 2
  },
  {
    "if": [
      "whole milk"
    ],
    "then": [
      "cereal"
    ],
    "support": 0.2,
    "confidence": 0.5,
    "lift": 2.5,
    "itemset_size": 2
  },
  {
    "if": [
      "cereal"
    ],
    "then": [
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 2.5,
    "itemset_size": 2
  },
  {
    "if": [
      "whole milk"
    ],
    "then": [
      "frozen dessert"
    ],
    "support": 0.2,
    "confidence": 0.5,
    "lift": 2.5,
    "itemset_size": 2
  },
  {
    "if": [
      "whole milk"
    ],
    "then": [
      "yogurt"
    ],
    "support": 0.2,
    "confidence": 0.5,
    "lift": 2.5,
    "itemset_size": 2
  },
  {
    "if": [
      "whole milk"
    ],
    "then": [
      "yogurt",
      "tropical fruit",
      "cereal"
    ],
    "support": 0.2,
    "confidence": 0.5,
    "lift": 2.5,
    "itemset_size": 4
  },
  {
    "if": [
      "frozen dessert"
    ],
    "then": [
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 2.5,
    "itemset_size": 2
  },
  {
    "if": [
      "yogurt",
      "cereal"
    ],
    "then": [
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 2.5,
    "itemset_size": 3
  },
  {
    "if": [
      "whole milk"
    ],
    "then": [
      "yogurt",
      "cereal"
    ],
    "support": 0.2,
    "confidence": 0.5,
    "lift": 2.5,
    "itemset_size": 3
  },
  {
    "if": [
      "tropical fruit"
    ],
    "then": [
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 2.5,
    "itemset_size": 2
  },
  {
    "if": [
      "whole milk"
    ],
    "then": [
      "tropical fruit"
    ],
    "support": 0.2,
    "confidence": 0.5,
    "lift": 2.5,
    "itemset_size": 2
  },
  {
    "if": [
      "tropical fruit",
      "cereal"
    ],
    "then": [
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 2.5,
    "itemset_size": 3
  },
  {
    "if": [
      "whole milk"
    ],
    "then": [
      "tropical fruit",
      "cereal"
    ],
    "support": 0.2,
    "confidence": 0.5,
    "lift": 2.5,
    "itemset_size": 3
  },
  {
    "if": [
      "yogurt",
      "tropical fruit"
    ],
    "then": [
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 2.5,
    "itemset_size": 3
  },
  {
    "if": [
      "whole milk"
    ],
    "then": [
      "yogurt",
      "tropical fruit"
    ],
    "support": 0.2,
    "confidence": 0.5,
    "lift": 2.5,
    "itemset_size": 3
  },
  {
    "if": [
      "yogurt",
      "tropical fruit",
      "cereal"
    ],
    "then": [
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 2.5,
    "itemset_size": 4
  },
  {
    "if": [
      "yogurt"
    ],
    "then": [
      "whole milk"
    ],
    "support": 0.2,
    "confidence": 1.0,
    "lift": 2.5,
    "itemset_size": 2
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
