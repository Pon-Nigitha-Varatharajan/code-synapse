#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 18:40:27 2025

@author: ponnigithav
"""

from apriori import run_apriori
from fp import run_fp_growth

def run_miner(algo, baskets, min_support, min_confidence, min_lift):
    if algo == "apriori":
        return run_apriori(baskets, min_support, min_confidence, min_lift)
    elif algo == "fp":
        return run_fp_growth(baskets, min_support, min_confidence, min_lift)
    else:
        raise ValueError(f"Unknown algorithm: {algo}")