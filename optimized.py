import time
import pandas as pd



def knapsack_optimized(capacity, actions):
    # Filtrer les actions avec un coût > 0
    filtered_actions = {key: action for key, action in actions.items() if float(action['cost']) > 0}
    
    # Triez les actions par rapport à leur rapport profit / coût
    sorted_actions = sorted(filtered_actions.items(), key=lambda x: float(x[1]['profit']) / float(x[1]['cost']), reverse=True)

    total_pay = 0
    total_load = 0
    selected_actions = {}

    for key, action in sorted_actions:
        cost = float(action['cost'])
        profit = float(action['profit'])
        if total_load + cost <= capacity:
            selected_actions[key] = action
            total_pay += profit
            total_load += cost

    return selected_actions

def startOptimized(data, budget):
    selected_actions = knapsack_optimized(budget, data)
    df = pd.DataFrame.from_dict(selected_actions, orient='index', columns=['cost', 'profit'])
    
    total_cost = df['cost'].astype(float).sum() # montant total acheté
    percentage_budget_used = (total_cost / budget) * 100 # pourcentage du budget utilisé

    total_profit = (df['cost'].astype(float) * df['profit'].astype(float) / 100).sum()


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
    df, total_profit, total_cost, percentage_budget_used = startOptimized(data, budget)
    endTime = time.time()

    executionTime = (endTime - startTime)

    print(f"Budget = {budget}")
    print("Actions achetées :")
    print(df)
    print(f"Profit total des actions : {total_profit:.2f} €")
    print(f"Montant total des actions achetées par rapport au budget : {total_cost:.2f} €")
    print(f"Pourcentage du budget utilisé : {percentage_budget_used:.2f} %")
    print(f"Temps d'execution = {executionTime:.5f} sec")

