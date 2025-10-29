class Piece():

    board = None  # référence au Plateau (instance) contenant les pièces

    """Classe représentant une pièce de jeu."""
    def __init__(self):
        """Initialise une pièce avec une position par défaut et une couleur."""
        self.position = None
        self.color = None

    def deplacement_valide(self, new_position):
        """Vérifie si le déplacement vers une nouvelle position est valide.
            Le déplacement est valide si la nouvelle position est dans les limites du plateau.
            Le déplacement est invalide si la nouvelle position est occupée par une autre pièce.
            Le déplacement est invalide si la pièce essaie de se déplacer en dehors des diagonales autorisées.
        """
        if new_position is None:
            return False
        ligne, colonne = new_position
        if not (0 <= ligne < 8 and 0 <= colonne < 8):
            return False  # en dehors des limites du plateau

        # Vérifier si la nouvelle position est occupée
        # utiliser l'API du plateau si disponible
        if self.board:
            occupant = self.board.get_piece_at(new_position)
        else:
            occupant = None
            for piece in getattr(self, 'plateau', []) or []:
                if piece and piece.position == new_position:
                    occupant = piece
                    break
        if occupant:
            return False  # position occupée

        # Vérifier les déplacements diagonaux
        if self.position is None:
            return False
        current_ligne, current_colonne = self.position
        if abs(current_ligne - ligne) == 1 and abs(current_colonne - colonne) == 1:
            return True  # déplacement diagonal valide

        return False  # déplacement invalide

    def deplacement(self, new_position):
        """Déplace la pièce à une nouvelle position si le déplacement est valide."""
        if self.deplacement_valide(new_position):
            self.position = new_position
        else:
            raise ValueError("Déplacement invalide.")

    def possible_captures(self):
        """Retourne une liste des positions où la pièce peut capturer une autre pièce.
            On fait un parcours du plateau pour vérifier les positions adjacentes.
            On vérifie si les coordonnées sont valides grâce à la méthode deplacement_valide.
            On vérifie ensuite si la case derrière la pièce adverse est libre pour effectuer la capture.
            Et on ajoute cette position à la liste des captures possibles et des séquences de captures multiples.
        """
        captures = []
        # # # si la pièce n'a pas de position (retirée du plateau), il n'y a rien à calculer
        if self.position is None:
            return captures
        current_ligne, current_colonne = self.position
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonales

        for d_ligne, d_colonne in directions:
            adj_position = (current_ligne + d_ligne, current_colonne + d_colonne)
            behind_position = (current_ligne + 2 * d_ligne, current_colonne + 2 * d_colonne)

            # Vérifier si la position adjacente contient une pièce adverse
            if self.board:
                piece_adjacente = self.board.get_piece_at(adj_position)
            else:
                piece_adjacente = next((p for p in getattr(self, 'plateau', []) if p and p.position == adj_position), None)

            if piece_adjacente and piece_adjacente.color != self.color:
                # Vérifier si la position derrière est dans les limites et libre
                bl, bc = behind_position
                if not (0 <= bl < 8 and 0 <= bc < 8):
                    continue
                if self.board:
                    behind_occupant = self.board.get_piece_at(behind_position)
                else:
                    behind_occupant = next((p for p in getattr(self, 'plateau', []) if p and p.position == behind_position), None)
                if behind_occupant is None:
                    captures.append(behind_position)

        return captures
    
    def afficher_captures_possibles(self):
        """Affiche les positions où la pièce peut capturer une autre pièce."""
        captures = self.possible_captures()
        if not captures:
            print(f"Aucune capture possible pour la pièce {self.color} en {self.position}.")
            return
        for pos in captures:
            print(f"Capture possible en position: {pos}")

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

