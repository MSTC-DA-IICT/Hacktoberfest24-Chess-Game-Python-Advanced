# Class representing a bishop piece
class Bishop:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    # Representation for printing the piece
    def __repr__(self):
        return self.piece_type if self.color == 'w' else self.piece_type.lower()

    # Placeholder for validating bishop movement
    def is_valid_move(self, board, start, end):

        start_x, start_y = start
        end_x, end_y = end

        # The bishop can only move diagonally
        if not self.is_diagonal_move(start, end):
            return False
        
        # If the end position have a piece then that piece color should not be same as currunt piece color
        if board[end_x][end_y] and board[end_x][end_y].color == self.color:
            return False

        # Now check that there are no pieces in the path from start to end
        is_any_piece_present = False
        dx = 1 if start_x < end_x else -1
        dy = 1 if start_y < end_y else -1
        x, y = start_x + dx, start_y + dy

        while x != end_x and y != end_y:
            is_any_piece_present = is_any_piece_present or (board[x][y] is not None)
            x += dx
            y += dy

        return not is_any_piece_present

    # Placeholder for validating diagonal movement
    def is_diagonal_move(self, start, end):
        
        start_x, start_y = start
        end_x, end_y = end

        # Check for valid diagonal move usign the condition: (x, y) where |x-i| = |y-j|
        is_dia_move = (abs(start_x - end_x) == abs(start_y - end_y))
        return is_dia_move
