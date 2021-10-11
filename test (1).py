# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import matplotlib.pyplot as plt
import sympy as sym #permet d'introduire le calcul symbolique
import numpy as np #facilite le calcul matricielle
from interpole import evalHorner

#pour limiter la zone de la figure
#plt.xlim(-np.pi,np.pi)
#plt.ylim(-1.5,1.5)
#points d'interpolation:
#les coordonnées sur l'axe des abscisses
x=np.linspace(-np.pi,np.pi,10) #5 points de distances égales de -pi à pi sur l'axe des abscisses 
#les coordonnées des 5 points sur l'axe des ordonnées : tout simplement f(x)
y=np.sin(x) 
#Représentation graphique des cinq points avec des cercles pleins
plt.plot(x,y,linestyle='',marker='o', label="points")
#les points pour dessiner les courbes du polynôme et de la fonction
t=np.linspace(-.5-np.pi,(np.pi)+.5,1000)
#calcul poly(t)
poly=evalHorner(x,y,t)   
plt.plot(t,poly,label="poly")
plt.plot(t,np.sin(t),label="sin")
plt.legend() #montrer la légende