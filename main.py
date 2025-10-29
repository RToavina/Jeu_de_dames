from piece import *
from plateau import *

if __name__ == "__main__":
    # Création du plateau
    plateau = Plateau()
    plateau.display()

    # Forcer une situation de capture simple :
    # - placer une pièce blanche en (2,1)
    # - placer une pièce noire adjacente en (3,2)
    # - s'assurer que (4,3) est libre pour l'atterrissage
    piece_blanche = Blanc()
    plateau.set_piece_at((2, 1), piece_blanche)

    piece_noire = Noir()
    plateau.set_piece_at((3, 2), piece_noire)

    # s'assurer que la case d'atterrissage est libre (on la libère si nécessaire)
    occupant = plateau.get_piece_at((4, 3))
    if occupant:
        # déplacer l'occupant ailleurs (si présent)
        plateau.set_piece_at((5, 4), occupant)

    print("\nAprès modification du plateau :")
    plateau.refresh()

    # Afficher toutes les captures possibles
    plateau.afficher_captures_possibles()






