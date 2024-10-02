# chess.py

from game import Game

def main():
    """
    Main function to start the chess game.

    This function creates an instance of the Game class and calls 
    the play method to begin the game.
    """
    game = Game()  # Create an instance of the Game class
    game.play()    # Start playing the game

if __name__ == "__main__":
    main()  # Call the main function if this script is executed
