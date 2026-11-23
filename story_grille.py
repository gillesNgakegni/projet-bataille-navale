from grille import Grille

# Nom : "Plouf dans l'eau"

# Utilisateur : un joueur

# Story : on veut pouvoir gérer les tirs de l'adversaire

# Actions :

# 1. créer une grille à 5 lignes et 8 colonnes

g = Grille(5, 8)


# 2. afficher la grille à l'écran

print(g)


# 3. demande à l'utilisateur de rentrer deux coordonnées x et y
print(
    "choississez l'endroit de la grille où vous souhaitez tirer en renseignant les coordonnées x et y."
)
x = input("Ecrivez la valeur de x (un entier) : ")
y = input("Ecrivez la valeur de y (un entier) : ")


# 4. tirer à l'endroit indiqué sur la grille

g.tirer(int(x), int(y))


# 5. retour en 2

print(g)
