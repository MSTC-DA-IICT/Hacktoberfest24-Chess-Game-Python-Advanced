# Class representing a bishop piece
class Bishop:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    # Representation for printing the piece
    def __repr__(self):
        return self.piece_type if self.color == 'w' else self.piece_type.lower()

    # Placeholder for validating bishop movement
    def is_valid_move(self, start, end, player_color):
        pass

    # Placeholder for validating diagonal movement
    def is_diagonal_move(self, board, start, end):
        pass