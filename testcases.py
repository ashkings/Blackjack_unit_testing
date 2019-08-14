import unittest

from blackjack import blackjack, get_card_value, get_sum_of_cards
from player import Player

from deck import get_deck, Deck


class TestBlackjack(unittest.TestCase):
    def test_number_of_decks_not_empty(self):
        self.assertRaises(ValueError, lambda: get_deck(0))

    def test_number_of_players_not_zero(self):
        jack = Player()
        deck = get_deck(1)
        self.assertRaises(ValueError, lambda: jack.hand_for_each_player(0, deck))

    def test_number_of_players_do_not_exceed_eight_the_max_limit(self):
        jack = Player()
        deck = get_deck(1)
        self.assertRaises(ValueError, lambda: jack.hand_for_each_player(10, deck))

    def test_number_of_decks_do_not_exceed_eight_the_max_limit(self):
        self.assertRaises(ValueError, lambda: get_deck(9))

    def test_get_initial_cards_give_only_2_set_of_cards(self):
        dek = Deck()
        deck = get_deck(1)
        cards = dek.get_initial_cards(deck)
        self.assertEqual(len(cards), 2)

    def test_get_deck_creates_a_deck_successfully(self):
        deck = get_deck()
        self.assertEqual(deck,
                         ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                          'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                          'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
                          'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
                         )

    def test_hand_for_each_player_gives_cards_list_equal_to_number_of_players(self):
        deck = get_deck()
        player = Player()
        players_cards = player.hand_for_each_player(7, deck)
        self.assertEqual(len(players_cards), 7)

    def test_blacjack(self):
        jack = blackjack(['A', 'J'])
        self.assertEqual(jack, True)

    def test_card_value_returns_correct_value(self):
        card1 = get_card_value('A')
        card2 = get_card_value('J')
        card3 = get_card_value(2)
        self.assertEqual(card1, 11)
        self.assertEqual(card2, 10)
        self.assertEqual(card3, 2)

    def test_sum_of_cards(self):
        cards_sum = get_sum_of_cards(['A', 10])
        self.assertEqual(cards_sum, 21)


if __name__ == '__main__':
    unittest.main()
