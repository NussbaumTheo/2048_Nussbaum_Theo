# Janvier 2023
# création et test unitaire d'une fonction (tasse_4)
# chaque élève doit créer et tester sa fonction (durée environ 4 périodes)


#fait descendre un plot vers le "bas", et fusionne s'il tombe sur un de même valeur
# reçoit 4 nombres, tasse vers le a,  et en renvoie 5
def tasse_4(a,b,c,d):
    nmove=0 #sert à savoir si on a réussi à bouger
    # ici le code va manipuler a,b,c et d
    if (c==0):
        c=d
        d=0
        nmove += 1

    if (b==0):
        b=c
        c=d
        d=0
        nmove += 1

    if (a==0):
        a=b
        b=c
        c=d
        d=0
        nmove += 1

    if (a==b):
        a = a+b
        b = c
        c = d
        d = 0
        nmove += 1

    if (b==c):
        b = b+c
        c = d
        d = 0
        nmove += 1

    if (a==b):
        c = c+d
        d = 0
        nmove += 1

    # ici on retourne les cinq valeurs en un tableau
    temp=[a,b,c,d,nmove] #tableau temporaire de fin
    return temp

#Test de la fonction tasse
#On demande 4 valeurs numériques, et on veut comme résultats les 4 valeurs tassées vers a
#et en cinquième résultat on veut le nombre de tassements
a = int(input('entrez une valeur numérique : '))
b = int(input('entrez une valeur numérique : '))
c = int(input('entrez une valeur numérique : '))
d = int(input('entrez une valeur numérique : '))

# on envoie les 4 nombres saisis pour tester la fonction
res=tasse_4(a,b,c,d)

# on affiche le résultat (tableau de 5 valeurs)
print(res)
