# Tic Tac Toe Game - First Python Project

import os
import sys

# Globals - Table position, Players symbols
table = {'a1': ' ', 'a2': ' ', 'a3': ' ', 'b1': ' ', 'b2': ' ', 'b3': ' ', 'c1': ' ', 'c2': ' ', 'c3': ' '}
players = {'1': '', '2': ''}


# Draw table
def draw_table():
    os.system('cls')
    print('')
    print(f'  1 | {table["a1"]} | {table["b1"]} | {table["c1"]} |')
    print('  ---------------')
    print(f'  2 | {table["a2"]} | {table["b2"]} | {table["c2"]} |')
    print('  ---------------')
    print(f'  3 | {table["a3"]} | {table["b3"]} | {table["c3"]} |')
    print(f'  ---------------')
    print('      A   B   C   ')


# Draw message
def draw_message(msg=''):
    draw_table()
    print(msg)


# Draw prompter
def prompter(player):
    return input(f'Player {player} >>')


# Pick symbols
def pick_x(player):
    options = ['x', 'o']
    draw_message("Pick letter 'X' or letter 'O':")
    response = prompter(player)

    if str(response).lower() not in options:
        return False
    else:
        players[str(player)] = str(response).lower()
        options.remove(str(response).lower())
        players[str(3 - player)] = options[0]
        return True


# Check response
def check_response(player, response):
    return 'valid'


# Save response
def save_response(player, response):
    table[response] = players[str(player).upper()]


# Check winner
def check_winner():
    pass


# Play
def play_game():
    i = 0
    response = ''
    while True:
        player = i % 2 + 1
        draw_table()
        if i == 0:
            symbol_picked = pick_x(player)
            if not symbol_picked:
                continue

        draw_message("(Press 'q' to quit anytime)")
        response = prompter(player)
        if response == 'q':
            sys.exit(0)
        if check_response(player, response) != 'valid':
            continue
        save_response(player, response)
        check_winner()

        i += 1


# MAIN ENTRY
play_game()
