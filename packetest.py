#! /usr/bin/env python
# -*- coding: utf-8 -*-

import dpkt, pcap

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
  
