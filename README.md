# Game of Nim

## Features

- **Classic Nim Game:**  
  A variant where each row of objects is represented by an integer, and players take turns removing a specified number of objects from a chosen row.

- **AI Opponent:**  
  The computer makes its move using an alpha-beta search algorithm (via `alpha_beta_player`), offering a challenging gameplay experience.

- **Interactive Command Line Interface:**  
  Human players input moves via the terminal in a user-friendly format.

- **Modular and Extensible:**  
  The design is easy to adapt to different game configurations or AI algorithms.

## Prerequisites

- Python 3.6 or higher.
- A module named `games` that provides:
  - The base classes `Game` and `GameState`.
  - The `alpha_beta_player` function for AI move computation.

> **Note:** This project relies on the `games` module, which is part of this GitHub account. You must clone or download the repository containing these classes and functions from [this GitHub account](https://github.com/aimacode/aima-python/blob/master/search.py#L440) and ensure it is available in your project (either in the same directory as `game_of_nim.py` or installed in your Python environment).

## Installation

1. Clone this repository or download the `game_of_nim.py` file.
2. Clone or download the `games` module from the above GitHub account and place it in the same directory as `game_of_nim.py` or ensure it is installed in your Python environment.

## How to Run

1. Open a terminal and navigate to the directory containing the files.
2. Run the script using Python:

   ```bash
   python3 game_of_nim.py
