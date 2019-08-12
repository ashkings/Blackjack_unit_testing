import unittest
from game import Blackjack


class TestBlackjack(unittest.TestCase):
    def test_number_of_decks_not_empty(self):
        jack = Blackjack(7, 0)
        self.assertRaises(ValueError, lambda: jack.create_deck(jack.number_of_decks))


if __name__ == '__main__':
    unittest.main()
