from bruteforce import startBruteforce
from simple_term_menu import TerminalMenu
 
import time, os
import csv


FILE_PATH = "Data/"
DATA = []


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
                    DATA.append(ligne)
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


def main():
    files = selectData()

    for file in files:
        readFile(FILE_PATH + file)
        #print(FILE_PATH + file)
    
    startTime = time.time()
    startBruteforce(DATA)
    endTime = time.time()

    executionTime = (endTime - startTime)
    print(f"Temps d'execution = {executionTime:.5f}sec")

if __name__ == "__main__":
    main()