from bruteforce import startBruteforce
from optimized import startOptimized
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
        options = ["Bruteforce", "Optimized"]

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
        startBruteforce(DATA, BUDGET)
        endTime = time.time()
    elif algo_selected == 1:

        startTime = time.time()
        startOptimized(DATA, BUDGET)
        endTime = time.time()

    executionTime = (endTime - startTime)

    
    print(f"Temps d'execution = {executionTime:.5f}sec")

if __name__ == "__main__":
    main()