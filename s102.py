from json import *
from s101 import *  # fichier contenant les fonctions crée lors de la première SAE 101

# Fonction principale : 

# Question 1 :

def create_answers_from_text_file ( nom_fichier ) :

    """
    Cette fonction crée un dictionnaire organisé à partir d'un fichier.

    nom fichier (entrée) : le nom du fichier contenant les noms des élèves et leurs réponses.

    valeur retournée : un dictionnaire dont les clés sont les noms des élèves et les valeurs sont des tableaux de 10 entiers ( leurs réponses ).
    """

    # Stocker sous forme de tableau toutes les données du fichier 'nom_fichier' (de par la fonction lecture_reponses de la SAÉ S101)
    tab = lecture_reponses( nom_fichier ) 

    # Création du dictionnaire qui sera retourné à la fin de cette fonction 
    dico = {}
    i = 0

    if len(tab) == 0 : # Vérifie si le tableau de données est vide. (reviens a tester si le fichier est vide)
       return False
    
    while i < len ( tab ) :
        reponses = [] # Tableau qui stocke toutes les réponses d'un élève 
        nom = tab[ i ] # Variable qui stocke le nom de l'élève
        j = 1

        while j <= 10: 
            reponses.append( tab[ i + j ] )  # Stocke les 10 réponses une par une 
            j = j + 1
        dico[ nom ] = reponses 

        # Incrémentation pour passer au prochain nom (de 11 indices car : 1 nom + 10 réponses)
        i = i + 11   

    return dico

# Question 2 :

def Euclidean_distance(tab1, tab2):

    """
    Cette fonction calcule la distance Euclidienne entre deux tableau de nombres.
    
    tab1 (list) : le premier tableau d'entiers à comparer.
    tab2 (list) : le second tableau d'entiers à comparer.

    Valeur retournée : float , la distance calculée entre les deux tableaux .
    
    """

    resultat = 0

    # Somme des carrés des différences pour chaque note
    for i in range(len(tab1)):
        resultat += (tab1[i] - tab2[i]) ** 2
    
    # La distance est la racine carrée de cette somme
    return resultat ** 0.5

# Question 3 :

def Euclidean_house(reponse, ensemble_de_references):

    """
    Cette fonction détermine le nom de la maison d'affectation d'un élève par (plus proche voisin).

    reponse (list) : un tableau d'entiers contenant les réponses d'un élève.
    ensemble_de_references (list) : un tableau de dictionnaires contenant les références fondateur 
    ( réponses et la maisons).

    str : le nom de la maison introduit par la méthode (plus proche voisin).
    """

    if len ( reponse ) == 0 :
        #Attention : Le tableau est vide  
        return False
    
    mini = Euclidean_distance(reponse, ensemble_de_references[0]["answer"]) # initialisation du minimun (première référence) 
    maison = ensemble_de_references[0]["house"] # initialisation de la  maison du minimum  

    for i in range(1, len(ensemble_de_references)):
        
        distance_actuelle = Euclidean_distance(reponse, ensemble_de_references[i]["answer"])

        if distance_actuelle < mini: # si la distance est plus proche (ou égale) que celle défini par mini 

            mini = distance_actuelle # changement vers la meilleurs correspondance de maison
            maison = ensemble_de_references[i]["house"] # changement de sa maison associée

    return maison 

# Question 4 : 

def Euclidean_repartition(dico_reponse, ensemble_de_references):

    """
    Cette fonction affecte une maison à chaque élève selon son fondateur le plus proche.

    dico_reponse (dict) : dictionnaire contenant les noms des élèves et leurs réponses.
    ensemble_de_references (list) : tableau de dictionnaires contenant les références des fondateurs.

    Valeur retournée : dict , un dictionnaire contenant chaque nom d'élève à sa maison d'affectation.
    """

    dico = {}

    for cle in dico_reponse.keys():
        dico[cle] = Euclidean_house(dico_reponse[cle], ensemble_de_references)

    return dico

def pourcentage_erreur(dico1, dico2):

    """
    Calcule le taux de divergence entre deux dictionnaires de répartition.
    """

    compteur = 0
    iteration = 0

    for cle in dico1.keys():
        if dico1[cle] != dico2[cle]:
            compteur += 1
        iteration += 1

    return (compteur / iteration) * 100

# Question 5 : 

def question_5(affectation_premiere_annee,ensemble_de_reference_multiple):
    
    """
    Cette fonction calcule la précision de la méthode du plus proche voisin avec les 40 références .
    
    affectation_premiere_annee (dict) : dictionnaire défini par L'SAE S101 contient (nom : maison).
    ensemble_de_reference_multiple (list) : ensemble de données de référence contenant 
    les maison et leurs réponses associer, des 40 fondateur.

    Valeur retournée : float : le pourcentage d'erreur de la méthode de répartition avec 40 fondateur  .
    """
    # Chargement des réponses et nom des élèves à partir du fichier
    dico_reponse = create_answers_from_text_file("questionnaire_premiere_annee_10q.txt")
    
    # Calcul de la répartition des élèves en utilisant l'ensemble de références multiples
    repartition_multiples_houses_ref = Euclidean_repartition(dico_reponse, ensemble_de_reference_multiple)  
    
    # Calcul le pourcentage d'erreurs entre la méthode de repartition de cette SAE et celle du choixpeau (SAE 101). 
    res=pourcentage_erreur(repartition_multiples_houses_ref, affectation_premiere_annee) 

    return res


