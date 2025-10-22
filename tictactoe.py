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
    print("\n==========================\n")
    print(f' 1 | 2 | 3 ')
    print('---+---+---')
    print(f' 4 | 5 | 6 ')
    print('---+---+---')
    print(f' 7 | 8 | 9 ')
    print("\n==========================\n")

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

def minimax(state, depth, is_maximizing):
    """
    Minimax algorithm to determine the best move for the AI.
    """
    winner = check_winner(state)

    # Base cases
    if winner == 'O':
        return 10 - depth
    elif winner == 'X':
        return depth - 10
    elif is_draw(state):
        return 0

    # Recursive cases
    # If it's the maximizing player's turn (AI)
    if is_maximizing:
        best_score = -math.inf
        for (r, c) in get_available_moves(state):
            state[r][c] = 'O'
            score = minimax(state, depth + 1, False)
            state[r][c] = " "
            best_score = max(score, best_score)
        return best_score
    # If it's the minimizing player's turn (User)
    else:
        best_score = math.inf
        for (r, c) in get_available_moves(state):
            state[r][c] = 'X'
            score = minimax(state, depth + 1, True)
            state[r][c] = " "
            best_score = min(score, best_score)
        return best_score
    
def get_ai_move(state):
    """
    Determines the best move for the AI using the minimax algorithm.
    Returns the move as a tuple (row, col).
    """
    best_score = -math.inf
    best_move = None
    for (r, c) in get_available_moves(state):
        state[r][c] = 'O'
        score = minimax(state, 0, False)
        state[r][c] = " "
        if score > best_score:
            best_score = score
            best_move = (r, c)
    return best_move

def get_user_move(state):
    """
    Prompts the user for their move and returns it as a tuple (row, col).
    """
    while True:
            move = int(input("\nEnter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if (row, col) in get_available_moves(state):
                return (row, col)
            else:
                print("Invalid move. Try again.")

def check_winner(state):
    """
    Checks the board for a winner.
    Returns 'X' if player X wins, 'O' if player O wins, or None if no winner.
    """
    # Check rows and columns
    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2] != " ":
            return state[i][0]
        if state[0][i] == state[1][i] == state[2][i] != " ":
            return state[0][i]
    
    # Check diagonals
    if state[0][0] == state[1][1] == state[2][2] != " ":
        return state[0][0]
    if state[0][2] == state[1][1] == state[2][0] != " ":
        return state[0][2]
    
def is_draw(state):
    """
    Checks if the game is a draw.
    Returns True if the game is a draw, False otherwise.
    """
    # Checks if all cells are filled and there is no winner.
    return all(cell != " " for row in state for cell in row) and check_winner(state) is None

def print_menu():
    # Prints the game menu and prompts for user choice.
    print("1. Play a Game!")
    print("2. Clear Terminal")
    print("3. Exit")
    choice = None
    while choice not in ['1', '2', '3']:
        choice = input("Enter your choice: ")
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
    return choice

def reset_state():
    # Resets the game state to an empty board.
    return [[" " for _ in range(3)] for _ in range(3)]

def play_game():
    # Will add option for user to choose to go first or second later
    #choice = input("Do you want to go first? (y/n): ").lower()
    state = reset_state()
    choice = 'y'
    user_turn = choice == 'y'
    game_over = False
    # Will implement score tracking later
    user_win_counter = 0
    ai_win_counter = 0

    while not game_over:
        print_state_with_positions(state)
        print_state(state)
        if user_turn:
            row, col = get_user_move(state)
            state[row][col] = 'X'
        else:
            print("\nAI is making a move...")
            # Added to simulate thinking time
            time.sleep(1)
            row, col = get_ai_move(state)
            state[row][col] = 'O'
        
        winner = check_winner(state)
        if winner:
            print_state(state)
            if winner == 'X':
                print("\nCongratulations! You win!")
            else:
                print("\nAI wins! Better luck next time.")
            game_over = True
        elif is_draw(state):
            print_state(state)
            print("\nIt's a draw!")
            game_over = True
        else:
            user_turn = not user_turn

if __name__ == "__main__":
    # Initial empty board
    state = [[" " for _ in range(3)] for _ in range(3)]

    print('=' * 60)
    print("Welcome to Aiden's Tic-Tac-Toe!")
    print("You will be playing against an AI using the Minimax algorithm.")
    print('=' * 60 + '\n')

    # Print the initial state
    # print_state_with_positions(state)
    # print_state(state)

    # Main game loop
    while True: 
        choice = print_menu()
        if choice == '1':
            play_game()
        elif choice == '2':
            os.system('cls')
