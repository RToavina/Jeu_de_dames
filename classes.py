
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

    def __init__(self, width, height):
        """Initialise le plateau avec une largeur et une hauteur données."""
        self.width = width
        self.height = height

    def is_within_bounds(self, x, y):
        """Vérifie si les coordonnées (x, y) sont dans les limites du plateau."""
        return 0 <= x <= self.width and 0 <= y <= self.height
    
    def display(self):
        """Affiche les coordonnées de chaque case du plateau."""
        for y in range(self.height + 1):
            for x in range(self.width + 1):
                print(f"({x},{y})", end=" ")
            print()