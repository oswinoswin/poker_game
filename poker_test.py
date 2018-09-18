import unittest
from poker import PokerGame


class TestPokerGame(unittest.TestCase):
    def test_tie(self):
        with open("test_cases/tie", "r") as file:
            for line in file:
                line = line.strip().split(" ")
                first_hand = line[2]
                second_hand = line[3]
                game = PokerGame(first_hand, second_hand)
                self.assertEqual(game.play(), "It's a tie!")

    def test_first_wins(self):
        with open("test_cases/first_wins", "r") as file:
            for line in file:
                line = line.strip().split(" ")
                first_hand = line[2]
                second_hand = line[3]
                game = PokerGame(first_hand, second_hand)
                self.assertEqual(game.play(), "First hand wins!")

    def test_second_wins(self):
        with open("test_cases/second_wins", "r") as file:
            for line in file:
                line = line.strip().split(" ")
                first_hand = line[2]
                second_hand = line[3]
                game = PokerGame(first_hand, second_hand)
                self.assertEqual(game.play(), "Second hand wins!")


if __name__ == '__main__':
    unittest.main()
