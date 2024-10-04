# Class representing the chessboard
class ChessBoard:
    def __init__(self):
        # Initializes the board with pieces
        self.board = self.create_board()

    # Creates the 8x8 chessboard and places all pieces
    def create_board(self): 
        board = [[None for _ in range(8)] for _ in range(8)]  # Create 8x8 grid
        # Place white pawns at row 1 and black pawns at row 6
        for i in range(8):
            board[1][i] = Pawn('b', 'P')  # Black pawn
            board[6][i] = Pawn('w', 'P')  # White pawn

        # Define the placement of other pieces (Rooks, Knights, Bishops, Queen, King)
        placement = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for i in range(8):
            if placement[i] == 'R':
                board[0][i] = Rook('b', placement[i])  # Black Rook
                board[7][i] = Rook('w', placement[i])  # White Rook
            elif placement[i] == 'N':
                board[0][i] = Knight('b', placement[i])  # Black Knight
                board[7][i] = Knight('w', placement[i])  # White Knight
            elif placement[i] == 'B':
                board[0][i] = Bishop('b', placement[i])  # Black Bishop
                board[7][i] = Bishop('w', placement[i])  # White Bishop
            elif placement[i] == 'Q':
                board[0][i] = Queen('b', placement[i])   # Black Queen
                board[7][i] = Queen('w', placement[i])   # White Queen
            elif placement[i] == 'K':
                board[0][i] = King('b', placement[i])    # Black King
                board[7][i] = King('w', placement[i])    # White King
        return board

    # Function to print the board in a human-readable format
    def print_board(self):

        i=8
        print("     ----------------- ")
        for row in self.board:
            print(f'  {i} |', ' '.join([str(piece) if piece else '.' for piece in row]), '|')  # Display pieces or '.' for empty squares
            i-=1
        print("     ----------------- ")
        print("      A B C D E F G H")  # Display pieces or '.' for empty squares

    # Placeholder function for moving pieces (to be implemented)
    def move_piece(self, start, end):
        
        start_x, start_y = start
        end_x, end_y = end

        # To make rook or king touched
        if self.board[start_x][start_y].__repr__() in ('k', 'r', 'K', 'R'):
            self.board[start_x][start_y].is_untouched = False

        self.board[end_x][end_y] = self.board[start_x][start_y]
        self.board[start_x][start_y] = None

    # Placeholder function for validating moves (to be implemented)
    def is_valid_move(self, start, end, player_color):

        start_x, start_y = start
        end_x, end_y = end

        # Check for valid position
        if (start_x < 0 or start_x > 7) or (start_y < 0 or start_y > 7) or (end_x < 0 or end_x > 7) or (end_y < 0 or end_y > 7):
            return False
        
        # Check for existance of valid piece
        if not self.board[start_x][start_y]:
            return False
        
        # Check for valid piece color
        if self.board[start_x][start_y] and (self.board[start_x][start_y].color != player_color[0]):
            return False
        
        # Check for castle move before
        if self.board[start_x][start_y].__repr__() in ('k', 'K'): 
            is_castle_move = self.board[start_x][start_y].is_valid_king_castle_move(self.board, start, end)
            if is_castle_move:
                self.perform_rook_move_for_king_castle(start, end)
                return True
        
        return self.board[start_x][start_y].is_valid_move(board=self.board, start=start, end=end)

    # Function to perform rook move if the move is king castle
    def perform_rook_move_for_king_castle(self, start, end):

        start_x, start_y = start
        end_x, end_y = end

        rook_start_x, rook_start_y = 0, 0
        rook_end_x, rook_end_y = 0, 0
        # Four possible castles

        if start_x == 7 and start_y == 4 and end_x == 7 and end_y == 6:
            # White-King Kingside Castle
            rook_start_x, rook_start_y = (7, 7)
            rook_end_x, rook_end_y = (7, 5)

        elif start_x == 7 and start_y == 4 and end_x == 7 and end_y == 2:
            # White-King Queenside Castle
            rook_start_x, rook_start_y = (7, 0)
            rook_end_x, rook_end_y = (7, 3)
    
        elif start_x == 0 and start_y == 4 and end_x == 0 and end_y == 6:
            # Black-King Kingside Castle
            rook_start_x, rook_start_y = (0, 7)
            rook_end_x, rook_end_y = (0, 5)
        
        elif start_x == 0 and start_y == 4 and end_x == 0 and end_y == 2:
            # Black-King Queenside Castle
            rook_start_x, rook_start_y = (0, 0)
            rook_end_x, rook_end_y = (0, 3)
        else:
            return
        
        self.move_piece(start=(rook_start_x, rook_start_y), end=(rook_end_x, rook_end_y))
        return
    
    # Placeholder function to check if pawn promotion is possible
    def is_pawn_promotion_possible(self, start, end, player_color):
        
        start_x, start_y = start
        end_x, end_y = end

        # The moved piece has to be pawn
        is_pawn = self.board[start_x][start_y].__repr__() in ('p', 'P')
        # is_pawn = isinstance(self.board[start_x][start_y], Pawn)

        # The ending row should be '0' if the player is 'white' and '7' if the player is 'black'
        reached_end = (player_color == 'white' and  end_x == 0) or (player_color == 'black' and end_x == 7)
        
        # Both the above condition has to be satisfied
        return is_pawn and reached_end
    
    # Placeholder function for asking player to promote pawn
    def ask_for_pawn_promotion(self, start, end, player_color):

        start_x, start_y = start
        end_x, end_y = end

        promotion_choices = {
            '1': Queen(player_color[0], 'Q'),
            '2': Rook(player_color[0], 'R'),
            '3': Bishop(player_color[0], 'B'),
            '4': Knight(player_color[0], 'N')
        }
        
        # Display Options
        print("Your pawn can be promoted! Please choose a piece for promotion: \n1. Queen \n2. Rook \n3. Bishop \n4. Knight")
        
        while True:
            piece = input("Enter the number corresponding to the piece you want (1-4): ")
            if piece not in promotion_choices:
                print("Invalid input. Please choose a number between 1 and 4.")
            else:
                break
        
        # First move the pawn to end location
        self.move_piece(start, end)

        # Promote the pawn
        self.board[end_x][end_y] = promotion_choices[piece]

        if piece == '2':
            self.board[end_x][end_y].is_untouched = False

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

