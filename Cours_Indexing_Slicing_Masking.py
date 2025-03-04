# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 11:28:26 2025

@author: c12085
"""
import numpy as np

# On travail souvent dans des tableaux à 2 dimensions
## Axe 0 -> lignes; Axe 1 -> colonnes
## Quand on se déplace sur un axe à la fois, notre position change sur cet Axe uniquement
### on indique donc des index pour se repérer

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
A

A[1,1]