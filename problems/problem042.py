# coding: utf-8

import math

import math_ext


def is_square_root_of_number(n):
    return int(math.sqrt(n)) ** 2 == n


def is_triangular_number(n):
    x = 1 + 8 * n
    return is_square_root_of_number(x) and math_ext.odd(x)


def word2num(word):
    return sum([ord(c) - ord("A") + 1 for c in word])


def solve():
    with open("./problems/datas/problem042/words.txt") as f:
        words = f.read()
    words = [word.strip("\"") for word in words.split(",")]
    return sum([1 for word in words if is_triangular_number(word2num(word))])
