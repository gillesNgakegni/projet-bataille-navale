from bateau import Bateau
from grille import Grille


def test_init():
    b = Bateau(1, 3)
    assert isinstance(b, Bateau)
    assert b.longueur == 1
    assert b.vertical == False


def test_positions():
    assert Bateau(2, 3, longueur=3).positions() == [(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, longueur=3, vertical=True).positions() == [
        (2, 3),
        (3, 3),
        (4, 3),
    ]


def test_coulé():
    g = Grille(2, 3)
    b = Bateau(1, 0, longueur=2, vertical=False)
    g.ajoute(b)
    positions = b.positions()
    for p in positions:
        g.tirer(p[0], p[1])

    assert b.coulé(g)

    g = Grille(2, 3)
    bat = Bateau(1, 0, longueur=2, vertical=False)
    g.ajoute(bat)
    g.tirer(1, 0)
    assert not bat.coulé(g)
