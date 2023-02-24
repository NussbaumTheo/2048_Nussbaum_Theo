'''
Auteur : Nussbaum Théo
Date : 07..01.2023
Version : 0.1
Description : recrée le jeux du 2048 en python
'''
#importation du module tkinter de python
from tkinter import *
import tkinter.font

# tableau 2 dimensions avec des mots (3x3)
number = [[2, 2, 8, 16], [32, 64, 128, 256], [512, 1024, 2048, 4096], [8192, 0, 0, 0]]

# tableau 2 dimensions avec des vides qui deviendront des labels.
labels = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]

width=90 #espacement horizontal en pixels des étiquettes (remarque la taille des labels est en caractères)
height=80 #espacement vertical en pixels des étiquettes

#création d'un bibliothèque ft: Ryan Cardamone
color = {0: "#FFFFFF",
         2: "#FFFFFF",
         4: "#EEEEEE",
         8: "#FFE8F7",
         16: "#FFDFCA",
         32: "#FFE694",
         64: "#F9F871",
         128: "#FFC75F",
         256: "#FF9671",
         512: "#FF6F91",
         1024: "#D65DB1",
         2048: "#917CFA",
         4096: "#839EFA",
         8192: "#845EC2"}



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
            colors = color[var]
            labels[line][col].config(bg= colors, text=var)
            if number[line][col] == 0:
                labels[line][col].config(text="",bg=colors)

#appeller la fonction display pour afficher le tableau
display()

#ouvrir la fenêtre
fen.mainloop()
