# Unbeatable TIC-TAC-TOE

An interactive game of Tic-Tac-Toe which a player plays against the machine.

## Algorithm
The computer uses the minimax algorithm to minimize the loss when deciding it's next move. Since the sample space for the game of Tic-Tac-Toe is relatively small, it is possible for computer to explore the decision tree to the very end of the game. This ensures a draw in the worst case.

## Running the game
To start the game, simply run the TicTacToe.py in your terminal using the following command:

> `python TicTacToe.py`

## TODO

- [ ] Animate the existing board instead of printing a new board on state change.
- [ ] Offer difficulty levels by limiting the depth of sample space tree explored by the algorithm.

## Resources
1. Wikipedia article for Minimax algorithm, https://en.wikipedia.org/wiki/Minimax
