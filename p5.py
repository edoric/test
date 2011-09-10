#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

import mtime

def gcm(a, b):
    result = a
    k = 0
    n = b
    while k != 0 :
        k = result % n 
        result = n
        n = k
    return result 

def lcm(a, b):
    g = gcm(a, b)
    return a / gcm(a,b) * b 

def lcm_n(L):
    l = L[0]
    for i in range(1, len(L)):
        print l
        l = lcm(l, L[i])
    return l


t = mtime.mtime()
print lcm_n([x for x in range(1, 10)])
t.end()
t.tprint()

