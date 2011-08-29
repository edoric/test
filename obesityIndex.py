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

def calc(rang):
    val = rang.split()
    if len(val) != 3 :
        print 'It is few Element!'
        print 'Again Execute!\nSee you agein!'
        return
    if val[0].isdigit() == False and isfloat(val[1]) == False :
        print 'height or weight miss value.'
        print 'Again Execute!\nSee you agein!'
        return
    if not val[2] in (1,2) :
        print 'Sex miss value.'
        print 'Again Execute!\nSee you agein!'
        return
    height = float(val[0])
    weight = float(val[1])
    sex = int(val[2])
    if sex == 1 :
        std_weight = ( height - 139 ) * 0.613 + 42.2
    elif sex == 2 :
        std_weight = ( height - 139 ) * 0.510 + 43.2
    obesity = ( weight - std_weight ) / std_weight * 100
    print 'Obesith Index : ', obesity

if __name__ == '__main__' :
    print 'Enter value height(cm) weight(km) Sex:men(1) or femail(2) ?'
    rang = raw_input()
    calc(rang)

