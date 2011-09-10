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
        if isfloat(i) == False :
            print 'Miss value.'
            print 'Again Execute!\nSee you agein!'
            return
    a, b, c = [float(x) for x in v ]
    try :
        assert( c > abs(a-b) )
    except AssertionError, e :
        print e
        print "a : %f, b : %f, a-b : %d, %f : %f", (a, b, abs(a-b), c)
    if ( (a + b) > c ) :
        s = ( a + b + c ) / 2
        ans = sqrt(s*(s - a)*(s - b)*(s - c))
        print "Ans :", ans
    else :
        print "Please Again exec"

     
if __name__ == '__main__' :
    from math import sqrt
    print 'Enter three number :',
    val = raw_input()
    calc(val)

