# Tic-Tac-Toe AI

## Overview
This project is an implementation of the classic game Tic-Tac-Toe with a twist: you can play against an AI! The game is built using Python, with the graphical interface powered by the Pygame library. The AI uses the Minimax algorithm to calculate its moves, ensuring a challenging experience.

## Installation

### Prerequisites
- Python 3.x
- Pygame library

### Setup
1. Clone the repository to your local machine.
2. Install Pygame if you haven't already, using `pip install pygame`.

## Usage

To play the game, run `python runner.py` from the command line. The game window will open, and you can choose to play as either X or O.

## How to Play
- Select whether you want to play as X or O at the start of the game.
- Click on an empty tile to make your move.
- The AI will make its move after you.
- The game ends when either player wins or all tiles are filled, resulting in a tie.
- You can play again by clicking the "Play Again" button after a game is over.

## Features
- **Intuitive Interface**: Easy to use graphical interface.
- **AI Opponent**: Play against a challenging AI opponent.
- **Replayability**: Option to play again after each game.

## Code Structure
- `tictactoe.py`: Contains the game logic and AI algorithm.
- `runner.py`: Manages the graphical interface and game loop using Pygame.
