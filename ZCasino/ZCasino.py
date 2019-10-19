# -*-coding:UTF-8 *-

import random
import os

porteMonaie = input("Saisissez le montant que vous souhaitez mettre en jeu : ")

try:
    porteMonaie = int(porteMonaie)
    assert porteMonaie > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre")
    continue
except AssertionError:
    print("Le montant du porte-monaie doit être supérieur à 0")

rejouer = True

while rejouer != True or porteMonaie == 0:
    
    mise = input("Quel montant souhaitez vous miser ? : ")

    try:
        mise = int(mise)
        assert mise > 0
    except ValueError:
        print("Vous n'avez pas saisi un nombre")
        continue
    except AssertionError:
        print("Le montant de la mise doit être supérieur à 0")

    nombre = input("Sur quel nombre souhaitez vous miser ?")

    try:
        nombre = int(nombre)
        assert nombre >= 0 and nombre <= 49
    except ValueError:
        print("Vous n'avez pas saisi un nombre")
    except AssertionError:
        print("Vous devez miser sur un nombre entre 0 et 49")

    nombreGagnant = random.randrange(50)

    

    if nombreGagnant == nombre:
        porteMonaie = porteMonaie + (mise * 3)
        print("Le nombre gagnant est : ", nombreGagnant, ". Vous remportez :", mise * 3)
    elif nombreGagnant % 2 == 0 and nombre % 2 == 0:
        porteMonaie = porteMonaie + (mise * 0.5)
        print("Le nombre gagnant est : ", nombreGagnant, ". Vous remportez :", mise * 0.5)
    else:
        porteMonaie =porteMonaie - mise
        print("Le nombre gagnant est : ", nombreGagnant, ". Vous perdez :", mise)

    rejouer = input("Voulez vous rejouer ? (o/n)")

    if rejouer == "o" or rejouer == "O":
        rejouer = True
    else:
        rejouer = False

os.system("pause")
