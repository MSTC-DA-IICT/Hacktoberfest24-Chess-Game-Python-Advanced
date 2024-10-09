from Pieces.pawn import Pawn
from Pieces.rook import Rook
from Pieces.knight import Knight
from Pieces.bishop import Bishop
from Pieces.queen import Queen
from Pieces.king import King

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

    # Placeholder to check if the palyer king is under check after player has completed his turn
    def is_king_check_free(self, player_color):
        return not self.check_if_there_is_check_on_king(player_color)
    
    # Placeholder for checking if the king is in check
    def check_if_there_is_check_on_king(self, player_color):
    
        # Find the location of the king
        king_position = None

        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece.__repr__() in ('k', 'K') and piece.color == player_color[0]:
                    king_position = (i, j)
                    break
            if king_position:
                break
        
        opponant_player = 'white' if player_color == 'black' else 'black'
        # Now using every opponant piece try to validate the king-capture move

        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece and piece.color == opponant_player[0]:
                    is_possible_capture_king = self.is_valid_move(start=(i, j), end=king_position, player_color=opponant_player)
                    if is_possible_capture_king:
                        # King is in check
                        return True
        
        return False

    # Placeholder for checking if there is check or checkmate
    def check_check_and_mate(self):
        pass
