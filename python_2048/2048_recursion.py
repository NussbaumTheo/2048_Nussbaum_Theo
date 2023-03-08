'''
Autheur     : JCVD pour montrer
Version     : 0.2
Date        : 24.02.23
Description : 2048
'''
import random
from tkinter import *

# Constantes
# les couleurs sont ordonées avec les chiffres
#             0             2           4            8          ...
COLORS = {0: "#FFFFFF", 2: "#E699FF", 4: "#D966FF", 8: "#CC33FF", 16: "#BF00FF", 32: "#A100E2", 64: "#8200C5",
          128: "#6300A9", 256: "#43008D", 512: "#230073",
          1024: "#000059", 2048: "#000540", 4096: "#000329", 8192: "#000113"}

GAMES = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

LABELS = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
LABEL_WIDTH = 100
LABEL_HEIGHT = 100
n=0 # compteur de nb appel
d=0 # profondeur de récursion

# Variables
window = Tk()
window.geometry("487x602")
window.title("2048")

# généré les labels
for line in range(len(LABELS)):
    for col in range(len(LABELS[line])):
        LABELS[line][col] = Label(text=GAMES[line][col], width=8, height=4, borderwidth=1, relief="solid",
                                  font=("Arial", 14), bg="#FFFFFF", fg="#FFFFFF")
        # placement du label dans la fenêtre par ses coordonnées en pixels
        LABELS[line][col].place(x=45 + LABEL_WIDTH * col, y=150 + LABEL_WIDTH * line)

# bouton new game
Button(text="+ 2 tuiles", command=lambda: spawn_tile(2)).place(x=370, y=70)


def display():
   # affichage du jeu
    for line in range(len(GAMES)):
        for col in range(len(GAMES[line])):
            # met la couleur corespendant au text ce trouvant dans le label acutel
            LABELS[line][col].config(bg=COLORS[GAMES[line][col]], text=GAMES[line][col])

def fnprint(n,d,i, t):
    print (" >"*d + " n:" + str(n) + " i" + str(i) + t)

def spawn_tile(number_of_tile):
   # génération de 2 nouvelles tuiles
   # si on tombe sur une tuile déjà prise, on relance la fonction
   # les n,d, fnprint ne servent qu'à expliquer la récursivité
    global n, d, GAMES
    for i in range(number_of_tile):
        line = random.randint(0, 3)
        col = random.randint(0, 3)

        # si le label n'as pas été encore changé alors en le met a 2
        if GAMES[line][col] == 0:
            GAMES[line][col] = 2
            display()
            n+=1 #cas où on tombe sur un normal, n prend 1
            fnprint(n,d,i, " OK")

        else:
            # si il a été changé alors en relance la fonction
            fnprint(n+1,d,i, "?")
            d+=1 #cas où on est tombé sur un plein, on relance en n prend 1000
            spawn_tile(1)
            d-=1
            fnprint(n,d,i, "<")
            display()

window.mainloop()
