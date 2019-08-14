from deck import Deck


def hit_or_stand():
    return input('Press h to make a hit  s to make a stand: ', ).lower()


class Player(Deck):
    def __init__(self):
        self.players_card = []

    def hand_for_each_player(self, player_count, deck):
        if not player_count:
            raise ValueError('Number of Player cant be ZERO(0)')

        elif player_count > 8:
            raise ValueError('No more than 8 players can play at a time.')

        else:
            dek = Deck()
            self.players_card = [dek.get_initial_cards(deck)
                                 for _ in range(player_count)]
        return self.players_card


class NameList:
    def __init__(self, player_count):
        self.number_of_players = player_count
        self.name_list = []

    def generate_player_list(self):
        self.name_list = [input('Enter player name: ', )
                          for player in range(self.number_of_players)]
