#! /usr/bin/env python
# -*- coding: utf-8 -*-

import MeCab

def guess_charset(data) :
    f = lambda d, enc: d.decode(enc) and enc

    try: return f(data, 'utf-8')
    except: pass
    try: return f(data, 'shift-jis')
    except: pass
    try: return f(data, 'euc-jp')
    except: pass
    try: return f(data, 'iso2022-jp')
    except: pass
    try: return f(data, 'ascii')
    except: pass
    return None

def conv(data) :
    charset = guess_charset(data)
    print charset
    try :
        u = data.decode(charset)
    except: 
        u = data
    return u.encode('utf-8')

sentence = raw_input()

t = MeCab.Tagger()
m = t.parseToNode(sentence)
m = m.next
while m:
    print m
    print m.surface, '\t', m.feature
    sur = conv(m.surface)
    fea = conv(m.feature)
    print sur, '\t', fea
    m = m.next
print "EOS"

