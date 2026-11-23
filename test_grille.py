from grille import Grille
from bateau import Bateau, Porte_avion, Croiseur, Torpilleur, Sous_marin


def test_init():
    assert isinstance(Grille(3, 4), Grille)


def test_int_2():
    G = Grille(3, 4)
    assert G.matrice == ["∿" for _ in range(G.nombre_colonnes * 3)]


def test_tirer():
    G = Grille(3, 4)
    G.tirer(1, 2)
    assert G.matrice[1 * G.nombre_colonnes + 2] == "x"


def test_str():
    G = Grille(2, 3)
    assert Grille.__str__(G) == ". . . " + "\n" + ". . . " + "\n"
    G.tirer(0, 1)
    assert Grille.__str__(G) == ". x . " + "\n" + ". . . " + "\n"


def test_ajoute():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=False))
    assert g.matrice == ["∿", "∿", "∿", "⛵", "⛵", "∿"]
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=True))
    assert g.matrice == ["∿", "∿", "∿", "∿", "∿", "∿"]
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=4, vertical=True))
    assert g.matrice == ["∿", "∿", "∿", "∿", "∿", "∿"]


def test_ajoute_porte_avion():
    g = Grille(2, 5)
    p = Porte_avion(1, 0, vertical=False)
    g.ajoute(p)
    assert p.longueur == 4
    assert g.matrice == ["∿", "∿", "∿", "∿", "∿", "🚢", "🚢", "🚢", "🚢", "∿"]


def test_ajoute_croiseur():
    g = Grille(2, 5)
    c = Croiseur(1, 0, vertical=False)
    g.ajoute(c)
    assert c.longueur == 3
    assert g.matrice == ["∿", "∿", "∿", "∿", "∿", "⛴", "⛴", "⛴", "∿", "∿"]


def test_ajoute_torpilleur():
    g = Grille(2, 3)
    t = Torpilleur(1, 0, vertical=False)
    g.ajoute(t)
    assert t.longueur == 2
    assert g.matrice == ["∿", "∿", "∿", "🚣", "🚣", "∿"]


def test_ajoute_sous_marin():
    g = Grille(2, 3)
    s = Sous_marin(1, 0, vertical=False)
    g.ajoute(s)
    assert s.longueur == 2
    assert g.matrice == ["∿", "∿", "∿", "🐟", "🐟", "∿"]
