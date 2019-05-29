# ======================================================================================
#   BLACKJACK  TERMINAL CARD GAME
# ======================================================================================
from Modules import blackjack_lib
import os
import sys
import shutil
import time
from colorama import init, Fore, Style

# ======================================================================================
#  Initializeaza obiectele
# ======================================================================================
# creaza un pachet de carti
deck = blackjack_lib.Deck()

# amesteca pachetul
deck.shuffle()

# creaza mainile pt jucator si pentru dealer
player_hand = blackjack_lib.Hand()
dealer_hand = blackjack_lib.Hand()

# creaza potul
pot = blackjack_lib.Pot()

# creaza banii jucatorului (1000)
stack = blackjack_lib.Stack(1000)

# check screen
screen_width = shutil.get_terminal_size()[0]
number_of_spaces = (screen_width - 9) // 2


# ======================================================================================
#   Redeseneaza ecranul
# ======================================================================================
def redraw_screen():
    os.system('cls')

    print('')
    print(' ' + '=' * (shutil.get_terminal_size()[0] - 2))
    print(' ' * number_of_spaces + 'BLACKJACK')
    print(' ' + '-' * (shutil.get_terminal_size()[0] - 2))
    print(f' Stack: {stack}' + ' ' * (screen_width - len(f'Stack: {stack}') - 2 - len(f'Bet: {pot}')) + f'Bet: {pot}')
    print(' ' + '=' * (shutil.get_terminal_size()[0] - 2))

    print(f' Dealer:{dealer_hand}')
    if player_hand.cards:
        eval_count = len(f'Hand value: {str(player_hand.eval()[0])}')
        if player_hand.eval()[0] > 21:
            eval_string = f'Hand value: {Style.BRIGHT + Fore.RED + str(player_hand.eval()[0]) + Style.RESET_ALL}'
        else:
            eval_string = f'Hand value: {Style.BRIGHT + Fore.BLUE + str(player_hand.eval()[0]) + Style.RESET_ALL}'

        for i in range(1, len(player_hand.eval())):
            eval_count += len(f' or {str(player_hand.eval()[i])}')
            if player_hand.eval()[i] > 21:
                eval_string += f' or {Style.BRIGHT + Fore.RED + str(player_hand.eval()[i]) + Style.RESET_ALL}'
            else:
                eval_string += f' or {Style.BRIGHT + Fore.BLUE + str(player_hand.eval()[i]) + Style.RESET_ALL}'

        print(f' Player:{player_hand}' + ' ' * (
                screen_width - player_hand.number_of_chars - 9 - eval_count) + eval_string)

    else:
        print(' Player:')

    print(' ' + '=' * (shutil.get_terminal_size()[0] - 2))



redraw_screen()

for i in range(2):
    time.sleep(0.1)
    dealer_hand.add_card(deck.deal())
    redraw_screen()

time.sleep(0.1)

for i in range(6):
    time.sleep(0.1)
    player_hand.add_card(deck.deal())
    redraw_screen()

