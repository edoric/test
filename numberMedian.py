#! /usr/bin/env python
# -*- coding: utf-8 -*-

def calc(val):
    v = val.split()
    if len(v) != 3 :
        print 'It is few Element!'
        print 'Again Execute!\nSee you agein!'
        return
    for i in v :
        if i.isdigit() == False :
            print 'Miss value.'
            print 'Again Execute!\nSee you agein!'
            return
    a, b, c = sorted([int(x) for x in v ])
    #表明(必ずこの箇所では成立すると証明する事)
    try :
        assert(a <= b)
    except AssertionError, e:
        print 'a = %d, b = %d' % (a, b)
        raise AssertionError(v) 
    print 'Median value : ', b

if __name__ == '__main__' :
    print 'Enter three number :',
    val = raw_input()
    calc(val)

