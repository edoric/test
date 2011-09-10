#! /usr/bin/env python
# -*- coding: utf-8 -*-

def calc(val):
    rang = int(val)
    if rang <= 2 :
        price = 650
    else :
        rang -= 2
        price = 650 + ( ( rang*1000 / 600 ) * 80 )
    print 'SUM : ', price


if __name__ == '__main__' :
    print 'Enter range : ',
    val = raw_input()
    calc(val)

