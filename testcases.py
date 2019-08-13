import unittest
from deck import Table
from player import Player


class TestBlackjack(unittest.TestCase):
    def test_number_of_decks_not_empty(self):
        jack = Table()
        self.assertRaises(ValueError, lambda: jack.get_deck(0))

    def test_number_of_players_not_zero(self):
        jack = Player()
        table = Table()
        deck = table.get_deck(1)
        self.assertRaises(ValueError, lambda: jack.hand_for_each_player(0, deck))


if __name__ == '__main__':
    unittest.main()