#! /usr/bin/env python
# -*- coding: utf-8 -*-

def calc(rang):
    val = rang.split()
    if len(val) != 1 :
        print 'Again Execute!\nSee you agein!'
        return
    if val[0].isdigit() == False :
        print 'Again Execute!\nSee you agein!'
        return
    num = int(val[0])
    a = num % 7
    b = num % 5
    c = num % 3
    s = 15 * a + 21 * b + 70 * c
    print s % 105

if __name__ == '__main__' :
    print 'Enter value : ',
    rang = raw_input()
    calc(rang)

