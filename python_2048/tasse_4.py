'''
Auteur : Nussbaum Théo
Date : 03.03.2023
Version : 0.2
Description : Ici on trouve la fonction tasse_4 + tasse_(direction) pour mon code du 2048
'''
from main import score

# ici on a la fonction tasse_4 de base
def tasse_4(a, b, c, d):
    #fait deplacer une case vers la "gauche", et fusionne s'il tombe sur un de même valeur
    #reçoit 4 nombres, tasse vers le a,  et en renvoie 4
    if a == 0:
        a = b
        b = c
        c = d
        d = 0
        

    if b == 0:
        b = c
        c = d
        d = 0

    if c == 0:
        c = d
        d = 0

    if a == 0:
        a = b
        b = c
        c = d
        d = 0

# ici il va tasser
    if a == b:
        a = a * 2
        b = c
        c = d
        d = 0
        score += a

    if b == c:
        b = b * 2
        c = d
        d = 0
        score += b

    if c == d:
        c = c * 2
        d = 0
        score += c

    # ici on retourne les 4 valeurs en un tableau
    temp = [a, b, c, d] #tableau temporaire de fin
    return temp
