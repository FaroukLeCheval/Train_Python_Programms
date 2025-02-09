# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:50:19 2025

@author: ouatt
"""

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


def fibbo(n):
    a=0
    b=1
    while a < n:
        print(a)
        a,b = b,a+b











