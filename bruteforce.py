import time
import itertools
import pandas as pd



def calculate_total_profit_and_load(actions):
    total_profit, total_load = 0, 0
    for action in actions.values():
        total_profit += float(action['profit'])
        total_load += float(action['cost'])

    return total_profit, total_load


def knapsack(capacity, actions):
    filtered_actions = {key: action for key, action in actions.items() if float(action['cost']) > 0}
    del actions
    solutions = []

    # Générer toutes les combinaisons possibles d'actions sans spécifier la taille
    all_combinations = itertools.chain.from_iterable(
        itertools.combinations(filtered_actions.keys(), r)
        for r in range(1, len(filtered_actions) + 1)
    )

    # Parcourir toutes les combinaisons possibles
    for solution in all_combinations:
        selected_actions = {key: filtered_actions[key] for key in solution}
        total_profit, total_load = calculate_total_profit_and_load(selected_actions)
        if total_load <= capacity:
            solutions.append((total_profit, total_load, selected_actions))

    del all_combinations
    solutions.sort(reverse=True, key=lambda x: x[0])

    return solutions


def startBruteforce(data, budget):
    solutions = knapsack(budget, data)
    solution = solutions[0]

    df = pd.DataFrame.from_dict(solution[2], orient='index', columns=['cost', 'profit'])

    

    total_cost = df['cost'].astype(float).sum()  # montant total acheté

    percentage_budget_used = (total_cost / budget) * 100  # pourcentage du budget utilisé

    # Correction du calcul du profit total
    total_profit = (df['cost'].astype(float) * df['profit'].astype(float) / 100).sum()

    return df, total_profit, total_cost, percentage_budget_used

if __name__ == '__main__':
    budget = 500

    data = {'Action-1': {'cost': '20', 'profit': '5.0'},
            'Action-10': {'cost': '34', 'profit': '27.0'},
            'Action-11': {'cost': '42', 'profit': '17.0'},
            'Action-12': {'cost': '110', 'profit': '9'},
            'Action-13': {'cost': '38', 'profit': '23.0'},
            'Action-14': {'cost': '14', 'profit': '1.0'},
            'Action-15': {'cost': '18', 'profit': '3.0'},
            'Action-16': {'cost': '8', 'profit': '8.0'},
            'Action-17': {'cost': '4', 'profit': '12.0'},
            'Action-18': {'cost': '10', 'profit': '14.0'},
            'Action-19': {'cost': '24', 'profit': '21.0'},
            'Action-2': {'cost': '30', 'profit': '10.0'},
            'Action-20': {'cost': '114', 'profit': '18.0'},
            'Action-21': {'cost': '0', 'profit': '50'},
            'Action-22': {'cost': '-7', 'profit': '90'},
            'Action-3': {'cost': '50', 'profit': '15.0'},
            'Action-4': {'cost': '70', 'profit': '20.0'},
            'Action-5': {'cost': '60', 'profit': '17.0'},
            'Action-6': {'cost': '80', 'profit': '25.0'},
            'Action-7': {'cost': '22', 'profit': '7.0'},
            'Action-8': {'cost': '26', 'profit': '11.0'},
            'Action-9': {'cost': '48', 'profit': '13.0'}}

    print("recherche en cours...")
    startTime = time.time()
    df, total_profit, total_cost, percentage_budget_used = startBruteforce(data, budget)
    endTime = time.time()

    executionTime = (endTime - startTime)


    print(f"Budget = {budget}")
    print("Actions achetées :")
    print(df)
    print(f"Profit total des actions : {total_profit:.2f} €")
    print(f"Montant total des actions achetées par rapport au budget : {total_cost:.2f} €")
    print(f"Pourcentage du budget utilisé : {percentage_budget_used:.2f} %")
    print(f"Temps d'execution = {executionTime:.5f} sec")
