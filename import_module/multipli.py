# -*-coding:UTF-8 *-

def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de 1 * jusqu'a max * nb """

    i = 0

    while i < max:
        print(i + 1, " * ", nb, " = ", (i + 1) * nb)
        i += 1