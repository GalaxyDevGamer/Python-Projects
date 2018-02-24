# -*- coding:utf-8 -*-
from Tkinter import *
import sys
import Dialog

root = Tk()
u = 'user1'
u2 = 'user2'
u3 = 'user3'
u4 = 'user4'

def MIP():
    b = open('id.dat', 'w')
    c = open('pw.dat', 'w')
    d = open('id2.dat', 'w')
    e = open('pw2.dat', 'w')
    f = open('id3.dat', 'w')
    g = open('pw3.dat', 'w')
    h = open('id4.dat', 'w')
    i = open('pw4.dat', 'w')
    b.write(u)
    d.write(u2)
    f.write(u3)
    h.write(u4)
    b.close
    d.close
    f.close
    h.close
    com()
def mip(event):
    b = open('id.dat', 'w')
    c = open('pw.dat', 'w')
    d = open('id2.dat', 'w')
    e = open('pw2.dat', 'w')
    f = open('id3.dat', 'w')
    g = open('pw3.dat', 'w')
    h = open('id4.dat', 'w')
    i = open('pw4.dat', 'w')
    b.write(u)
    d.write(u2)
    f.write(u3)
    h.write(u4)
    b.close
    d.close
    f.close
    h.close
    com()
def com():
    Dialog.Dialog(root, title = 'Finish', bitmap = 'info',
                  text = u'作成しました',
                  strings = ['OK'], default = 0)

Label(root, text = 'ID&PW Maker for Galaxy-OS Universe').pack()
Label(root, text = u'＊すでにIDとPWのファイルがあればこのツールは不要です。終了してください').pack()
Label(root, text = u'＊すでにファイルがある場合、実行すればID及びPW情報が初期化されます').pack()
b2 = Button(root, text = u'ID&PWファイル作成', command = MIP)
b2.pack()
b2.bind('<Return>', mip)
b2.focus_set()
b1 = Button(root, text = u'終了', command = sys.exit)
b1.pack()
b1.bind('<Return>', sys.exit)
b1.focus_set()

root.mainloop()
