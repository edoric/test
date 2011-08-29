#! /usr/bin/env python
# -*- coding: utf-8 -*-

def isfloat(flt):
    try :
        idx = flt.index('.')
        if flt[idx-1].isdigit() and flt[idx+1] :
            return True
        else :
            return False
    except :
        return False

def calc(val):
    v = val.split()
    if len(v) != 3 :
        print 'It is few Element!'
        print 'Again Execute!\nSee you agein!'
        return
    for i in v :
        if isdigit(i) == False :
            print 'Miss value.'
            print 'Again Execute!\nSee you agein!'
            return
     
 
if __name__ == '__main__' :
    print 'Enter three number :',
    val = raw_input()
    calc(val)

