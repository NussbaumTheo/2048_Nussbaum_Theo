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
win = False
loose = False

# tableau 2 dimensions avec des mots (3x3)
number = [[2, 4, 8, 16], [32, 64, 128, 256], [512, 1024, 2048, 4096], [8192, 2, 4, 8]]

# tableau 2 dimensions avec des vides qui deviendront des labels.
labels = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
# liste de numéro de la case
liste = [2, 2, 2, 2 , 2, 2, 2, 2, 2, 4]

width=137 #espacement horizontal en pixels des étiquettes (remarque la taille des labels est en caractères)
height=150 #espacement vertical en pixels des étiquettes

#création d'un bibliothèque ft: Ryan Cardamone
color = {0: "#FFFFFF", 2: "#B0E0E6", 4: "#ADD8E6", 8: "#87CEEB", 16: "#87CEFA", 32: "#00BFFF", 64: "#1E90FF", 128: "#1E90FF", 256: "#6495ED", 512: "#6495ED", 1024: "#6495ED", 2048: "#6495ED", 4096: "#00008B", 8192: "#000080"}

# Construction de la fenêtre :
fen = Tk()
fen.geometry("652x770")
fen.minsize(652,770)
fen.maxsize(652,770)
fen.title(' 2048 by Théo')
fen.config(bg="#C4C9C7")

#ajoute d'un titre et du score
title = Label(fen, text="2048",font=("Arial", 50), bg="#C4C9C7")
title.place(x=60,y=40)
scorelbl = Label(fen, text=f"Score: {score}",font=("Arial", 10), bg="#C4C9C7")
scorelbl.place(x=480,y=80)
hightscorelbl = Label(fen, text=f"Hightscore: {hightscore}",font=("Arial", 10), bg="#C4C9C7")
hightscorelbl.place(x=480,y=100)
imgwin = PhotoImage(file="win590.png")
imgloose = PhotoImage(file="loose590.png")

revoire = Button(fen, text="Revoir")
continuer = Button(fen, text="Continuer")

#Lire le highscore dans highscore.txt
fichier = open("hightscore.txt", "r")
hightscore = fichier.readline()

#Création des labels (d'abord on les définit avec =, puis on les place dans la fenêtre avec .place(x,y)
for line in range(len(number)):
    for col in range(len(number[line])):
        # construction de chaque label sans le placer
        labels[line][col] = tkinter.Label (width=7, height=4, borderwidth=1, relief="solid", font=("Arial", 23))

        # placement du label dans la fenêtre par ses coordonnées en pixels
        labels[line][col].place(x=60 + width * col, y=140 + height * line)

# création des labels pour les images
labelsImg = Label(fen, image=imgwin, width=590, height=590)
labelsImg.place_forget()
labelsImgloose = Label(fen, image=imgloose, width=590, height=590)
labelsImgloose.place_forget()

#création d'un fonction d'affichage ft: John Jacard
def display():
    for line in range(len(number)):
        for col in range(len(number[line])):
            var = number[line][col]
            if var <= 8192:
                colors = color[var]
            else:
                colors = "Red"
            labels[line][col].config(bg= colors, text=var, fg="Black")
            if number[line][col] == 0:
                labels[line][col].config(text="",bg=colors)
            if number[line][col] >= 4096:
                labels[line][col].config(bg=colors, text=var, fg="white")
    scorelbl.config(text=f"Score: {score}")
    hightscorelbl.config(text=f"Hightscore: {hightscore}")

#appeller la fonction display pour afficher le tableau
display()

# bind des touches
def bind(event):
    fen.bind("<Key>",lambda event:move(event))

# unbind des touches
def unbind(event):
    fen.unbind("<Key>")

def spawn_tuiles():
    var = number[line][col]
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
            labels[x][y].config(text=number[x][y],bg="black", fg="white")
            
def new_game():
    global number, score, win
    score = 0
    win = False
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
    bind("<Key>")
    labelsImg.place_forget()
    continuer.place_forget()
    revoire.place_forget()
    labelsImgloose.place_forget()
    # rappelle de la fonction display pour afficher le tableau
    display()
    
#création d'un boutton new_game
bouton_new_game = Button(fen, text="New Game", command=new_game)
bouton_new_game.place(x=297, y=100)

# fonction pour afficher l'image de win + boutton continuer
def win_game():
    global continuer
    labelsImg.place(x=30, y = 140)
    continuer.config(command=continu)
    continuer.place(x=290,y=740)
    unbind("<Key>")

def loose_game():
    labelsImgloose.place(x=30, y = 140)
    revoire.config(command=revoire_game)
    revoire.place(x=290,y=740)
    unbind("<Key>")
    
# fonction pour dèsafficher l'image de win + le boutton continuer
def continu():
    bind("<Key>")
    labelsImg.place_forget()
    continuer.place_forget()

def revoire_game():
    unbind("<Key>")
    labelsImgloose.place_forget()
    revoire.place_forget()

# ici on a la fonction tasse_4 de base
def tasse_4(a, b, c, d):
    global score
    #fait deplacer une case vers la "gauche", et fusionne s'il tombe sur un de même valeur
    #ici on enleve les 0
    if c == 0:
        c = d
        d = 0

    if b == 0:
        b = c
        c = d
        d = 0

    if a == 0:
        a = b
        b = c
        c = d
        d = 0
# ici il va tasser 4 nombres dans la fonction tasse_4
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
bind("<Key>")
def move(event):
    global score, hightscore, win, loose
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
    # faire spawn deux 2 dans des case alléatoire
    if save != number:
        spawn_tuiles()
    # deffinir si on a gagné ou pas (ft Jimmy LAM)
    if win == False:
        for line in range(len(number)):
            for col in range(len(number[line])):
                if number[line][col] == 2048:
                    win_game()
                    win = True
    # copier de du tabeleaux number
    loosetable = copy.deepcopy(number)

    #comnptage des 0
    cont_zero = 0
    for col in range(len(loosetable)):
       for line in range(len(loosetable)):
            if loosetable[line][col] == 0:
                cont_zero += 1
    #comptage des paires
    cont_paire = 0
    for line in range(len(loosetable)):
        for col in range(len(loosetable)-1):
            if loosetable[line][col] == loosetable[line][col + 1] and loosetable[line][col]!= 0:
                cont_paire += 1

    for col in range(len(loosetable)):
       for line in range(len(loosetable)-1):
            if loosetable[line][col] == loosetable[line + 1][col] and loosetable[line][col]!= 0:
                cont_paire += 1

           
    print(cont_zero)
    print(cont_paire)

    # pour perdre, il faut plus de place et plus de paires
    if cont_paire == 0 and cont_zero == 0:
        loose_game()
        loose = True

    #si le score en cours dépasse le highscore, on l'écrit
    if score > int(hightscore):
        fichier = open("hightscore.txt", "w")
        fichier.write(str(score))
        fichier.close()
        hightscore = str(score)
    
#ouvrir la fenêtre
fen.mainloop()