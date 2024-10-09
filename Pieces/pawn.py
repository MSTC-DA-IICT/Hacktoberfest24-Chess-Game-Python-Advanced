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
        
        start_x, start_y = start
        end_x, end_y = end

        # If the end position have a piece then that piece color should not be same as currunt piece color
        if board[end_x][end_y] and board[end_x][end_y].color == self.color:
            return False
        
        return self.is_forward_move_valid(board, start, end) or self.is_diagonal_move_valid(board, start, end)
    
    # Placeholder for validating forward moves
    def is_forward_move_valid(self, board, start, end):

        start_x, start_y = start
        end_x, end_y = end

        # White Pawn Forward Move: (i-1, j) or (i-2, j)
        # Black Pawn Forward Move: (i+1, j) or (i+2, j)

        del_white = [(-1, 0), (-2, 0)]
        del_black = [(1, 0), (2, 0)]

        is_valid_end_position = False

        # Check for valid position
        if self.color == 'w':
            # For first move we have two choices
            if start_x == 6:
                for dx, dy in del_white:
                    is_valid_end_position = is_valid_end_position or (start_x + dx == end_x and start_y + dy == end_y)
            else:
                dx, dy = del_white[0]
                is_valid_end_position = (start_x + dx == end_x and start_y + dy == end_y)
            
        else:

            # For first move we have two choices
            if start_x == 1:
                for dx, dy in del_black:
                    is_valid_end_position = is_valid_end_position or (start_x + dx == end_x and start_y + dy == end_y)
            else:
                dx, dy = del_black[0]
                is_valid_end_position = (start_x + dx == end_x and start_y + dy == end_y)
            

        # Check for empty cell
        is_empty_position = (board[end_x][end_y] is None)

        return is_valid_end_position and is_empty_position

    # Placeholder for validating diagonal moves (used for capturing)
    def is_diagonal_move_valid(self, board, start, end):
        
        start_x, start_y = start
        end_x, end_y = end

        # White Pawn Diagonal Move: (i-1, j-1) or (i-1, j+1)
        # Black Pawn Diagonal Move: (i+1, j-1) or (i+1, j+1)

        del_white = [(-1, -1), (-1, 1)]
        del_black = [(1, -1), (1, 1)]

        is_valid_end_position = False

        # Check for valid position
        if self.color == 'w':
            for dx, dy in del_white:
                is_valid_end_position = is_valid_end_position or (start_x + dx == end_x and start_y + dy == end_y)
        else:
            for dx, dy in del_black:
                is_valid_end_position = is_valid_end_position or (start_x + dx == end_x and start_y + dy == end_y)
            
        # Check for filled cell
        is_filled_position = (not board[end_x][end_y] is None)

        return is_valid_end_position and is_filled_position
