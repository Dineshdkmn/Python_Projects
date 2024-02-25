##Tic-Tac-Toe AI

This code implements a Tic Tac Toe game with different player types: Human, Random Computer, and Smart Computer. Here's a breakdown of the components:

1. **TicTacToe Class**: 
   - Represents the game itself.
   - Initializes the board and keeps track of the current winner.
   - Methods to print the board, print board numbers for reference, check available moves, make a move, and determine a winner.

2. **play Function**: 
   - Manages the game flow, alternating between players' moves until the game is over.
   - Calls `get_move()` on each player to determine their move.
   - Handles printing the game state and checking for a winner or tie.

3. **Player Classes**:
   - `Player`: Base class for different types of players.
   - `HumanPlayer`: Allows a human player to input moves via command line.
   - `RandomComputerPlayer`: Generates random moves for a computer player.
   - `SmartComputerPlayer`: Implements a minimax algorithm for an intelligent computer player.

4. **Minimax Algorithm** (implemented within `SmartComputerPlayer`):
   - A recursive algorithm used to search through the game tree to determine the best move for the AI player.
   - It evaluates all possible moves and their outcomes to make the best decision.
   - The algorithm assigns scores to each possible outcome and chooses the move with the best score.

Overall, the code allows for playing Tic Tac Toe against either a human or computer players, including a smart AI player that uses the minimax algorithm to make strategic moves.