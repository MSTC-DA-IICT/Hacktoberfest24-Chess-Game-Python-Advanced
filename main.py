from game import Game
from AutomatedTesting import testHandler  

# Main entry point to run the game
if __name__ == "__main__":
    # Prompt user for input
    choice = input("Do you want to play with predefined moves (type '1') or start from scratch (type '2')? ")

    if choice == '1':
        # Run the test handler to process predefined moves
        testHandler.run_predefined_moves()  
    elif choice == '2':
        # Start a new game
        game = Game()
        game.play()
    else:
        print("Invalid choice! Please enter '1' or '2'.")
