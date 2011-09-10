#! /usr/bin/env python
# -*- coding: utf-8 -*-

def calc(val):
    v = int(val)
    if v < 20 :
        price = 800
    else :
        price = 750
    sm = v * price
    print 'summary : ', sm

if __name__ == '__main__' :
    print 'Enter number : ',
    val = raw_input()
    calc(val)


