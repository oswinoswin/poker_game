import argparse
from collections import Counter


class PokerGame:
    def __init__(self, first_hand, second_hand):
        self.first_hand = sort_cards(first_hand)
        self.second_hand = sort_cards(second_hand)

    def play(self):
        if self.first_hand == self.second_hand:
            return "It's a tie!"

        #check for better combination
        for i in range(min(len(self.first_hand), len(self.second_hand))):
            if self.first_hand[i][1] > self.second_hand[i][1]:
                return "First hand wins!"
            elif self.first_hand[i][1] < self.second_hand[i][1]:
                return "Second hand wins!"

        #combinations are the same, look at values
        self.first_by_value = rearrange_for_value_comparison(self.first_hand)
        self.second_by_value = rearrange_for_value_comparison(self.second_hand)

        for key in sorted(self.first_by_value.keys(), reverse=True):
            first_values_sorted = sorted(self.first_by_value[key], reverse=True)
            second_values_sorted = sorted(self.second_by_value[key], reverse=True)
            for i in range(min(len(first_values_sorted), len(second_values_sorted))):
                if first_values_sorted[i] > second_values_sorted[i]:
                    return "First hand wins!"
                if first_values_sorted[i] < second_values_sorted[i]:
                    return "Second hand wins!"


def rearrange_for_value_comparison(hand):
    rearranged = {}
    for val, amount in hand:
        if amount in rearranged.keys():
            rearranged[amount].append(val)
        else:
            rearranged[amount] = [val]
    return rearranged


def sort_cards(cards):
    cards_values = [map_letter_to_value(letter) for letter in cards]
    cards_counted = Counter(cards_values)
    return sorted(cards_counted.items(), key=lambda kv: kv[1], reverse=True)


def map_letter_to_value(card):
    cards_values = { "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    if card in cards_values.keys():
        return cards_values[card]
    else:
        return int(card)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("first_hand")
    parser.add_argument("second_hand")
    args = parser.parse_args()
    my_first_hand = args.first_hand
    my_second_hand = args.second_hand
    game = PokerGame(my_first_hand, my_second_hand)
    result = game.play()
    print(result)
