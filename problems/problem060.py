# coding: utf-8

import math_ext


def is_prime_pair(p1, p2):
    p3 = int(str(p1) + str(p2))
    p4 = int(str(p2) + str(p1))
    return math_ext.is_prime(p3) and math_ext.is_prime(p4)


def is_prime_pair_set(new_p, prime_pair_set):
    for p in prime_pair_set:
        if not is_prime_pair(new_p, p):
            return False
    return True


def solve():
    prime_pair_sets = []
    for new_p in math_ext.primes():
        for prime_pair_set in prime_pair_sets:
            if is_prime_pair_set(new_p, prime_pair_set):
                new_prime_pair_set = (new_p,) + prime_pair_set
                if len(new_prime_pair_set) == 5:
                    return sum(new_prime_pair_set)
                prime_pair_sets.append(new_prime_pair_set)
        prime_pair_sets.append((new_p,))
