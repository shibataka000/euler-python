# coding: utf-8

from fractions import Fraction
import itertools


def reciprocal(n):
    return Fraction(n.denominator, n.numerator)


def square_root_as_continued_fractions():
    f = Fraction(1, 2)
    while True:
        yield Fraction(1, 1) + f
        f = reciprocal(Fraction(2, 1) + f)


def digits(n):
    return len(str(n))


def solve():
    fractions = itertools.islice(square_root_as_continued_fractions(), 1000)
    return len([f for f in fractions
                if digits(f.numerator) > digits(f.denominator)])
