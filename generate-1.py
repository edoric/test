#! /usr/bin/env python
# -*- coding: utf8 -*-

import tokenize
reader = open('test.py').readline
tokens = tokenize.generate_tokens(reader)
print tokens.next()

