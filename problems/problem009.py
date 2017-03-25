# coding: utf-8


def is_pythagoras_number(a, b, c):
    [a, b, c] = sorted([a, b, c])
    return a ** 2 + b ** 2 == c ** 2


def solve():
    [(a, b, c)] = [(a, b, 1000 - a - b)
                   for a in range(1, 1001)
                   for b in range(a, 1001)
                   if 1000 - a - b > b and
                   is_pythagoras_number(a, b, 1000 - a - b)]
    return a * b * c
