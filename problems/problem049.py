# coding: utf-8

import itertools

import math_ext


def get_4_digit_primes():
    primes = math_ext.primes()
    primes = itertools.dropwhile(lambda n: n < 1000, primes)
    primes = itertools.takewhile(lambda n: n < 10000, primes)
    return primes


def filter_permutations(elem, seq):
    return filter(lambda x: sorted(str(elem)) == sorted(str(x)), seq)


def find_3_elem_arithmetic_sequence(seq):
    seq = sorted(seq)
    if len(seq) < 3:
        return None
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            seq_k = seq[j] + (seq[j] - seq[i])
            if seq_k in seq:
                return [seq[i], seq[j], seq_k]


def solve():
    primes = list(get_4_digit_primes())
    for p in primes:
        seq = filter_permutations(p, primes)
        seq = find_3_elem_arithmetic_sequence(seq)
        if seq and 1487 not in seq:
            return int("".join([str(n) for n in seq]))
