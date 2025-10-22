# AI Tic-Tac-Toe Game using Minimax Algorithm
# Aiden Cary
# AI w/ Prof Stein
# Tic-Tac-Toe is a zero-sum, perfect information game with a small state space that is perfect for demonstrating the Minimax algorithm.
# The max depth of a game tree is 9 plys total which is one for each cell on the board

import math
import random
import time
import os

def print_state(state):
    # Prints the Tic-Tac-Toe board
    print(f' {state[0][0]} | {state[0][1]} | {state[0][2]} ')
    print('---+---+---')
    print(f' {state[1][0]} | {state[1][1]} | {state[1][2]} ')
    print('---+---+---')
    print(f' {state[2][0]} | {state[2][1]} | {state[2][2]} ')

def print_state_with_positions(state):
    # Prints the Tic-Tac-Toe board with position numbers for user reference
    print(f' 1 | 2 | 3 ')
    print('---+---+---')
    print(f' 4 | 5 | 6 ')
    print('---+---+---')
    print(f' 7 | 8 | 9 ')

def get_available_moves(state):
    """
    Returns a list of available moves on the board.
    Each move is represented as a tuple (row, col).
    """
    moves = []
    # Checks for empty spaces on the board using a nested loop.
    for r in range(3):
        for c in range(3):
            # If the cell is empty, add the move to the list.
            if state[r][c] == " ":
                moves.append((r, c))
    return moves


if __name__ == "__main__":
    # Initial empty board
    state = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Aiden's Tic-Tac-Toe!")
    print("You will be playing against an AI using the Minimax algorithm.")

    # Print the initial state
    print_state_with_positions(state)
    print_state(state)