"""
    BLACKJACK CLASS LIBRARY
"""

import random
from colorama import init, Fore, Style

# initializeaza colorama
init(autoreset=True)


# ======================================================================================
#   O carte
# ======================================================================================
class Card:
    suit_icon = {'H': u"\u2665", 'C': u"\u2663", 'S': u"\u2660", 'D': u"\u2666"}
    ranks = {'2': [2], '3': [3], '4': [4], '5': [5], '6': [6], '7': [7], '8': [8], '9': [9], '10': [10], 'A': [1, 11],
             'J': [10], 'Q': [10], 'K': [10]}

    # constructor
    def __init__(self, rank, suit, dummy=False):
        # cupa si caroul, cu rosu
        if suit == 'H' or suit == 'D':
            icon = Style.BRIGHT + Fore.RED + self.suit_icon[suit] + Style.RESET_ALL
        else:
            icon = Style.BRIGHT + self.suit_icon[suit] + Style.RESET_ALL
        if not dummy:
            self.info = {'rank': rank, 'suit': icon, 'value': self.ranks[rank]}
        else:
            self.info = {'rank': u"\U0001F0CF", 'suit': '', 'value': [0]}

    # print card
    def __str__(self):
        return f"{self.info['rank']} {self.info['suit']}"


# ======================================================================================
#  Pachetul de carti
# ======================================================================================
class Deck:
    suit = ['C', 'S', 'H', 'D']  # clubs, spades, hearts, diamonds
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # constructor
    def __init__(self):
        self.deck = []
        for c in self.cards:
            for s in self.suit:
                self.deck.append(Card(c, s))

    # amesteca pachetul
    def shuffle(self):
        random.shuffle(self.deck)

    # deal
    def deal(self):
        return self.deck.pop()

    # print deck
    def __str__(self):
        return_string = ''
        for crd in self.deck:
            return_string += f"{crd.info['rank']} {crd.info['suit']}\n"

        return return_string


# ======================================================================================
#   Carti in mana
# ======================================================================================
class Hand:
    # constructor
    def __init__(self):
        self.cards = []
        self.number_of_chars = 0

    # adauga o carte in mana
    def add_card(self, carte):
        self.cards.append(carte)

    # numară la cât s-a ajuns. Întoarce o listă cu valori unice pentru a fi evaluată (așii pot fi 1 sau 11)
    def eval(self):
        hand_value = [0]
        if self.cards:
            for carte in self.cards:
                for i in range(len(hand_value)):
                    hand_value[i] += carte.info['value'][0]
                if len(carte.info['value']) > 1:  # e As. Scot valoarea veche, o adaug pe cea noua si fac append
                    for i in range(len(hand_value)):
                        hand_value.append(hand_value[i] - carte.info['value'][0] + carte.info['value'][1])
        return_list = list(set(hand_value))  # trec lista prin set ca sa scot duplicatele
        return_list.sort()
        return return_list

        # print hand

    def __str__(self):
        return_string = ''
        i = 0
        for c in self.cards:
            return_string += f"{str(c.info['rank']).rjust(3)}{str(c.info['suit']).rjust(3)}"
            i += 1
        self.number_of_chars = 4 * i  # am nevoie de numarul asta la formatarea ecranului
        return return_string


class DealerHand(Hand):

    def __init__(self):
        Hand.__init__(self)
        self.hidden_card = ''

    def hide_card(self):
        self.hidden_card = self.cards.pop()
        self.cards.append(Card('A', 'C', True))

    def unhide(self):
        self.cards.pop()
        self.cards.append(self.hidden_card)
        self.hidden_card = ''


# ======================================================================================
#   Banca
# ======================================================================================
class Stack:
    # constructor
    def __init__(self, ammount):
        self.ammount = ammount

    # withdraw
    def withdraw(self, bet):
        if bet <= self.ammount:
            self.ammount -= bet
            return {'success': 1, 'balance': self.ammount}
        else:
            return {'success': 0, 'balance': self.ammount}

    # add to stack
    def add(self, bet):
        self.ammount += bet
        return {'success': 1, 'balance': self.ammount}

    # print stack
    def __str__(self):
        return str(self.ammount)


# ======================================================================================
#   Pot
# ======================================================================================
class Pot:
    # constructor
    def __init__(self):
        self.sum = 0

    # add to pot
    def add(self, suma):
        self.sum += suma

    # clear pot
    def clear(self):
        self.sum = 0

    # print
    def __str__(self):
        return str(self.sum)
