#! /usr/bin/env python
# -*- coding: utf-8 -*-

def add():
    a, b = 0, 1
    while True :
        a += b
        yield a

au = add()
print [ au.next() for x in range(10) ]

