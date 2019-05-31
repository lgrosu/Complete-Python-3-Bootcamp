# ======================================================================================
#   SIMPLE BLACKJACK  TERMINAL CARD GAME
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
            f = Figlet(font='big')

            print('')
            print(' ' + '=' * (get_terminal_size()[0] - 2))
            print(f.renderText('BLACKJACK'))
            print(' ' + '-' * (get_terminal_size()[0] - 2))
            print(f' You have: {stack}' + ' ' * (screen_width - len(f'You have: {stack}') - 2 - len(f'Pot: {pot}')) + f'Pot: {pot}')
            print(' ' + '=' * (get_terminal_size()[0] - 2))

            # Dealer Line
            if dealer_hand.cards:
                eval_count = len(f'Hand value: {str(dealer_hand.eval()[0])}')
                if dealer_hand.eval()[0] > 21:
                    eval_string = f'Hand value: {Style.BRIGHT + Fore.RED + str(dealer_hand.eval()[0]) + Style.RESET_ALL}'
                else:
                    eval_string = f'Hand value: {Style.BRIGHT + Fore.LIGHTGREEN_EX + str(dealer_hand.eval()[0]) + Style.RESET_ALL}'

                for j in range(1, len(dealer_hand.eval())):
                    eval_count += len(f' or {str(dealer_hand.eval()[j])}')
                    if dealer_hand.eval()[j] > 21:
                        eval_string += f' or {Style.BRIGHT + Fore.RED + str(dealer_hand.eval()[j]) + Style.RESET_ALL}'
                    else:
                        eval_string += f' or {Style.BRIGHT + Fore.LIGHTGREEN_EX + str(dealer_hand.eval()[j]) + Style.RESET_ALL}'

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
                    eval_string = f'Hand value: {Style.BRIGHT + Fore.LIGHTGREEN_EX + str(player_hand.eval()[0]) + Style.RESET_ALL}'

                for j in range(1, len(player_hand.eval())):
                    eval_count += len(f' or {str(player_hand.eval()[j])}')
                    if player_hand.eval()[j] > 21:
                        eval_string += f' or {Style.BRIGHT + Fore.RED + str(player_hand.eval()[j]) + Style.RESET_ALL}'
                    else:
                        eval_string += f' or {Style.BRIGHT + Fore.LIGHTGREEN_EX + str(player_hand.eval()[j]) + Style.RESET_ALL}'

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
        #  DOUBLE DOWN CHOICE
        # ======================================================================================
        def double_down():
            response = stack.withdraw(pot.bet)
            if response['success'] == 1:
                pot.add(pot.bet)
                return 0
            else:
                return 1

        # ======================================================================================
        #  SURRENDER CHOICE
        # ======================================================================================
        def surrender():
            stack.add(pot.pot / 2)
            pot.clear_bet()
            pot.clear_pot()
            return 0

        # ======================================================================================
        #  EVEN MONEY CHOICE
        # ======================================================================================
        def even_money():
            stack.add(pot.bet)
            pot.pot = pot.pot - pot.bet
            pot.clear_bet()
            return 0

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
            player_busted = True
            dealer_busted = True
            if turn == 'player':
                for number in player_hand.eval():
                    if number < 21:
                        player_busted = False
                    elif number == 21:
                        return 'blackjack'

                if player_busted:
                    pot.clear_bet()
                    pot.clear_pot()
                    return ' Player BUSTED!'
                return 0
            else:  # Dealer's Turn
                # check for blackjack
                if 21 in player_hand.eval():
                    if 21 in dealer_hand.eval():
                        pot.clear_bet()
                        return ' PUSH!'
                    else:
                        if turn != 'intermediar':
                            stack.add(pot.pot + pot.bet * 2)
                            pot.clear_bet()
                            pot.clear_pot()
                            return ' BLACKJACK! Player wins.'

                for number in dealer_hand.eval():
                    if number < 21:
                        dealer_busted = False
                    elif number == 21:
                        pot.clear_bet()
                        pot.clear_pot()
                        return ' Dealer BLACKJACK! Dealer wins.'
                if turn != 'intermediar':
                    if dealer_busted:
                        stack.add(pot.pot + pot.bet)
                        pot.clear_bet()
                        pot.clear_pot()
                        return ' Dealer BUSTED!'

                if turn != 'intermediar':
                    player_list = [a for a in player_hand.eval() if a < 21]
                    dealer_list = [a for a in dealer_hand.eval() if a < 21]
                else:
                    player_list = [a for a in player_hand.eval() if a <= 21]
                    dealer_list = [a for a in dealer_hand.eval() if a <= 21]

                if not len(player_list):
                    pot.clear_bet()
                    pot.clear_pot()
                    return ' Player BUSTED!'

                if turn != 'intermediar':
                    if not len(dealer_list):
                        stack.add(pot.pot + pot.bet)
                        pot.clear_bet()
                        pot.clear_pot()
                        return ' Dealer BUSTED!'

                player_list.sort()
                dealer_list.sort()

                player_best = player_list.pop()
                dealer_best = dealer_list.pop()

                if player_best < dealer_best:
                    pot.clear_bet()
                    pot.clear_pot()
                    return ' Dealer wins!'
                elif player_best > dealer_best:
                    if turn != 'intermediar':
                        stack.add(pot.pot + pot.bet)
                        pot.clear_bet()
                        pot.clear_pot()
                        return ' Player wins!'
                else:
                    pot.clear_bet()
                    return ' PUSH!'

        # ======================================================================================
        #  PLAY GAME
        # ======================================================================================
        def play():
            while True:
                redraw_screen()

                # cere betul initial
                while True:
                    try:
                        bet = 0
                        while place_bet(bet):
                            redraw_screen()
                            bet = int(prompt('Place your bet!'))
                        break
                    except ValueError:
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

                # Decision
                choices = ['d', 's']
                choice = ''
                msg = 'Double Down?/Surrender? (d/s)'
                if len(dealer_hand.eval()) > 1 and 21 in player_hand.eval():
                    choices = ['y', 'n']
                    msg = 'Even Money? yes/no (y/n)'
                while choice not in choices:
                    choice = prompt(msg)
                    redraw_screen()
                # Double Down
                if choice == 'd':
                    while double_down():
                        choice = prompt(msg)
                        redraw_screen()
                    redraw_screen()
                    winner = check_winner('player')
                    if winner:
                        if winner != 'blackjack':
                            print(winner)
                            prompt('Press Enter to continue...')
                            return
                        else:
                            print(' BLAKJACK! Wait for the dealer to play...')
                            sleep(2)

                # Surrender
                if choice == 's':
                    surrender()
                    redraw_screen()
                    sleep(0.5)
                    return
                # Even Money
                if choice == 'y':
                    even_money()
                    redraw_screen()
                    sleep(0.5)
                    return

                # continue player's turn
                # verifica daca e blackjack servit
                while True:
                    if 21 in player_hand.eval():
                        break
                    p = prompt('Hit?/Stay? (h/s)')
                    if p == 'h':
                        play_hand()
                    redraw_screen()
                    winner = check_winner('player')
                    if winner:
                        if winner != 'blackjack':
                            print(winner)
                            prompt('Press Enter to continue...')
                            return
                        else:
                            print(' BLAKJACK! Wait for the dealer to play...')
                            sleep(2)
                    if p == 's':
                        break

                # dealer's turn
                i = 0
                dealer_hand.unhide()
                sleep(1)
                redraw_screen()
                winner = check_winner('intermediar')
                if winner:
                    print(winner)
                    prompt('Press Enter to continue...')
                    return
                if min(dealer_hand.eval()) <= 17:
                    while True:
                        i += 1
                        sleep(1)
                        play_hand('dealer')
                        redraw_screen()
                        if min(dealer_hand.eval()) > 17:
                            break
                        winner = check_winner('intermediar')
                        if winner:
                            print(winner)
                            prompt('Press Enter to continue...')
                            return

                winner = check_winner()
                if winner:
                    print(winner)
                    prompt('Press Enter to continue...')
                    return

        #  run play() & exit main_program
        return play()

    # run main_program & exit main_stack
    while stack.ammount:
        main_program()

    return


# ======================================================================================
#  MAIN ENTRY
# ======================================================================================
if __name__ == '__main__':
    while True:
        main_stack()
        resp = ''
        while resp not in ['y', 'n']:
            print(' You have lost all your money. Play again? (y = yes)')
            response = input(' >>')
            if response == 'y':
                break
            else:
                exit(0)
