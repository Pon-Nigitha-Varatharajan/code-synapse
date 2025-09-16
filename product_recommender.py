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
      "tropical fruit"
    ],
    "then": "yogurt",
    "support": 0.0293,
    "confidence": 0.2791,
    "lift": 2.0005
  },
  {
    "if": [
      "yogurt"
    ],
    "then": "tropical fruit",
    "support": 0.0293,
    "confidence": 0.2099,
    "lift": 2.0005
  },
  {
    "if": [
      "cream cheese"
    ],
    "then": "yogurt",
    "support": 0.0124,
    "confidence": 0.3128,
    "lift": 2.2424
  },
  {
    "if": [
      "pip fruit"
    ],
    "then": "yogurt",
    "support": 0.018,
    "confidence": 0.2379,
    "lift": 1.7054
  },
  {
    "if": [
      "long life bakery product"
    ],
    "then": "other vegetables",
    "support": 0.0107,
    "confidence": 0.2853,
    "lift": 1.4746
  },
  {
    "if": [
      "long life bakery product"
    ],
    "then": "whole milk",
    "support": 0.0135,
    "confidence": 0.3614,
    "lift": 1.4144
  },
  {
    "if": [
      "whole milk"
    ],
    "then": "other vegetables",
    "support": 0.0748,
    "confidence": 0.2929,
    "lift": 1.5136
  },
  {
    "if": [
      "other vegetables"
    ],
    "then": "whole milk",
    "support": 0.0748,
    "confidence": 0.3868,
    "lift": 1.5136
  },
  {
    "if": [
      "yogurt"
    ],
    "then": "whole milk",
    "support": 0.056,
    "confidence": 0.4016,
    "lift": 1.5717
  },
  {
    "if": [
      "whole milk"
    ],
    "then": "yogurt",
    "support": 0.056,
    "confidence": 0.2193,
    "lift": 1.5717
  },
  {
    "if": [
      "butter"
    ],
    "then": "whole milk",
    "support": 0.0276,
    "confidence": 0.4972,
    "lift": 1.9461
  },
  {
    "if": [
      "butter"
    ],
    "then": "yogurt",
    "support": 0.0146,
    "confidence": 0.2642,
    "lift": 1.894
  },
  {
    "if": [
      "bottled beer"
    ],
    "then": "other vegetables",
    "support": 0.0162,
    "confidence": 0.2008,
    "lift": 1.0375
  },
  {
    "if": [
      "rolls/buns"
    ],
    "then": "other vegetables",
    "support": 0.0426,
    "confidence": 0.2316,
    "lift": 1.197
  },
  {
    "if": [
      "other vegetables"
    ],
    "then": "rolls/buns",
    "support": 0.0426,
    "confidence": 0.2202,
    "lift": 1.197
  },
  {
    "if": [
      "chocolate"
    ],
    "then": "other vegetables",
    "support": 0.0127,
    "confidence": 0.2561,
    "lift": 1.3238
  },
  {
    "if": [
      "white bread"
    ],
    "then": "other vegetables",
    "support": 0.0137,
    "confidence": 0.3261,
    "lift": 1.6853
  },
  {
    "if": [
      "bottled water"
    ],
    "then": "other vegetables",
    "support": 0.0248,
    "confidence": 0.2245,
    "lift": 1.1601
  },
  {
    "if": [
      "tropical fruit"
    ],
    "then": "other vegetables",
    "support": 0.0359,
    "confidence": 0.3421,
    "lift": 1.7678
  },
  {
    "if": [
      "citrus fruit"
    ],
    "then": "tropical fruit",
    "support": 0.0199,
    "confidence": 0.2408,
    "lift": 2.2947
  },
  {
    "if": [
      "bottled water"
    ],
    "then": "yogurt",
    "support": 0.023,
    "confidence": 0.2079,
    "lift": 1.4904
  },
  {
    "if": [
      "curd"
    ],
    "then": "whole milk",
    "support": 0.0261,
    "confidence": 0.4905,
    "lift": 1.9195
  },
  {
    "if": [
      "tropical fruit"
    ],
    "then": "whole milk",
    "support": 0.0423,
    "confidence": 0.4031,
    "lift": 1.5776
  },
  {
    "if": [
      "bottled water"
    ],
    "then": "whole milk",
    "support": 0.0344,
    "confidence": 0.3109,
    "lift": 1.2169
  },
  {
    "if": [
      "citrus fruit"
    ],
    "then": "whole milk",
    "support": 0.0305,
    "confidence": 0.3686,
    "lift": 1.4424
  },
  {
    "if": [
      "citrus fruit"
    ],
    "then": "yogurt",
    "support": 0.0217,
    "confidence": 0.2617,
    "lift": 1.8758
  },
  {
    "if": [
      "curd"
    ],
    "then": "yogurt",
    "support": 0.0173,
    "confidence": 0.3244,
    "lift": 2.3256
  },
  {
    "if": [
      "frankfurter"
    ],
    "then": "rolls/buns",
    "support": 0.0192,
    "confidence": 0.3259,
    "lift": 1.7716
  },
  {
    "if": [
      "rolls/buns"
    ],
    "then": "soda",
    "support": 0.0383,
    "confidence": 0.2084,
    "lift": 1.1951
  },
  {
    "if": [
      "soda"
    ],
    "then": "rolls/buns",
    "support": 0.0383,
    "confidence": 0.2198,
    "lift": 1.1951
  },
  {
    "if": [
      "root vegetables"
    ],
    "then": "other vegetables",
    "support": 0.0474,
    "confidence": 0.4347,
    "lift": 2.2466
  },
  {
    "if": [
      "other vegetables"
    ],
    "then": "root vegetables",
    "support": 0.0474,
    "confidence": 0.2449,
    "lift": 2.2466
  },
  {
    "if": [
      "waffles"
    ],
    "then": "other vegetables",
    "support": 0.0101,
    "confidence": 0.2619,
    "lift": 1.3536
  },
  {
    "if": [
      "tropical fruit"
    ],
    "then": "root vegetables",
    "support": 0.021,
    "confidence": 0.2006,
    "lift": 1.8402
  },
  {
    "if": [
      "salty snack"
    ],
    "then": "other vegetables",
    "support": 0.0108,
    "confidence": 0.2849,
    "lift": 1.4726
  },
  {
    "if": [
      "root vegetables"
    ],
    "then": "rolls/buns",
    "support": 0.0243,
    "confidence": 0.2229,
    "lift": 1.2121
  },
  {
    "if": [
      "tropical fruit"
    ],
    "then": "rolls/buns",
    "support": 0.0246,
    "confidence": 0.2345,
    "lift": 1.2749
  },
  {
    "if": [
      "sausage"
    ],
    "then": "rolls/buns",
    "support": 0.0306,
    "confidence": 0.3258,
    "lift": 1.771
  },
  {
    "if": [
      "chocolate"
    ],
    "then": "rolls/buns",
    "support": 0.0118,
    "confidence": 0.2377,
    "lift": 1.2923
  },
  {
    "if": [
      "chocolate"
    ],
    "then": "soda",
    "support": 0.0135,
    "confidence": 0.2725,
    "lift": 1.5629
  },
  {
    "if": [
      "sausage"
    ],
    "then": "soda",
    "support": 0.0243,
    "confidence": 0.2587,
    "lift": 1.4833
  },
  {
    "if": [
      "shopping bags"
    ],
    "then": "soda",
    "support": 0.0246,
    "confidence": 0.2497,
    "lift": 1.4322
  },
  {
    "if": [
      "fruit/vegetable juice"
    ],
    "then": "soda",
    "support": 0.0184,
    "confidence": 0.2546,
    "lift": 1.4599
  },
  {
    "if": [
      "bottled water"
    ],
    "then": "rolls/buns",
    "support": 0.0242,
    "confidence": 0.219,
    "lift": 1.1904
  },
  {
    "if": [
      "napkins"
    ],
    "then": "rolls/buns",
    "support": 0.0117,
    "confidence": 0.2233,
    "lift": 1.214
  },
  {
    "if": [
      "napkins"
    ],
    "then": "other vegetables",
    "support": 0.0144,
    "confidence": 0.2757,
    "lift": 1.425
  },
  {
    "if": [
      "hamburger meat"
    ],
    "then": "other vegetables",
    "support": 0.0138,
    "confidence": 0.4159,
    "lift": 2.1494
  },
  {
    "if": [
      "sugar"
    ],
    "then": "whole milk",
    "support": 0.015,
    "confidence": 0.4444,
    "lift": 1.7394
  },
  {
    "if": [
      "root vegetables"
    ],
    "then": "whole milk",
    "support": 0.0489,
    "confidence": 0.4487,
    "lift": 1.756
  },
  {
    "if": [
      "sugar"
    ],
    "then": "other vegetables",
    "support": 0.0108,
    "confidence": 0.3183,
    "lift": 1.6451
  },
  {
    "if": [
      "berries"
    ],
    "then": "other vegetables",
    "support": 0.0103,
    "confidence": 0.3089,
    "lift": 1.5963
  },
  {
    "if": [
      "pork"
    ],
    "then": "whole milk",
    "support": 0.0222,
    "confidence": 0.3845,
    "lift": 1.5047
  },
  {
    "if": [
      "whipped/sour cream"
    ],
    "then": "whole milk",
    "support": 0.0322,
    "confidence": 0.4496,
    "lift": 1.7598
  },
  {
    "if": [
      "berries"
    ],
    "then": "whole milk",
    "support": 0.0118,
    "confidence": 0.3547,
    "lift": 1.3883
  },
  {
    "if": [
      "pork"
    ],
    "then": "other vegetables",
    "support": 0.0217,
    "confidence": 0.3757,
    "lift": 1.9415
  },
  {
    "if": [
      "whipped/sour cream"
    ],
    "then": "other vegetables",
    "support": 0.0289,
    "confidence": 0.4028,
    "lift": 2.0819
  },
  {
    "if": [
      "pork"
    ],
    "then": "soda",
    "support": 0.0119,
    "confidence": 0.2063,
    "lift": 1.1833
  },
  {
    "if": [
      "pastry"
    ],
    "then": "soda",
    "support": 0.021,
    "confidence": 0.2366,
    "lift": 1.3567
  },
  {
    "if": [
      "dessert"
    ],
    "then": "whole milk",
    "support": 0.0137,
    "confidence": 0.3699,
    "lift": 1.4475
  },
  {
    "if": [
      "dessert"
    ],
    "then": "other vegetables",
    "support": 0.0116,
    "confidence": 0.3123,
    "lift": 1.6142
  },
  {
    "if": [
      "waffles"
    ],
    "then": "whole milk",
    "support": 0.0127,
    "confidence": 0.3307,
    "lift": 1.2942
  },
  {
    "if": [
      "domestic eggs"
    ],
    "then": "yogurt",
    "support": 0.0143,
    "confidence": 0.226,
    "lift": 1.6198
  },
  {
    "if": [
      "root vegetables"
    ],
    "then": "yogurt",
    "support": 0.0258,
    "confidence": 0.2369,
    "lift": 1.6985
  },
  {
    "if": [
      "pastry"
    ],
    "then": "whole milk",
    "support": 0.0332,
    "confidence": 0.3737,
    "lift": 1.4626
  },
  {
    "if": [
      "brown bread"
    ],
    "then": "whole milk",
    "support": 0.0252,
    "confidence": 0.3887,
    "lift": 1.5213
  },
  {
    "if": [
      "domestic eggs"
    ],
    "then": "whole milk",
    "support": 0.03,
    "confidence": 0.4728,
    "lift": 1.8502
  },
  {
    "if": [
      "brown bread"
    ],
    "then": "yogurt",
    "support": 0.0145,
    "confidence": 0.2241,
    "lift": 1.6067
  },
  {
    "if": [
      "domestic eggs"
    ],
    "then": "root vegetables",
    "support": 0.0143,
    "confidence": 0.226,
    "lift": 2.0731
  },
  {
    "if": [
      "coffee"
    ],
    "then": "whole milk",
    "support": 0.0187,
    "confidence": 0.3222,
    "lift": 1.2611
  },
  {
    "if": [
      "berries"
    ],
    "then": "yogurt",
    "support": 0.0106,
    "confidence": 0.318,
    "lift": 2.2798
  },
  {
    "if": [
      "bottled water"
    ],
    "then": "soda",
    "support": 0.029,
    "confidence": 0.2622,
    "lift": 1.5036
  },
  {
    "if": [
      "yogurt"
    ],
    "then": "rolls/buns",
    "support": 0.0344,
    "confidence": 0.2464,
    "lift": 1.3394
  },
  {
    "if": [
      "newspapers"
    ],
    "then": "rolls/buns",
    "support": 0.0197,
    "confidence": 0.2471,
    "lift": 1.3436
  },
  {
    "if": [
      "curd"
    ],
    "then": "other vegetables",
    "support": 0.0172,
    "confidence": 0.3225,
    "lift": 1.6668
  },
  {
    "if": [
      "butter"
    ],
    "then": "root vegetables",
    "support": 0.0129,
    "confidence": 0.233,
    "lift": 2.1379
  },
  {
    "if": [
      "curd"
    ],
    "then": "root vegetables",
    "support": 0.0109,
    "confidence": 0.2042,
    "lift": 1.8734
  },
  {
    "if": [
      "butter"
    ],
    "then": "other vegetables",
    "support": 0.02,
    "confidence": 0.3615,
    "lift": 1.8681
  },
  {
    "if": [
      "whipped/sour cream"
    ],
    "then": "rolls/buns",
    "support": 0.0146,
    "confidence": 0.2043,
    "lift": 1.1105
  },
  {
    "if": [
      "whipped/sour cream"
    ],
    "then": "root vegetables",
    "support": 0.0171,
    "confidence": 0.2383,
    "lift": 2.1862
  },
  {
    "if": [
      "butter"
    ],
    "then": "rolls/buns",
    "support": 0.0134,
    "confidence": 0.2422,
    "lift": 1.3168
  },
  {
    "if": [
      "ham"
    ],
    "then": "whole milk",
    "support": 0.0115,
    "confidence": 0.4414,
    "lift": 1.7275
  },
  {
    "if": [
      "brown bread"
    ],
    "then": "other vegetables",
    "support": 0.0187,
    "confidence": 0.2884,
    "lift": 1.4905
  },
  {
    "if": [
      "margarine"
    ],
    "then": "other vegetables",
    "support": 0.0197,
    "confidence": 0.3368,
    "lift": 1.7407
  },
  {
    "if": [
      "fruit/vegetable juice"
    ],
    "then": "other vegetables",
    "support": 0.021,
    "confidence": 0.2911,
    "lift": 1.5047
  },
  {
    "if": [
      "domestic eggs"
    ],
    "then": "other vegetables",
    "support": 0.0223,
    "confidence": 0.351,
    "lift": 1.8138
  },
  {
    "if": [
      "beef"
    ],
    "then": "rolls/buns",
    "support": 0.0136,
    "confidence": 0.2597,
    "lift": 1.4119
  },
  {
    "if": [
      "pastry"
    ],
    "then": "rolls/buns",
    "support": 0.0209,
    "confidence": 0.2354,
    "lift": 1.28
  },
  {
    "if": [
      "frozen vegetables"
    ],
    "then": "whole milk",
    "support": 0.0204,
    "confidence": 0.4249,
    "lift": 1.6631
  },
  {
    "if": [
      "frozen vegetables"
    ],
    "then": "other vegetables",
    "support": 0.0178,
    "confidence": 0.37,
    "lift": 1.9121
  },
  {
    "if": [
      "salty snack"
    ],
    "then": "whole milk",
    "support": 0.0112,
    "confidence": 0.2957,
    "lift": 1.1573
  },
  {
    "if": [
      "beef"
    ],
    "then": "whole milk",
    "support": 0.0213,
    "confidence": 0.405,
    "lift": 1.5852
  },
  {
    "if": [
      "sausage"
    ],
    "then": "whole milk",
    "support": 0.0299,
    "confidence": 0.3182,
    "lift": 1.2453
  },
  {
    "if": [
      "pip fruit"
    ],
    "then": "whole milk",
    "support": 0.0301,
    "confidence": 0.3978,
    "lift": 1.557
  },
  {
    "if": [
      "pip fruit"
    ],
    "then": "tropical fruit",
    "support": 0.0204,
    "confidence": 0.2702,
    "lift": 2.5746
  },
  {
    "if": [
      "rolls/buns"
    ],
    "then": "whole milk",
    "support": 0.0566,
    "confidence": 0.3079,
    "lift": 1.205
  },
  {
    "if": [
      "whole milk"
    ],
    "then": "rolls/buns",
    "support": 0.0566,
    "confidence": 0.2216,
    "lift": 1.205
  },
  {
    "if": [
      "chocolate"
    ],
    "then": "whole milk",
    "support": 0.0167,
    "confidence": 0.3361,
    "lift": 1.3152
  },
  {
    "if": [
      "margarine"
    ],
    "then": "whole milk",
    "support": 0.0242,
    "confidence": 0.4132,
    "lift": 1.6171
  },
  {
    "if": [
      "oil"
    ],
    "then": "whole milk",
    "support": 0.0113,
    "confidence": 0.4022,
    "lift": 1.574
  },
  {
    "if": [
      "newspapers"
    ],
    "then": "whole milk",
    "support": 0.0274,
    "confidence": 0.3427,
    "lift": 1.3411
  },
  {
    "if": [
      "frankfurter"
    ],
    "then": "whole milk",
    "support": 0.0205,
    "confidence": 0.3483,
    "lift": 1.363
  },
  {
    "if": [
      "butter milk"
    ],
    "then": "whole milk",
    "support": 0.0116,
    "confidence": 0.4145,
    "lift": 1.6224
  },
  {
    "if": [
      "bottled beer"
    ],
    "then": "soda",
    "support": 0.017,
    "confidence": 0.2109,
    "lift": 1.2092
  },
  {
    "if": [
      "fruit/vegetable juice"
    ],
    "then": "whole milk",
    "support": 0.0266,
    "confidence": 0.3685,
    "lift": 1.4422
  },
  {
    "if": [
      "domestic eggs"
    ],
    "then": "rolls/buns",
    "support": 0.0157,
    "confidence": 0.2468,
    "lift": 1.3418
  },
  {
    "if": [
      "margarine"
    ],
    "then": "rolls/buns",
    "support": 0.0147,
    "confidence": 0.2517,
    "lift": 1.3686
  },
  {
    "if": [
      "frozen vegetables"
    ],
    "then": "rolls/buns",
    "support": 0.0102,
    "confidence": 0.2114,
    "lift": 1.1494
  },
  {
    "if": [
      "fruit/vegetable juice"
    ],
    "then": "rolls/buns",
    "support": 0.0145,
    "confidence": 0.2011,
    "lift": 1.0935
  },
  {
    "if": [
      "frozen vegetables"
    ],
    "then": "root vegetables",
    "support": 0.0116,
    "confidence": 0.241,
    "lift": 2.2112
  },
  {
    "if": [
      "sausage"
    ],
    "then": "yogurt",
    "support": 0.0196,
    "confidence": 0.2089,
    "lift": 1.4973
  },
  {
    "if": [
      "chicken"
    ],
    "then": "root vegetables",
    "support": 0.0109,
    "confidence": 0.2536,
    "lift": 2.3262
  },
  {
    "if": [
      "chicken"
    ],
    "then": "other vegetables",
    "support": 0.0179,
    "confidence": 0.4171,
    "lift": 2.1554
  },
  {
    "if": [
      "citrus fruit"
    ],
    "then": "root vegetables",
    "support": 0.0177,
    "confidence": 0.2138,
    "lift": 1.9611
  },
  {
    "if": [
      "citrus fruit"
    ],
    "then": "other vegetables",
    "support": 0.0289,
    "confidence": 0.3489,
    "lift": 1.8031
  },
  {
    "if": [
      "fruit/vegetable juice"
    ],
    "then": "yogurt",
    "support": 0.0187,
    "confidence": 0.2588,
    "lift": 1.8551
  },
  {
    "if": [
      "napkins"
    ],
    "then": "yogurt",
    "support": 0.0123,
    "confidence": 0.235,
    "lift": 1.6842
  },
  {
    "if": [
      "napkins"
    ],
    "then": "whole milk",
    "support": 0.0197,
    "confidence": 0.3767,
    "lift": 1.4743
  },
  {
    "if": [
      "beef"
    ],
    "then": "root vegetables",
    "support": 0.0174,
    "confidence": 0.3314,
    "lift": 3.0404
  },
  {
    "if": [
      "frankfurter"
    ],
    "then": "other vegetables",
    "support": 0.0165,
    "confidence": 0.2793,
    "lift": 1.4435
  },
  {
    "if": [
      "sausage"
    ],
    "then": "other vegetables",
    "support": 0.0269,
    "confidence": 0.2868,
    "lift": 1.4822
  },
  {
    "if": [
      "hamburger meat"
    ],
    "then": "whole milk",
    "support": 0.0147,
    "confidence": 0.4434,
    "lift": 1.7354
  },
  {
    "if": [
      "cream cheese"
    ],
    "then": "whole milk",
    "support": 0.0165,
    "confidence": 0.4154,
    "lift": 1.6257
  },
  {
    "if": [
      "pastry"
    ],
    "then": "other vegetables",
    "support": 0.0226,
    "confidence": 0.2537,
    "lift": 1.3112
  },
  {
    "if": [
      "shopping bags"
    ],
    "then": "other vegetables",
    "support": 0.0232,
    "confidence": 0.2353,
    "lift": 1.216
  },
  {
    "if": [
      "coffee"
    ],
    "then": "other vegetables",
    "support": 0.0134,
    "confidence": 0.2312,
    "lift": 1.1947
  },
  {
    "if": [
      "hard cheese"
    ],
    "then": "whole milk",
    "support": 0.0101,
    "confidence": 0.4108,
    "lift": 1.6077
  },
  {
    "if": [
      "hygiene articles"
    ],
    "then": "whole milk",
    "support": 0.0128,
    "confidence": 0.3889,
    "lift": 1.522
  },
  {
    "if": [
      "pip fruit"
    ],
    "then": "other vegetables",
    "support": 0.0261,
    "confidence": 0.3454,
    "lift": 1.7852
  },
  {
    "if": [
      "citrus fruit"
    ],
    "then": "rolls/buns",
    "support": 0.0168,
    "confidence": 0.2027,
    "lift": 1.102
  },
  {
    "if": [
      "yogurt"
    ],
    "then": "other vegetables",
    "support": 0.0434,
    "confidence": 0.3112,
    "lift": 1.6085
  },
  {
    "if": [
      "other vegetables"
    ],
    "then": "yogurt",
    "support": 0.0434,
    "confidence": 0.2244,
    "lift": 1.6085
  },
  {
    "if": [
      "frozen vegetables"
    ],
    "then": "yogurt",
    "support": 0.0124,
    "confidence": 0.2579,
    "lift": 1.8489
  },
  {
    "if": [
      "white bread"
    ],
    "then": "whole milk",
    "support": 0.0171,
    "confidence": 0.4058,
    "lift": 1.5881
  },
  {
    "if": [
      "cream cheese"
    ],
    "then": "other vegetables",
    "support": 0.0137,
    "confidence": 0.3462,
    "lift": 1.789
  },
  {
    "if": [
      "whipped/sour cream"
    ],
    "then": "yogurt",
    "support": 0.0207,
    "confidence": 0.2894,
    "lift": 2.0743
  },
  {
    "if": [
      "sliced cheese"
    ],
    "then": "whole milk",
    "support": 0.0108,
    "confidence": 0.4398,
    "lift": 1.7214
  },
  {
    "if": [
      "pip fruit"
    ],
    "then": "root vegetables",
    "support": 0.0156,
    "confidence": 0.2056,
    "lift": 1.8867
  },
  {
    "if": [
      "pork"
    ],
    "then": "root vegetables",
    "support": 0.0136,
    "confidence": 0.2363,
    "lift": 2.1682
  },
  {
    "if": [
      "butter milk"
    ],
    "then": "other vegetables",
    "support": 0.0104,
    "confidence": 0.3709,
    "lift": 1.9169
  },
  {
    "if": [
      "beef"
    ],
    "then": "other vegetables",
    "support": 0.0197,
    "confidence": 0.376,
    "lift": 1.9431
  },
  {
    "if": [
      "napkins"
    ],
    "then": "soda",
    "support": 0.012,
    "confidence": 0.2291,
    "lift": 1.314
  },
  {
    "if": [
      "newspapers"
    ],
    "then": "other vegetables",
    "support": 0.0193,
    "confidence": 0.242,
    "lift": 1.2509
  },
  {
    "if": [
      "onions"
    ],
    "then": "whole milk",
    "support": 0.0121,
    "confidence": 0.3902,
    "lift": 1.527
  },
  {
    "if": [
      "onions"
    ],
    "then": "other vegetables",
    "support": 0.0142,
    "confidence": 0.459,
    "lift": 2.3723
  },
  {
    "if": [
      "margarine"
    ],
    "then": "yogurt",
    "support": 0.0142,
    "confidence": 0.2431,
    "lift": 1.7423
  },
  {
    "if": [
      "chicken"
    ],
    "then": "whole milk",
    "support": 0.0176,
    "confidence": 0.41,
    "lift": 1.6044
  },
  {
    "if": [
      "beef"
    ],
    "then": "yogurt",
    "support": 0.0117,
    "confidence": 0.2229,
    "lift": 1.5976
  },
  {
    "if": [
      "white bread"
    ],
    "then": "soda",
    "support": 0.0103,
    "confidence": 0.244,
    "lift": 1.399
  },
  {
    "if": [
      "tropical fruit",
      "yogurt"
    ],
    "then": "whole milk",
    "support": 0.0151,
    "confidence": 0.5174,
    "lift": 2.0248
  },
  {
    "if": [
      "tropical fruit",
      "whole milk"
    ],
    "then": "yogurt",
    "support": 0.0151,
    "confidence": 0.3582,
    "lift": 2.5675
  },
  {
    "if": [
      "yogurt",
      "whole milk"
    ],
    "then": "tropical fruit",
    "support": 0.0151,
    "confidence": 0.2704,
    "lift": 2.5771
  },
  {
    "if": [
      "citrus fruit",
      "yogurt"
    ],
    "then": "whole milk",
    "support": 0.0103,
    "confidence": 0.4742,
    "lift": 1.8558
  },
  {
    "if": [
      "citrus fruit",
      "whole milk"
    ],
    "then": "yogurt",
    "support": 0.0103,
    "confidence": 0.3367,
    "lift": 2.4134
  },
  {
    "if": [
      "yogurt",
      "curd"
    ],
    "then": "whole milk",
    "support": 0.0101,
    "confidence": 0.5824,
    "lift": 2.2791
  },
  {
    "if": [
      "whole milk",
      "curd"
    ],
    "then": "yogurt",
    "support": 0.0101,
    "confidence": 0.3852,
    "lift": 2.7614
  },
  {
    "if": [
      "tropical fruit",
      "other vegetables"
    ],
    "then": "root vegetables",
    "support": 0.0123,
    "confidence": 0.3428,
    "lift": 3.1448
  },
  {
    "if": [
      "tropical fruit",
      "root vegetables"
    ],
    "then": "other vegetables",
    "support": 0.0123,
    "confidence": 0.5845,
    "lift": 3.021
  },
  {
    "if": [
      "root vegetables",
      "other vegetables"
    ],
    "then": "tropical fruit",
    "support": 0.0123,
    "confidence": 0.2597,
    "lift": 2.4745
  },
  {
    "if": [
      "rolls/buns",
      "root vegetables"
    ],
    "then": "other vegetables",
    "support": 0.0122,
    "confidence": 0.5021,
    "lift": 2.5949
  },
  {
    "if": [
      "rolls/buns",
      "other vegetables"
    ],
    "then": "root vegetables",
    "support": 0.0122,
    "confidence": 0.2864,
    "lift": 2.6275
  },
  {
    "if": [
      "root vegetables",
      "other vegetables"
    ],
    "then": "rolls/buns",
    "support": 0.0122,
    "confidence": 0.2575,
    "lift": 1.4
  },
  {
    "if": [
      "root vegetables"
    ],
    "then": "whole milk",
    "support": 0.0232,
    "confidence": 0.2127,
    "lift": 2.8421
  },
  {
    "if": [
      "root vegetables",
      "whole milk"
    ],
    "then": "other vegetables",
    "support": 0.0232,
    "confidence": 0.474,
    "lift": 2.4498
  },
  {
    "if": [
      "root vegetables",
      "other vegetables"
    ],
    "then": "whole milk",
    "support": 0.0232,
    "confidence": 0.4893,
    "lift": 1.9148
  },
  {
    "if": [
      "whole milk",
      "other vegetables"
    ],
    "then": "root vegetables",
    "support": 0.0232,
    "confidence": 0.3098,
    "lift": 2.8421
  },
  {
    "if": [
      "whipped/sour cream"
    ],
    "then": "whole milk",
    "support": 0.0146,
    "confidence": 0.2043,
    "lift": 2.7294
  },
  {
    "if": [
      "whole milk",
      "whipped/sour cream"
    ],
    "then": "other vegetables",
    "support": 0.0146,
    "confidence": 0.4543,
    "lift": 2.3477
  },
  {
    "if": [
      "other vegetables",
      "whipped/sour cream"
    ],
    "then": "whole milk",
    "support": 0.0146,
    "confidence": 0.507,
    "lift": 1.9844
  },
  {
    "if": [
      "pork",
      "whole milk"
    ],
    "then": "other vegetables",
    "support": 0.0102,
    "confidence": 0.4587,
    "lift": 2.3707
  },
  {
    "if": [
      "pork",
      "other vegetables"
    ],
    "then": "whole milk",
    "support": 0.0102,
    "confidence": 0.4695,
    "lift": 1.8374
  },
  {
    "if": [
      "soda",
      "whole milk"
    ],
    "then": "other vegetables",
    "support": 0.0139,
    "confidence": 0.3477,
    "lift": 1.797
  },
  {
    "if": [
      "soda",
      "other vegetables"
    ],
    "then": "whole milk",
    "support": 0.0139,
    "confidence": 0.4255,
    "lift": 1.6651
  },
  {
    "if": [
      "tropical fruit",
      "whole milk"
    ],
    "then": "root vegetables",
    "support": 0.012,
    "confidence": 0.2837,
    "lift": 2.6024
  },
  {
    "if": [
      "tropical fruit",
      "root vegetables"
    ],
    "then": "whole milk",
    "support": 0.012,
    "confidence": 0.57,
    "lift": 2.231
  },
  {
    "if": [
      "root vegetables",
      "whole milk"
    ],
    "then": "tropical fruit",
    "support": 0.012,
    "confidence": 0.2453,
    "lift": 2.3379
  },
  {
    "if": [
      "soda",
      "yogurt"
    ],
    "then": "whole milk",
    "support": 0.0105,
    "confidence": 0.3829,
    "lift": 1.4985
  },
  {
    "if": [
      "soda",
      "whole milk"
    ],
    "then": "yogurt",
    "support": 0.0105,
    "confidence": 0.2614,
    "lift": 1.874
  },
  {
    "if": [
      "root vegetables",
      "yogurt"
    ],
    "then": "whole milk",
    "support": 0.0145,
    "confidence": 0.563,
    "lift": 2.2034
  },
  {
    "if": [
      "root vegetables",
      "whole milk"
    ],
    "then": "yogurt",
    "support": 0.0145,
    "confidence": 0.2973,
    "lift": 2.1311
  },
  {
    "if": [
      "yogurt",
      "whole milk"
    ],
    "then": "root vegetables",
    "support": 0.0145,
    "confidence": 0.2595,
    "lift": 2.381
  },
  {
    "if": [
      "rolls/buns",
      "tropical fruit"
    ],
    "then": "whole milk",
    "support": 0.011,
    "confidence": 0.4463,
    "lift": 1.7466
  },
  {
    "if": [
      "tropical fruit",
      "whole milk"
    ],
    "then": "rolls/buns",
    "support": 0.011,
    "confidence": 0.2596,
    "lift": 1.4115
  },
  {
    "if": [
      "rolls/buns",
      "whole milk"
    ],
    "then": "other vegetables",
    "support": 0.0179,
    "confidence": 0.316,
    "lift": 1.633
  },
  {
    "if": [
      "rolls/buns",
      "other vegetables"
    ],
    "then": "whole milk",
    "support": 0.0179,
    "confidence": 0.42,
    "lift": 1.6439
  },
  {
    "if": [
      "whole milk",
      "other vegetables"
    ],
    "then": "rolls/buns",
    "support": 0.0179,
    "confidence": 0.2391,
    "lift": 1.3001
  },
  {
    "if": [
      "rolls/buns",
      "root vegetables"
    ],
    "then": "whole milk",
    "support": 0.0127,
    "confidence": 0.523,
    "lift": 2.0469
  },
  {
    "if": [
      "rolls/buns",
      "whole milk"
    ],
    "then": "root vegetables",
    "support": 0.0127,
    "confidence": 0.2244,
    "lift": 2.0589
  },
  {
    "if": [
      "root vegetables",
      "whole milk"
    ],
    "then": "rolls/buns",
    "support": 0.0127,
    "confidence": 0.2599,
    "lift": 1.4129
  },
  {
    "if": [
      "citrus fruit",
      "root vegetables"
    ],
    "then": "other vegetables",
    "support": 0.0104,
    "confidence": 0.5862,
    "lift": 3.0296
  },
  {
    "if": [
      "citrus fruit",
      "other vegetables"
    ],
    "then": "root vegetables",
    "support": 0.0104,
    "confidence": 0.3592,
    "lift": 3.295
  },
  {
    "if": [
      "root vegetables",
      "other vegetables"
    ],
    "then": "citrus fruit",
    "support": 0.0104,
    "confidence": 0.2189,
    "lift": 2.6446
  },
  {
    "if": [
      "whole milk",
      "domestic eggs"
    ],
    "then": "other vegetables",
    "support": 0.0123,
    "confidence": 0.4102,
    "lift": 2.1198
  },
  {
    "if": [
      "other vegetables",
      "domestic eggs"
    ],
    "then": "whole milk",
    "support": 0.0123,
    "confidence": 0.5525,
    "lift": 2.1623
  },
  {
    "if": [
      "whole milk",
      "pip fruit"
    ],
    "then": "other vegetables",
    "support": 0.0135,
    "confidence": 0.4493,
    "lift": 2.3222
  },
  {
    "if": [
      "other vegetables",
      "pip fruit"
    ],
    "then": "whole milk",
    "support": 0.0135,
    "confidence": 0.5175,
    "lift": 2.0254
  },
  {
    "if": [
      "root vegetables",
      "yogurt"
    ],
    "then": "other vegetables",
    "support": 0.0129,
    "confidence": 0.5,
    "lift": 2.5841
  },
  {
    "if": [
      "root vegetables",
      "other vegetables"
    ],
    "then": "yogurt",
    "support": 0.0129,
    "confidence": 0.2725,
    "lift": 1.9536
  },
  {
    "if": [
      "yogurt",
      "other vegetables"
    ],
    "then": "root vegetables",
    "support": 0.0129,
    "confidence": 0.2974,
    "lift": 2.7287
  },
  {
    "if": [
      "whole milk",
      "yogurt"
    ],
    "then": "other vegetables",
    "support": 0.0223,
    "confidence": 0.3975,
    "lift": 2.0541
  },
  {
    "if": [
      "whole milk",
      "other vegetables"
    ],
    "then": "yogurt",
    "support": 0.0223,
    "confidence": 0.2976,
    "lift": 2.133
  },
  {
    "if": [
      "yogurt",
      "other vegetables"
    ],
    "then": "whole milk",
    "support": 0.0223,
    "confidence": 0.5129,
    "lift": 2.0072
  },
  {
    "if": [
      "fruit/vegetable juice",
      "whole milk"
    ],
    "then": "other vegetables",
    "support": 0.0105,
    "confidence": 0.3931,
    "lift": 2.0318
  },
  {
    "if": [
      "fruit/vegetable juice",
      "other vegetables"
    ],
    "then": "whole milk",
    "support": 0.0105,
    "confidence": 0.4976,
    "lift": 1.9474
  },
  {
    "if": [
      "tropical fruit",
      "whole milk"
    ],
    "then": "other vegetables",
    "support": 0.0171,
    "confidence": 0.4038,
    "lift": 2.0871
  },
  {
    "if": [
      "tropical fruit",
      "other vegetables"
    ],
    "then": "whole milk",
    "support": 0.0171,
    "confidence": 0.4759,
    "lift": 1.8626
  },
  {
    "if": [
      "whole milk",
      "other vegetables"
    ],
    "then": "tropical fruit",
    "support": 0.0171,
    "confidence": 0.2283,
    "lift": 2.1753
  },
  {
    "if": [
      "yogurt",
      "whipped/sour cream"
    ],
    "then": "other vegetables",
    "support": 0.0102,
    "confidence": 0.4902,
    "lift": 2.5334
  },
  {
    "if": [
      "other vegetables",
      "whipped/sour cream"
    ],
    "then": "yogurt",
    "support": 0.0102,
    "confidence": 0.3521,
    "lift": 2.5241
  },
  {
    "if": [
      "yogurt",
      "other vegetables"
    ],
    "then": "whipped/sour cream",
    "support": 0.0102,
    "confidence": 0.2342,
    "lift": 3.2671
  },
  {
    "if": [
      "butter"
    ],
    "then": "whole milk",
    "support": 0.0115,
    "confidence": 0.2073,
    "lift": 2.7706
  },
  {
    "if": [
      "whole milk",
      "butter"
    ],
    "then": "other vegetables",
    "support": 0.0115,
    "confidence": 0.417,
    "lift": 2.155
  },
  {
    "if": [
      "butter",
      "other vegetables"
    ],
    "then": "whole milk",
    "support": 0.0115,
    "confidence": 0.5736,
    "lift": 2.2449
  },
  {
    "if": [
      "tropical fruit",
      "yogurt"
    ],
    "then": "other vegetables",
    "support": 0.0123,
    "confidence": 0.4201,
    "lift": 2.1713
  },
  {
    "if": [
      "tropical fruit",
      "other vegetables"
    ],
    "then": "yogurt",
    "support": 0.0123,
    "confidence": 0.3428,
    "lift": 2.4571
  },
  {
    "if": [
      "yogurt",
      "other vegetables"
    ],
    "then": "tropical fruit",
    "support": 0.0123,
    "confidence": 0.2834,
    "lift": 2.7005
  },
  {
    "if": [
      "yogurt",
      "whipped/sour cream"
    ],
    "then": "whole milk",
    "support": 0.0109,
    "confidence": 0.5245,
    "lift": 2.0527
  },
  {
    "if": [
      "whole milk",
      "whipped/sour cream"
    ],
    "then": "yogurt",
    "support": 0.0109,
    "confidence": 0.3375,
    "lift": 2.4196
  },
  {
    "if": [
      "sausage",
      "whole milk"
    ],
    "then": "other vegetables",
    "support": 0.0102,
    "confidence": 0.3401,
    "lift": 1.7579
  },
  {
    "if": [
      "sausage",
      "other vegetables"
    ],
    "then": "whole milk",
    "support": 0.0102,
    "confidence": 0.3774,
    "lift": 1.4768
  },
  {
    "if": [
      "citrus fruit",
      "whole milk"
    ],
    "then": "other vegetables",
    "support": 0.013,
    "confidence": 0.4267,
    "lift": 2.2051
  },
  {
    "if": [
      "citrus fruit",
      "other vegetables"
    ],
    "then": "whole milk",
    "support": 0.013,
    "confidence": 0.4507,
    "lift": 1.7639
  },
  {
    "if": [
      "rolls/buns",
      "yogurt"
    ],
    "then": "whole milk",
    "support": 0.0156,
    "confidence": 0.4527,
    "lift": 1.7716
  },
  {
    "if": [
      "rolls/buns",
      "whole milk"
    ],
    "then": "yogurt",
    "support": 0.0156,
    "confidence": 0.2747,
    "lift": 1.969
  },
  {
    "if": [
      "yogurt",
      "whole milk"
    ],
    "then": "rolls/buns",
    "support": 0.0156,
    "confidence": 0.2777,
    "lift": 1.5096
  },
  {
    "if": [
      "whole milk",
      "bottled water"
    ],
    "then": "other vegetables",
    "support": 0.0108,
    "confidence": 0.3136,
    "lift": 1.6208
  },
  {
    "if": [
      "bottled water",
      "other vegetables"
    ],
    "then": "whole milk",
    "support": 0.0108,
    "confidence": 0.4344,
    "lift": 1.7002
  },
  {
    "if": [
      "rolls/buns",
      "yogurt"
    ],
    "then": "other vegetables",
    "support": 0.0115,
    "confidence": 0.3343,
    "lift": 1.7278
  },
  {
    "if": [
      "rolls/buns",
      "other vegetables"
    ],
    "then": "yogurt",
    "support": 0.0115,
    "confidence": 0.2697,
    "lift": 1.9332
  },
  {
    "if": [
      "yogurt",
      "other vegetables"
    ],
    "then": "rolls/buns",
    "support": 0.0115,
    "confidence": 0.2646,
    "lift": 1.4388
  },
  {
    "if": [
      "pastry",
      "whole milk"
    ],
    "then": "other vegetables",
    "support": 0.0106,
    "confidence": 0.318,
    "lift": 1.6437
  },
  {
    "if": [
      "pastry",
      "other vegetables"
    ],
    "then": "whole milk",
    "support": 0.0106,
    "confidence": 0.4685,
    "lift": 1.8334
  }
]

def recommend_products(basket, top_n=5):
    """
    Recommend products for a given basket using Apriori rules.
    """
    basket_set = set(basket)
    recs = []
    for rule in apriori_rules:
        if set(rule['if']).issubset(basket_set) and rule['then'] not in basket_set:
            recs.append(rule['then'])
    recs = list(dict.fromkeys(recs))  # remove duplicates
    return recs[:top_n]

if __name__ == "__main__":
    sample_basket = ["whole milk", "rolls/buns"]
    print("Sample Basket:", sample_basket)
    print("Recommended Products:", recommend_products(sample_basket))
