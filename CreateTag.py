#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import imp

if hasattr(sys,"setdefaultencoding"):
    sys.setdefaultencoding("utf-8")

def main_is_frozen():
    return (hasattr(sys, "frozen") or 
            hasattr(sys, "importers")
            or imp.is_frozen("__main__"))

def get_main_dir():
    if main_is_frozen():
        return os.path.abspath(os.path.dirname(sys.executable))
    return os.path.abspath(os.path.dirname(sys.argv[0]))



def guess_charset(data) :
    func = lambda d, enc: d.decode(enc) and enc

    try:
        return func(data, 'utf-8')
    except:
        pass
    try:
        return func(data, 'shift-jis')
    except:
        pass
    try:
        return func(data, 'euc-jp')
    except:
        pass
    try:
        return func(data, 'iso2022-jp')
    except:
        pass
    try:
        return func(data, 'ascii')
    except:
        pass
    return None

def conv(data) :
    charset = guess_charset(data)
#    print charset
    try :
        deco = data.decode(charset)
        return deco.encode('utf-8')
    except: 
        deco = data
        return deco

import MeCab
import re
import random
from PIL import Image, ImageDraw, ImageFont

PATH = "C:\Documents and Settings"
WNAME = "tag.txt"
RNAME = "create.txt"

WPATH = PATH + '\\' + WNAME
RPATH = PATH + '\\' + RNAME

print u"保存先 : ", WPATH
print u"読込ファイル : ", RPATH

M = MeCab.Tagger()
RF = open(RPATH, 'r')
WF = open(WPATH, 'w')
GRPLISTS = [u"助詞", u"助動詞", u"副詞", u"記号", u"接続詞", u"連体詞", u"接続詞",
        u"動詞", u"形容詞", u"代名詞", u"接尾", u"非自立", u"数", u"人名", u"BOS"]
RMCHAR = u""""
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,
A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,
あ,い,う,え,お,か,き,く,け,こ,
さ,し,す,せ,そ,た,ち,つ,て,と,
な,に,ぬ,ね,の,は,ひ,ふ,へ,ほ,
ま,み,む,め,も,や,ゆ,よ,ら,り,
る,れ,ろ,わ,を,ん,
人,
"""
chars = RMCHAR.split(',')
RMLISTS = [" ", ".", ":", "-", "/", ",", "_", "=", "<<[", "|", "?", "!", "[","]", "*",
        u"「", u"」", "(",")"]
RMLISTS.extend(chars)
DIC = {}
NDIC = {}
P = re.compile('http:[a-zA-Z0-9./%_-]*')

for txt in RF.readlines():
#    print 'PREV : ',txt
    txt = conv(txt)
    if P.search(txt) != None :
        txt = P.sub("", txt)
#        print 'AFTER : ',txt
    n = M.parseToNode(txt)
    n = n.next
    while n:
        lengths = max([n.feature.find(a) for a in GRPLISTS ])
        if n.surface in RMLISTS :
            n = n.next
            continue
        if n.surface.isdigit() :
            n = n.next
            continue
        if lengths == -1 :
            if not DIC.has_key(n.surface):
                DIC[n.surface] = 1
                NDIC[n.surface] = n.feature
            else :
                DIC[n.surface] += 1
        n = n.next

LISTS = [(x, y) for x, y in DIC.items()]
LISTS = sorted(LISTS, key=lambda x:x[1], reverse=True)
ONE, TWO, THREE = LISTS[0][0], LISTS[1][0], LISTS[2][0]
WF.write('************************** KEYWORD **************************\n')
WORD = ONE+','+TWO+','+THREE+'\n'
WF.write(WORD)
WF.write('*************************************************************\n')
for x, y in LISTS :
    WF.write(x)
    WF.write(' : ')
    WF.write(str(y))
    WF.write('            ')
    WF.write(NDIC[x])
    WF.write('\n')

WF.write('*************************************************************\n')
WF.write('median keyword color y_point med-y\n')
IMG1 = Image.new("RGB", (650, 650), (0xff, 0xff, 0xff))
DRAW = ImageDraw.Draw(IMG1)

LISTSET = list(set([y for x, y in LISTS]))
if len(LISTSET) % 2 == 0 :
    med = LISTSET[len(LISTSET)/2] +LISTSET[len(LISTSET)/2+1] / 2
else :
    med = LISTSET[len(LISTSET)/2]

for x, y in LISTS :
    x = x.decode('utf-8')
    yd = y % 10
    font = ImageFont.truetype("C:\WINDOWS\Fonts\meiryo.ttc", 5*yd)
    ix = random.randint(20, 500)
    iy = random.randint(20, 600)
    color = (0, 0, 0)
    ym = y - med

    if ym <= -10.0 :
        color = (204, 255, 255)
    if -10.0 < ym and ym < -5.0 :
        color = (204, 204, 204)
    if -5.0 <= ym and ym < 0 :
        color = (204, 153, 153)
    if 0 <= ym and ym < 5 :
        color = (204, 102, 102)
    if 5 <= ym and ym < 10 :
        color = (204, 51, 51)
    if 10 <= ym :
        color = (204, 0, 0)

    DRAW.text((ix, iy), x, fill=color, font=font)
    txt = str(med) + ' ' + str(x) + ' ' + str(color) + ' ' + str(y) + ' ' + str(ym) + '\n'
    WF.write(txt)

WF.close()
IMG1.save("e:\PySave\script-save\sample633a.jpg")
IMG1.show()

