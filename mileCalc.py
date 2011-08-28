#! /usr/bin/env python
# -*- coding: utf-8 -*-

def calc(rang):
    val = rang.split()
    if len(val) != 2 :
        print 'Again Execute!\nSee you agein!'
        return
    for i in val :
        if i.isdigit() == False :
            print 'Again Execute!\nSee you agein!'
            return
    mile = int(val[0])
    yard = int(val[1])
    km = ( mile + yard / 1760.0 ) * 1.0693
    print 'mile %d, yard %f -> %f' % (mile, yard, km) 
 
if __name__ == '__main__' :
    print 'Enter value : ',
    rang = raw_input()
    calc(rang)


