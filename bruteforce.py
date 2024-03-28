from pprint import pprint
from itertools import combinations



def maximiser_profit(actions, budget):
    nombre_actions = len(actions)
    meilleur_profit = 0
    meilleure_combinaison = None

    for i in range(1, 2**nombre_actions):
        combinaison_actuelle = []
        
        cout_total = 0
        profit_total = 0
        
        for j in range(nombre_actions):
            if (i >> j) & 1:
                action = actions[j]
                cout = int(action[1])
                pourcentage_profit = float(action[2][:-1]) / 100  
                
                if cout_total + cout <= budget:
                    combinaison_actuelle.append(action)
                    print(combinaison_actuelle)
                    cout_total += cout
                    profit_total += pourcentage_profit * cout
        
        if profit_total > meilleur_profit:
            meilleur_profit = profit_total
            meilleure_combinaison = combinaison_actuelle

    return meilleure_combinaison, meilleur_profit




def startBruteforce(data):
    
    pprint(data)
    budget_max = 500
    actions_choisies, profit_total = maximiser_profit(data, budget_max)

    print("Actions choisies pour maximiser le profit :")
    for action in actions_choisies:
        print(action)

    print("Profit total après deux ans d'investissement : {}%".format(profit_total))
    
