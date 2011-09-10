#! /usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

def starting_at_five():
    value = raw_input().strip()
    while value != "" :
        for el in itertools.islice(value.split(), 4, None) :
            yield el
        value = raw_input().strip()
        

iter = starting_at_five()
while True :
    print iter.next()

