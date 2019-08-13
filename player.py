from deck import Deck


class Player(Deck):
    players = {}

    def hand_for_each_player(self, player_count, deck):
        if not player_count:
            raise ValueError('Number of Player cant be ZERO(0)')
        else:
            for player in range(player_count):
                self.hand = []
                player_name = input('Enter player name : ', )
                self.players[player_name] = self.get_hand(deck)
        return self.players

    def hit_or_stand(self):
        return input('Press h or H to make a hit  s or S to make a stand: ', )
