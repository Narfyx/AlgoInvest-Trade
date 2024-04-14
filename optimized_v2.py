import time
import pandas as pd

def knapSack(W, weights, values, n):
    K = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    selected_items = []
    k = W
    for i in range(n, 0, -1):
        if K[i][k] != K[i-1][k]:
            selected_items.append(i-1)
            k -= weights[i-1]

    return selected_items


def startOptimizedDynamic(data, budget):
    scale = 100
    filtered_actions = {
        key: {
            'cost': int(float(action['cost']) * scale),
            'profit': float(action['profit'])
        }
        for key, action in data.items() if float(action['cost']) > 0
    }

    names, weights, values = zip(*((key, action['cost'], action['profit']) for key, action in filtered_actions.items()))

    W = budget * scale
    n = len(values)
    
    selected_indices = knapSack(W, weights, values, n)
    
    # Ajustement de la création du DataFrame pour inclure la mise à l'échelle correcte des coûts
    selected_actions = {
        names[i]: {
            'cost': filtered_actions[names[i]]['cost'] / scale,  # Coûts ajustés
            'profit': filtered_actions[names[i]]['profit']
        }
        for i in selected_indices
    }
    df = pd.DataFrame.from_dict(selected_actions, orient='index')

    total_cost = df['cost'].sum()
    percentage_budget_used = (total_cost / budget) * 100
    total_profit = (df['cost'] * df['profit']).sum() / 100

    return df, total_profit, total_cost, percentage_budget_used







if __name__ == '__main__':
    budget = 500
    data = {
        'Action-1': {'cost': '20', 'profit': '5.0'},
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
        'Action-9': {'cost': '48', 'profit': '13.0'}
    }
    
    print("Recherche en cours...")
    startTime = time.time()
    df, total_profit, total_cost, percentage_budget_used = startOptimizedDynamic(data, budget)
    endTime = time.time()

    executionTime = (endTime - startTime)

    print(f"Budget = {budget}")
    print("Actions achetées :")
    print(df)
    print(f"Profit total des actions : {total_profit:.2f} €")
    print(f"Montant total des actions achetées par rapport au budget : {total_cost:.2f} €")
    print(f"Pourcentage du budget utilisé : {percentage_budget_used:.2f} %")
    print(f"Temps d'execution = {executionTime:.5f} sec")

