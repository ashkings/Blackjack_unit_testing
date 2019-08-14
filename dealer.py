from deck import Deck


class Dealer(Deck):
    dealer_cards = []

    def __init__(self, deck):
        dek = Deck()
        self.dealer_name = input('Enter dealers name:')
        self.dealer_cards = dek.get_initial_cards(deck)

    def show_initial_cards(self):
        print('Dealers cards are:[{}'.format(self.dealer_cards[0]) + ',hole_card]')

    def show_hole_card(self):
        print(self.dealer_cards[1])
