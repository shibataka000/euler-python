# coding: utf-8

import itertools

import math_ext


def get_circular_numbers(x):
    x_str = str(x)
    return [int(x_str[i:] + x_str[:i]) for i in range(len(x_str))]


def is_circular_prime(x):
    return all([math_ext.is_prime(y) for y in get_circular_numbers(x)])


def solve():
    primes = itertools.takewhile(lambda x: x < 1000000, math_ext.primes())
    circular_primes = []
    for p in primes:
        circular_numbers = get_circular_numbers(p)
        if any([n % 2 == 0 for n in circular_numbers]):
            continue
        if min(circular_numbers) < p:
            continue
        if is_circular_prime(p):
            circular_primes += get_circular_numbers(p)
    return len(circular_primes)
