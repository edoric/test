#! /usr/bin/env python
# -*- coding: utf-8 -*-

def calc(a, b):
    print "%d + %d = %d" % (a,b, a+b)
    print "%d - %d = %d" % (a,b, a-b)
    print "%d * %d = %d" % (a,b, a*b)
    print "%d / %d = %d" % (a,b, a/b)

def inputcalc():
    while True :
        val = raw_input()
        print 'value : ', val
        v = val.split()
        if len(v) == 0 :
            print 'Again Execution !\n See you agein!'
            return 
        for ch in v :
            if ch.isdigit() == False :
                print 'Again Execution !\n See you agein!'
                return 
        if val.find(" ") != -1:
            a, b = val.split()
            calc(int(a), int(b))
        else :
            print 'Enter value : ',
            a = int(val)
            b = raw_input()
            calc(int(a), int(b))
        print "Again Enter value ",

if __name__ == '__main__' :
    print 'Enter value :',
    inputcalc()

