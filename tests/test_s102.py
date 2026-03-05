#!/usr/bin/env python3

from s102 import * # importer le code de cette SAE pour pouvoir tester ces fonctions

f=open("houses_ref.json")
houses_ref = load(f)
f.close()

f=open("houses_multiple_refs.json")
multiples_houses_ref = load(f)
f.close()

f=open("affectation_premiere_annee.json")
affectation_premiere_annee = load(f)
f.close()

# Variable : 

exemple_dico_reponse = {
    "Lisa Fischer"   : [7, 4, 8, 5, 7, 10, 3, 7, 8, 5],
    "Donna Weiss"    : [4, 6, 2, 10, 2, 10, 4, 8, 7, 9],
    "Justin Sanchez" : [6, 5, 9, 2, 2, 7, 6, 7, 8, 4]
}

neighbors=[                      
            {                   
                "house": "Serpentard",          
                "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]  
            },                
            {                   
                "house": "Poufsouffle",          
                "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]  
            },                  
            {                   
                "house": "Serdaigle",         
                "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]   
            },                  
            {                   
                "house": "Gryffondor",          
                "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]  
            }   ]



answer=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
ref={ "house":"Serdaigle","answer": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}


# Question 1 : 

def test_create_answers_from_text_file():
    
    """
    La fonction teste de la fonction : create_answers_from_text_file
    """
    # Appel de la fonction à tester
    fonction=create_answers_from_text_file("questionnaire_premiere_annee_10q.txt")
    
    assert len(fonction) == 124 ,"Erreur 1 create_answers_from_text_file, Le nombre d'élèves est incorrect . "
    assert fonction["Lisa Fischer"] == [7,4,8,5,7,10,3,7,8,5] ,"Erreur 2 create_answers_from_text_file, Les réponses de Lisa Fischer sont incorrectes . "
    assert fonction["Linda Edwards"] == [7,6,3,9,10,6,10,10,6,1] ,"Erreur 3 create_answers_from_text_file, les réponses de Linda Edwards sont incorrectes . "

    print("La fonction : create_answers_from_text_file fonctionne correctement. ")

# Question 2 :
 
def test_Euclidean_distance():

    """
    La fonction teste de la fonction : Euclidean_distance
    """

    lisa = [7, 4, 8, 5, 7, 10, 3, 7, 8, 5]
    donna = [4, 6, 2, 10, 2, 10, 4, 8, 7, 9]

    assert round(Euclidean_distance(lisa, donna), 5) == 10.86278, "Erreur 1 Euclidean_distance, le résultat n'est pas le bon "
    assert Euclidean_distance([5,5], [5,5]) == 0.0, "Erreur 2 Euclidean_distance, le résultat n'est pas le bon "
    assert round(Euclidean_distance([-2, -8], [2, 4]), 3) == 12.649, "Erreur 3 Euclidean_distance, le résultat n'est pas le bon "
    
    print("La fonction : Euclidean_distance fonctionne correctement")
 
# Question 3 :    

def test_Euclidean_house() :

    """
    La fonction teste de la fonction : Euclidean_house
    """
    
    f=open("houses_ref.json","r",encoding="utf-8")
    ensemble_de_reference=load(f)
    f.close() 
    
    assert Euclidean_house([], ensemble_de_reference.copy()) == False, "Erreur 1, Euclidean_house, le résultat attendu est False" 
    assert Euclidean_house( [2, 10, 4, 5, 2, 10, 4, 3, 7, 3], ensemble_de_reference.copy() ) == "Serdaigle" ,"Erreur 2 Euclidean_house, le résultat attendu est Serdaigle "
    assert Euclidean_house( [9, 4, 5, 3, 9, 2, 5, 1, 8, 2]  , ensemble_de_reference.copy()) == "Gryffondor" ,"Erreur 3 Euclidean_house, le résultat attendu est Gryffondor "
    
    print("La fonction : Euclidean_house fonctionne correctement. ")

# Question 4 : 

def test_Euclidean_repartition():

    """
    La fontion teste de la fonction : Euclidean_repartition
    """

    assert Euclidean_repartition(exemple_dico_reponse.copy(), houses_ref.copy()) == {"Lisa Fischer" : "Serpentard", "Donna Weiss" : "Serpentard", "Justin Sanchez" : "Serdaigle"}, "Erreur 1 Euclidean_repartition"
    
    print("La fonction : euclidean_repartition fonctionne correctement")

