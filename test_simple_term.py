

from simple_term_menu import TerminalMenu


def main():
    terminal_menu = TerminalMenu(
        ["dog", "cat", "mouse", "squirrel"],
        multi_select=True,
        show_multi_select_hint=True,
    )
    menu_entry_indices = terminal_menu.show()
    print(menu_entry_indices)
    print(terminal_menu.chosen_menu_entries)


if __name__ == "__main__":
    main()



import os

def lister_fichiers(chemin_dossier):
    """
    Renvoie une liste des fichiers présents dans le dossier spécifié.
    
    Args:
        chemin_dossier (str): Le chemin absolu ou relatif du dossier.
        
    Returns:
        list: Une liste des noms de fichiers présents dans le dossier.
    """
    # Vérification si le chemin est un dossier
    if not os.path.isdir(chemin_dossier):
        print("Le chemin spécifié n'est pas un dossier valide.")
        return []
    
    # Listage des fichiers dans le dossier
    fichiers = os.listdir(chemin_dossier)
    
    return fichiers

# Exemple d'utilisation
chemin_dossier = '/chemin/vers/votre/dossier'
liste_fichiers = lister_fichiers(chemin_dossier)
print("Liste des fichiers dans le dossier {}: {}".format(chemin_dossier, liste_fichiers))
