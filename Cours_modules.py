# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:47:51 2025

@author: ouatt
"""

# si je veut pouvoir utiliser les fonction des programmes précédents je fais :
#import Cours_if_boucle
#import Cours_list_tuples
#import Cours_dictionnaires
#import Cours_list_dict_comprehension
# ainsi j'ai ccès à toutes les fonctions et variables présente dans les autres fichiers
## Ici on crée projet 1 avec la fonction fibonnacci et classeur
import sys
sys.path.append(r"C:\users\ouatt\desktop\python training")
import projet_1 as p1
p1.fibbo(20)

# on peut aussi choisir de n'importer qu'une fonction
from projet_1 import fibbo # avec import * on importe toutes le fonction directement
fibbo(20) # on a plus beson d'écrire p1