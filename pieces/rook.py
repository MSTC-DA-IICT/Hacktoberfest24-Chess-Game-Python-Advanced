# Class representing a rook piece
class Rook:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    # Representation for printing the piece
    def __repr__(self):
        return self.piece_type if self.color == 'w' else self.piece_type.lower()

    # Placeholder for validating rook movement
    def is_valid_move(self, board, start, end):
        pass

    # Placeholder for checking horizontal movement
    def is_horizontal_move(self, board, start, end):
        pass

    # Placeholder for checking vertical movement
    def is_vertical_move(self, board, start, end):
        pass
