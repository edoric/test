#! /usr/bin/env python
# -*- coding: utf-8 -*-

import dpkt, pcap
import Tkinter as Tk
import random as R

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
#    print charset
    try :
        u = data.decode(charset)
        return u.encode('utf-8')
    except: 
        u = data
        return u

HOTAL_SIZE = 3
HOTAL_COLOR = 'yellow'
NIGHT_COLOR = 'midnightblue'

class Packmon():
    canvas = None

    def __init__(self, x, y) :
        self.id = Packmon.canvas.create_oval(x-HOTAL_SIZE, y-HOTAL_SIZE,
                x+HOTAL_SIZE, y+HOTAL_SIZE,
                fill=HOTAL_COLOR,width=0)


class Frame(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title(u'パケットモニター')
        self.master.geometry("+20+20")
        self.cvs = Tk.Canvas(self, width=500, height=500,
                relief=Tk.SUNKEN, borderwidth=2,
                bg=NIGHT_COLOR)
        self.cvs.pack(fill=Tk.BOTH, expand=1)

        Packmon.canvs = self.cvs

        self.main = [20, 240, 20, 20]
        self.sub = [(210, 30, 20, 20)]

        self.create_hotaru()
        pak = self.Packetmonitor()
        while True :
            try :
                s = pak.next()
                self.move_hotaru()
            except StopIteration :
                break


    def move_hotaru(self):
        color = 'green'
        x0, y0, x1, y1 = self.sub[0]
        self.rect1 = self.cvs.create_rectangle(x0, y0, x1, y1,fill=color,width=0)

        dx = abs(20-x0) / 10
        dy = abs(240-y0) / 10

        for i in range(10) :
            self.cvs.move(self.rect1,dx,dy)

    def create_hotaru(self):
        cnv = Tk.Canvas()
        color = 'red'
        x0, y0, x1, y1 = self.main
        self.rect = self.cvs.create_rectangle(x0, y0, x1, y1,fill=color, width=0)

        color = 'blue'
        x0, y0, x1, y1 = self.sub[0]
        self.rect = self.cvs.create_rectangle(x0, y0, x1, y1,fill=color, width=0)

    def Packetmonitor(self):
        pc = pcap.pcap(name="eth1", promisc=False)
        #pc.setfilter('tcp'||'icmp')
        for ts,pkt in pc:
            try :
                dpt = dpkt.ethernet.Ethernet(pkt)
                ip = dpt.data
                if not ip.__module__.endswith('ip') :
                    continue
                cp = ip.data
                print ip.__class__
                print cp.__class__
                pro = cp.__module__
                if pro.endswith('tcp') or pro.endswith('udp') :
                    print 'TCP or UDP'
                    tcp = ip.data
                    spt = tcp.sport
                    dpt = tcp.dport
                    print ip.len, spt, dpt
                    yield dpt
                if pro.endswith('icmp') :
                    print 'ICMP'
                    icmp = ip.data
                    print icmp
            except :
                wf = open('e:\PySave\ca3.txt', 'w')
                wf.write('FAILURE\nIP\n')
                wf.write(conv("".join(ip)))
                wf.write('\n')
                wf.close()
                continue
  
       
if __name__ == '__main__':
    f = Frame()
    f.pack(fill=Tk.BOTH, expand=1)
    f.mainloop()


