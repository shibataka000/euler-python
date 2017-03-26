# coding: utf-8

import itertools

import math_ext


def slice_seq(seq, start, end):
    seq = itertools.dropwhile(lambda x: x < start, seq)
    seq = itertools.takewhile(lambda x: x < end, seq)
    return seq


def get_max_consecutive_prime_sum(threashold):
    primes = list(slice_seq(math_ext.primes(), 0, threashold))
    start, end = 0, 1
    for i in range(len(primes)):
        for j in range(i + end - start, len(primes)):
            p = sum(primes[i:j])
            if p >= threashold:
                break
            if math_ext.is_prime(p):
                start, end = i, j
    return sum(primes[start:end])


def solve():
    return get_max_consecutive_prime_sum(1000000)
