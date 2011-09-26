#! /usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as Tk
import tkFileDialog as Fd
import ScrolledText as St
import sys, os
import CreateTag

class App(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title('Text Viewer')
        self.master.option_add('*font', ('FixedSys', 14))
        self.init()

    def init(self):
        self.button1 = Tk.Button(self.master, text = 'Delete',
                            command=self.text_delete)
        self.button2 = Tk.Button(self.master, text = u'解析',
                            command=self.createtag)

        self.button1.grid(row=1, column=0, sticky='e')
        self.button2.grid(row=1, column=0, sticky='n')

        self.t0 = St.ScrolledText()
        self.t0.grid(row=3,column=0, sticky='n')
        self.create_menu()

    def create_menu(self):
        self.num_flag = Tk.BooleanVar()
        self.num_flag.set(True)

        self.m0 = Tk.Menu(self.master)
        self.master.configure(menu = self.m0)

        self.m1 = Tk.Menu(self.m0, tearoff = 0 )
        self.m1.add_command(label='Open', under=0, command=self.load_file)
        self.m1.add_separator
        self.m1.add_command(label='Exit', under=0, command=sys.exit)
        self.m0.add_cascade(label='File', under=0, menu=self.m1)

    def load_file(self):
        path_name = "e:\PySave\script-save"
        filename = Fd.askopenfilename(filetypes = [('Text Files', ('.txt'))],
                                    initialdir = path_name)

        if filename != "":
            path_name = os.path.dirname(filename)
            fi = open(filename)
            self.t0.delete('1.0', 'end')
            for x in fi :
                self.t0.insert('end', x.decode('utf-8'))
            fi.close()
            if self.num_flag.get() :
                self.change_number()
            self.t0.focus_set()

    def change_number(self):
        line = int(float(self.t0.index('end')))
        if self.num_flag.get():
            for x in range(1, line):
                self.t0.insert('%d.0' % x, '%6d:' % x)
        else :
            for x in range(1, line):
                self.t0.delete('%d.0' % x, '%d.7' % x)

    def text_delete(self):
        self.t0.delete('1.0', 'end')

    def createtag(self):
        crtag = CreateTag.main()
        crtag.run()


if __name__ == '__main__':
    app = App()
    app.mainloop()

"""
root = Tk.Tk() #トップレベルのウィンドウ(メインウィンドウ)を作成

#ウィジェットを設定してウィンドウを配置
button = Tk.Button(root, text = 'Python')
button.pack()

#文字や数をを入力 Variableクラスを使う
buff = Tk.StringVar()
buff.set("")

#ラベル作成
label = Tk.Label(root, textvariable = buff)
label.pack()

#イベントループを開始してユーザーからの要求(イベント)を処理
root.mainloop()
"""
