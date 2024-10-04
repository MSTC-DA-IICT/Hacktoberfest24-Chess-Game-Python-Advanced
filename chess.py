# Class representing the chessboard
class ChessBoard:
    def __init__(self):
        # Initializes the board with pieces
        self.board = self.create_board()

    # Creates the 8x8 chessboard and places all pieces
    def create_board(self): 

        board = [["." for _ in range(8)] for _ in range(8)]  # Create 8x8 grid

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
        i=8
        for row in reversed(self.board):
            print(f'  {i} ', ' '.join([str(piece) if piece else '.' for piece in row]))  # Display pieces or '.' for empty squares
            i-=1
        
        print("     A B C D E F G H")  # Display pieces or '.' for empty squares

    # Placeholder function for moving pieces (to be implemented)
    def move_piece(self, start, end):
        pass

    # Placeholder function for validating moves (to be implemented)
    def is_valid_move(self, start, end, player_color):
        pass

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
        pass

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
                start_x, start_y = map(int, [ord(start_input[0]) - ord('A') + 1, start_input[1]])
                end_x, end_y = map(int, [ord(end_input[0]) - ord('A') + 1, end_input[1]])

                print(f"\nMove requested: Piece at {start_input} to {end_input} as {piece_input}\n")

            except ValueError:
                print("\nInvalid input format. Please ensure you're using (x,y) format.\n")
                continue

            # Switch the turn after capturing the move
            self.switch_turn()

# Main entry point to run the game
if __name__ == "__main__":
    game = Game()
    game.play()
