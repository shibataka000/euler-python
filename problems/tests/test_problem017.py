# coding: utf-8

import problems.problem017 as problem


def test_get_word():
    assert problem.get_word(1) == "one"
    assert problem.get_word(20) == "twenty"
    assert problem.get_word(21) == "twenty-one"
    assert problem.get_word(30) == "thirty"
    assert problem.get_word(31) == "thirty-one"
    assert problem.get_word(99) == "ninety-nine"
    assert problem.get_word(100) == "one hundred"
    assert problem.get_word(101) == "one hundred and one"
    assert problem.get_word(121) == "one hundred and twenty-one"
    assert problem.get_word(200) == "two hundred"
    assert problem.get_word(999) == "nine hundred and ninety-nine"
    assert problem.get_word(1000) == "one thousand"


def test_solve():
    assert problem.solve() == 21124
