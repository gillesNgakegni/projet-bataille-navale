from grille import Grille
from bateau import Bateau, Porte_avion, Croiseur, Torpilleur, Sous_marin
import random

# Une grille de 8 lignes et 10 colonnes

g = Grille(8, 10)

# Une liste de 4 bateaux de chaque type
liste_bateaux = []

# fonction chevauchement


def chevauchement(bateau1, bateau2):
    positions_bateau1 = bateau1.positions()
    positions_bateau2 = bateau2.positions()
    SeChevauchent = False
    for p in positions_bateau1:
        if p in positions_bateau2:
            SeChevauchent = SeChevauchent or True

    return SeChevauchent


# Ajoute un porte-avion dans la grille

while "🚢" not in g.matrice:
    xp = random.randrange(0, 8)
    yp = random.randrange(0, 10)
    vp = random.choice([True, False])
    un_porte_avion = Porte_avion(xp, yp, vertical=vp)
    g.ajoute(un_porte_avion)

print("porte_avion : ", (xp, yp, vp))
print(un_porte_avion.positions())

liste_bateaux.append(un_porte_avion)

# Placement d'un croiseur : calcul de tous les couples (case, orientation) ne produisant pas un chevauchement

pas_de_chevauchement1 = []
for ligne in range(8):
    for colonne in range(10):
        for orientation in [True, False]:
            c = Croiseur(ligne, colonne, orientation)
            if not chevauchement(c, liste_bateaux[0]):
                if all(0 <= p[0] < 8 and 0 <= p[1] < 10 for p in c.positions()):

                    pas_de_chevauchement1.append((ligne, colonne, orientation))

# On place un croiseur dans la grille

case_orientation1 = random.choice(pas_de_chevauchement1)

xc = case_orientation1[0]
yc = case_orientation1[1]
vc = case_orientation1[2]

un_croiseur = Croiseur(xc, yc, vc)
g.ajoute(un_croiseur)
print("croiseur : ", (xc, yc, vc))
print(un_croiseur.positions())
liste_bateaux.append(un_croiseur)


# Placement d'un torpilleur : calcul de tous les couples (case, orientation) ne produisant pas un chevauchement

pas_de_chevauchement2 = []
for ligne in range(8):
    for colonne in range(10):
        for orientation in [True, False]:
            t = Torpilleur(ligne, colonne, orientation)
            if not (
                chevauchement(t, liste_bateaux[0]) or chevauchement(t, liste_bateaux[1])
            ):
                if all(0 <= p[0] < 8 and 0 <= p[1] < 10 for p in t.positions()):

                    pas_de_chevauchement2.append((ligne, colonne, orientation))


# On place un torpilleur dans la grille

case_orientation2 = random.choice(pas_de_chevauchement2)

xt = case_orientation2[0]
yt = case_orientation2[1]
vt = case_orientation2[2]


un_torpilleur = Torpilleur(xt, yt, vt)
g.ajoute(un_torpilleur)
print("torpilleur : ", (xt, yt, vt))
print(un_torpilleur.positions())
liste_bateaux.append(un_torpilleur)


# Placement d'un sous-marin : calcul de tous les couples (case, orientation) ne produisant pas un chevauchement

pas_de_chevauchement3 = []
for ligne in range(8):
    for colonne in range(10):
        for orientation in [True, False]:
            s = Sous_marin(ligne, colonne, orientation)
            if not (
                chevauchement(s, liste_bateaux[0])
                or chevauchement(s, liste_bateaux[1])
                or chevauchement(s, liste_bateaux[2])
            ):
                if all(0 <= p[0] < 8 and 0 <= p[1] < 10 for p in s.positions()):
                    pas_de_chevauchement3.append((ligne, colonne, orientation))


# On place un sous-marin dans la grille

case_orientation3 = random.choice(pas_de_chevauchement3)

xs = case_orientation3[0]
ys = case_orientation3[1]
vs = case_orientation3[2]


un_sous_marin = Sous_marin(xs, ys, vs)
g.ajoute(un_sous_marin)
print("sous_marin: ", (xs, ys, vs))
print(un_sous_marin.positions())
liste_bateaux.append(un_sous_marin)

# Affiche la grille


print(g)

# Boucle de gameplay : on affiche directement la grille g

tirs_effectués = []
bateaux_coulés = []

while len(bateaux_coulés) < len(liste_bateaux):

    print(g)

    try:
        ligne = int(input("Choisissez une ligne entre 0 et 7 : "))
        colonne = int(input("Choisissez une colonne entre 0 et 9 : "))
    except ValueError:
        print("Veuillez entrer des nombres entiers !")
        continue

    if not (0 <= ligne < 8 and 0 <= colonne < 10):
        print("Cette case est en dehors de la grille !")
        continue

    if (ligne, colonne) in tirs_effectués:
        print("Vous avez déjà tiré sur cette case !")
        continue

    tirs_effectués.append((ligne, colonne))
    touche = False

    for bateau in liste_bateaux:
        if (ligne, colonne) in bateau.positions():
            touche = True
            g.tirer(ligne, colonne, "💣")
            print("Touché ! 💣")

            if bateau.coulé(g):
                bateaux_coulés.append(bateau)

                # On révèle les cases du bateau coulé avec sa marque.
                # On modifie directement la matrice, car tirer() remettrait 💣.
                for p in bateau.positions():
                    k = p[0] * g.nombre_colonnes + p[1]
                    g.matrice[k] = bateau.marque

                if isinstance(bateau, Porte_avion):
                    print("Le porte-avion est coulé !")
                elif isinstance(bateau, Croiseur):
                    print("Le croiseur est coulé !")
                elif isinstance(bateau, Torpilleur):
                    print("Le torpilleur est coulé !")
                elif isinstance(bateau, Sous_marin):
                    print("Le sous-marin est coulé !")

            break

    if not touche:
        g.tirer(ligne, colonne, "o")
        print("À l'eau !")

print(g)
print("Bravo ! Vous avez coulé tous les bateaux !")
