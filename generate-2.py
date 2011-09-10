#! /usr/bin/env pyton
# -*- coding: utf-8 -*-

def psychologist():
    print 'Please tell me your problems'
    while True:
        answer = yield
        if answer is not None:
            if answer.endswith('?'):
                print "Dont't ask yourself too much questions"
            elif 'good' in answer :
                print "A that's good, go on"
            elif 'bad' in answer :
                print "Don't be so negative"

free = psychologist()
free.next()
free.send('I feel bad')
free.send("Why I shouldn't ?")
free.send("ok then i should find what is good for me")
free.send("")
free.next()

