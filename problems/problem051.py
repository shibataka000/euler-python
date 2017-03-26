# coding: utf-8

import math_ext


def get_replaced_primes(prime):
    def get_digit_replaced_primes(prime, n):
        str_prime, str_n = str(prime), str(n)
        rps = []
        if str_n not in str_prime:
            return [prime]
        for i in range(10):
            str_i = str(i)
            str_rp = str_prime.replace(str_n, str_i)
            rp = int(str_rp)
            if math_ext.is_prime(rp) and not str_rp.startswith("0"):
                rps.append(rp)
        return rps

    replaced_primes = [get_digit_replaced_primes(prime, i)
                       for i in range(10)]
    return max(replaced_primes, key=lambda x: len(x))


def solve():
    cache = []
    for p in math_ext.primes():
        if p in cache:
            continue
        replaced_primes = get_replaced_primes(p)
        cache += replaced_primes
        if len(replaced_primes) == 8:
            return p
