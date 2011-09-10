#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
13195 の素因数は 5、7、13、29 である。

600851475143 の素因数のうち最大のものを求めよ。

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import mtime

def prime(a, n):
    prm = []
    while n >= (a * a) :
        if n % a == 0:
            prm.append(a)
            n = n / a
        else :
            a += 1
    prm.append(n)
    return max(prm)

print prime(2, 600851475143)

