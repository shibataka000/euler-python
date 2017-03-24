# coding: utf-8

import problems.problem042 as problem


def test_is_square_root_of_number():
    assert all([problem.is_square_root_of_number(n)
                for n in [1, 4, 9]])
    assert all([not problem.is_square_root_of_number(n)
                for n in [2, 3, 5, 6, 7, 8]])


def test_is_triangular_number():
    trianglar_number = [1, 2, 6, 10, 15, 21, 28, 36, 45]
    for i in range(46):
        if i in trianglar_number:
            assert problem.is_triangular_number(i)
        else:
            assert not problem.is_triangular_number(i)


def test_word2num():
    assert problem.word2num("SKY") == 55


def test_solve():
    assert problem.solve() == 162
