# chessboard.py

from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King

class ChessBoard:
    def __init__(self):
        """
        Initializes the ChessBoard and creates the initial board setup.
        """
        self.board = self.create_board()  # Create the chessboard layout

    def create_board(self):
        """
        Creates an 8x8 chessboard with initial piece placements.

        :return: The initialized chessboard.
        """
        board = [[None for _ in range(8)] for _ in range(8)]  # Create an 8x8 grid
        
        # Place pawns
        for i in range(8):
            board[1][i] = Pawn('w', 'P')  # White pawns
            board[6][i] = Pawn('b', 'P')  # Black pawns

        # Place other pieces
        placements = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece_class in enumerate(placements):
            board[0][i] = piece_class('w', piece_class.__name__[0])  # White pieces
            board[7][i] = piece_class('b', piece_class.__name__[0])  # Black pieces

        return board

    def move_piece(self, start, end):
        """
        Moves a piece from the start position to the end position.

        :param start: The starting coordinates of the piece (row, column).
        :param end: The target coordinates to move the piece (row, column).
        :return: True if the move is successful, False otherwise.
        """
        piece = self.board[start[0]][start[1]]  # Get the piece at the starting position
        # Removed move validation logic
        if piece:  # If there is a piece at the start position
            self.board[end[0]][end[1]] = piece  # Move the piece to the end position
            self.board[start[0]][start[1]] = None  # Remove the piece from the start position
            return True  # Move successful
        return False  # Move unsuccessful

    def print_board(self):
        """
        Prints the chessboard in a human-readable format.

        Each piece is displayed or '.' for empty squares.
        """
        for row in self.board:
            print(' '.join([str(piece) if piece else '.' for piece in row]))  # Display pieces
