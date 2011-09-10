#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
10未満の自然数のうち、3 もしくは 5 の倍数になっているものは 3, 5, 6, 9 の4つがあり、 これらの合計は 23 になる。

同じようにして、1,000 未満の 3 か 5 の倍数になっている数字の合計を求めよ。

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import mtime

def sum(lst):
    s = 0
    for i in lst:
        s += i
    return s

t = mtime.mtime()
print sum([x for x in range(0,1000) if x % 3 == 0 or x % 5 == 0 ])
t.end()
t.tprint()


def add():
    i = 0
    while True:
        if i % 3 == 0 or i % 5 == 0:
            yield i
        else :
            yield 0
        i += 1

s = 0
ad = add()
t = mtime.mtime()
for x in range(0,1000):
    s += ad.next()
print s
t.end()
t.tprint()


