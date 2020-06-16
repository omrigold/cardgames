from itertools import product
import random

# class Suit():
#     '''Methods and attributes of a card suit or color'''

#     def __init__(self, name, abbrev=None, expanded=None):
#         self.name = name 
#         self.abbrev = abbrev if abbrev else name[0]
#         self.expanded = expanded if expanded else f"{rank} of {suit}"
        

class Card():
    '''Methods and attributes of a single playing card'''

    def __init__(self, rank, suit=None):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return '{self.suit} {self.rank}'.format(self=self)

class Deck():
    '''Methods and attributes of a deck of playing cards'''

    def __init__(self, cards):
        self.cards = cards
        self.talon = []
        self.discard = []
    
    def __str__(self):
        return '\n'.join('{card.suit} {card.rank}'.format(card=card) for card in self.cards)
    
    def shuffle(self, pile=None):
        shuffle_pile = pile if pile else self.cards
        self.talon = random.sample(shuffle_pile, len(shuffle_pile))
        print('\n'.join('{card.suit} {card.rank}'.format(card=card) for card in self.talon))

class StandardDeck(Deck):
    '''Instantiate a standard playing card deck'''

    def __init__(self):
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
        self.cards = [Card(rank, suit) for rank, suit in product(ranks, suits)]

class Player():
    '''Methods and attributes of a player of a card game'''

class Game():
    '''Base methods and attributes of general card games'''

deck = StandardDeck()
print(deck)