def test_pourcentage_erreur():
    """
    La fontion teste de la fonction : pourcentage_erreur
    """   
    d1 = {"A": "Gryffondor", "B": "Serdaigle"}
    d2 = {"A": "Serpentard", "B": "Poufsouffle"}
    d3 = {"A": "Gryffondor", "B": "Serdaigle"}
    d4 = {"A": "Gryffondor", "B": "Poufsouffle"}
    
    assert pourcentage_erreur(d1, d2) == 100.0
    assert pourcentage_erreur(d1, d1) == 0.0
    assert pourcentage_erreur(d3, d4) == 50.0
    
    print("La fonction : pourcentage_erreur fonctionne correctement")

# Question 5 : 
    
def test_question_5():

    """
    La fontion teste de la fonction : Question 5
    """

    f=open("affectation_premiere_annee.json","r",encoding="utf-8")
    affectation_premiere_annee=load(f)
    f.close()

    f=open("houses_multiple_refs.json","r",encoding="utf-8")
    ensemble_de_reference_multiple=load(f)
    f.close()

    assert question_5(affectation_premiere_annee,ensemble_de_reference_multiple)==16.129032258064516, "Erreur question_5,ce n'est pas le bon pourcentage attendu"
    print("La fonction : question_5 fonctionne correctement. ")
 
# Question 6 : 

def test_insertion_position_NN():

    """
    La fonction teste de la fonction : insertion_position_NN
    """

    assert insertion_position_NN([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], {"house": "Serdaigle","answer": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]}, houses_ref.copy()) == 0, "Erreur 1 insertion_position_NN, le resultat attendu n'est pas le bon"
    assert insertion_position_NN([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], {"house": "Serdaigle","answer": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, houses_ref.copy()) == 4, "Erreur 2 insertion_position_NN, le resultat attendu n'est pas le bon"
    assert insertion_position_NN([10, 10, 10], {"house": "Serdaigle", "answer": [7, 7, 7]}, [{"house": "Gryffondor", "answer": [9, 9, 9]}, {"house": "Serpentard", "answer": [5, 5, 5]}]) == 1, "Erreur 3 insertion_position_NN, le resultat attendu n'est pas le bon"
    
    print("La fonction : insertion_position_NN fonctionne correctement")

# Question 7 :  

def test_insertion_NN() :

    """
     La fonction teste de la fonction : insertion_NN
    """

    neighbors=[                      
            {                   
                "house": "Serpentard",          
                "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]  
            },                
            {                   
                "house": "Poufsouffle",          
                "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]  
            },                  
            {                   
                "house": "Serdaigle",         
                "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]   
            },                  
            {                   
                "house": "Gryffondor",          
                "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]  
            }   ]

    answer=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    ref={ "house":"Serdaigle","answer": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}

    assert insertion_NN( answer.copy() , ref.copy() , neighbors.copy() , 5) == [   
        {'house': 'Serpentard', 'answer': [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]}, 
        {'house': 'Poufsouffle', 'answer': [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]}, 
        {'house': 'Serdaigle', 'answer': [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]}, 
        {'house': 'Gryffondor', 'answer': [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]}, 
        {'house': 'Serdaigle', 'answer': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}    ] ,"Erreur 1 Insertion_NN, le résultat n'est pas celui attendu"
    

    assert insertion_NN(answer.copy() , ref.copy(), neighbors.copy() , 3  ) == [
        {'house': 'Serpentard', 'answer': [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]}, 
        {'house': 'Poufsouffle', 'answer': [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]}, 
        {'house': 'Serdaigle', 'answer': [2, 10, 4, 5, 2, 10, 4, 3, 7, 3]}, 
        {'house': 'Gryffondor', 'answer': [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]}],"Erreur 2 Insertion_NN, le résultat n'est pas celui attendu"
    
    
    print("La fonction : insertion_NN fonctionne correctement ")

# Question 8 : 

def test_NN():

    """
    La fontion teste de la fonction : NN
    """

    answer = [2, 1, 5, 6, 8, 2, 4, 3, 5, 9]
    
    assert NN([2, 1, 5, 6, 8, 2, 4, 3, 5, 9], houses_ref.copy(), 2) == [{'house': 'Poufsouffle', 'answer': [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]}, {'house': 'Gryffondor', 'answer': [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]}], "Erreur 1 NN, le résultat n'est pas celui attendu"
    assert len(NN(answer.copy(), houses_ref.copy(), 1)) == 1, "Erreur 2 NN, le résultat n'est pas celui attendu"
    assert len(NN(answer.copy(), houses_ref.copy(), 4)) == 4, "Erreur 3 NN, le résultat n'est pas celui attendu"
    
    print("La fonction : NN fonctionne correctement")
    
# Question 9 : 

def test_NN_house() :

    """
    La fonction teste de la fonction : NN_house
    """
    neighbors=[                    
    {                 
        "house": "Serpentard",          
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]   
    },                 
    {                 
        "house": "Gryffondor",          
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]   
    },                  
    {                 
        "house": "Serdaigle",          
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3] 
    },                  
    {                 
        "house": "Gryffondor",          
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]   
    } ]
    
    neighbors2=[                    
    {                 
        "house": "Serpentard",          
        "answer": [4, 6, 5, 9, 1, 7, 3, 10, 9, 8]   
    },                 
    {                 
        "house": "Gryffondor",          
        "answer": [3, 4, 9, 3, 6, 5, 10, 1, 9, 9]   
    },                  
    {                 
        "house": "Serdaigle",          
        "answer": [2, 10, 4, 5, 2, 10, 4, 3, 7, 3] 
    },                  
    {                 
        "house": "Gryffondor",          
        "answer": [9, 3, 6, 2, 10, 2, 5, 1, 8, 2]   
    },                 
    {                 
        "house": "Serpentard",          
        "answer": [8, 6, 6, 10, 8, 5, 5, 6, 7, 8]   
    } ]

    assert NN_house( neighbors ) == "Gryffondor" ,"Erreur 1 NN_house, le résultat n'est pas le bon "
    assert NN_house( neighbors2 ) == "Serpentard" ,"Erreur 2 N_house, le résultat n'est pas le bon "

    print("La fonction : NN_house fonctionne correctement ")

