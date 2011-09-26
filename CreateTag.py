#! /usr/bin/env python
# -*- coding: utf-8 -*-

import MeCab
import re
import random
import hashlib
from PIL import Image, ImageDraw, ImageFont

class ChangeStr():
    def __init__(self):
        u""" 文字列をユニコード型に変換 """
        pass

    def guess_charset(self, data) :
        u""" 文字コードを判別 """
        func = lambda d, enc: d.decode(enc) and enc

        try: return func(data, 'utf-8')
        except: pass
        try: return func(data, 'shift-jis')
        except: pass
        try: return func(data, 'euc-jp')
        except: pass
        try: return func(data, 'iso2022-jp')
        except: pass
        try: return func(data, 'ascii')
        except: pass
        return None

    def conv(self, data) :
        u""" 文字列をユニコード型に変換 """
        charset = self.guess_charset(data)
        try :
            deco = data.decode(charset)
            return deco.encode('utf-8')
        except: 
            deco = data
            return deco

class File_ope():
    def __init__(self, path, rfile, wfile):
        u""" 読込ファイルと書込みファイルを設定 """
        self.pth = path
        self.rfle = rfile
        self.wfle = wfile

        self.rpath = path + "\\" + rfile
        self.wpath = path + "\\Tag\\" + wfile
        print u"読込ファイル : ", self.rpath
        print u"書込みファイル : ", self.wpath

    def ropen(self):
        u""" 読込ファイルオープン """
        self.rf = open(self.rpath, 'r')

    def wopen(self):
        u""" 書込みファイルオープン """
        self.wf = open(self.wpath, 'w')

    def rclose(self):
        u""" 読込ファイルクローズ """
        self.rf.close()

    def wclose(self):
        u""" 書込みファイルクローズ """
        self.wf.close()

class Filter():
    def __init__(self):
        u""" 必要な文字を抽出 """
        self.p = re.compile('http:[a-zA-Z0-9./%_-]*')
        self.grplists = [u"助詞", u"助動詞", u"副詞", u"記号", u"接続詞", u"連体詞", u"接続詞",
                        u"動詞", u"形容詞", u"代名詞", u"接尾", u"非自立", u"数", u"人名", u"BOS"]
        self.rmchar()

    def resub(self, txt):
        u""" 空白を削除 """
        if self.p.search(txt) != None :
            return self.p.sub("", txt)
        return txt

    def rmchar(self):
        u""" 除去リスト作成 """
        rmlists = [" ", ".", ":", "-", "/", ",", "_", "=", "<<[", "|", "?", "!", "[","]", "*",
                u"「", u"」", "(",")"]
        char = u""""a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,
                    A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,
                    あ,い,う,え,お,か,き,く,け,こ,さ,し,す,せ,そ,た,ち,つ,て,と,
                    な,に,ぬ,ね,の,は,ひ,ふ,へ,ほ,ま,み,む,め,も,や,ゆ,よ,ら,り,
                    る,れ,ろ,わ,を,ん,人,
                """
        rmlists.extend(char.split(','))
        self.rmlists = rmlists

class Analyzer():
    def __init__(self):
        u""" 形態素解析 """
        self.dic = {}
        self.cdic = {}

    def analyze(self, phrase):
        u""" MeCab init """
        self.text = phrase
        self.mcb = MeCab.Tagger()
    
    def genToken(self):
        u""" 文字列分割 """
        self.ptn = self.mcb.parseToNode(self.text)

        while self.ptn != None :
            self.ptn = self.ptn.next
            yield self.ptn

        
class main():
    def __init__(self):
        self.path = "E:\PySave\Example"
        self.readfile = "create.txt"
        self.ritefile = "tag.txt"

        print "Start CreateTag !"
    
        self.f = open(self.path+'\\'+self.readfile).read()
        self.h = hashlib.new('md5')
        self.h.update(ChangeStr().conv(self.f))
        self.hexdgt = str(self.h.hexdigest())

        self.w = open(self.path+'\\Create\\'+self.hexdgt+'.txt', 'w')
        self.w.write(ChangeStr().conv(self.f))
        self.w.close()
        self.writefile = self.hexdgt+'.txt'

    def run(self):
        self.fope = File_ope(self.path, self.readfile, self.writefile)
        self.mathine = Analyzer()
        self.fil = Filter()
 
        self.fope.ropen()
        self.fope.wopen()

        for txt in self.fope.rf.readlines():
            txt = ChangeStr().conv(txt)
            phrase = self.fil.resub(txt) 
            if phrase == None:
                continue
            self.mathine.analyze(phrase)
            for gen in self.mathine.genToken():
                if gen == None :
                    continue
                feature = gen.feature
                surface = gen.surface
                lengths = max([feature.find(a) for a in self.fil.grplists])
                if surface in self.fil.rmlists :
                    continue
                if surface.isdigit():
                    continue
                if lengths == -1:
                    if not self.mathine.dic.has_key(surface):
                        self.mathine.dic[surface] = 1
                        self.mathine.cdic[surface] = feature
                    else :
                        self.mathine.dic[surface] += 1

        self.lists = [(x, y) for x, y in self.mathine.dic.items()]
        self.lists.sort(key=lambda x:x[1], reverse=True)

        one, two, three = self.lists[0][0], self.lists[1][0], self.lists[2][0]
        word = one+','+two+','+three+'\n'
        self.fope.wf.write('************************** KEYWORD **************************\n')
        self.fope.wf.write(word)
        self.fope.wf.write('*************************************************************\n')

        for x, y in self.lists:
            w = x+' : '+str(y)+'            '+self.mathine.cdic[x]+'\n'
            self.fope.wf.write(w)

        self.fope.wf.write('*************************************************************\n')
        self.fope.wf.write('median keyword color y_point med-y\n')


        img1 = Image.new('RGB', (650, 650), (0xff, 0xff, 0xff))
        draw = ImageDraw.Draw(img1)

        self.listset = list(set([y for x, y in self.lists]))
        if len(self.listset) % 2 == 0 :
            MED = self.listset[len(self.listset)/2] + self.listset[len(self.listset)/2+1] / 2
        else :
            MED = self.listset[len(self.listset)/2]
    
        for x, y in self.lists:
            x = x.decode('utf-8')
            yd = y % 10
            font = ImageFont.truetype("C:\WINDOWS\Fonts\meiryo.ttc", 5*yd)
            ix = random.randint(20, 500)
            iy = random.randint(20, 600)
            color = (0, 0, 0)
            ym = y - MED

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

            draw.text((ix, iy), x, fill=color, font=font)
            txt = str(MED) + ' ' + str(x) + ' ' + str(color) + ' ' + str(y) + ' ' + str(ym) + '\n'
            self.fope.wf.write(txt)
    
        self.fope.rf.close()
        self.fope.wf.close()
 
        print u"finish\n作成完了!"

        img1.save("e:\PySave\script-save\sample633a.jpg")
        img1.show()


# end ;

