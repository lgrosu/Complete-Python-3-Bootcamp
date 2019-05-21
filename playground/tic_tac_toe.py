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
    print('       -----------')
    print(f'  1   | {table["a1"]} | {table["b1"]} | {table["c1"]} |')
    print('       -----------')
    print(f'  2   | {table["a2"]} | {table["b2"]} | {table["c2"]} |')
    print('       -----------')
    print(f'  3   | {table["a3"]} | {table["b3"]} | {table["c3"]} |')
    print(f'       -----------')
    print('        a   b   c   ')


# Clear Data
def clear_data():
    global table
    global players
    table = {'a1': ' ', 'a2': ' ', 'a3': ' ', 'b1': ' ', 'b2': ' ', 'b3': ' ', 'c1': ' ', 'c2': ' ', 'c3': ' '}
    players = {'1': '', '2': ''}


# Draw message
def draw_message(msg=''):
    print(msg)


# Draw prompter
def prompter(player=0):
    if player:
        return input(f'Player {player} >>')
    else:
        return input(' >>')


# Pick symbols (X or O)
def pick_x(player):
    options = ['x', 'o']
    draw_message("Pick letter 'X' or letter 'O':")
    response = prompter(player)

    if str(response).lower() not in options:
        return False
    else:
        players[str(player)] = str(response).upper()
        options.remove(str(response).lower())
        players[str(3 - player)] = options[0].upper()
        draw_table()
        return True


# Check response
def check_response(player, response):
    already_filled_cells = list({k: v for k, v in table.items() if v != ' '})
    if response in already_filled_cells or response not in list(table):
        return 'invalid'
    else:
        return 'valid'


# Save response
def save_response(player, response):
    table[response] = players[str(player)].upper()


# Check winner
def check_winner(player):
    ocupate = list({k: v for k, v in table.items() if v == players[str(player)].upper()})
    if (
            'a1' in ocupate and 'b1' in ocupate and 'c1' in ocupate) or (
            'a2' in ocupate and 'b2' in ocupate and 'c2' in ocupate) or (
            'a3' in ocupate and 'b3' in ocupate and 'c3' in ocupate) or (
            'a1' in ocupate and 'a2' in ocupate and 'a3' in ocupate) or (
            'b1' in ocupate and 'b2' in ocupate and 'b3' in ocupate) or (
            'c1' in ocupate and 'c2' in ocupate and 'c3' in ocupate) or (
            'a1' in ocupate and 'b2' in ocupate and 'c3' in ocupate) or (
            'a3' in ocupate and 'b2' in ocupate and 'c1' in ocupate):
        return player
    elif len({k: v for k, v in table.items() if v != ' '}) == 9:
        return 3
    else:
        return 0


# Play
def play_game():
    i = 0
    response = ''
    while True:
        player = i % 2 + 1
        draw_table()

        if i == 0 and players['1'] == '':
            symbol_picked = pick_x(player)
            if not symbol_picked:
                continue

        winner = check_winner(3 - player)
        if winner:
            if winner == 3:
                draw_message("Draw! Play again? (y/n)")
            else:
                draw_message(f"Player {winner} won! Play again? (y/n)")
            play_again = prompter()

            if play_again.lower() == 'y':
                clear_data()
                return
            elif play_again.lower() == 'n':
                return 'game_over'
            else:
                continue

        draw_message("(Press 'a1', 'c3' etc. to play, 'q' to quit anytime)")
        response = prompter(player)
        if response == 'q':
            sys.exit(0)

        if check_response(player, response) != 'valid':
            continue

        save_response(player, response.lower())
        i += 1


if __name__ == '__main__':
    # MAIN ENTRY
    while True:
        message = play_game()
        if message == 'game_over':
            break
