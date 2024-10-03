# Class representing a pawn piece
class Pawn:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    # Representation for printing the piece (uppercase for white, lowercase for black)
    def __repr__(self):
        return self.piece_type if self.color == 'w' else self.piece_type.lower()

    # Placeholder for validating pawn movement
    def is_valid_move(self, board, start, end):
        pass

    # Placeholder for validating diagonal moves (used for capturing)
    def is_diagonal_move_valid(self, board, start, end):
        pass