#! /usr/bin/env python
# -*- coding: utf-8 -*-

class DistinctError(Exception):
    pass

class distinctdict(dict):
    def __setitem__(self, key, value):
        for existing_key, existing_value in self.items():
            if existing_value == value and existing_key != key:
                raise DistinctError("This value already exists for %r" % \
                                    existing_value)
            #super()については後で説明します
        super(distinctdict, self).__setitem__(key,value)

my = distinctdict()
my['key'] = 'value'
my['other_key'] = 'value'
my['other_key'] = 'value2'

my

