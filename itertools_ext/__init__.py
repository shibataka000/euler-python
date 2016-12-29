# coding: utf-8

import itertools


def find(func, seq):
    return next(itertools.dropwhile(lambda x: not func(x), seq))
