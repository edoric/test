#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
左右どちらから読んでも同じ値になる数を回文数という。 2桁の数の積で表される回文数のうち、最大のものは 9009 = 91 × 99 である。

では、3桁の数の積で表される回文数のうち最大のものはいくらになるか。

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import mtime

L = []
for i in range(0, 900):
    s = 100 + i
    for m in range(100, 1000):
        a = str(s * m)
        if a[0] == a[len(a)-1] and a[1] == a[len(a)-2] and a[2] == a[len(a)-3]:
            L.append(int(a))
            print s, m , a

print max(L)
