from bateau import Bateau

# Nom: chevauchement

# Utilisateur : un joueur

# Story : Positionner des bateaux sans chevauchement

# Actions :

# 1. créer un bateau b1

b1 = Bateau(2, 3, longueur=3)

# 2. créer un bateau b2

b2 = Bateau(1, 3, longueur=3, vertical=True)

# 3. vérifiez si les 2 bateaux se chevauchent (la fonction chevauchement(bateau1,bateau2))


def chevauchement(bateau1, bateau2):
    positions_bateau1 = bateau1.positions()
    positions_bateau2 = bateau2.positions()
    SeChevauchent = False
    # positions_chevauchement=[]
    for p in positions_bateau1:
        if p in positions_bateau2:
            SeChevauchent = SeChevauchent or True
            # positions_chevauchement.append(p)

    return SeChevauchent


# 4. bateaux qui se chevauchent (b1 et b2)

booléen1 = chevauchement(b1, b2)

if booléen1:

    print("les 2 bateaux b1 et b2 se chevauchent ")

else:
    print("les 2 bateaux b1 et b2 ne se chevauchent pas")


# 5. bateaux qui ne se chevauchent pas (b1 et b3)

b3 = Bateau(1, 2, longueur=3, vertical=True)

booléen2 = chevauchement(b1, b3)
if booléen2:

    print("les 2 bateaux b1 et b3 se chevauchent ")

else:
    print("les 2 bateaux b1 et b3 ne se chevauchent pas")
