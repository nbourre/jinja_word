# Utilisation

1. Décompresser le fichier zip
2. Ouvrir Thonny

## Extracteur de champ
Le fichier `extraction_des_champs.py` permet d'extraire les champs d'un modèle Word avec des paramètres compatibles avec `Jinja2`.

1. Ouvrir le fichier `extraction_des_champs.py`
2. Modifier la ligne où il est écrit `fichier_source = r'...'` pour y inscrire le chemin vers le fichier Word à analyser.
3. Dans Thonny, appuyer sur le bouton "Play" pour exécuter le script.
4. Un fichier ayant le même nom que le modèle Word avec le suffixe `_fields` sera créé. Il contiendra les champs extraits.


## Programme de génération de documents
Le fichier `generateur_doc.py` permet de générer des documents à partir d'un modèle Word et d'un fichier de données.

La première étape sera d'avoir un fichier de données avec le contenu qui doit remplir le modèle Word. Vous pouvez jeter un coup d'oeil au fichier `template_context.csv` dans le dossier `data` pour voir le format attendu.

1. Ouvrir le fichier `generateur_doc.py`
2. Exécuter le script
3. Appuyer sur le bouton `Sélectionner le modèle` pour choisir le modèle Word à utiliser
4. Appuyer sur le bouton `Charger les champs` pour choisir le fichier de données à utiliser
5. Appuyer sur le bouton `Générer le document` pour générer le document.
6. L'outil demandera l'endroit où enregistrer le fichier.

