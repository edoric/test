#! /usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

seq = range(10)
def with_head(iterable, headsize=1):
    a, b = itertools.tee(iterable)
    return list(itertools.islice(a, headsize)), b

print with_head(seq)
print with_head(seq, 4)

