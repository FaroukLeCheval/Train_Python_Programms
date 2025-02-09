# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 23:01:51 2025

@author: ouatt
"""

# Cours sur les listes 
## Liste[début:fin:pas]
## chaque element possede un index
liste_1 = [1,4,2,7,35,84]
villes = ['Paris','Berlin','Londres','Bruxelles']
liste_2 = [liste_1,villes]
liste_vide = []

print(villes[0])
print(villes[-1])
## Extraire les 3 premiers elements de villes
print(villes[:3])
print(villes[2:])
print(villes[::2])
print(villes[::-1]) 

# Tuples
tuple_1 = (1,6,7,82) # ne peu pas etre edit


# string
prenom = 'nicolas'
print(prenom[:3])

# Différentes actions a faire sur une liste

villes.append('New-York')
villes

villes_2 = ['amsterdam','mulouse']
villes.extend(villes_2)
villes

villes.insert(2, 'Madrid') # .insert(index, value)
villes

len(villes)

villes.sort(reverse=True)

# Liste avec if/else
if 'Paris' in villes:
    print('yes')
else:
    print('no')
    
for i in villes:
    print(i)


for index, valeur in enumerate(villes):
    print(index,valeur)

# Commande zip
liste_3 = [1,4,81,56,20,30,15]
for a, b in zip(villes,liste_3):
    print(a,b)
    

# Exercice: reprendre fibbonacci mais il faut qu'elle nous retourne une liste des elemets de la suite de fibonacci jusqu'a n
def liste_fibbo(n):
    a=0
    b=1
    li_fib = []
    while a < n:
        li_fib.append(a)
        a,b = b,a+b
    return li_fib
    print(li_fib)

liste_fibbo(1000)



