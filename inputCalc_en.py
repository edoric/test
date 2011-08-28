#! /usr/bin/env python
# -*- coding: utf-8 -*-

def isfloat(flt):
    idx = flt.index('.')
    if flt[idx-1].isdigit() and flt[idx+1] :
        return True
    else :
        return False

def calc(a, b):
    print "%f + %f = %f" % (a,b, a+b)
    print "%f - %f = %f" % (a,b, a-b)
    print "%f * %f = %f" % (a,b, a*b)
    print "%f / %f = %f" % (a,b, a/b)

def inputcalc():
    while True :
        val = raw_input()
        print 'value : ', val
        v = val.split()
        if len(v) == 0 :
            print 'Again Execution !\n See you agein!'
            return 
        for ch in v :
            if ch.isdigit() == False and isfloat(ch) == False:
                print 'Again Execution !\n See you agein!'
                return 
        if val.find(" ") != -1:
            a, b = val.split()
            calc(float(a), float(b))
        else :
            print 'Enter value : ',
            a = float(val)
            b = raw_input()
            calc(float(a), float(b))
        print "Again Enter value ",

if __name__ == '__main__' :
    print 'Enter value :',
    inputcalc()

