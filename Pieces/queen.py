# Class representing a queen piece
class Queen:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    # Representation for printing the piece
    def __repr__(self):
        return self.piece_type if self.color == 'w' else self.piece_type.lower()

    # Placeholder for validating queen movement
    def is_valid_move(self, board, start, end):
        
        start_x, start_y = start
        end_x, end_y = end  

        # If the end position have a piece then that piece color should not be same as currunt piece color
        if board[end_x][end_y] and board[end_x][end_y].color == self.color:
            return False
        
        is_any_piece_present = False

        if self.is_horizontal_move(start, end):
            
            # Now check that no other pieces are there in path fron start to end
            if start_y < end_y:  

                # Right Move 
                for k in range(start_y+1, end_y, 1):
                    is_any_piece_present = is_any_piece_present or (board[start_x][k] is not None)

            elif start_y > end_y:  

                # Left Move
                for k in range(start_y-1, end_y, -1):
                    is_any_piece_present = is_any_piece_present or (board[start_x][k] is not None)

            else:  
                # No Move
                return False
            
        elif self.is_vertical_move(start, end):
            
            # Now check that no other pieces are there in path fron start to end
            if start_x < end_x:  

                # Down Move 
                for k in range(start_x+1, end_x, 1):
                    is_any_piece_present = is_any_piece_present or (board[k][start_y] is not None)

            elif start_x > end_x:  

                # Up Move
                for k in range(start_x-1, end_x, -1):
                    is_any_piece_present = is_any_piece_present or (board[k][start_y] is not None)

            else:  
                # No Move
                return False

        elif self.is_diagonal_move(start, end):
            
            is_any_piece_present = False
            dx = 1 if start_x < end_x else -1
            dy = 1 if start_y < end_y else -1
            x, y = start_x + dx, start_y + dy

            while x != end_x and y != end_y:
                is_any_piece_present = is_any_piece_present or (board[x][y] is not None)
                x += dx
                y += dy
            
        else:
            return False
        
        return not is_any_piece_present

    # Placeholder for horizontal movement check
    def is_horizontal_move(self, start, end):
        
        start_x, start_y = start
        end_x, end_y = end 

        # Check for horizontal movement using the condition: (i, k) where 0 <= k <= 7, k != j i.e. start and end position should have same x coordinate
        is_hr_move = (start_x == end_x)

        return is_hr_move

    # Placeholder for vertical movement check
    def is_vertical_move(self, start, end):
        
        start_x, start_y = start
        end_x, end_y = end 

        # Check for horizontal movement using the condition: (k, j) where 0 <= k <= 7, k != i i.e. start and end position should have same y coordinate

        is_vr_move = (start_y == end_y)
        
        return is_vr_move

    # Placeholder for diagonal movement check
    def is_diagonal_move(self, start, end):

        start_x, start_y = start
        end_x, end_y = end

        # Check for valid diagonal move usign the condition: (x, y) where |x-i| = |y-j|
        is_dia_move = (abs(start_x - end_x) == abs(start_y - end_y))
        return is_dia_move
  