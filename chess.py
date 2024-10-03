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
            board[1][i] = Pawn('w', 'P')  # White pawn
            board[6][i] = Pawn('b', 'P')  # Black pawn

        # Define the placement of other pieces (Rooks, Knights, Bishops, Queen, King)
        placement = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for i in range(8):
            if placement[i] == 'R':
                board[0][i] = Rook('w', placement[i])  # White Rook
                board[7][i] = Rook('b', placement[i])  # Black Rook
            elif placement[i] == 'N':
                board[0][i] = Knight('w', placement[i])  # White Knight
                board[7][i] = Knight('b', placement[i])  # Black Knight
            elif placement[i] == 'B':
                board[0][i] = Bishop('w', placement[i])  # White Bishop
                board[7][i] = Bishop('b', placement[i])  # Black Bishop
            elif placement[i] == 'Q':
                board[0][i] = Queen('w', placement[i])   # White Queen
                board[7][i] = Queen('b', placement[i])   # Black Queen
            elif placement[i] == 'K':
                board[0][i] = King('w', placement[i])    # White King
                board[7][i] = King('b', placement[i])    # Black King
        return board

    # Function to print the board in a human-readable format
    def print_board(self):
        for row in self.board:
            print(' '.join([str(piece) if piece else '.' for piece in row]))  # Display pieces or '.' for empty squares

    # Placeholder function for moving pieces (to be implemented)
    def move_piece(self, start, end):
        pass

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
        
        return self.board[start_x][start_y].is_valid_move(board=self.board, start=start, end=end)

    # Placeholder function to check if pawn promotion is possible
    def is_pawn_promotion_possible(self, start, end, player_color):
        pass

    # Placeholder function for asking player to promote pawn
    def ask_for_pawn_promotion(self, start, end, player_color):
        pass

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
            anyPiece = False
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
        if not self.is_diagonal_move(self, start, end):
            return False
        
        # If the end position have a piece then that piece color should not be same as currunt piece color
        if board[end_x][end_y] and board[end_x][end_y].color == self.color:
            return False

        # Now check that there are no pieces in the path from start to end
        any_piece_present = False
        dx, dy = int(start_x < end_x), int(start_y < end_y) # dx and dy are the directions of movement 
        x, y = start_x + dx, start_y + dy

        while (x, y) != end:
            any_piece_present = any_piece_present or (board[x][y] is not None)
            x += dx
            y += dx

        return not any_piece_present

    # Placeholder for validating diagonal movement
    def is_diagonal_move(self, start, end):
        
        start_x, start_y = start
        end_x, end_y = end

        # Check for valid diagonal move usign the condition: (x, y) where |x-y| = |i-j|
        is_dia_move = (abs(start_x-start_y) == abs(end_x-end_y))
        return is_dia_move

# Class representing a king piece
class King:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    # Representation for printing the piece
    def __repr__(self):
        return self.piece_type if self.color == 'w' else self.piece_type.lower()

    # Placeholder for validating king movement
    def is_valid_move(self, start, end, player_color):
        pass

    # Placeholder for horizontal move validation
    def is_horizontal_move(self, start, end, player_color):
        pass

    # Placeholder for diagonal move validation
    def is_diagonal_move(self, board, start, end):
        pass

    # Placeholder for vertical move validation
    def is_vertical_move(self, board, start, end):
        pass

# Class representing a queen piece
class Queen:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    # Representation for printing the piece
    def __repr__(self):
        return self.piece_type if self.color == 'w' else self.piece_type.lower()

    # Placeholder for validating queen movement
    def is_valid_move(self, start, end, player_color):
        pass

    # Placeholder for horizontal movement check
    def is_horizontal_move(self, board, start, end):
        pass

    # Placeholder for vertical movement check
    def is_vertical_move(self, board, start, end):
        pass

    # Placeholder for diagonal movement check
    def is_diagonal_move(self, board, start, end):
        pass

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
            start_input = input("Enter starting coordinate (x,y) or 'exit' to quit: ").strip()
            if start_input.lower() == 'exit':
                print("Exiting the game.")
                break

            # Prompt for ending coordinate
            end_input = input("Enter ending coordinate (x,y): ").strip()
            if end_input.lower() == 'exit':
                print("Exiting the game.")
                break

            # Prompt for piece
            piece_input = input("Enter piece (P, R, N, B, Q, K): ").strip()
            if piece_input.lower() == 'exit':
                print("Exiting the game.")
                break

            # Process the inputs
            try:
                start_x, start_y = map(int, start_input.split(','))
                end_x, end_y = map(int, end_input.split(','))

                print(f"Move requested: Piece at ({start_x}, {start_y}) to ({end_x}, {end_y}) as {piece_input}")

            except ValueError:
                print("Invalid input format. Please ensure you're using (x,y) format.")
                continue
            
            
            is_valid_move = self.board.is_valid_move(start=(start_x, start_x), end=(end_x, end_y), player_color=self.turn)
            if not is_valid_move:
                print("Invalid Move! Try again.")
                continue
            


            # Switch the turn after capturing the move
            self.switch_turn()

# Main entry point to run the game
if __name__ == "__main__":
    game = Game()
    game.play()
