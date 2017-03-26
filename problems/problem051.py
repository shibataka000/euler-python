# coding: utf-8

import math_ext


def get_replaced_numbers(number, src):
    str_number, str_src = str(number), str(src)
    replaced_numbers = []
    if str_src not in str_number:
        return [number]
    for i in range(10):
        str_replaced_number = str_number.replace(str_src, str(i))
        if str_replaced_number.startswith("0"):
            continue
        replaced_number = int(str_replaced_number)
        replaced_numbers.append(replaced_number)
    return replaced_numbers


def get_all_replaced_numbers(number):
    replaced_numbers = []
    for i in range(10):
        replaced_numbers += get_replaced_numbers(number, i)
    replaced_numbers = list(sorted(list(set(replaced_numbers))))
    return replaced_numbers


def has_number_of_primes(numbers, prime_count):
    threashold = len(numbers) - prime_count
    for n in numbers:
        if not math_ext.is_prime(n):
            threashold -= 1
        if threashold < 0:
            return False
    return True


def has_number_of_replaced_primes(prime, prime_count):
    for i in range(10):
        replaced_numbers = get_replaced_numbers(prime, i)
        if has_number_of_primes(replaced_numbers, prime_count):
            return True
    return False


def solve():
    for p in math_ext.primes():
        if has_number_of_replaced_primes(p, 8):
            return p
