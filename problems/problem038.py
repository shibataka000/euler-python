# coding: utf-8


def is_pandigital_number(n):
    return {int(c) for c in str(n)} == {i for i in range(1, 10)}


def solve():
    for n in range(9876, 0, -1):
        L = list(str(n) + str(n * 2))
        i = 3
        while len(L) < 9:
            L += str(n * i)
            i += 1
        m = int("".join(L))
        if is_pandigital_number(m):
            return m
