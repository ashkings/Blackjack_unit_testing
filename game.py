import random


class Blackjack:
    number_of_players = 0
    number_of_decks = 0
    deck = []
    hand = []

    def __init__(self, number_of_players=0, number_of_decks=0):
        self.number_of_players = number_of_players
        self.number_of_decks = number_of_decks

    def create_deck(self, deck_count=1):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * (4 * deck_count)
        if len(self.deck) == 0:
            raise ValueError('Deck invalid.Restart the game')

'''
jack = Blackjack(random.randint(0, 9), random.randint(0, 9))
jack.create_deck(jack.number_of_decks)
'''