from deck import Table
from Players_Name_list import NameList


def hit_or_stand():
    return input('Press h to make a hit  s to make a stand: ', ).lower()


class Player(Table):
    def __init__(self):
        self.players_card = []

    def hand_for_each_player(self, player_count, deck):
        if not player_count:
            raise ValueError('Number of Player cant be ZERO(0)')

        elif player_count > 8:
            raise ValueError('No more than 8 players can play at a time.')

        else:
            table = Table()
            self.players_card = [table.get_initial_cards(deck)
                                 for player in range(player_count)]
        return self.players_card