# Question 6 : 

def insertion_position_NN(answer, ref, neighbors):

    """
    Cette fonction trouve la position d'insertion dans le tableau des voisins triée par distance.

    answer (list) : les réponses d'un élève.
    ref (dict) : la référence dont on veut calculer la distance.
    neighbors (list) : le tableau des voisins déjà triés.

    Valeur retournée : (int) , la position où insérer la nouvelle référence dans le tableau neighbors.
    """

    # Calcul de la distance de la nouvelle référence par rapport à l'élève
    distance = Euclidean_distance(answer, ref["answer"])
    
    # On parcourt les voisins déjà identifiés
    for i in range(len(neighbors)):
        # Si la nouvelle distance est inférieure ou égale à celle du voisin à l'indice i,
        # alors c'est ici qu'on doit insérer la nouvelle référence.
        if distance <= Euclidean_distance(answer, neighbors[i]["answer"]):
            return i
        
    return len(neighbors)

# Question 7 : 

def insertion_NN ( answer , ref , neighbors , k ) :

    """
    Cette fonction insère une reférence dans un tableau de voisins trié et le rétrécie si besoins (par rapport a k).

    answer (list) : les réponses d'un élèves .
    ref (dict) : le dictionnaire contenant la maison et les réponses a possiblement insérer .
    k (int) :  k représente la taille maximale de neighbors (nombre max de voisins) .
    neighbors (list) : un tableau de références trié du plus proche au moins proche voisins .

    (list) : le tableau neighbors renouveler et limité aux k voisins plus proches.
    """

    # Définie la position où la référence doit être insérée dans le tableau neighbors .
    position = insertion_position_NN ( answer , ref , neighbors ) 
    
    neighbors.insert( position , ref ) # Insertion de la référence à la position calculer par la variable position .

        
    if len ( neighbors ) > k :  # Si la taille du tableau est plus grand que celle défini par k .
        neighbors.pop() # Supprime la rdernière référence du tableau neighbors .

    return neighbors

# Question 8 : 

def NN(answer, tab_reference, k):

    """
    Cette fonction identifie les k voisins les plus proches parmi toutes les références .

    answer (list) : les réponses d'un élève.
    tab_reference (list) : le tableau contenant l'ensemble des références .
    k (int) : le nombre de voisins les plus proches ,ainsi la taille max .

    Valeur retournée : (list) ,  un tableau contenant les k dictionnaires de références les plus proches.
    """

    neighbors = []

    # On teste chaque référence du dataset une par une
    for i in range(len(tab_reference)):
        # La fonction d'insertion s'occupe de garder uniquement les k meilleurs
        insertion_NN(answer, tab_reference[i], neighbors, k)

    return neighbors

# Question 9 :

def NN_house(neighbors):

    """
    Cette fonction calcule la maison du plus proche voisin dans neighbors .

    neighbors (list) : un tableau de références trié du plus proche au moins proche voisins .

    (str) : renvoie la maison du plus proche voisin .

    """

    # cas de valeur vide en paramètre . 
    if neighbors==[]:
        return False 
    
    dico = {}
    
    # Calcule du nombre d'occurrences pour chaque maison présente dans les voisins .
    for i in range(len(neighbors)): 

        maison = neighbors[i]["house"]

        if maison not in dico:

            dico[maison] = 1 # Initialiser  le compteur à 1 lors de la première rencontre de la maison .
    
        else:

            dico[maison] += 1 # incrémentation si une nouvelle occurrence de la maison (déjà connue) .

    maxi = 0 # initialisation du plus grand nombre d'occurence de maison .

    for v in dico.values():

        if v >= maxi:

            maxi = v #stocke la plus grande occurence de maison rencontrée .
    
    # Initialisation d'un tableau contant la ou les maisons (cas égalité) avec la plus grand occurence .
    maison_gagnante = [] 

    for cle in dico.keys():

        if dico[cle] == maxi:

            maison_gagnante.append(cle)

    for i in range(len(neighbors)): # Parcours du tableau neighbors pour définire le gagnant en cas d'égalité

        if neighbors[i]["house"] in maison_gagnante: 
    
            # Retourne la première maison rencontré contenue aussi dans le tableau maison_gagnant
            return neighbors[i]["house"]
        

# Question 10 : 

def NN_repartition(dico_reponse, ensemble_reference, k):

    """
    Cette fonction fait la répartition des élèves selon la méthode des k plus proches voisins.

    dico_reponse (dict) : dictionnaire contenant les noms des élèves et leurs réponses.
    ensemble_reference (list) : tableau de toutes les références de données disponibles.
    k (int) : le nombre de voisins à considérer pour le vote de chaque élève.

    Valeur retournée : (dict), un dictionnaire contenant chaque élève à sa maison calculée.
    """

    repartition = {}

    # Pour chaque élève du dictionnaire de réponses
    for cle in dico_reponse.keys():
        # 1. Trouver ses k voisins les plus proches
        neighbors = NN(dico_reponse[cle], ensemble_reference, k)

        # 2. En déduire sa maison via le vote majoritaire
        repartition[cle] = NN_house(neighbors)

    return repartition
