# 🧙‍♂️ SAÉ S1.02 : Le nouveau choixpeau magique de Poudlard

   Ce projet a été réalisé dans le cadre de la **SAÉ S1.02 (année 2025/2026)** au département Informatique de l'IUT Villetaneuse. Il s'agit d'une suite directe de la SAÉ S1.01 visant à optimiser la répartition des élèves dans les maisons de Poudlard grâce à l'algorithme des k plus proches voisins.
   
##  Binôme
* **Anass Fathi**
* **Anis Rocher**

##  Présentation du sujet
   Pour améliorer la précision du Choixpeau, nous passons de 4 à **10 questions de personnalité**. L'objectif est de comparer les réponses des futurs élèves à celles des fondateurs des maisons (Gryffondor, Serpentard, Serdaigle, Poufsouffle) pour les affecter à la maison dont ils sont les plus proches.

##  Concepts Techniques
Le projet repose sur plusieurs piliers de l'informatique et de l'algorithmique :

   * **Structures de données complexes** : Utilisation de dictionnaires où chaque clé est un nom d'élève et chaque valeur est un tableau de 10 entiers représentant ses réponses.
   * **Distance Euclidienne** : Mesure de la similarité entre deux réponses en calculant la distance entre deux points dans un espace à 10 dimensions.
   * **Algorithme k-NN (k-Nearest Neighbors)** : Classification d'un élève en fonction de la maison majoritaire parmi ses $k$ voisins les plus proches.
   * **Optimisation du tri** : Utilisation d'une variante du **tri par insertion** pour maintenir un classement efficace des voisins du plus proche au moins proche.



## 📂 Organisation du dépôt
   * `s102.py` : Contient l'implémentation de toutes les fonctions demandées (calcul de distance, k-NN, répartition).
   * `s101.py` : Code de base de la SAÉ précédente servant de référence.
   * `test_s102.py` : Suite de tests unitaires pour valider la robustesse de chaque fonction.
   * `conclusion_question_sae101.ipynb` : Notebook contenant l'analyse expérimentale et la comparaison des taux d'erreur.
   * `data/` : Dossier contenant les fichiers JSON (références des fondateurs) et les fichiers texte (questionnaires élèves).

## Utilisation et Tests
Pour vérifier le bon fonctionnement de l'algorithme :

1. **Lancer les tests unitaires** :
   ```bash
   python test_s102.py
