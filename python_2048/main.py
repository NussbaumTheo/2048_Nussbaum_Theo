'''
Auteur : Nussbaum Théo
Date : 07..01.2023
Version : 0.2
Description : recrée le jeux du 2048 en python
'''
#importation du module tkinter de python
from tkinter import *
import tkinter.font
import random 
import copy


#variable
score = 0
hightscore = 0


# tableau 2 dimensions avec des mots (3x3)
number = [[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0]]

# tableau 2 dimensions avec des vides qui deviendront des labels.
labels = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
# liste de numéro de la case
liste = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]

width=90 #espacement horizontal en pixels des étiquettes (remarque la taille des labels est en caractères)
height=80 #espacement vertical en pixels des étiquettes

#création d'un bibliothèque ft: Ryan Cardamone
color = {0: "#FFFFFF", 2: "#FFFFFF", 4: "#EEEEEE", 8: "#FFE8F7", 16: "#FFDFCA", 32: "#FFE694", 64: "#F9F871", 128: "#FFC75F", 256: "#FF9671", 512: "#FF6F91", 1024: "#D65DB1", 2048: "#917CFA", 4096: "#839EFA", 8192: "#845EC2"}

# Construction de la fenêtre :
fen = Tk()
fen.geometry("480x500")
fen.minsize(480,500)
fen.maxsize(480,500)
fen.title(' 2048 by Théo')
fen.config(bg="#F9CB9C")

#ajoute d'un titre et du score
title = Label(fen, text="2048",font=("Arial", 50), bg="#F9CB9C")
title.place(x=60,y=40)
scorelbl = Label(fen, text=f"Score: {score}",font=("Arial", 10), bg="#F9CB9C")
scorelbl.place(x=320,y=80)
hightscorelbl = Label(fen, text=f"Hightscore: {hightscore}",font=("Arial", 10), bg="#F9CB9C")
hightscorelbl.place(x=320,y=100)

#Lire le highscore dans highscore.txt
fichier = open("hightscore.txt", "r")
hightscore = fichier.readline()

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
    scorelbl.config(text=f"Score: {score}")
    hightscorelbl.config(text=f"Hightscore: {hightscore}")

#appeller la fonction display pour afficher le tableau
display()

def spawn_tuiles():

    if 0 in number[0]+number[1]+number[2]+number[3]:
        # faire spawn deux 2 dans des case alléatoire
        for i in range(1):
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            while number[x][y] != 0:
                x = random.randint(0, 3)
                y = random.randint(0, 3)
            number[x][y] = random.choice(liste)
            display()

def new_game():
    global number, score, highscore
    score = 0
    highscore = 0
    number = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if 0 in number[0]+number[1]+number[2]+number[3]:
        # faire spawn deux 2 dans des case alléatoire
        for i in range(2):
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            while number[x][y] != 0:
                x = random.randint(0, 3)
                y = random.randint(0, 3)
            number[x][y] = 2


    display()
    
#création d'un boutton new_game
bouton_new_game = Button(fen, text="New Game", command=new_game)
bouton_new_game.place(x=205, y=465)

# ici on a la fonction tasse_4 de base
def tasse_4(a, b, c, d):
    global score
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
    global score, hightscore
    save = copy.deepcopy(number)
    touche = event.keysym
    if touche=="w" or touche == "W" or touche =="Up":
        tasse_up(event)
    if touche=="a" or touche == "A" or touche =="Left":
        tasse_left(event)
    if touche=="s" or touche == "S" or touche =="Down":
        tasse_down(event)
    if touche=="d" or touche == "D" or touche =="Right":
        tasse_right(event)
    if save != number:
        spawn_tuiles()
    print(hightscore)

    #si le score en cours dépasse le highscore, on l'écrit
    if score > int(hightscore):
        fichier = open("hightscore.txt", "w")
        fichier.write(str(score))
        fichier.close()
        hightscore = str(score)
    

#ouvrir la fenêtre
fen.mainloop()