# Class representing a rook piece
class Rook:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type
        self.is_untouched = True

    # Representation for printing the piece
    def __repr__(self):
        return self.piece_type if self.color == 'w' else self.piece_type.lower()

    # Placeholder for validating rook movement
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
            
        else:
            return False
        
        return not is_any_piece_present

    # Placeholder for checking horizontal movement
    def is_horizontal_move(self, start, end):

        start_x, start_y = start
        end_x, end_y = end 

        # Check for horizontal movement using the condition: (i, k) where 0 <= k <= 7, k != j i.e. start and end position should have same x coordinate
        is_hr_move = (start_x == end_x)

        return is_hr_move

    # Placeholder for checking vertical movement
    def is_vertical_move(self, start, end):

        start_x, start_y = start
        end_x, end_y = end 

        # Check for horizontal movement using the condition: (k, j) where 0 <= k <= 7, k != i i.e. start and end position should have same y coordinate

        is_vr_move = (start_y == end_y)
        
        return is_vr_move

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
        dx = 1 if int(start_x < end_x) else -1
        dy = 1 if int(start_y < end_y) else -1
        x, y = start_x + dx, start_y + dy

        while x != end_x and y != end_y:
            is_any_piece_present = is_any_piece_present or (board[x][y] is not None)
            x += dx
            y += dx

        return not is_any_piece_present

    # Placeholder for validating diagonal movement
    def is_diagonal_move(self, start, end):
        
        start_x, start_y = start
        end_x, end_y = end

        # Check for valid diagonal move usign the condition: (x, y) where |x-i| = |y-j|
        is_dia_move = (abs(start_x - end_x) == abs(start_y - end_y))
        return is_dia_move

