from deck import Table


class Dealer(Table):
    dealer_name = ''
    dealer_cards = []

    def __init__(self, deck):
        self.dealer_name = input('Enter dealers name: ', )
        self.dealer_cards = self.get_hand(deck)
