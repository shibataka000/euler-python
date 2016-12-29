# coding: utf-8

import itertools
import itertools_ext


def test_find():
    assert itertools_ext.find(lambda x: x >= 10, itertools.count()) == 10
