from itertools import product
import random

class Suit():
    '''Methods and attributes of a card suit or color'''

    def __init__(self, name, symbol=None, expanded=None):
        self.name = name 
        self.symbol = symbol if symbol else name[0]
        # self.expanded = expanded if expanded else f"{rank} of {suit}"
        

class Card():
    '''Methods and attributes of a single playing card'''

    def __init__(self, rank, suit=None):
        self.rank = rank
        self.suit = suit
        self.fullname = f'{self.rank} of {self.suit.name}'
        self.shortname = f'{self.rank[0]}{self.suit.symbol}'
        self.visible = True
    
    def __repr__(self):
        return self.fullname

    def display(self, full=False):
        ''' Display card suit & rank or conceal info if visibility off '''
        name = self.fullname if full else self.shortname 
        print(name if self.visible else '|?|')

class Deck():
    '''Methods and attributes of a deck of playing cards'''

    def __init__(self, cards):
        self.cards = cards
        self.talon = []
        self.discard = []
    
    def __repr__(self):
        return '\n'.join('{card.suit.name} {card.rank}'.format(card=card) for card in self.cards)
    
    def shuffle(self, pile=None):
        if pile is None: pile = self.cards
        return random.sample(pile, len(pile))

class StandardDeck(Deck):
    '''Instantiate a standard playing card deck'''

    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = [Suit('Diamonds','♦'), Suit('Clubs','♣'), Suit('Hearts','♥'), Suit('Spades','♠')]
        super().__init__(cards=[Card(rank, suit) for rank, suit in product(ranks, suits)])
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

class Player():
    '''Methods and attributes of a player of a card game'''

    def __init__(self, name, isDealer=False):
        self.name = name
        self.isDealer = isDealer

class Game():
    '''Base methods and attributes of general card games'''

    def __init__(self):
        self.players = []
        self.player_order = []
        self.current_player = 0

    def add_players(self, players, has_dealer=False):
        ''' Instantiate game players '''
        for player in players:
            self.players += Player(player)

    def assign_order(self):
        # for each player, randomly assign their positions
        # if there's a dealer role, assign the dealer and place their position last
        self.players = random.sample(self.players, len(self.players))

class War(Game):
    '''
    Play the game War using a standard deck.
    Rules: https://bicyclecards.com/how-to-play/war/
    '''

    def __init__(self):
        # super().__init__()
        # create 1 standard deck of cards
        self.deck = StandardDeck()

        # shuffle deck
        self.deck.talon = self.deck.shuffle()

        # instantiate 2 players with no dealer role and assign a play order
        super().add_players(players=['Player 1','Player 2'], has_dealer=False)
        super().assign_order()

        # deal whole deck evenly among them
        pass

    def play(self):
        # play 1 card each simultaneously
        # evaluate card ranks:
        #   if one card greater, add these cards to the bottom of this player's deck
        #   if ranks equal, start war
        pass

deck = StandardDeck()
# print(deck)