from bruteforce import startBruteforce
from optimized import startOptimized
from optimized_v2 import startOptimizedDynamic
from simple_term_menu import TerminalMenu

from pprint import pprint

import time, os
import csv

BUDGET = 500
FILE_PATH = "Data/"
DATA = {}


def lister_fichiers(chemin_dossier):
    # Vérification si le chemin est un dossier
    if not os.path.isdir(chemin_dossier):
        print("Le chemin spécifié n'est pas un dossier valide.")
        return []
    
    # Listage des fichiers dans le dossier
    fichiers = os.listdir(chemin_dossier)
    
    return fichiers


def selectData():
    terminal_menu = TerminalMenu(
        lister_fichiers(FILE_PATH),
        multi_select=True,
        show_multi_select_hint=True,
    )
    menu_entry_indices = terminal_menu.show()
    
    return terminal_menu.chosen_menu_entries


def readFile(nom_fichier):
    try:
        with open(nom_fichier, 'r', newline='', encoding="utf-8") as fichier_csv:
            lecteur_csv = csv.reader(fichier_csv)
            for ligne in lecteur_csv:
                if ligne == ['\ufeffname', 'price', 'profit'] or ligne == ['name', 'price', 'profit'] or ligne == []:
                    continue
                else:
                    DATA[ligne[0]] = {'cost':ligne[1], 'profit':ligne[2]}
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def select_algo():
        print("==================")
        options = ["Bruteforce", "Optimized", "Optimized_V2"]

        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
        return menu_entry_index

def main():
    files = selectData()

    for file in files:
        readFile(FILE_PATH + file)
        #print(FILE_PATH + file)
    algo_selected = select_algo()

    if algo_selected == 0:
        print("recherche en cours...")
        startTime = time.time()
        df, total_profit, total_cost, percentage_budget_used = startBruteforce(DATA, BUDGET)
        endTime = time.time()
    elif algo_selected == 1:

        startTime = time.time()
        df, total_profit, total_cost, percentage_budget_used = startOptimized(DATA, BUDGET)
        endTime = time.time()
    elif algo_selected == 2:

        startTime = time.time()
        df, total_profit, total_cost, percentage_budget_used = startOptimizedDynamic(DATA, BUDGET)
        endTime = time.time()

    executionTime = (endTime - startTime)

    print(f"Budget = {BUDGET}")
    print("Actions achetées :")
    print(df)
    print(f"Profit total des actions : {total_profit:.2f} €")
    print(f"Montant total des actions achetées par rapport au budget : {total_cost:.2f} €")
    print(f"Pourcentage du budget utilisé : {percentage_budget_used:.2f} %")
    print(f"Temps d'execution = {executionTime:.5f} sec")

if __name__ == "__main__":
    main()