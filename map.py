import os

def mapper_dossier(dossier, indentation=''):
    # Liste tous les éléments du dossier
    elements = os.listdir(dossier)

    # Parcours de tous les éléments
    for element in elements:
        # Chemin complet de l'élément
        chemin_element = os.path.join(dossier, element)

        # Affiche le chemin de l'élément avec une indentation
        print(indentation + element)

        # Si l'élément est un dossier, mapper récursivement son contenu
        if os.path.isdir(chemin_element):
            mapper_dossier(chemin_element, indentation + '  ')  # Augmente l'indentation pour les sous-dossiers

# Appel de la fonction pour mapper un dossier spécifique
dossier_a_mapper = 'C:/Users/GREGH/OneDrive/Bureau\\project'
mapper_dossier(dossier_a_mapper)
