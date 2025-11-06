from itertools import combinations
from collections import defaultdict
import itertools
import csv
import os

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
                        "lift": round(lift, 4),
                        "itemset_size": len(itemset)
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

def save_rules_to_csv(rules, filename="apriori_rules.csv", include_params=False, params=None):
    """Save Apriori rules to CSV file"""
    if not rules:
        print("No rules to save.")
        return
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        if include_params and params:
            fieldnames = ['antecedent', 'consequent', 'support', 'confidence', 'lift', 
                         'itemset_size', 'min_support', 'min_confidence', 'min_lift', 'rule_id']
        else:
            fieldnames = ['antecedent', 'consequent', 'support', 'confidence', 'lift', 'itemset_size', 'rule_id']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i, rule in enumerate(rules):
            row_data = {
                'antecedent': ';'.join(map(str, rule['if'])),
                'consequent': ';'.join(map(str, rule['then'])),
                'support': rule['support'],
                'confidence': rule['confidence'],
                'lift': rule['lift'],
                'itemset_size': rule.get('itemset_size', len(rule['if']) + len(rule['then'])),
                'rule_id': f"apriori_rule_{i+1:04d}"
            }
            
            if include_params and params:
                row_data['min_support'] = params[0]
                row_data['min_confidence'] = params[1]
                row_data['min_lift'] = params[2]
            
            writer.writerow(row_data)
    
    print(f"Successfully saved {len(rules)} Apriori rules to {filename}")

def save_all_rules_to_csv(all_rules_data, filename="all_apriori_rules.csv"):
    """Save ALL rules from ALL parameter combinations to a single CSV file"""
    if not all_rules_data:
        print("No rules data to save.")
        return
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['antecedent', 'consequent', 'support', 'confidence', 'lift', 
                     'itemset_size', 'min_support', 'min_confidence', 'min_lift', 
                     'parameter_set', 'rule_id']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        rule_counter = 1
        for param_set, rules in all_rules_data:
            s, c, l = param_set
            for rule in rules:
                writer.writerow({
                    'antecedent': ';'.join(map(str, rule['if'])),
                    'consequent': ';'.join(map(str, rule['then'])),
                    'support': rule['support'],
                    'confidence': rule['confidence'],
                    'lift': rule['lift'],
                    'itemset_size': rule.get('itemset_size', len(rule['if']) + len(rule['then'])),
                    'min_support': s,
                    'min_confidence': c,
                    'min_lift': l,
                    'parameter_set': f"s{s}_c{c}_l{l}",
                    'rule_id': f"apriori_all_{rule_counter:06d}"
                })
                rule_counter += 1
    
    print(f"Successfully saved {rule_counter-1} total rules from all parameter combinations to {filename}")

def save_parameter_summary(all_rules_data, filename="apriori_parameter_summary.csv"):
    """Save summary of rules generated for each parameter combination"""
    if not all_rules_data:
        return
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['min_support', 'min_confidence', 'min_lift', 'num_rules', 
                     'avg_confidence', 'avg_lift', 'avg_support', 'parameter_set']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for params, rules in all_rules_data:
            s, c, l = params
            if rules:
                avg_conf = sum(rule['confidence'] for rule in rules) / len(rules)
                avg_lift = sum(rule['lift'] for rule in rules) / len(rules)
                avg_supp = sum(rule['support'] for rule in rules) / len(rules)
                
                writer.writerow({
                    'min_support': s,
                    'min_confidence': c,
                    'min_lift': l,
                    'num_rules': len(rules),
                    'avg_confidence': round(avg_conf, 4),
                    'avg_lift': round(avg_lift, 4),
                    'avg_support': round(avg_supp, 4),
                    'parameter_set': f"s{s}_c{c}_l{l}"
                })
    
    print(f"Saved parameter summary to {filename}")

