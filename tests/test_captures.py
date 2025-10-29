import sys
import os

# ajouter le répertoire parent (racine du projet) au path pour importer les modules locaux
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from piece import Blanc, Noir
from plateau import Plateau


def test_simple_capture():
    plateau = Plateau()

    # placer une blanche en (2,1) et une noire en (3,2) ; (4,3) doit être libre
    blanc = Blanc()
    plateau.set_piece_at((2, 1), blanc)
    noir = Noir()
    plateau.set_piece_at((3, 2), noir)

    # Vérifier que la pièce blanche a une capture possible vers (4,3)
    captures = blanc.possible_captures()
    assert (4, 3) in captures


def test_no_capture_on_initial_setup():
    plateau = Plateau()

    # sur la configuration initiale standard il ne doit pas y avoir de captures immédiates
    any_capture = False
    for p in plateau.plateau:
        if p and p.position:
            if p.possible_captures():
                any_capture = True
                break

    assert not any_capture


if __name__ == "__main__":
    # Runner simple pour exécuter les tests sans pytest
    try:
        test_simple_capture()
        print("test_simple_capture: OK")
    except AssertionError:
        print("test_simple_capture: FAILED")

    try:
        test_no_capture_on_initial_setup()
        print("test_no_capture_on_initial_setup: OK")
    except AssertionError:
        print("test_no_capture_on_initial_setup: FAILED")
