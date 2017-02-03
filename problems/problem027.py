# coding: utf-8

import itertools

import math_ext


def generate_primes(a, b):
    for n in itertools.count():
        yield n ** 2 + a * n + b


def get_prime_length(a, b):
    return len(list(itertools.takewhile(
        math_ext.is_prime,
        generate_primes(a, b)
    )))


def solve():
    max_elem = {"a": 1, "b": 41, "len": 40}
    for b in range(0, 1001):
        if abs(b) <= max_elem["len"] or not math_ext.is_prime(b):
            continue
        for a in range(-1000, 1001):
            if get_prime_length(a, b) > max_elem["len"]:
                max_elem = {"a": a, "b": b, "len": get_prime_length(a, b)}
    return max_elem["a"] * max_elem["b"]
