# ======================================================================================
#   BLACKJACK  TERMINAL CARD GAME
# ======================================================================================
from Modules import blackjack_lib
from os import system
from sys import exit
from shutil import get_terminal_size
from time import sleep
from pyfiglet import Figlet
from colorama import Fore, Style


def main_stack():
    # creaza potul
    pot = blackjack_lib.Pot()
    # creaza banii jucatorului (hardcoded 1000)
    stack = blackjack_lib.Stack(1000)
    # check screen
    screen_width = get_terminal_size()[0]

    def main_program():
        # ======================================================================================
        #  Initializeaza obiectele
        # ======================================================================================
        # creaza un pachet de carti
        deck = blackjack_lib.Deck()
        # amesteca pachetul
        deck.shuffle()
        # creaza mainile pt jucator si pentru dealer
        player_hand = blackjack_lib.Hand()
        dealer_hand = blackjack_lib.DealerHand()

        # number_of_spaces = (screen_width - 36) // 2

        # ======================================================================================
        #   Redeseneaza ecranul
        # ======================================================================================
        def redraw_screen():
            system('cls')
            f = Figlet(font='bubble')

            print('')
            print(' ' + '=' * (get_terminal_size()[0] - 2))
            print(f.renderText('BLACKJACK'))
            print(' ' + '-' * (get_terminal_size()[0] - 2))
            print(f' You have: {stack}' + ' ' * (screen_width - len(f'You have: {stack}') - 2 - len(f'Bet: {pot}')) + f'Bet: {pot}')
            print(' ' + '=' * (get_terminal_size()[0] - 2))

            # Dealer Line
            if dealer_hand.cards:
                eval_count = len(f'Hand value: {str(dealer_hand.eval()[0])}')
                if dealer_hand.eval()[0] > 21:
                    eval_string = f'Hand value: {Style.BRIGHT + Fore.RED + str(dealer_hand.eval()[0]) + Style.RESET_ALL}'
                else:
                    eval_string = f'Hand value: {Style.BRIGHT + Fore.BLUE + str(dealer_hand.eval()[0]) + Style.RESET_ALL}'

                for j in range(1, len(dealer_hand.eval())):
                    eval_count += len(f' or {str(dealer_hand.eval()[j])}')
                    if dealer_hand.eval()[j] > 21:
                        eval_string += f' or {Style.BRIGHT + Fore.RED + str(dealer_hand.eval()[j]) + Style.RESET_ALL}'
                    else:
                        eval_string += f' or {Style.BRIGHT + Fore.BLUE + str(dealer_hand.eval()[j]) + Style.RESET_ALL}'

                if dealer_hand.hidden_card:
                    print(f' Dealer:{dealer_hand}' + ' ' * (screen_width - dealer_hand.number_of_chars - 12 - eval_count) + eval_string)
                else:
                    print(f' Dealer:{dealer_hand}' + ' ' * (screen_width - dealer_hand.number_of_chars - 9 - eval_count) + eval_string)
            else:
                print(' Dealer:')

            # Player Line
            if player_hand.cards:
                eval_count = len(f'Hand value: {str(player_hand.eval()[0])}')
                if player_hand.eval()[0] > 21:
                    eval_string = f'Hand value: {Style.BRIGHT + Fore.RED + str(player_hand.eval()[0]) + Style.RESET_ALL}'
                else:
                    eval_string = f'Hand value: {Style.BRIGHT + Fore.BLUE + str(player_hand.eval()[0]) + Style.RESET_ALL}'

                for j in range(1, len(player_hand.eval())):
                    eval_count += len(f' or {str(player_hand.eval()[j])}')
                    if player_hand.eval()[j] > 21:
                        eval_string += f' or {Style.BRIGHT + Fore.RED + str(player_hand.eval()[j]) + Style.RESET_ALL}'
                    else:
                        eval_string += f' or {Style.BRIGHT + Fore.BLUE + str(player_hand.eval()[j]) + Style.RESET_ALL}'

                print(f' Player:{player_hand}' + ' ' * (screen_width - player_hand.number_of_chars - 9 - eval_count) + eval_string)
            else:
                print(' Player:')

            print(' ' + '=' * (get_terminal_size()[0] - 2))

        # ======================================================================================
        #  PROMPT
        # ======================================================================================
        def prompt(message):
            quit_msg = "('q' to quit anytime)"
            print(' ' + message + ' ' * (screen_width - len(message) - len(quit_msg) - 2) + quit_msg)
            response = input(' >>')
            if response == 'q':
                exit(0)
            return response

        # ======================================================================================
        #  PLACE BET
        # ======================================================================================
        def place_bet(bet):
            if bet != 0:
                response = stack.withdraw(bet)
                if response['success'] == 1:
                    pot.add(bet)
                    redraw_screen()
                    return 0
                else:
                    return 1
            else:
                return 1

        # ======================================================================================
        #  PLAY HAND
        # ======================================================================================
        def play_hand(player='player'):
            if player == 'player':
                player_hand.add_card(deck.deal())
            else:
                dealer_hand.add_card(deck.deal())
            return 0

        # ======================================================================================
        #  CHECK FOR WINNER
        # ======================================================================================
        def check_winner(turn='dealer'):
            return 0

        # ======================================================================================
        #  PLAY GAME
        # ======================================================================================
        def play():
            while True:
                redraw_screen()

                # primele doua carti
                for i in range(2):
                    sleep(0.5)
                    player_hand.add_card(deck.deal())
                    redraw_screen()
                    sleep(0.5)
                    dealer_hand.add_card(deck.deal())
                    if i == 1:
                        dealer_hand.hide_card()
                    redraw_screen()

                # cere betul
                while True:
                    try:
                        bet = 0
                        while place_bet(bet):
                            redraw_screen()
                            bet = int(prompt('Place your bet!'))
                        break
                    except ValueError:
                        redraw_screen()

                # player's turn
                while True:
                    p = prompt('Hit?/Stay? (h/s)')
                    if p == 'h':
                        play_hand()
                    redraw_screen()
                    winner = check_winner('player')
                    if p == 's' or winner:
                        break

                # dealer's turn
                i = 0
                dealer_hand.unhide()
                while True:
                    i += 1
                    redraw_screen()
                    winner = check_winner()
                    if winner or i == 6:  # test
                        return winner
                    play_hand('dealer')
                    sleep(1)

        #  run play() & exit main_program
        return play()

    # run main_program & exit main_stack
    return main_program()


# ======================================================================================
#  MAIN ENTRY
# ======================================================================================
if __name__ == '__main__':
    main_stack()

# redraw_screen()
#

#
# sleep(0.1)
#
# for i in range(6):
#     sleep(0.1)
#     player_hand.add_card(deck.deal())
#     redraw_screen()
#
# dealer_hand.unhide()
# redraw_screen()
