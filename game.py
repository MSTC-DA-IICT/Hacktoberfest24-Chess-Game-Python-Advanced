from chessboard import ChessBoard

# Class representing the game logic
class Game:
    def __init__(self, predefined_moves=None):
        self.board = ChessBoard()  # Create the chessboard
        self.turn = 'white'  # White player starts
        self.predefined_moves = predefined_moves  # List of predefined moves
        self.current_move_index = 0  # Index for tracking moves

    # Function to execute predefined moves
    def execute_predefined_moves(self):
        while self.predefined_moves and self.current_move_index < len(self.predefined_moves):
            move = self.predefined_moves[self.current_move_index]
            start_input, end_input = move  # Unpack the move tuple
            self.make_move(start_input, end_input)
            self.current_move_index += 1

    # Function to make a move based on user input
    def make_move(self, start_input, end_input):
        # Convert string input location to grid coordinates
        try:
            start_x, start_y = 8 - int(start_input[1]), ord(start_input[0].upper()) - ord('A')
            end_x, end_y = 8 - int(end_input[1]), ord(end_input[0]) - ord('A')
            is_valid_move = self.board.is_valid_move(start=(start_x, start_y), end=(end_x, end_y), player_color=self.turn)
            
            if not is_valid_move:
                print(f"Invalid Move: {start_input} to {end_input}.")
                return
            
            if self.board.is_pawn_promotion_possible(start=(start_x, start_y), end=(end_x, end_y), player_color=self.turn):
                self.board.ask_for_pawn_promotion(start=(start_x, start_y), end=(end_x, end_y), player_color=self.turn)
            else:
                self.board.move_piece(start=(start_x, start_y), end=(end_x, end_y))

            # Check if there is a check on the opponent's king
            opponent_player = 'white' if self.turn == 'black' else 'black'
            if self.board.check_if_there_is_check_on_king(player_color=opponent_player):
                print(f"Check! {opponent_player}'s king is under attack.")

            # Switch the turn after capturing the move
            self.switch_turn()
        
        except Exception as e:
            print(f"Error occurred while making a move: {e}")

    # Placeholder to switch turns between players
    def switch_turn(self):
        if self.turn == 'white':
            self.turn = 'black'  # Switch to black
        else:
            self.turn = 'white'  # Switch to white

    # Function to start and display the game board
    def play(self):
        # Execute predefined moves first
        self.execute_predefined_moves()
        
        # Now switch to manual play
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

            self.make_move(start_input, end_input)


