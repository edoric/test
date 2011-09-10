#! /usr/bin/env python
# -*- coding: utf-8 -*-

f = open('./test.txt', 'w')
f.write('TEST\n')
import MeCab
m = MeCab.Tagger('-Ochasen')
f.write(m.parse('今日もしないとね'))
n = m.parseToNode('今日もしないとね')
n = n.next
f.write('\n')
while n :
    f.write(n.surface)
    f.write('\n')
    f.write(n.feature)
    f.write('\n')
    n = n.next

f.close()
