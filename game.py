# game.py

import pygame
from board.chessboard import ChessBoard

class Game:
    def __init__(self):
        """
        Initializes the Game class, setting up the Pygame environment and 
        creating the chessboard.
        """
        pygame.init()  # Initialize Pygame
        self.window_size = (640, 640)  # Define window size for the game
        self.screen = pygame.display.set_mode(self.window_size)  # Create the game window
        pygame.display.set_caption("Chess Game")  # Set the window title
        self.clock = pygame.time.Clock()  # Create a clock to manage the game's frame rate
        self.board = ChessBoard()  # Create an instance of the ChessBoard
        self.selected_piece = None  # Variable to store the currently selected piece
        self.selected_position = None  # Variable to store the position of the selected piece

    def draw_board(self):
        """
        Draws the chessboard and its pieces on the screen.

        This function iterates through the board and draws alternating colors 
        for the squares, placing pieces in their respective positions.
        """
        colors = [(255, 206, 158), (209, 139, 71)]  # Define colors for light and dark squares
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]  # Alternate colors for squares
                pygame.draw.rect(self.screen, color, (col * 80, row * 80, 80, 80))  # Draw the square
                piece = self.board.board[row][col]  # Get the piece at the current position
                if piece:
                    self.screen.blit(piece.image, (col * 80, row * 80))  # Draw the piece image

    def handle_click(self, pos):
        """
        Handles mouse click events to select and move pieces.

        :param pos: The position of the mouse click.
        """
        col = pos[0] // 80  # Determine the column based on the click position
        row = pos[1] // 80  # Determine the row based on the click position

        if self.selected_piece:
            # Try to move the selected piece to the clicked position
            if self.board.move_piece(self.selected_position, (row, col)):
                self.selected_piece = None  # Deselect the piece if the move is successful
                self.selected_position = None
            else:
                # Reset selection if the move is not valid
                self.selected_piece = None
                self.selected_position = None
        else:
            # Select a piece if one is clicked
            self.selected_piece = self.board.board[row][col]
            if self.selected_piece:
                self.selected_position = (row, col)  # Store the position of the selected piece

    def play(self):
        """
        Main game loop that runs the game until the player quits.

        This function handles events, updates the screen, and keeps the game running.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Exit the game if the quit event is triggered
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(pygame.mouse.get_pos())  # Handle mouse click events

            self.screen.fill((0, 0, 0))  # Clear the screen with a black color
            self.draw_board()  # Draw the chessboard and pieces
            pygame.display.flip()  # Update the display
            self.clock.tick(60)  # Limit the frame rate to 60 FPS

        pygame.quit()  # Quit Pygame when the game loop ends

# Main entry point to run the game
if __name__ == "__main__":
    game = Game()  # Create an instance of the Game class
    game.play()    # Start the game loop
