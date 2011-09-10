#! /usr/bin/env python
# -*- coding: utf-8 -*-

def mydecorator(function):
    def _mydecorator(*args, **kw):
        #実際の関数を呼び出す前に行う処理
        res = function(*args, **kw)
        #呼び出し後に行う処理
        return res
    #内部で作成したサブ関数を返す
    return _mydecorator


