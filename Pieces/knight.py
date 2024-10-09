# Class representing a knight piece
class Knight:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    # Representation for printing the piece
    def __repr__(self):
        return self.piece_type if self.color == 'w' else self.piece_type.lower()

    # Placeholder for validating knight movement
    def is_valid_move(self, board, start, end):

        # (i+2, j-1) or (i+2, j+1)   or  (i-1, j+2) or (i+1, j+2)
        # (i-2, j-1) or (i-2, j+1)   or  (i-1, j-2) or (i+1, j-2)

        start_x, start_y = start
        end_x, end_y = end

        # If the end position have a piece then that piece color should not be same as currunt piece color
        if board[end_x][end_y] and board[end_x][end_y].color == self.color:
            return False

        delta_knight = [(2, -1), (2, 1), (-1, 2), (1, 2), (-2, -1), (-2, 1), (-1, -2), (1, -2)]
        is_valid_end_position = False

        # Check for valid end position
        for dx, dy in delta_knight:
            is_valid_end_position = is_valid_end_position or (start_x + dx == end_x and start_y + dy == end_y)

        return is_valid_end_position