# Class representing a king piece
class King:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type
        self.is_untouched = True

    # Representation for printing the piece
    def __repr__(self):
        return self.piece_type if self.color == 'w' else self.piece_type.lower()

    # Placeholder for validating king movement
    def is_valid_move(self, board, start, end):

        start_x, start_y = start
        end_x, end_y = end

        # If the end position have a piece then that piece color should not be same as currunt piece color
        if board[end_x][end_y] and board[end_x][end_y].color == self.color:
            return False

        is_valid_hr_move =  self.is_horizontal_move(start, end)
        is_valid_dia_move = self.is_diagonal_move(start, end)
        is_valid_vr_move = self.is_vertical_move(start, end)

        return is_valid_hr_move or is_valid_dia_move or is_valid_vr_move

    # Placeholder for horizontal move validation
    def is_horizontal_move(self, start, end):

        start_x, start_y = start
        end_x, end_y = end

        is_hr_move = (start_x == end_x and abs(start_y-end_y) == 1)

        return is_hr_move

    # Placeholder for diagonal move validation
    def is_diagonal_move(self, start, end):

        start_x, start_y = start
        end_x, end_y = end

        delta = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        is_dia_move = ((end_x-start_x, end_y-start_y) in delta)

        return is_dia_move

    # Placeholder for diagonal move validation
    def is_valid_king_castle_move(self, board, start, end):
        
        start_x, start_y = start
        end_x, end_y = end

        # Four possible castles
        # To castle king and rook should be at their original location
        # There should not a any piece between rook and king

        rook_is_present = False
        no_piece_in_bw = True
        is_untouched = False

        if start_x == 7 and start_y == 4 and end_x == 7 and end_y == 6:
            # White-King Kingside Castle
            # King's Position should be (7,4) and Rook's Position should be (7,7) and there should not be any piece between them
            # Also the end position should be (7, 6)
            
            rook_is_present = (board[7][7].__repr__() in ('r', 'R'))
            no_piece_in_bw = True
            for k in range(5, 7):
                no_piece_in_bw = no_piece_in_bw and (not board[7][k])
            is_untouched = self.is_untouched and (rook_is_present and board[7][7].is_untouched)

        elif start_x == 7 and start_y == 4 and end_x == 7 and end_y == 2:
            # White-King Queenside Castle
            # King's Position should be (7,4) and Rook's Position should be (7,0) and there should not be any piece between them
            # Also the end position should be (7,2)

            rook_is_present = (board[7][0].__repr__() in ('r', 'R'))
            no_piece_in_bw = True
            for k in range(1, 4):
                no_piece_in_bw = no_piece_in_bw and (not board[7][k])
            is_untouched = self.is_untouched and (rook_is_present and board[7][0].is_untouched)

        elif start_x == 0 and start_y == 4 and end_x == 0 and end_y == 6:
            # Black-King Kingside Castle
            # King's Position should be (0,4) and Rook's Position should be (0,7) and there should not be any piece between them
            # Also the end position should be (0, 6)
            
            rook_is_present = (board[0][7].__repr__() in ('r', 'R'))
            no_piece_in_bw = True
            for k in range(5, 7):
                no_piece_in_bw = no_piece_in_bw and (not board[0][k])
            is_untouched = self.is_untouched and (rook_is_present and board[0][7].is_untouched)

        elif start_x == 0 and start_y == 4 and end_x == 0 and end_y == 2:
            # Black-King Queenside Castle
            # King's Position should be (0,4) and Rook's Position should be (0,0) and there should not be any piece between them
            # Also the end position should be (0, 2)

            rook_is_present = (board[0][0].__repr__() in ('r', 'R'))
            no_piece_in_bw = True
            for k in range(1, 4):
                no_piece_in_bw = no_piece_in_bw and (not board[0][k])
            is_untouched = self.is_untouched and (rook_is_present and board[0][0].is_untouched)

        else:
            return False
        
        return rook_is_present and no_piece_in_bw and is_untouched

    # Placeholder for vertical move validation
    def is_vertical_move(self, start, end):

        start_x, start_y = start
        end_x, end_y = end

        is_vr_move = (start_y == end_y and abs(start_x-end_x) == 1)

        return is_vr_move

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
            dx = 1 if int(start_x < end_x) else -1
            dy = 1 if int(start_y < end_y) else -1
            x, y = start_x + dx, start_y + dy

            while x != end_x and y != end_y:
                is_any_piece_present = is_any_piece_present or (board[x][y] is not None)
                x += dx
                y += dx
            
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
    
# Class representing the game logic
class Game:
    def __init__(self):
        self.board = ChessBoard()  # Create the chessboard
        self.turn = 'white'  # White player starts

    # Placeholder for checking if there is check or checkmate
    def check_check_and_mate(self):
        pass

    # Placeholder to check if the palyer king is under check after player has completed his turn
    def is_king_check_free(self, turn):
        pass

    # Placeholder to switch turns between players
    def switch_turn(self):
        if self.turn == 'white':
            self.turn = 'black'  # Switch to black
        else:
            self.turn = 'white'  # Switch to white

    # Placeholder for checking if the king is in check
    def check_is_there_is_check_on_king(self, turn):
        pass

    # Function to start and display the game board
    def play(self):
        while True:
            self.board.print_board()  # Print the chessboard
            print(f"{self.turn.capitalize()}'s Turn")

            # Prompt for starting coordinate
            start_input = input("Enter starting location of piece or 'exit' to quit: ").strip()
            if start_input.lower() == 'exit':
                print("Exiting the game.")
                break

            # Prompt for ending coordinate
            end_input = input("Enter ending location of piece: ").strip()
            if end_input.lower() == 'exit':
                print("Exiting the game.")
                break
            
            if len(start_input) != 2 or len(end_input) != 2:
                print("Invalid input format. Please ensure you're using standard format.")
                continue

            # Process the inputs
            try:

                # Convert string input location to grid coordinates
                start_x, start_y = 8-int(start_input[1]), ord(start_input[0].upper()) - ord('A')
                end_x, end_y = 8-int(end_input[1]), ord(end_input[0]) - ord('A')

                print(f"Move requested: Piece at {start_input}({start_x}, {start_y}) to {end_input}({end_x}, {end_y}).")

            except ValueError:
                print("Invalid input format. Please ensure you're using standard format.")
                continue
            
            is_valid_move = self.board.is_valid_move(start=(start_x, start_y), end=(end_x, end_y), player_color=self.turn)
            if not is_valid_move:
                print("Invalid Move! Try again.")
                continue
            
            if self.board.is_pawn_promotion_possible(start=(start_x, start_y), end=(end_x, end_y), player_color=self.turn):
                self.board.ask_for_pawn_promotion(start=(start_x, start_y), end=(end_x, end_y), player_color=self.turn)
            else:
                # Move piece if move is valid
                self.board.move_piece(start=(start_x, start_y), end=(end_x, end_y))

            # Switch the turn after capturing the move
            self.switch_turn()

# Main entry point to run the game
if __name__ == "__main__":
    game = Game()
    game.play()
