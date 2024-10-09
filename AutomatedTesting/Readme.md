# Game Testing

This folder contains files for automated testing of the chess game.

## testing.txt Format

The `testing.txt` file should contain a series of moves to be executed automatically during testing. The format is as follows:

1. **Moves**: Each move should be on a new line, in the format `START END` (e.g., `E2 E4`).
2. **Example Moves**:
E2 E4 
G1 F3 
D2 D4
3. **Remember** White makes the first move.


**Note**: Moves are **case-insensitive**. For example, `e2 e4` is valid.
- Ensure that the file is placed in the "AutomatedTesting" directory alongside this README.

## Usage

- When running the game, the predefined moves in `testing.txt` will be executed automatically. After all moves have been processed, the game will allow manual play to continue.
- If there is any invalid move, the game will exit. You should recheck the test.txt file in this case.



