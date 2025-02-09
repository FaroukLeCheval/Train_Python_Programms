# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:17:58 2025

@author: ouatt
"""
import time

# tous les carré de 0 à 9
start = time.time()
liste_1 = []
for i in range(100):
    liste_1.append(i**2)

end = time.time()
print(liste_1)
print(end-start)

# inserer une boucle for dans une list grace à LIST COMPREHENSION
start = time.time()
liste_2 = [i**2 for i in range(100)]

end = time.time()
print(liste_2)
print(end-start)
## plus rapide
## plus pro
## plus efficace pour les temps de calculs

# avec une nested list

liste_3 = [[i for i in range(3)] for j in range(3)]
print(liste_3)


# Dictionnaire compréhension
prenoms = ['Pierre', 'Jean', 'Julie', 'Sophie']
dico = {k:v for k,v in enumerate(prenoms)}
print(dico)
print(dico.values())
print(dico.keys())

ages = [24,58,92,3]

dico_2 = {prenoms:ages for prenoms, ages in zip(prenoms,ages)}
dico_2

# inclure des condition a la boucle for

dico_2 = {prenoms:ages for prenoms, ages in zip(prenoms,ages) if ages > 20}
dico_2

# Dictionnaire compréhension
## {keys:values for keys,values in 'list;zip;tuples,etc...' if 'condition'}

# tuple comprehension
tuple_1 = (i**2 for i in range(10))
tuple_1 # on crée un generateur

tuple_2 = tuple((i**2 for i in range(10)))
tuple_2 #méthode tuple pour aficher ce que l'on veut sino on obtient un generateur

# Crée un dictionnaire k:v avec k = 0-20 et v = k**2
dict_exo = {str(k):k**2 for k in range(20)}
print(dict_exo)





