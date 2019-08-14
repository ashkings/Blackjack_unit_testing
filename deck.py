import random


def get_deck(deck_count=1):
    if not deck_count:
        raise ValueError('Deck cannot be empty.')

    elif deck_count > 8:
        raise ValueError('Number of decks cannot be more than 8.')

    else:
        deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4 * deck_count
        return deck


class Table:
    def __init__(self):
        self.hand = []

    def get_initial_cards(self, deck):
        for item in range(2):
            random.shuffle(deck)
            new_card = deck.pop()
            self.hand.append(new_card)
        copy_hand = self.hand
        self.hand = []
        return copy_hand
