'''
Auteur : Nussbaum Théo
Date : 07..01.2023
Version : 0.2
Description : recrée le jeux du 2048 en python
'''
#importation du module tkinter de python
from tkinter import *
import tkinter.font
#importation du module tasse_4
from python_2048.tasse_4 import tasse_4

# tableau 2 dimensions avec des mots (3x3)
number = [[64, 64, 128, 256], [512, 1024, 2048, 4096], [8192, 16384, 32768, 65536], [131072, 262144, 524288, 1048576]]

# tableau 2 dimensions avec des vides qui deviendront des labels.
labels = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]

width=90 #espacement horizontal en pixels des étiquettes (remarque la taille des labels est en caractères)
height=80 #espacement vertical en pixels des étiquettes

#création d'un bibliothèque ft: Ryan Cardamone
color = {0: "#FFFFFF", 2: "#FFFFFF", 4: "#EEEEEE", 8: "#FFE8F7", 16: "#FFDFCA", 32: "#FFE694", 64: "#F9F871", 128: "#FFC75F", 256: "#FF9671", 512: "#FF6F91", 1024: "#D65DB1", 2048: "#917CFA", 4096: "#839EFA", 8192: "#845EC2"}

# Construction de la fenêtre :
fen = Tk()
fen.geometry("480x480")
fen.minsize(480,480)
fen.maxsize(480,480)
fen.title(' 2048 by Théo')
fen.config(bg="#F9CB9C")

#ajoute d'un titre et du score
title = Label(text="2048",font=("Gamer", 60), bg="#F9CB9C")
title.place(x=60,y=40)
score = Label(text="Score: ",font=("Gamer", 15), bg="#F9CB9C")
score.place(x=320,y=85)

#Création des labels (d'abord on les définit avec =, puis on les place dans la fenêtre avec .place(x,y)
for line in range(len(number)):
    for col in range(len(number[line])):
        # construction de chaque label sans le placer
        labels[line][col] = tkinter.Label (width=7, height=3, borderwidth=1, relief="solid", font=("Arial", 15))

        # placement du label dans la fenêtre par ses coordonnées en pixels
        labels[line][col].place(x=60 + width * col, y=140 + height * line)

#création d'un fonction d'affichage ft: John Jacard
def display():
    for line in range(len(number)):
        for col in range(len(number[line])):
            var = number[line][col]
            if var <= 8192:
                colors = color[var]
            else:
                colors = "Red"
            labels[line][col].config(bg= colors, text=var)
            if number[line][col] == 0:
                labels[line][col].config(text="",bg=colors)

#appeller la fonction display pour afficher le tableau
display()

# fonction pour tasser a gauche (ft : Ryan Cardamone)
def tasse_left(event):
    for line in range(len(number)):
        [number[line][0], number[line][1], number[line][2], number[line][3]] = tasse_4(number[line][0], number[line][1], number[line][2], number[line][3])
    display()

# fonction pour tasser a droit
def tasse_right(event):
    for line in range(len(number)):
        [number[line][3], number[line][2], number[line][1], number[line][0]] = tasse_4(number[line][3], number[line][2], number[line][1], number[line][0])
    display()

# fonction pour tasser en haut
def tasse_up(event):
    for col in range(len(number)):
        [number[0][col], number[1][col], number[2][col], number[3][col]] = tasse_4(number[0][col], number[1][col], number[2][col], number[3][col])
    display()

# fonction pour tasser en bas
def tasse_down(event):
    for col in range(len(number)):
        [number[3][col], number[2][col], number[1][col], number[0][col]] = tasse_4(number[3][col], number[2][col], number[1][col], number[0][col])
    display()

#attraper les touches
fen.bind("<Key>",lambda event:move(event))
def move(event):
    touche = event.keysym
    if touche=="w" or touche == "W" or touche =="Up":
        tasse_up(event)
    if touche=="a" or touche == "A" or touche =="Left":
        tasse_left(event)
    if touche=="s" or touche == "S" or touche =="Down":
        tasse_down(event)
    if touche=="d" or touche == "D" or touche =="Right":
        tasse_right(event)

#ouvrir la fenêtre
fen.mainloop()
