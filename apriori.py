from itertools import combinations
from collections import defaultdict
import itertools

def get_support(itemset, baskets):
    return sum(1 for basket in baskets if set(itemset).issubset(basket)) / len(baskets)


def generate_rules(all_freq_itemsets, baskets, min_confidence, min_lift):
    rules = []
    for itemset, support in all_freq_itemsets.items():
        if len(itemset) < 2:
            continue
        for i in range(1, len(itemset)):
            for lhs in combinations(itemset, i):
                lhs_set = frozenset(lhs)
                rhs_set = itemset - lhs_set
                lhs_support = all_freq_itemsets.get(lhs_set, get_support(lhs_set, baskets))
                rhs_support = all_freq_itemsets.get(rhs_set, get_support(rhs_set, baskets))
                confidence = support / lhs_support if lhs_support > 0 else 0
                lift = confidence / rhs_support if rhs_support > 0 else 0
                if confidence >= min_confidence and lift >= min_lift:
                    rules.append({
                        "if": list(lhs_set),
                        "then": list(rhs_set),
                        "support": round(support, 4),
                        "confidence": round(confidence, 4),
                        "lift": round(lift, 4)
                    })
    return rules


def run_apriori(baskets, min_support, min_confidence, min_lift):
    total_baskets = len(baskets)
    item_counts = defaultdict(int)

    # Step 1: 1-itemsets
    for basket in baskets:
        for item in basket:
            item_counts[frozenset([item])] += 1

    freq_itemsets = {itemset: count / total_baskets
                     for itemset, count in item_counts.items()
                     if count / total_baskets >= min_support}
    all_freq_itemsets = dict(freq_itemsets)
    k = 2

    # Step 2: Iterative candidate generation
    while freq_itemsets:
        candidates = set()
        itemsets_list = list(freq_itemsets.keys())
        for i in range(len(itemsets_list)):
            for j in range(i+1, len(itemsets_list)):
                a, b = itemsets_list[i], itemsets_list[j]
                union_set = a | b
                if len(union_set) == k:
                    candidates.add(union_set)

        candidate_counts = defaultdict(int)
        for basket in baskets:
            basket_set = set(basket)
            for cand in candidates:
                if cand.issubset(basket_set):
                    candidate_counts[cand] += 1

        freq_itemsets = {cand: count / total_baskets
                         for cand, count in candidate_counts.items()
                         if count / total_baskets >= min_support}
        all_freq_itemsets.update(freq_itemsets)
        k += 1

    # Step 3: Generate rules
    rules = generate_rules(all_freq_itemsets, baskets, min_confidence, min_lift)
    return rules


def evaluate_rules(rules, test_baskets):
    """Evaluate coverage, average confidence and average lift on test set"""
    covered = 0
    total_confidence = 0
    total_lift = 0
    for basket in test_baskets:
        for rule in rules:
            if set(rule['if']).issubset(basket):
                covered += 1
                total_confidence += rule['confidence']
                total_lift += rule['lift']
                break
    coverage = covered / len(test_baskets) if len(test_baskets) > 0 else 0
    avg_confidence = total_confidence / covered if covered > 0 else 0
    avg_lift = total_lift / covered if covered > 0 else 0
    return coverage, avg_confidence, avg_lift


def find_optimal_thresholds(train_baskets, test_baskets,
                            support_values=[0.01,0.02,0.03],
                            confidence_values=[0.3,0.4,0.5],
                            lift_values=[0.5,1.0,1.5]):
    """
    Grid search over support, confidence, lift to find optimal thresholds based on test set coverage
    """
    best_score = -1
    best_params = None
    best_rules = []

    for s, c, l in itertools.product(support_values, confidence_values, lift_values):
        rules = run_apriori(train_baskets, min_support=s, min_confidence=c, min_lift=l)
        coverage, avg_conf, avg_lift = evaluate_rules(rules, test_baskets)
        # simple scoring: coverage * avg_conf * avg_lift
        score = coverage * avg_conf * avg_lift
        if score > best_score:
            best_score = score
            best_params = (s, c, l)
            best_rules = rules

    return {
        "optimal_support": best_params[0],
        "optimal_confidence": best_params[1],
        "optimal_lift": best_params[2],
        "coverage": evaluate_rules(best_rules, test_baskets)[0],
        "avg_confidence": evaluate_rules(best_rules, test_baskets)[1],
        "avg_lift": evaluate_rules(best_rules, test_baskets)[2],
        "rules": best_rules
    }