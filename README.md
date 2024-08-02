
# Chess Game

Welcome to the Chess Game project! This is a Python-based chess game developed using Pygame. It supports both player-vs-player and player-vs-AI modes. The AI opponent uses the Minimax algorithm to determine the best moves.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Gameplay](#gameplay)
- [AI Implementation](#ai-implementation)

## Features

- **Player vs. Player Mode**: Play a classic game of chess with another player on the same device.
- **Player vs. AI Mode**: Challenge the AI, which uses the Minimax algorithm to play against you.
- **Move Validation**: Ensures only legal moves can be made, including special moves like castling, en passant, and pawn promotion.
- **Check/Checkmate Detection**: Automatically detects check, checkmate, and stalemate situations.
- **Graphical Interface**: A user-friendly interface with visual feedback for selected pieces, valid moves, and game status.

## Installation

### Prerequisites

- **Python 3.12.3 or later**
- **Pygame**: A set of Python modules designed for writing video games.

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/chess-game.git
   cd chess-game
   ```

2. **Install Dependencies**:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   ```bash
   python src/main.py
   ```
   or for Linux and Mac os
   ```bash
   python3 src/main.py
   ``` 

## Usage

1. **Starting the Game**: Run the `main.py` file in the `src` directory to start the game.
2. **Main Menu**: Select between Player vs. Player or Player vs. AI modes.
3. **Playing**: Click on a piece to select it and then click on a destination square to make a move. The game automatically enforces chess rules.
4. **End Game**: The game will notify you of check, checkmate, or stalemate. You can restart the game or exit.

## Project Structure

```
chess-game/
│
├── src/
│   ├── main.py          # Main application entry point
│   ├── game.py          # Game logic and state management
│   ├── board.py         # Board representation and logic
│   ├── pieces.py        # Chess pieces and their movements
│   ├── ai.py            # AI logic and Minimax algorithm
│   ├── utils.py         # Utility functions and constants
│   ├── assets/          # Images and other assets
│   └── __init__.py      # Package initialization
│
└── README.md            # Project documentation
```

## Gameplay

### Controls

- **Mouse Click**: Select and move pieces.
- **Keyboard Shortcuts** (Optional): You can extend the game with keyboard shortcuts for various actions.

### Rules

- Standard chess rules apply, including:
  - Pawn promotion
  - Castling
  - En passant
  - Check, checkmate, and stalemate detection

## AI Implementation

The AI uses the Minimax algorithm with alpha-beta pruning. The algorithm evaluates possible moves up to a certain depth and selects the move with the best evaluation score. The evaluation function considers material value, piece positions, and other heuristics to determine the best move.


