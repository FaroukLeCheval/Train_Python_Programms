# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:11:48 2025

@author: ouatt
"""

# Cours If/Else/Elif
x = 0
def signe(x):
        
    if (x>0) :
        print(x,'positif')
    elif x==0:
        print(x,'nul')
    else:
        print(x, 'négatif')
    
signe(5)

# Cours sur les boucles
for i in range (5, 10, 2): #☺range prend 3 arguments (Départ, Arrivée, Pas)
    print(i)
    
# While
variable = 0
while variable < 10:
    print(variable)
    variable+=1
    
# Exercice fibonacci qui retourne la suite de fibbnacci jusqu'a la valeur de n
def fibbo(n):
    a=0
    b=1
    while a < n:
        print(a)
        a,b = b,a+b
    