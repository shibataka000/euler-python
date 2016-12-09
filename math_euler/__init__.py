# coding: utf-8


def fibonacci():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b


def primes():
    def mark_sieve(prime, sieve):
        i, l = 2 * prime, len(sieve)
        while i < l:
            sieve[i] = False
            i += prime

    yield 2
    primes = [2]
    sieve = [True]
    i = 3
    while True:
        if i >= len(sieve):
            sieve = [True] * (10 * len(sieve))
            for p in primes:
                mark_sieve(p, sieve)
        if sieve[i]:
            primes.append(i)
            mark_sieve(i, sieve)
            yield i
        i += 2
        

def prime_decompose(x):
    if x == 1:
        return [1]
    factors = []
    for p in primes():
        if p > x:
            break
        while x % p == 0:
            factors.append(p)
            x /= p
    return factors


def gcd(a, b):
    if b > a:
        return gcd(b, a)
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return int(a * b / gcd(a, b))
