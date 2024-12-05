# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:58:40 2024
group 21 - 41
"""

import random

# Initialize the board
board = [str(_) for _ in range(1, 10)]

def print_board():
    print("******************************")
    print(f"*    {board[0]}    *   {board[1]}     *    {board[2]}   *")
    print("******************************")
    print(f"*    {board[3]}    *    {board[4]}    *    {board[5]}   *")
    print("******************************")
    print(f"*    {board[6]}    *    {board[7]}    *    {board[8]}   *")
    print("******************************\n")

def move_placer(move, player):
    if board[move] not in ['X', 'O']:
        board[move] = player
        return True  # Move successful
    else:
        return False  # Invalid move

def check_winner(player):
    # Winning combinations: rows, columns, diagonals
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for combo in win_conditions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_full():
    return all(space in ['X', 'O'] for space in board)

def get_computer_move():
    available_moves = [i for i in range(9) if board[i] not in ['X', 'O']]
    return random.choice(available_moves)

def position(play):
    pos_map = {5
        0: "top left", 1: "top center", 2: "top right",
        3: "middle left", 4: "middle center", 5: "middle right",
        6: "bottom left", 7: "bottom center", 8: "bottom right"
    }
    return pos_map[play]

# Game Start
print("Welcome to Tic-Tac-Toe!")
print_board()

# First move: Computer places 'X'
computer_start = random.randint(0, 8)
move_placer(computer_start, 'X')
print(f"Computer starts with 'X' in {position(computer_start)}.")
print_board()

# Main game loop
while True:
    # User's Turn
    while True:
        try:
            user_move = int(input("Your turn (enter 1-9): ")) - 1
            if 0 <= user_move <= 8 and move_placer(user_move, 'O'):
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

    print(f"You played in {position(user_move)}.")
    print_board()

    if check_winner('O'):
        print("Congratulations! You win!")
        break
    if is_full():
        print("It's a tie!")
        break

    # Computer's Turn
    print("Computer's turn...")
    computer_move = get_computer_move()
    move_placer(computer_move, 'X')

    print(f"Computer played in {position(computer_move)}.")
    print_board()

    if check_winner('X'):
        print("Computer wins! Better luck next time!")
        break
    if is_full():
        print("It's a tie!")
        break
