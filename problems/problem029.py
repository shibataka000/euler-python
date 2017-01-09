# coding: utf-8


def solve():
    L = [a ** b
         for a in range(2, 101)
         for b in range(2, 101)]
    return len(set(L))
