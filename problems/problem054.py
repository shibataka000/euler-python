# coding: utf-8

import enum
from functools import reduce


class Rank(enum.IntEnum):
    high_card = 1
    one_pair = 2
    two_pairs = 3
    three_of_a_kind = 4
    straight = 5
    flush = 6
    full_house = 7
    four_of_a_kind = 8
    straight_flush = 9
    royal_flush = 10


class Suit(enum.Enum):
    spade = 1
    heart = 2
    diamond = 3
    club = 4


class Card():
    str_to_number = {
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9,
        "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
    }
    str_to_suit = {
        "S": Suit.spade,
        "H": Suit.heart,
        "D": Suit.diamond,
        "C": Suit.club
    }

    def __init__(self, str_card):
        self.str_card = str_card
        self.number = self.str_to_number[str_card[0]]
        self.suit = self.str_to_suit[str_card[1]]


def get_numbers(cards):
    return sorted([c.number for c in cards])


def is_one_pair(cards):
    numbers = get_numbers(cards)
    return sorted([numbers.count(n) for n in numbers]) == [1, 1, 1, 2, 2]


def is_two_pairs(cards):
    numbers = get_numbers(cards)
    return sorted([numbers.count(n) for n in numbers]) == [1, 2, 2, 2, 2]


def is_three_of_a_kind(cards):
    numbers = get_numbers(cards)
    return sorted([numbers.count(n) for n in numbers]) == [1, 1, 3, 3, 3]


def is_straight(cards):
    numbers = get_numbers(cards)
    n = numbers[0]
    return numbers == list(range(n, n + 5))


def is_flush(cards):
    r = reduce(lambda a, b: a if a == b else None, [c.suit for c in cards])
    return r is not None


def is_full_house(cards):
    numbers = get_numbers(cards)
    return sorted([numbers.count(n) for n in numbers]) == [2, 2, 3, 3, 3]


def is_four_of_a_kind(cards):
    numbers = get_numbers(cards)
    return sorted([numbers.count(n) for n in numbers]) == [1, 4, 4, 4, 4]


def is_straight_flush(cards):
    return is_straight(cards) and is_flush(cards)


def is_royal_flush(cards):
    return is_flush(cards) and get_numbers(cards) == [10, 11, 12, 13, 14]


def get_rank(cards):
    if is_royal_flush(cards):
        return Rank.royal_flush
    elif is_straight_flush(cards):
        return Rank.straight_flush
    elif is_four_of_a_kind(cards):
        return Rank.four_of_a_kind
    elif is_full_house(cards):
        return Rank.full_house
    elif is_flush(cards):
        return Rank.flush
    elif is_straight(cards):
        return Rank.straight
    elif is_three_of_a_kind(cards):
        return Rank.three_of_a_kind
    elif is_two_pairs(cards):
        return Rank.two_pairs
    elif is_one_pair(cards):
        return Rank.one_pair
    else:
        return Rank.high_card


def get_max_number_in_rank_card(cards):
    rank = get_rank(cards)
    numbers = get_numbers(cards)
    assert rank != Rank.high_card
    if rank in [Rank.one_pair, Rank.two_pairs, Rank.three_of_a_kind,
                Rank.four_of_a_kind]:
        return max([n for n in numbers if numbers.count(n) >= 2])
    elif rank == Rank.full_house:
        return max([n for n in numbers if numbers.count(n) >= 3])
    else:
        return max(numbers)


def player1_win(player1, player2):
    rank1 = get_rank(player1)
    rank2 = get_rank(player2)
    if rank1 != rank2:
        return rank1 > rank2
    else:
        if rank1 != Rank.high_card:
            max_number1 = get_max_number_in_rank_card(player1)
            max_number2 = get_max_number_in_rank_card(player2)
            if max_number1 != max_number2:
                return max_number1 > max_number2
        numbers1 = sorted(get_numbers(player1), reverse=True)
        numbers2 = sorted(get_numbers(player2), reverse=True)
        assert numbers1 != numbers2
        return numbers1 > numbers2


def read_data():
    all_cards = []
    with open("./problems/datas/problem054/poker.txt") as f:
        for row in f:
            cards = [Card(str_card) for str_card in row.split(" ")]
            player1, player2 = cards[:5], cards[5:]
            assert len(player1) == len(player2) == 5
            all_cards.append((player1, player2))
    return all_cards


def solve():
    all_cards = read_data()
    return len([(player1, player2) for (player1, player2) in all_cards
                if player1_win(player1, player2)])
