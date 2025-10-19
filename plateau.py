from piece import *

class Plateau:
    """Classe représentant le plateau de jeu."""
    longueur = 8
    largeur = 8
    plateau = []

    def __init__(self):
        """Initialise le plateau avec une largeur et une hauteur données."""
        #pieces blanches
        for ligne in range(3):
            for colonne in range(self.largeur):
                if (ligne + colonne) % 2 == 1:
                    piece_blanche = Blanc()
                    piece_blanche.set_position((ligne, colonne))
                    self.plateau.append(piece_blanche)

        #pièces noires
        for ligne in range(5, 8):
            for colonne in range(self.largeur):
                if (ligne + colonne) % 2 == 1:
                    piece_noire = Noir()
                    piece_noire.set_position((ligne, colonne))
                    self.plateau.append(piece_noire)
        
        #cases vides
        for ligne in range(3, 5):
            for colonne in range(self.largeur):
                if (ligne + colonne) % 2 == 1:
                    self.plateau.append(None)


    def display(self):
        """Affiche le plateau de jeu."""
        for ligne in range(self.longueur):
            row_display = ""
            for colonne in range(self.largeur):
                piece = next((p for p in self.plateau if p and p.get_position() == (ligne, colonne)), None)
                if piece is None:
                    row_display += "[ ] "
                elif piece.color == "blanc":
                    row_display += "[B] "
                else:
                    row_display += "[N] "
            print(row_display)
