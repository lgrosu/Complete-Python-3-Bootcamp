"""
    BLACKJACK CLASS LIBRARY
"""

import random
from colorama import init, Fore, Style

# initializeaza colorama
init(autoreset=True)


# ======================================================================================
#
# ======================================================================================
class Card:
    suit_icon = {'H': u"\u2665", 'C': u"\u2663", 'S': u"\u2660", 'D': u"\u2666"}
    ranks = {'2': [2], '3': [3], '4': [4], '5': [5], '6': [6], '7': [7], '8': [8], '9': [9], '10': [10], 'A': [1, 11],
             'J': [10], 'Q': [10], 'K': [10]}

    # constructor
    def __init__(self, rank, suit):
        # cupa si caroul, cu rosu
        if suit == 'H' or suit == 'D':
            icon = Style.BRIGHT + Fore.RED + self.suit_icon[suit] + Style.RESET_ALL
        else:
            icon = Style.BRIGHT + self.suit_icon[suit] + Style.RESET_ALL

        self.info = {'rank': rank, 'suit': icon, 'value': self.ranks[rank]}

    # print card
    def __str__(self):
        return f"{self.info['rank']} {self.info['suit']}"


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


class Hand:
    # constructor
    def __init__(self):
        self.cards = []

    # adauga o carte in mana
    def add_card(self, carte):
        self.cards.append(carte)

    # numară la cât s-a ajuns. Întoarce o listă pentru a fi evaluată (așii pot fi 1 sau 11)
    def eval(self):
        hand_value = [0, 0]
        if self.cards:
            for carte in self.cards:
                hand_value[0] += carte.info['value'][0]
                if len(carte.info['value']) > 1:  # e As
                    hand_value[1] += carte.info['value'][1] - carte.info['value'][0]

        hand_value[1] += hand_value[0]
        return hand_value

    def __str__(self):
        return_string = ''
        for c in self.cards:
            return_string += f" {c.info['rank']} {c.info['suit']}  "  # @todo-Rosi => Preaty Print
        return return_string


my_deck = Deck()
my_deck.shuffle()
hand = Hand()

hand.add_card(my_deck.deal())
hand.add_card(my_deck.deal())
hand.add_card(my_deck.deal())

print(hand.eval())
print(hand)

# print(card.info)

# print(my_deck)
#
# print('' * 10)
# print('Carti in mana:\n')
# for i in range(5):
#     card = my_deck.deal()
#     print(card)
