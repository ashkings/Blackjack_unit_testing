import random


class Table:
    hand = []

    def get_hand(self, deck):
        for item in range(2):
            random.shuffle(deck)
            new_card = deck.pop()
            self.hand.append(new_card)
        copy_hand = self.hand.copy()
        self.hand = []
        return copy_hand

    def get_deck(self, deck_count=1):
        if not deck_count:
            raise ValueError('Deck cannot be empty.')
        else:
            deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'k'] * 4 * deck_count
            return deck
