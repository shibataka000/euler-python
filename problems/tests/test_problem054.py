# coding: utf-8

from problems.problem054 import Card, Suit, Rank
import problems.problem054 as problem


def test_cards():
    card = Card("AS")
    assert card.suit == Suit.spade and card.number == 14
    card = Card("2H")
    assert card.suit == Suit.heart and card.number == 2


def test_get_numbers():
    str_cards = ["AS", "2H", "JD", "QC", "KC"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_numbers(cards) == [2, 11, 12, 13, 14]


def test_is_one_pair():
    str_cards = ["AS", "2S", "3S", "4S", "5S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert not problem.is_one_pair(cards)
    str_cards = ["AS", "AS", "3S", "4S", "5S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.is_one_pair(cards)


def test_is_two_pairs():
    str_cards = ["AS", "AS", "3S", "4S", "5S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert not problem.is_two_pairs(cards)
    str_cards = ["AS", "AS", "3S", "3S", "5S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.is_two_pairs(cards)


def test_three_of_a_kind():
    str_cards = ["AS", "AS", "3S", "4S", "5S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert not problem.is_three_of_a_kind(cards)
    str_cards = ["AS", "AS", "AS", "4S", "5S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.is_three_of_a_kind(cards)


def test_straight():
    str_cards = ["2S", "3S", "4S", "5S", "6S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.is_straight(cards)


def test_is_flush():
    str_cards = ["AS", "2S", "3S", "4S", "5H"]
    cards = [Card(str_card) for str_card in str_cards]
    assert not problem.is_flush(cards)
    str_cards = ["AS", "2S", "3S", "4S", "5S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.is_flush(cards)


def test_full_house():
    str_cards = ["AS", "AS", "3S", "3S", "5S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert not problem.is_full_house(cards)
    str_cards = ["AS", "AS", "3S", "3S", "3S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.is_full_house(cards)


def test_four_of_a_kind():
    str_cards = ["AS", "AS", "AS", "4S", "3S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert not problem.is_four_of_a_kind(cards)
    str_cards = ["AS", "AS", "AS", "AS", "3S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.is_four_of_a_kind(cards)


def test_straight_flush():
    str_cards = ["2S", "3S", "4S", "5S", "7S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert not problem.is_straight_flush(cards)
    str_cards = ["2S", "3S", "4S", "5S", "7H"]
    cards = [Card(str_card) for str_card in str_cards]
    assert not problem.is_straight_flush(cards)
    str_cards = ["2S", "3S", "4S", "5S", "6S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.is_straight_flush(cards)


def test_royal_flush():
    str_cards = ["AS", "TS", "JS", "QS", "KH"]
    cards = [Card(str_card) for str_card in str_cards]
    assert not problem.is_royal_flush(cards)
    str_cards = ["AS", "TS", "JS", "QS", "9S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert not problem.is_royal_flush(cards)
    str_cards = ["AS", "TS", "JS", "QS", "KS"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.is_royal_flush(cards)


def test_get_rank():
    str_cards = ["AS", "AS", "3S", "4S", "5H"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_rank(cards) == Rank.one_pair
    str_cards = ["AS", "AS", "3S", "3S", "5H"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_rank(cards) == Rank.two_pairs
    str_cards = ["AS", "AS", "AS", "4S", "5H"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_rank(cards) == Rank.three_of_a_kind
    str_cards = ["2S", "3S", "4S", "5S", "6H"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_rank(cards) == Rank.straight
    str_cards = ["AS", "AS", "3S", "4S", "5S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_rank(cards) == Rank.flush
    str_cards = ["AS", "AS", "3S", "3S", "3S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_rank(cards) == Rank.full_house
    str_cards = ["AS", "AS", "AS", "AS", "5S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_rank(cards) == Rank.four_of_a_kind
    str_cards = ["2S", "3S", "4S", "5S", "6S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_rank(cards) == Rank.straight_flush
    str_cards = ["AS", "TS", "JS", "QS", "KS"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_rank(cards) == Rank.royal_flush
    str_cards = ["AS", "2S", "3S", "4S", "6H"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_rank(cards) == Rank.high_card


def test_get_max_number_in_rank_card():
    str_cards = ["2S", "3S", "4S", "5S", "3H"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_max_number_in_rank_card(cards) == 3
    str_cards = ["2S", "3S", "4S", "5S", "6S"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_max_number_in_rank_card(cards) == 6
    str_cards = ["3S", "3S", "2S", "2S", "2H"]
    cards = [Card(str_card) for str_card in str_cards]
    assert problem.get_max_number_in_rank_card(cards) == 2


def test_player1_win():
    str_player1 = ["5H", "5C", "6S", "7S", "KD"]
    str_player2 = ["2C", "3S", "8S", "8D", "TD"]
    player1 = [Card(str_card) for str_card in str_player1]
    player2 = [Card(str_card) for str_card in str_player2]
    assert problem.get_rank(player1) == Rank.one_pair
    assert problem.get_max_number_in_rank_card(player1) == 5
    assert problem.get_rank(player2) == Rank.one_pair
    assert problem.get_max_number_in_rank_card(player2) == 8
    assert not problem.player1_win(player1, player2)

    str_player1 = ["5D", "8C", "9S", "JS", "AC"]
    str_player2 = ["2C", "5C", "7D", "8S", "QH"]
    player1 = [Card(str_card) for str_card in str_player1]
    player2 = [Card(str_card) for str_card in str_player2]
    assert problem.get_rank(player1) == Rank.high_card
    assert problem.get_rank(player2) == Rank.high_card
    assert problem.player1_win(player1, player2)

    str_player1 = ["2D", "9C", "AS", "AH", "AC"]
    str_player2 = ["3D", "6D", "7D", "TD", "QD"]
    player1 = [Card(str_card) for str_card in str_player1]
    player2 = [Card(str_card) for str_card in str_player2]
    assert problem.get_rank(player1) == Rank.three_of_a_kind
    assert problem.get_max_number_in_rank_card(player1) == 14
    assert problem.get_rank(player2) == Rank.flush
    assert not problem.player1_win(player1, player2)

    str_player1 = ["4D", "6S", "9H", "QH", "QC"]
    str_player2 = ["3D", "6D", "7H", "QD", "QS"]
    player1 = [Card(str_card) for str_card in str_player1]
    player2 = [Card(str_card) for str_card in str_player2]
    assert problem.get_rank(player1) == Rank.one_pair
    assert problem.get_max_number_in_rank_card(player1) == 12
    assert problem.get_rank(player2) == Rank.one_pair
    assert problem.get_max_number_in_rank_card(player2) == 12
    assert problem.player1_win(player1, player2)

    str_player1 = ["2H", "2D", "4C", "4D", "4S"]
    str_player2 = ["3C", "3D", "3S", "9S", "9D"]
    player1 = [Card(str_card) for str_card in str_player1]
    player2 = [Card(str_card) for str_card in str_player2]
    assert problem.get_rank(player1) == Rank.full_house
    assert problem.get_max_number_in_rank_card(player1) == 4
    assert problem.get_rank(player2) == Rank.full_house
    assert problem.get_max_number_in_rank_card(player2) == 3
    assert problem.player1_win(player1, player2)


def test_solve():
    assert problem.solve() == 376
