from chessBoard import ChessBoard # Import the chessboard class

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

            # Switch the turn after capturing the move
            self.switch_turn()

# Main entry point to run the game
if __name__ == "__main__":
    game = Game()
    game.play()
