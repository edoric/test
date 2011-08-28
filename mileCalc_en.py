#! /usr/bin/env python
# -*- coding: utf-8 -*-

def isfloat(flt):
    idx = flt.index('.')
    if flt[idx-1].isdigit() and flt[idx+1] :
        return True
    else :
        return False

def calc(rang):
    val = rang.split()
    if len(val) != 1 :
        print 'Again Execute!\nSee you agein!'
        return
    km = val[0]
    if isfloat(km) == False :
        print 'Again Execute!\nSee you agein!'
        return
    km = float(km)
    mile = km / 1.0693
    yard = km % 1.0693 * 1764
    print 'km %f -> mile %d, yard %f' % (km, mile, yard)
 
if __name__ == '__main__' :
    print 'Enter value : ',
    rang = raw_input()
    calc(rang)

