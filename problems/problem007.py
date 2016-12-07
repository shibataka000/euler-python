# coding: utf-8

import itertools

from math_euler import primes


def solve():
    index = 10001
    index_th_prime_iter = itertools.islice(primes(), index - 1, index)
    index_th_prime = list(index_th_prime_iter)[0]
    return index_th_prime
