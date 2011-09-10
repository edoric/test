#! /usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import groupby

def compress(data):
    return ((len(list(group)),name ) for name, group in groupby(data))

def decompress(data):
    return (car * size for size, car in data)

print list(compress('get uuuuuuuuuuuuuuuuuuuuuuuuuup'))
compressed = compress('get uuuuuuuuuuuuuuuuuuuuuuuuuup') 

print ''.join(decompress(compressed))

f = "e:\PySave\script-save\echoserver.py"
com = list(compress((x for x in open(f).readlines() )))

print com

print "".join(decompress(com))


