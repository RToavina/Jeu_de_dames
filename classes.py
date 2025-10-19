
class Piece:
    """Classe représentant une pièce de jeu."""
    def __init__(self):
        """Initialise une pièce avec une position par défaut et une couleur."""
        self.position = None
        self.color = None

    def set_position(self, position):
        """Définit la position de la pièce."""
        self.position = position

    def get_position(self):
        """Retourne la position actuelle de la pièce."""
        return self.position

    def move(self, new_position):
        """Déplace la pièce à une nouvelle position."""
        self.position = new_position
    
    def set_color(self, color):
        """Définit la couleur de la pièce."""
        self.color = color

class Blanc(Piece):
    """Classe représentant une pièce blanche."""
    def __init__(self):
        super().__init__()
        self.set_color("blanc")

class Noir(Piece):
    """Classe représentant une pièce noire."""
    def __init__(self):
        super().__init__()
        self.set_color("noir")

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

