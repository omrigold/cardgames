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
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
        self.cards = [Card(rank, suit) for rank, suit in product(ranks, suits)]
        self.rank_order = {
            '2': 0,
            '3': 1,
            '4': 2,
            '5': 3,
            '6': 4,
            '7': 5,
            '8': 6,
            '9': 7,
            '10': 8,
            'Jack': 9,
            'Queen': 10,
            'King': 11,
            'Ace': 12
        }
        spade = '♠'
        heart = '♥'
        diamond = '♦'
        club = '♣'

class Player():
    '''Methods and attributes of a player of a card game'''

    def __init__(self, isDealer=False):
        self.isDealer = isDealer

class Game():
    '''Base methods and attributes of general card games'''

    def create_players(self, player_count, has_dealer):
        # create number of players in player_count
        pass

    def assign_order(self):
        # for each player, randomly assign their positions
        # if there's a dealer role, assign the dealer and place their position last
        pass

class War():
    '''
    Play the game War using a standard deck.
    Rules: https://bicyclecards.com/how-to-play/war/
    '''

    def __init__(self):
        super().__init__(self)
        # create 1 standard deck of cards
        # shuffle deck
        # instantiate 2 players
        # deal whole deck evenly among them
        pass

    def play(self):
        # play 1 card each simultaneously
        # evaluate card ranks:
        #   if one card greater, add these cards to the bottom of this player's deck
        #   if ranks equal, start war

deck = StandardDeck()
print(deck)