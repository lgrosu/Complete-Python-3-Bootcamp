# ======================================================================================
#   BLACKJACK  TERMINAL CARD GAME
# ======================================================================================
from Modules import blackjack_lib
import os
import sys
import shutil

# ======================================================================================
#  Initializeaza obiectele
# ======================================================================================
# creaza un pachet de carti
deck = blackjack_lib.Deck()

# amesteca pachetul
deck.shuffle()

# creaza mainile pt jucator si pentru dealer
player_hand = blackjack_lib.Hand()
player_hand.add_card(deck.deal())
player_hand.add_card(deck.deal())

dealer_hand = blackjack_lib.Hand()
dealer_hand.add_card(deck.deal())
dealer_hand.add_card(deck.deal())

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
    print('=' * (shutil.get_terminal_size()[0] - 1))
    print(' ' * number_of_spaces + 'BLACKJACK')
    print('-' * (shutil.get_terminal_size()[0] - 1))
    print(f'Stack: {stack}' + ' ' * (screen_width - len(f'Stack: {stack}') - 1 - len(f'Bet: {pot}')) + f'Bet: {pot}')
    print('=' * (shutil.get_terminal_size()[0] - 1))

    print(f'Dealer: {dealer_hand}')

    eval_string = ' Value: '
    for i in range(len(player_hand.eval())):
        eval_string += f'or  {player_hand.eval()[i]}'


    if player_hand.eval()[0] == player_hand.eval()[1]:
        print(f'Player: {player_hand} Value: {player_hand.eval()[0]}')
    else:
        print(f'Player: {player_hand} Value: {player_hand.eval()[0]} or {player_hand.eval()[1]}')


redraw_screen()
