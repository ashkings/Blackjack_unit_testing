from deck import Table


class Player(Table):
    def __init__(self):
        self.players = {}

    def hand_for_each_player(self, player_count, deck):
        if not player_count:
            raise ValueError('Number of Player cant be ZERO(0)')
        else:
            for player in range(player_count):
                table = Table()
                player_name = input('Enter player name : ', )
                self.players[player_name] = table.get_hand(deck)
        return self.players

    def hit_or_stand(self):
        return input('Press h to make a hit  s to make a stand: ', )

    def show_cards(self):
        print(self.players)
