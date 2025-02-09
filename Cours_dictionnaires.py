# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:30:26 2025

@author: ouatt
"""
import numpy as np

dico_1 = { #association clef valeur (on ne peu pas avoir deux fois la même clef)
    "chien":"dog", # {Clef 1: valeur}
    "chat":"cat", # {Clef 2: valeur}
    "souris":"mouse", # {Clef 3: valeur}
    "oiseau":"bird" # {Clef 4: valeur}
    } 

inventaire = {
              "bannanes": 5000,
              "pommes": 2600,
              "poires": 412809
              }

dico_3 = {
    "dict_1":dico_1,
    "dict_2":inventaire}

parametres = {
    "W1":np.random.randn(10,100),
    "b1":np.random.randn(10,1),
    "W2":np.random.randn(10,10,),
    "b2":np.random.randn(10,100)
    }

# affihcer les valeurs d'un dictionnaire
inventaire.values()
# affihcer les clefs d'un dictionnaire
inventaire.keys()
# vérification de la taille
len(inventaire)
# ajouter une ascociation
inventaire["abricot"] = 4098
inventaire
# il n'y a pas de position dans un inventaire
# .get() permet de cherhcer uin valeur ascocié à une clef


print(inventaire.get('pêches',1)) # get(valeurs,valeurs_par_defaut)
print(inventaire.get('bannanes',1))

# fonction pop permet de retirer une ascociation
inventaire.pop('abricot')


for i in inventaire.values() :
    print (i)

for k, v in inventaire.items():
    print(k,v)

# crée un fonction trier permettant d'ajouter un chiffre dans une des deux liste en fonction du signe

classeur = {
    "positif" : [],
    "négatif" : []
    }
    
def trier (classeur, nombre):
    if nombre >= 0 :
        classeur['positif'].append(nombre)
    else:
        classeur['négatif'].append(nombre)
    return classeur

trier(classeur, 7)
trier(classeur, -7)
trier(classeur, 2)
trier(classeur, 3)
trier(classeur, 10)
trier(classeur, -1000)
trier(classeur, 15)
trier(classeur, 9)
trier(classeur, -0.5)




