
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

