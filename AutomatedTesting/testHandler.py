import os
from game import Game

def read_moves_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            moves = file.readlines()
        return [move.strip().upper() for move in moves if move.strip()]  # Return non-empty moves
    except FileNotFoundError:
        print("Error: The testing file was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def run_predefined_moves():
    # Path to the testing file
    

    file_path = os.path.join("AutomatedTesting",  'testing.txt')
    
    moves = read_moves_from_file(file_path)
    if not moves:
        print("No moves to process. Exiting the testing.")
        return

    game = Game()  # Initialize the game
    game.board.print_board()  # Print initial board
    
    for move in moves:
        start, end = move.split()  # Expecting moves in the format "A2 A3"
        
        # Convert string input location to grid coordinates
        start_x, start_y = 8 - int(start[1]), ord(start[0].upper()) - ord('A')
        end_x, end_y = 8 - int(end[1]), ord(end[0]) - ord('A')

        is_valid_move = game.board.is_valid_move(start=(start_x, start_y), end=(end_x, end_y), player_color=game.turn)
        if is_valid_move:
            game.board.move_piece(start=(start_x, start_y), end=(end_x, end_y))
            game.board.print_board()  # Print board after each move
            # Switch turns after each valid move
            game.switch_turn()
        else:
            print(f"Invalid Move: {move}")

    # After executing predefined moves, continue the game
    game.play()  # Allow players to continue manually
