# coding: utf-8

import itertools


def solve():
    for i, v in enumerate(itertools.permutations(range(10))):
        if (i + 1) == 1000000:
            answer_str = "".join([str(n) for n in v])
            return int(answer_str)
