#! /usr/bin/env python
# -*- coding: utf-8 -*-

def calc(val):
    v = val.split()
    for i in v :
        if i.isdigit() == False :
            print 'Again Execute!\nSee you agein!'
            return
    v = int(val)
    print 1.57079631847*v - 0.64596371106*v**3 +0.07968967928*v**5\
            - 0.0046376557*v**7 + 0.00015148419*v**9

    #ホーナーの方法を使うとこれだけ短くなる。
    #この方法は出来るだけ式を単純化するというもの
    print ( ( ( ( 0.00015148419 * v**2 - 0.0046376557 ) * v**2 + 0.07968967928 ) * v**2 - 0.64596371106 ) * v**2 + 1.57079631847 ) * v

if __name__ == '__main__' :
    print 'Enter value : ',
    val = raw_input()
    calc(val)


