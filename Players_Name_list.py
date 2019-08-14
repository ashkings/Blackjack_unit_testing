class NameList:
    def __init__(self, player_count):
        self.number_of_players = player_count
        self.name_list = []

    def generate_player_list(self):
        self.name_list = [input('Enter player name: ', )
                          for player in range(self.number_of_players)]
