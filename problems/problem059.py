# coding: utf-8

import itertools


def solve():
    with open("./problems/datas/problem059/cipher.txt") as f:
        cipher = f.read()
        cipher = [int(c) for c in cipher.split(",")]
    for key in itertools.product(range(ord("a"), ord("z") + 1), repeat=3):
        plain = [key[i % 3] ^ v for (i, v) in enumerate(cipher)]
        plain_msg = "".join([chr(m) for m in plain])
        if " Gospel " in plain_msg:
            return sum(plain)
