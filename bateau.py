class Bateau:

    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        positions_occupées = []
        if self.vertical:
            for i in range(self.longueur):
                positions_occupées.append((self.ligne + i, self.colonne))

        else:
            for j in range(self.longueur):
                positions_occupées.append((self.ligne, self.colonne + j))

        return positions_occupées

    def coulé(self, grille):
        est_coulé = True
        positions = self.positions()
        for p in positions:
            k = p[0] * grille.nombre_colonnes + p[1]
            if grille.matrice[k] == "💣":
                est_coulé = est_coulé and True
            else:
                est_coulé = est_coulé and False

        return est_coulé


class Porte_avion(Bateau):

    def __init__(self, ligne, colonne, vertical):
        super().__init__(ligne, colonne, vertical=vertical)
        self.longueur = 4
        self.marque = "🚢"


class Croiseur(Bateau):

    def __init__(self, ligne, colonne, vertical):
        super().__init__(ligne, colonne, vertical=vertical)
        self.longueur = 3
        self.marque = "⛴"


class Torpilleur(Bateau):

    def __init__(self, ligne, colonne, vertical):
        super().__init__(ligne, colonne, vertical=vertical)
        self.longueur = 2
        self.marque = "🚣"


class Sous_marin(Bateau):

    def __init__(self, ligne, colonne, vertical):
        super().__init__(ligne, colonne, vertical=vertical)
        self.longueur = 2
        self.marque = "🐟"
