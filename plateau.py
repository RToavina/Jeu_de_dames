from piece import *

class Plateau:
    """Classe représentant le plateau de jeu."""
    longueur = 8
    largeur = 8
    plateau = []

    def __init__(self):
        """Initialise le plateau avec une largeur et une hauteur données."""
        # utiliser une liste d'instance (évite le partage entre instances)
        self.plateau = []
        # donner aux pièces une référence au plateau courant (instance)
        try:
            from piece import Piece
            Piece.board = self
        except ImportError:
            pass
        #pieces blanches
        for ligne in range(3):
            for colonne in range(self.largeur):
                if (ligne + colonne) % 2 == 1:
                    piece_blanche = Blanc()
                    piece_blanche.position = (ligne, colonne)
                    self.plateau.append(piece_blanche)

        #pièces noires
        for ligne in range(5, 8):
            for colonne in range(self.largeur):
                if (ligne + colonne) % 2 == 1:
                    piece_noire = Noir()
                    piece_noire.position = (ligne, colonne)
                    self.plateau.append(piece_noire)
        
        #cases vides
        for ligne in range(3, 5):
            for colonne in range(self.largeur):
                if (ligne + colonne) % 2 == 1:
                    self.plateau.append(None)

        # garantir que la référence de Piece.board pointe vers le plateau courant
        try:
            from piece import Piece
            Piece.board = self
        except ImportError:
            pass


    def display(self):
        """Affiche le plateau de jeu."""
        for ligne in range(self.longueur):
            row_display = ""
            for colonne in range(self.largeur):
                piece = self.get_piece_at((ligne, colonne))
                if piece is None:
                    row_display += "[ ] "
                elif piece.color == "blanc":
                    row_display += "[B] "
                else:
                    row_display += "[N] "
            print(row_display)

    def refresh(self):
        """Rafraîchit l'affichage du plateau."""
        self.display()

    def afficher_captures_possibles(self):
        """Affiche pour chaque pièce les captures possibles (si elles existent)."""
        any_capture = False
        for p in self.plateau:
            if p is None or p.position is None:
                continue
            captures = p.possible_captures()
            if captures:
                any_capture = True
                print(f"Pièce {p.color} en {p.position} peut capturer en: {captures}")
        if not any_capture:
            print("Aucune capture possible pour le moment.")

    def get_piece_at(self, position):
        """Retourne la pièce à la position donnée ou None."""
        if position is None:
            return None
        return next((p for p in self.plateau if p and p.position == position), None)

    def set_piece_at(self, position, piece):
        """Place une pièce à la position donnée (ou retire la pièce si piece est None).
        Cette méthode met simplement à jour l'attribut position de la pièce et veille
        à ce qu'il n'y ait pas deux pièces à la même position.
        """
        # retirer occupant si présent
        existing = self.get_piece_at(position)
        if existing:
            existing.position = None

        if piece is None:
            return

        # placer la pièce (ajoute à la liste si nécessaire)
        piece.position = position
        if piece not in self.plateau:
            self.plateau.append(piece)
