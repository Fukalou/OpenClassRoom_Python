# -*-coding:UTF-8 -*

import os

annee = input("Saisissez une année : ")

try:
    annee = int(annee)
except:
    print("Erreur lors de la conversion de l'année (un nombre est attendu) !")


if annee % 400 == 0:
    bissextile = True
elif annee % 100 == 0:
    bissextile = False
elif annee % 4 == 0:
    bissextile = True
else:
    bissextile = False

if bissextile:
    print("L'année ", annee, " est bissextile !")
else:
    print("L'année ", annee, " n'est pas bissextile !")

# #Version optimisé :

# annee = input("Saisissez une année : ")
# annee = int(annee)

# if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
#     print("L'année ", annee, " est bissextile !")
# else:
#     print("L'année ", annee, " n'est pas bissextile !")

os.system("pause")