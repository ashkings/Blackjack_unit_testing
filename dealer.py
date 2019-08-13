from deck import Table


class Dealer(Table):
    dealer_name = 'abc'
    dealer_cards = []

    def __init__(self, deck):
        table = Table()
        self.dealer_name = input('Enter dealers name:')
        self.dealer_cards = table.get_hand(deck)

    def show_first_card(self):
        print('Dealers first card is:', end='')
        print(self.dealer_cards[0])
        return self.dealer_cards[0]

    def show_hole_card(self):
        print(self.dealer_cards[1])
        return self.dealer_cards[1]
