import unittest
from deck import Table, get_deck
from player import Player


class TestBlackjack(unittest.TestCase):
    def test_number_of_decks_not_empty(self):
        jack = Table()
        self.assertRaises(ValueError, lambda: get_deck(0))

    def test_number_of_players_not_zero(self):
        jack = Player()
        table = Table()
        deck = get_deck(1)
        self.assertRaises(ValueError, lambda: jack.hand_for_each_player(0, deck))

    def test_number_of_players_do_not_exceed_eight_the_max_limit(self):
        jack = Player()
        table = Table()
        deck = get_deck(1)
        self.assertRaises(ValueError, lambda: jack.hand_for_each_player(10, deck))

    def test_number_of_decks_do_not_exceed_eight_the_max_limit(self):
        jack = Table()
        self.assertRaises(ValueError, lambda: get_deck(9))

    def test_get_initial_cards_give_only_2_set_of_cards(self):
        table = Table()
        deck = get_deck(1)
        cards = table.get_initial_cards(deck)
        self.assertEqual(len(cards), 2)

    def test_get_deck_creates_a_deck_successfully(self):
        table = Table()
        deck = get_deck()
        self.assertEqual(deck,
                         ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                          'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                          'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                          'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
                         )

    def test_hand_for_each_player_gives_cards_list_equal_to_number_of_players(self):
        table = Table()
        deck = get_deck()
        player = Player()
        players_cards = player.hand_for_each_player(7, deck)
        self.assertEqual(len(players_cards), 7)


if __name__ == '__main__':
    unittest.main()