def load_rules_from_csv(filename="apriori_rules.csv"):
    """Load Apriori rules from CSV file"""
    rules = []
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rule_data = {
                    'if': row['antecedent'].split(';') if row['antecedent'] else [],
                    'then': row['consequent'].split(';') if row['consequent'] else [],
                    'support': float(row['support']),
                    'confidence': float(row['confidence']),
                    'lift': float(row['lift'])
                }
                if 'itemset_size' in row:
                    rule_data['itemset_size'] = int(row['itemset_size'])
                rules.append(rule_data)
        print(f"Successfully loaded {len(rules)} rules from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error loading rules from {filename}: {e}")
    
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
                            lift_values=[0.5,1.0,1.5],
                            save_rules=True,
                            output_csv="apriori_rules.csv",
                            save_all_rules=True):
    """
    Grid search over support, confidence, lift to find optimal thresholds based on test set coverage
    """
    best_score = -1
    best_params = None
    best_rules = []
    all_rules_data = []  # Store all rules from all parameter combinations
    
    print(f"Testing {len(support_values)} x {len(confidence_values)} x {len(lift_values)} = {len(support_values)*len(confidence_values)*len(lift_values)} parameter combinations")
    
    for s, c, l in itertools.product(support_values, confidence_values, lift_values):
        print(f"Testing support={s}, confidence={c}, lift={l}")
        rules = run_apriori(train_baskets, min_support=s, min_confidence=c, min_lift=l)
        
        # Store all rules with their parameters
        if rules:
            all_rules_data.append(((s, c, l), rules))
        
        coverage, avg_conf, avg_lift = evaluate_rules(rules, test_baskets)
        score = coverage * avg_conf * avg_lift
        print(f"  Rules: {len(rules)}, Coverage: {coverage:.3f}, Score: {score:.3f}")
        
        if score > best_score and len(rules) > 0:
            best_score = score
            best_params = (s, c, l)
            best_rules = rules

    # Save ALL rules from ALL parameter combinations
    if save_all_rules and all_rules_data:
        all_rules_filename = "all_apriori_rules.csv"
        save_all_rules_to_csv(all_rules_data, all_rules_filename)
        
        # Also save summary of parameter combinations
        save_parameter_summary(all_rules_data, "apriori_parameter_summary.csv")

    if best_rules:
        coverage, avg_conf, avg_lift = evaluate_rules(best_rules, test_baskets)
        
        # Save the optimal rules to CSV
        if save_rules:
            save_rules_to_csv(best_rules, output_csv, include_params=True, params=best_params)

        return {
            "optimal_support": best_params[0],
            "optimal_confidence": best_params[1],
            "optimal_lift": best_params[2],
            "coverage": coverage,
            "avg_confidence": avg_conf,
            "avg_lift": avg_lift,
            "rules": best_rules,
            "rules_file": output_csv,
            "all_rules_file": "all_apriori_rules.csv" if save_all_rules and all_rules_data else None,
            "parameter_summary_file": "apriori_parameter_summary.csv" if save_all_rules and all_rules_data else None,
            "total_parameter_combinations": len(list(itertools.product(support_values, confidence_values, lift_values))),
            "successful_combinations": len(all_rules_data)
        }
    else:
        return {"error": "No valid rules found with given parameters"}

# Example usage function
def example_usage():
    """Example demonstrating Apriori with CSV saving of ALL rules"""
    # Sample transaction data
    transactions = [
        ['milk', 'bread', 'butter'],
        ['milk', 'bread'],
        ['milk', 'eggs'],
        ['bread', 'butter', 'eggs'],
        ['milk', 'bread', 'eggs', 'butter'],
        ['bread', 'eggs'],
        ['milk', 'eggs'],
        ['milk', 'bread', 'eggs'],
        ['milk', 'bread', 'butter'],
        ['bread', 'butter']
    ]
    
    # Split into train/test
    train_data = transactions[:7]
    test_data = transactions[7:]
    
    print("Running Apriori with threshold optimization...")
    results = find_optimal_thresholds(
        train_baskets=train_data,
        test_baskets=test_data,
        support_values=[0.1, 0.2],
        confidence_values=[0.3, 0.5],
        lift_values=[1.0, 1.5],
        output_csv="optimal_apriori_rules.csv",
        save_all_rules=True
    )
    
    if "error" not in results:
        print(f"\n=== OPTIMAL PARAMETERS ===")
        print(f"Support: {results['optimal_support']}")
        print(f"Confidence: {results['optimal_confidence']}")
        print(f"Lift: {results['optimal_lift']}")
        print(f"Number of optimal rules: {len(results['rules'])}")
        print(f"Optimal rules saved to: {results['rules_file']}")
        
        if results.get('all_rules_file'):
            print(f"ALL rules saved to: {results['all_rules_file']}")
        if results.get('parameter_summary_file'):
            print(f"Parameter summary saved to: {results['parameter_summary_file']}")
        
        print(f"Parameter combinations tested: {results['total_parameter_combinations']}")
        print(f"Successful combinations: {results['successful_combinations']}")
        
        # Test loading the optimal rules
        loaded_rules = load_rules_from_csv("optimal_apriori_rules.csv")
        print(f"Successfully loaded {len(loaded_rules)} optimal rules from CSV")
        
        # Test loading ALL rules
        try:
            all_rules = load_rules_from_csv("all_apriori_rules.csv")
            print(f"Successfully loaded {len(all_rules)} total rules from ALL parameter combinations")
        except:
            print("Could not load all rules file")
    else:
        print(results["error"])

# Direct execution function
def run_apriori_and_save(baskets, min_support=0.02, min_confidence=0.3, min_lift=1.0, output_file="apriori_rules.csv"):
    """
    Run Apriori and save rules directly without grid search
    """
    print(f"Running Apriori with min_support={min_support}, min_confidence={min_confidence}, min_lift={min_lift}")
    rules = run_apriori(baskets, min_support, min_confidence, min_lift)
    
    if rules:
        save_rules_to_csv(rules, output_file)
        print(f"✅ Generated and saved {len(rules)} Apriori rules to {output_file}")
        return rules
    else:
        print("❌ No rules generated with current parameters")
        return []

if __name__ == "__main__":
    example_usage()