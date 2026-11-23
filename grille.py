from bateau import Bateau, Porte_avion, Croiseur, Torpilleur, Sous_marin


class Grille:

    def __init__(self, nombre_lignes, nombre_colonnes):
        self.matrice = ["∿" for _ in range(nombre_colonnes * nombre_lignes)]
        self.nombre_colonnes = nombre_colonnes

    def tirer(self, ligne, colonne, touche="x"):

        if self.matrice[ligne * self.nombre_colonnes + colonne] == "∿":
            self.matrice[ligne * self.nombre_colonnes + colonne] = touche

        else:

            self.matrice[ligne * self.nombre_colonnes + colonne] = "💣"

    def __str__(self):
        s = ""
        k = 0
        while k < len(self.matrice):
            numéro_colonne = 0
            while numéro_colonne < self.nombre_colonnes:
                if self.matrice[k] == "∿":
                    s += ". "
                else:
                    s += self.matrice[k] + " "
                k += 1
                numéro_colonne += 1
            s += "\n"
        return s

    def ajoute(self, bateau):
        positions_bateau = bateau.positions()
        est_dans_grille = True
        nombre_lignes = len(self.matrice) // self.nombre_colonnes

        if bateau.vertical == True:
            for p in positions_bateau:
                l = p[0] * self.nombre_colonnes + p[1]
                if (l < len(self.matrice)) and (
                    p[1] <= l <= (nombre_lignes - 1) * (self.nombre_colonnes) + p[1]
                ):
                    est_dans_grille = est_dans_grille and True
                else:
                    est_dans_grille = est_dans_grille and False

        else:
            for p in positions_bateau:
                l = p[0] * self.nombre_colonnes + p[1]
                if (l < len(self.matrice)) and (
                    p[0] * self.nombre_colonnes
                    <= l
                    <= (p[0] + 1) * (self.nombre_colonnes) - 1
                ):
                    est_dans_grille = est_dans_grille and True
                else:
                    est_dans_grille = est_dans_grille and False

        if est_dans_grille:

            for p in positions_bateau:
                k = p[0] * self.nombre_colonnes + p[1]
                if not (
                    isinstance(bateau, Porte_avion)
                    or isinstance(bateau, Croiseur)
                    or isinstance(bateau, Torpilleur)
                    or isinstance(bateau, Sous_marin)
                ):
                    self.matrice[k] = "⛵"

                else:

                    if isinstance(bateau, Porte_avion):
                        self.matrice[k] = bateau.marque

                    if isinstance(bateau, Croiseur):
                        self.matrice[k] = bateau.marque

                    if isinstance(bateau, Torpilleur):
                        self.matrice[k] = bateau.marque

                    if isinstance(bateau, Sous_marin):
                        self.matrice[k] = bateau.marque