# Question 10 : 

def test_NN_repartition():

    """
    La fonction teste de la fonction : NN_repartition
    """

    assert NN_repartition(exemple_dico_reponse.copy(), houses_ref.copy(), 0) == {'Lisa Fischer': False, 'Donna Weiss': False, 'Justin Sanchez': False}, "Erreur 1 NN_repartition le résultat n'est pas le bon"
    assert NN_repartition(exemple_dico_reponse.copy(), houses_ref.copy(), 6) == {'Lisa Fischer': 'Serpentard', 'Donna Weiss': 'Serpentard', 'Justin Sanchez': 'Serpentard'}, "Erreur 2 NN_repartition le résultat n'est pas le bon"
    assert NN_repartition(exemple_dico_reponse.copy(), houses_ref.copy(), 2) == {'Lisa Fischer': 'Serpentard', 'Donna Weiss': 'Serpentard', 'Justin Sanchez': 'Serpentard'}, "Erreur 3 NN_repartition le résultat n'est pas le bon"
    
    print("La fonction : NN_repartition fonctionne correctement")


# Exécution des tests et analyses 

test_create_answers_from_text_file()
test_Euclidean_distance()
test_Euclidean_house()
test_Euclidean_repartition()
test_pourcentage_erreur()
test_question_5()
test_insertion_position_NN()
test_insertion_NN()
test_NN()
test_NN_house()
test_NN_repartition()

# Analyses k-NN
dico_reponse = create_answers_from_text_file("questionnaire_premiere_annee_10q.txt")

test1 = NN_repartition(dico_reponse, multiples_houses_ref, 1)  # = 16.12% d'erreur
test2 = NN_repartition(dico_reponse, multiples_houses_ref, 2)  # =16.12% d'erreur
test3 = NN_repartition(dico_reponse, multiples_houses_ref, 3) # = 2.41% d'erreur
test4 = NN_repartition(dico_reponse, multiples_houses_ref, 4) #= 8.87% d'erreur
test5 = NN_repartition(dico_reponse, multiples_houses_ref, 5) # = 10.48% d'erreurs

