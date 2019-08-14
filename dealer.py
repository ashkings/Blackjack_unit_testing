from deck import Table


class Dealer(Table):
    dealer_cards = []

    def __init__(self, deck):
        table = Table()
        self.dealer_name = input('Enter dealers name:')
        self.dealer_cards = table.get_initial_cards(deck)

    def show_initial_cards(self):
        print('Dealers cards are:[', end='')
        print(self.dealer_cards[0], end='')
        print(',hole_card]')

    def show_hole_card(self):
        print(self.dealer_cards[1])
