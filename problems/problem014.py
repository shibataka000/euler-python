# coding: utf-8

import math_ext


def collatz(n):
    yield n
    while n != 1:
        if math_ext.even(n):
            n = n / 2
        else:
            n = 3 * n + 1
        yield n


def get_collatz_len(n, collatz_len_dict):
    _len = 0
    for i in collatz(n):
        if i in collatz_len_dict:
            return collatz_len_dict[i] + _len
        else:
            _len += 1
    return _len


def solve():
    collatz_len_dict = {}
    for i in range(1, 1000000):
        _len = get_collatz_len(i, collatz_len_dict)
        collatz_len_dict[i] = _len
    return max(collatz_len_dict.items(), key=lambda x: x[1])[0]
