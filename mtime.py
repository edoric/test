#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
class mtime(object) :
    def __init__(self):
        self.start = time.time()
        print 'start...'
    def end(self):
        self.end = time.time()
        print "...stop!"
    def tprint(self):
        self.process = self.end - self.start
        self.h = int(self.process / 3600)
        self.process -= self.h * 3600
        self.m = int(self.process / 60)
        self.process -= self.m * 60
        self.s = self.process

        print "time: %dh %dm %fs" % (self.h, self.m, self.s )


