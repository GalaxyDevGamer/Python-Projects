# -*- coding:utf-8-*-

from Tkinter import *
from time import *
from tkFileDialog import *
import tkFileDialog
import Tkinter
import Dialog
import sys
import os
import sys, os.path


root = Tk()

path = '/home/desktop'

w1 = None
w2 = None
w3 = None
w4 = None

op1 = BooleanVar()
op1.set(False)
op2 = BooleanVar()
op2.set(False)
op3 = BooleanVar()
op3.set(False)
op4 = BooleanVar()
op4.set(False)
op5 = BooleanVar()
op5.set(False)
op6 = BooleanVar()
op6.set(False)
op7 = BooleanVar()
op7.set(False)
op8 = BooleanVar()
op8.set(False)
op9 = BooleanVar()
op9.set(False)
op10 = BooleanVar()
op10.set(False)
op11 = BooleanVar()
op11.set(False)
op12 = BooleanVar()
op12.set(False)
op13 = BooleanVar()
op13.set(False)
op14 = BooleanVar()
op14.set(False)
op15 = BooleanVar()
op15.set(False)
op16 = BooleanVar()
op16.set(False)
op17 = BooleanVar()
op17.set(False)
op18 = BooleanVar()
op18.set(False)
op19 = BooleanVar()
op19.set(False)
op20 = BooleanVar()
op20.set(False)
op21 = BooleanVar()
op21.set(False)
op22 = BooleanVar()
op22.set(False)
op23 = BooleanVar()
op23.set(False)
op24 = BooleanVar()
op24.set(False)
op25 = BooleanVar()
op25.set(False)
op26 = BooleanVar()
op26.set(False)
op27 = BooleanVar()
op27.set(False)
op28 = BooleanVar()
op28.set(False)
op29 = BooleanVar()
op29.set(False)
buf = StringVar()
buf.set('')
buff = StringVar()
buff.set('')
buffe = StringVar()
buffe.set('')
buffers = StringVar()
buffers.set('')
names = StringVar()
names.set('')
pw = StringVar()
pw.set('')
mail = StringVar()
mail.set('')
actname = StringVar()
actname.set('')
actpw = StringVar()
actpw.set('')
actpwc = StringVar()
actpwc.set('')
regent = StringVar()
regent.set('')
e0 = StringVar()
e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()
e5 = StringVar()
e6 = StringVar()
e7 = StringVar()
e8 = StringVar()
e9 = StringVar()
e10 = StringVar()
e10.set('0')
e11 = StringVar()
e11.set('0')
e12 = StringVar()
e12.set('0')
e13 = StringVar()
e13.set('0')
e14 = StringVar()
e14.set('0')
e15 = StringVar()
e15.set('0')
e16 = StringVar()
e16.set('0')
e17 = StringVar()
e17.set('0')
e18 = StringVar()
e18.set('0')
e19 = StringVar()
e19.set('0')
e20 = StringVar()
e20.set('0')
e21 = StringVar()
e21.set('0')
e22 = StringVar()
e22.set('0')
e23 = StringVar()
e23.set('0')
e24 = StringVar()
e24.set('0')
e25 = StringVar()
e25.set('0')
e26 = StringVar()
e26.set('0')
e27 = StringVar()
e27.set('0')
e28 = StringVar()
e28.set('0')
e29 = StringVar()
e29.set('0')
e30 = StringVar()
e30.set('0')
e31 = StringVar()
e31.set('0')
e32 = StringVar()
e32.set('0')
e33 = StringVar()
e33.set('0')
e34 = StringVar()
e34.set('0')
e35 = StringVar()
e35.set('0')
e36 = StringVar()
e36.set('0')
e37 = StringVar()
e37.set('0')
e38 = StringVar()
e38.set('0')
e39 = StringVar()
e39.set('0')
e40 = StringVar()
e40.set('0')
e41 = StringVar()
e41.set('0')
e42 = StringVar()
e42.set('0')
e43 = StringVar()
e43.set('0')
e44 = StringVar()
e44.set('0')
e45 = StringVar()
e45.set('0')
e46 = StringVar()
e46.set('0')
e47 = StringVar()
e47.set('0')
e48 = StringVar()
e48.set('0')
e49 = StringVar()
e49.set('0')
pm1 = StringVar()
pm1.set('0')
pm2 = StringVar()
pm3 = StringVar()
pm3.set('0')
pm4 = StringVar()
pm4.set('0')

ans = 0

osnam = 'Galaxy-OS Universe'
buttons = []

def sleep():
    global w3
    w3 = Toplevel()
    Label(w3, text = u'作業中でもスリープモード（ロック画面）に入ってしまうのでご注意ください').pack()
    Label(w3, text = u'設定はホームから一度ロック画面に戻らないと適用されません').pack()
    Label(w3, text = u'放置すると無限にウィンドウが増え続けます').pack()
    f = LabelFrame(w3)
    Checkbutton(f, text = u'1分', variable = op24, command = w3.destroy).pack()
    Checkbutton(f, text = u'3分', variable = op25, command = w3.destroy).pack()
    Checkbutton(f, text = u'5分', variable = op26, command = w3.destroy).pack()
    Checkbutton(f, text = u'10分', variable = op27, command = w3.destroy).pack()
    Checkbutton(f, text = u'30分', variable = op22, command = w3.destroy).pack()
    Checkbutton(f, text = u'60分', variable = op21, command = w3.destroy).pack()
    Checkbutton(f, text = u'90分', variable = op20, command = w3.destroy).pack()
    Checkbutton(f, text = u'120分', variable = op19, command = w3.destroy).pack()
    buttons.append(Checkbutton)
    f.pack(padx = 5, pady = 5)
    w2.destroy()
def set():
    global w2
    w2 = Toplevel()
    Button(w2, text = u'スリープモードをオンにする', command = sleep).pack()
if op29.get():
    Button.configure(state = new_state)
    Button.new_state = 'disabled'
def hide(n):
    return lambda : buttons[n].lower()
def rus(event):
    w1.destroy()
    op28.set(True)
    if op10.get():
        unlock()
    elif op11.get():
        unlock2()
    elif op12.get():
        unlock3()
    elif op13.get():
        unlock4()
def ru4():
    w1.destroy()
    unlock4()
    op28.set(True)
def ru3():
    w1.destroy()
    unlock3()
    op28.set(True)
def ru2():
    w1.destroy()
    unlock2()
    op28.set(True)
def ru():
    w1.destroy()
    unlock()
    op28.set(True)
def homesec4():
    if op19.get():
        root.after(12000000, ru4)
    if op20.get():
        root.after(900000, ru4)
    if op21.get():
        root.after(6000000, ru4)
    if op22.get():
        root.after(1800000, ru4)
    if op24.get():
        root.after(60000, ru4)
    if op25.get():
        root.after(180000, ru4)
    if op26.get():
        root.after(300000, ru4)
    if op27.get():
        root.after(600000, ru4)
def homesec3():
    if op19.get():
        root.after(12000000, ru3)
    if op20.get():
        root.after(900000, ru3)
    if op21.get():
        root.after(6000000, ru3)
    if op22.get():
        root.after(1800000, ru3)
    if op24.get():
        root.after(60000, ru3)
    if op25.get():
        root.after(180000, ru3)
    if op26.get():
        root.after(300000, ru3)
    if op27.get():
        root.after(600000, ru3)
def homesec2():
    if op19.get():
        root.after(12000000, ru2)
    if op20.get():
        root.after(900000, ru2)
    if op21.get():
        root.after(6000000, ru2)
    if op22.get():
        root.after(1800000, ru2)
    if op24.get():
        root.after(60000, ru2)
    if op25.get():
        root.after(180000, ru2)
    if op26.get():
        root.after(300000, ru2)
    if op27.get():
        root.after(600000, ru2)
def homesec():
    if op19.get():
        root.after(12000000, ru)
    if op20.get():
        root.after(900000, ru)
    if op21.get():
        root.after(6000000, ru)
    if op22.get():
        root.after(1800000, ru)
    if op24.get():
        root.after(60000, ru)
    if op25.get():
        root.after(180000, ru)
    if op26.get():
        root.after(300000, ru)
    if op27.get():
        root.after(600000, ru)
def idc4():
    id4 = open('id4.dat', 'w')
    id4.write(actname.get())
    id4.close
    w4.destroy()
def idc3():
    id3 = open('id3.dat', 'w')
    id3.write(actname.get())
    id3.close
    w4.destroy()
def idc2():
    id2 = open('id2.dat', 'w')
    id2.write(actname.get())
    id2.close
    w4.destroy()
def idc():
    fff = open('id.dat', 'w')
    fff.write(actname.get())
    fff.close
    w4.destroy()
def cn4():
    global w4
    w4 = Toplevel()
    rpw = open('pw4.dat', 'r')
    for data8 in rpw:
        data8 == actpw
    if actpwc.get() == data8:
        Label(w4, text = u'新しいユーザー名の入力').pack()
        actname.set('')
        Entry(w4, textvariable = actname).pack()
        Button(w4, text = u'変更する', command = idc4).pack()
        w3.destroy()
def cn3():
    global w4
    w4 = Toplevel()
    rpw = open('pw3.dat', 'r')
    for data6 in rpw:
        data6 == actpw
    if actpwc.get() == data6:
        Label(w4, text = u'新しいユーザー名の入力').pack()
        actname.set('')
        Entry(w4, textvariable = actname).pack()
        Button(w4, text = u'変更する', command = idc3).pack()
        w3.destroy()
def cn2():
    global w4
    w4 = Toplevel()
    rpw = open('pw2.dat', 'r')
    for data4 in rpw:
        data4 == actpw
    if actpwc.get() == data4:
        Label(w4, text = u'新しいユーザー名の入力').pack()
        actname.set('')
        Entry(w4, textvariable = actname).pack()
        Button(w4, text = u'変更する', command = idc2).pack()
        w3.destroy()
def cn():
    global w4
    w4 = Toplevel()
    rpw = open('pw.dat', 'r')
    for data1 in rpw:
        data1 == actpw
    if actpwc.get() == data1:
        Label(w4, text = u'新しいユーザー名の入力').pack()
        actname.set('')
        Entry(w4, textvariable = actname).pack()
        Button(w4, text = u'変更する', command = idc).pack()
        w3.destroy()
def pc4():
    global w3
    w3 = Toplevel()
    actpwc.set('')
    ffo = open('id4.dat', 'r')
    for data7 in ffo:
        data7 == actname
    Label(w3, text = u'確認のためパスワードを入力').pack()
    Label(w3, text = '%s' % data7).pack()
    Entry(w3, textvariable = actpwc, show = '*').pack()
    Button(w3, text = u'次へ', command = cn4).pack()
    w2.destroy()
def pc3():
    global w3
    w3 = Toplevel()
    actpwc.set('')
    ffo = open('id3.dat', 'r')
    for data5 in ffo:
        data5 == actname
    Label(w3, text = u'確認のためパスワードを入力').pack()
    Label(w3, text = '%s' % data5).pack()
    Entry(w3, textvariable = actpwc, show = '*').pack()
    Button(w3, text = u'次へ', command = cn3).pack()
    w2.destroy()
def pc2():
    global w3
    w3 = Toplevel()
    actpwc.set('')
    ffo = open('id2.dat', 'r')
    for data3 in ffo:
        data3 == data3
    Label(w3, text = u'確認のためパスワードを入力').pack()
    Label(w3, text = '%s' % data3).pack()
    Entry(w3, textvariable = actpwc, show = '*').pack()
    Button(w3, text = u'次へ', command = cn2).pack()
    w2.destroy()
def pc():
    global w3
    w3 = Toplevel()
    actpwc.set('')
    ffo = open('id.dat', 'r')
    for data2 in ffo:
        data2 == actname
    Label(w3, text = u'確認のためパスワードを入力').pack()
    Label(w3, text = '%s' % data2).pack()
    Entry(w3, textvariable = actpwc, show = '*').pack()
    Button(w3, text = u'次へ', command = cn).pack()
    w2.destroy()
def done4():
    if actpw.get() == actpwc.get():
        wpw = open('pw4.dat', 'w')
        wpw.write(actpw.get())
        wpw.close
        w4.destroy()
    else:
        Message(w4, text = u'パスワードが違います').pack()
        pw.set('')
        actpwc.set('')
def done3():
    if actpw.get() == actpwc.get():
        wpw = open('pw3.dat', 'w')
        wpw.write(actpw.get())
        wpw.close
        w4.destroy()
    else:
        Message(w4, text = u'パスワードが違います').pack()
        pw.set('')
        actpwc.set('')
def done2():
    if actpw.get() == actpwc.get():
        wpw = open('pw2.dat', 'w')
        wpw.write(actpw.get())
        wpw.close
        w4.destroy()
    else:
        Message(w4, text = u'パスワードが違います').pack()
        pw.set('')
        actpwc.set('')
def done():
    if actpw.get() == actpwc.get():
        wpw = open('pw.dat', 'w')
        wpw.write(actpw.get())
        wpw.close
        w4.destroy()
    else:
        Message(w4, text = u'パスワードが違います').pack()
        pw.set('')
        actpwc.set('')
def cna4():
    global w4
    w4 = Toplevel()
    rpw = open('pw4.dat', 'r')
    for data8 in rpw:
        data8 == actpw
    if actpwc.get() == data8:
        actpwc.set('')
        actpw.set('')
        Label(w4, text = u'新しいパスワードを入力').pack()
        Entry(w4, textvariable = actpw, show = '*').pack()
        Label(w4, text = u'確認のためもう一度入力').pack()
        Entry(w4, textvariable = actpwc, show = '*').pack()
        Button(w4, text = u'変更する', command = done4).pack()
        w3.destroy()
    else:
        Message(w3, text = u'パスワードが違います').pack()
        actpwc.set('')
def cna3():
    global w4
    w4 = Toplevel()
    rpw = open('pw3.dat', 'r')
    for data6 in rpw:
        data6 == actpw
    if actpwc.get() == data6:
        actpwc.set('')
        actpw.set('')
        Label(w4, text = u'新しいパスワードを入力').pack()
        Entry(w4, textvariable = actpw, show = '*').pack()
        Label(w4, text = u'確認のためもう一度入力').pack()
        Entry(w4, textvariable = actpwc, show = '*').pack()
        Button(w4, text = u'変更する', command = done3).pack()
        w3.destroy()
    else:
        Message(w3, text = u'パスワードが違います').pack()
        actpwc.set('')
def cna2():
    global w4
    w4 = Toplevel()
    rpw = open('pw2.dat', 'r')
    for data4 in rpw:
        data4 == actpw
    if actpwc.get() == data4:
        actpwc.set('')
        actpw.set('')
        Label(w4, text = u'新しいパスワードを入力').pack()
        Entry(w4, textvariable = actpw, show = '*').pack()
        Label(w4, text = u'確認のためもう一度入力').pack()
        Entry(w4, textvariable = actpwc, show = '*').pack()
        Button(w4, text = u'変更する', command = done2).pack()
        w3.destroy()
    else:
        Message(w3, text = u'パスワードが違います').pack()
        actpwc.set('')
def cna():
    global w4
    w4 = Toplevel()
    rpw = open('pw.dat', 'r')
    for data1 in rpw:
        data1 == actpw
    if actpwc.get() == data1:
        actpwc.set('')
        actpw.set('')
        Label(w4, text = u'新しいパスワードを入力').pack()
        Entry(w4, textvariable = actpw, show = '*').pack()
        Label(w4, text = u'確認のためもう一度入力').pack()
        Entry(w4, textvariable = actpwc, show = '*').pack()
        Button(w4, text = u'変更する', command = done).pack()
        w3.destroy()
    else:
        Message(w3, text = u'パスワードが違います').pack()
        actpwc.set('')
def pca4():
    global w3
    w3 = Toplevel()
    actpwc.set('')
    Label(w3, text = u'古いパスワードを入力').pack()
    Entry(w3, textvariable = actpwc, show = '*').pack()
    Button(w3, text = u'次へ', command = cna4).pack()
    w2.destroy()
def pca3():
    global w3
    w3 = Toplevel()
    actpwc.set('')
    Label(w3, text = u'古いパスワードを入力').pack()
    Entry(w3, textvariable = actpwc, show = '*').pack()
    Button(w3, text = u'次へ', command = cna3).pack()
    w2.destroy()
def pca2():
    global w3
    w3 = Toplevel()
    actpwc.set('')
    Label(w3, text = u'古いパスワードを入力').pack()
    Entry(w3, textvariable = actpwc, show = '*').pack()
    Button(w3, text = u'次へ', command = cna2).pack()
    w2.destroy()
def pca():
    global w3
    w3 = Toplevel()
    actpwc.set('')
    Label(w3, text = u'古いパスワードを入力').pack()
    Entry(w3, textvariable = actpwc, show = '*').pack()
    Button(w3, text = u'次へ', command = cna).pack()
    w2.destroy()
def account4():
    global w2
    w2 = Toplevel()
    Button(w2, text = u'アカウント名を変更する', command = pc4).pack()
    Label(w2, text = u'＊ホーム画面のユーザー名はプログラム').pack()
    Label(w2, text = u'を再起動するまで適用されません').pack()
    Button(w2, text = u'パスワードを変更する', command = pca4).pack()
def account3():
    global w2
    w2 = Toplevel()
    Button(w2, text = u'アカウント名を変更する', command = pc3).pack()
    Label(w2, text = u'＊ホーム画面のユーザー名はプログラム').pack()
    Label(w2, text = u'を再起動するまで適用されません').pack()
    Button(w2, text = u'パスワードを変更する', command = pca3).pack()
def account2():
    global w2
    w2 = Toplevel()
    Button(w2, text = u'アカウント名を変更する', command = pc2).pack()
    Label(w2, text = u'＊ホーム画面のユーザー名はプログラム').pack()
    Label(w2, text = u'を再起動するまで適用されません').pack()
    Button(w2, text = u'パスワードを変更する', command = pca2).pack()
def account():
    global w2
    w2 = Toplevel()
    Button(w2, text = u'アカウント名を変更する', command = pc).pack()
    Label(w2, text = u'＊ホーム画面のユーザー名はプログラム').pack()
    Label(w2, text = u'を再起動するまで適用されません').pack()
    Button(w2, text = u'パスワードを変更する', command = pca).pack()
def calc(event):
    f5 = Frame(root)
    lb = Listbox(f5)
    expr = mail.get()
    lb.insert('end',expr)
    lb.see('end')
    mail.set('')
def loadpic():
	global picdata, path
	filename = tkFileDialog.askopenfilename(filetypes = [('Image Files', ('.gif', '.ppm'))], initialdir = path)
	if filename != '':
		path = os.path.dirname(filename)
		picdata = Tkinter.PhotoImage(file = filename)
		label1.configure(image = picdata)
def market():
    global w1
    w1 = Toplevel()
    f1 = Frame(w1)
    f2 = Frame(w1)
    f3 = LabelFrame(w1)
    ffo = open('id.dat', 'r')
    for data2 in ffo:
        actname = data2
    b = open('money.dat', 'r')
    for i in b:
        i == i
    a = open('etc1.dat', 'r')
    for a2 in a:
        a2 == a2
    c = open('etc2.dat', 'r')
    for c2 in c:
        c2 == c2
    Label(f1, text = 'Galaxy Store').pack(side = LEFT)
    Label(f2, text = '%s' % data2).pack(side = LEFT)
    Label(f2, text = u'クレジット %s円' % i).pack(side = RIGHT)
    Label(f3, text = u'アプリ一覧：').pack()
    b1 = Button(f3, text = u'GUIプログラミングⅠ(数学ⅠA+情報AB)100円', command = cal)
    b1.pack()
    if a2 == 'able':
        b1.configure(text = u'GUIプログラミングⅠ(数学ⅠA+情報AB)購入済み')
    b2 = Button(f3, text = u'GUIプログラミングⅡ(数学ⅡB+物理Ⅰ)300円', command = cal2)
    b2.pack()
    if c2 == 'able':
        b2.configure(text = u'GUIプログラミングⅡ(数学ⅡB+物理Ⅰ)購入済み')
    b3 = Button(f3, text = u'GUIプログラミングⅢ(数学ⅢC+物理Ⅱ)500円')
    b3.pack()
    f1.pack()
    f2.pack()
    f3.pack()
def cal2():
    price = 300
    things = 'able'
    a = open('money.dat', 'r')
    g = open('etc2.dat', 'r')
    for ii in g:
        ii == ii
    for i in a:
        i == i
    d = int(i)
    if ii == 'disable':
        if d == price or d > price:
            c = d-price
            b = open('money.dat', 'w')
            b.write(str(c))
            wri = open('etc2.dat', 'w')
            wri.write(things)
            wri.close
            out2()
            w1.destroy()
        else:
            Dialog.Dialog(root, title = 'title', bitmap = 'info',
                          text = u'所持金が不足しています',
                          strings = ['OK'], default = 0)
    elif ii == 'able':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'すでに購入済みです',
                      strings = ['OK'], default = 0)
def timer():
    global w1
    w1 = Toplevel()
    Label(w1, text = u'タイマー').pack()
def summ():
    global w3
    w3 = Toplevel()
    z = regent.get()
    a1 = int(e10.get())*int(e20.get())+int(e30.get())+int(e40.get())
    a2 = int(e11.get())*int(e21.get())+int(e31.get())+int(e41.get())
    a3 = int(e12.get())*int(e22.get())+int(e32.get())+int(e42.get())
    a4 = int(e13.get())*int(e23.get())+int(e33.get())+int(e43.get())
    a5 = int(e14.get())*int(e24.get())+int(e34.get())+int(e44.get())
    a6 = int(e15.get())*int(e25.get())+int(e35.get())+int(e45.get())
    a7 = int(e16.get())*int(e26.get())+int(e36.get())+int(e46.get())
    a8 = int(e17.get())*int(e27.get())+int(e37.get())+int(e47.get())
    a9 = int(e18.get())*int(e28.get())+int(e38.get())+int(e48.get())
    a0 = int(e19.get())*int(e29.get())+int(e39.get())+int(e49.get())
    ans = a1+a2+a3+a4+a5+a6+a7+a8+a9
    o = int(z)
    Label(w3, text = u'合計金額').pack()
    Label(w3, text = '%d' % ans).pack()
    Label(w3, text = u'お預かり').pack()
    Label(w3, text = '%d' % o).pack()
    if o > ans:
        r = o - ans
        Label(w3, text = u'お釣り').pack()
        Label(w3, text = u'%d円' % r).pack()
    elif o == ans:
        Label(w3, text = u'お釣りは0円です').pack()
    elif o < ans:
        w = ans - o
        Label(w3, text = u'%d円' % w).pack()
        Label(w3, text = u'不足しています').pack()
def regc():
    global w2
    w2 = Toplevel()
    f1 = LabelFrame(w2)
    f2 = LabelFrame(w2)
    f3 = LabelFrame(w2)
    f4 = LabelFrame(w2)
    f5 = LabelFrame(w2)
    f6 = Frame(w2)
    f7 = Frame(w2)
    f8 = Frame(w2)
    if e0.get() == '':
        e0.set('---')
    if e1.get() == '':
        e1.set('---')
    if e2.get() == '':
        e2.set('---')
    if e3.get() == '':
        e3.set('---')
    if e4.get() == '':
        e4.set('---')
    if e5.get() == '':
        e5.set('---')
    if e6.get() == '':
        e6.set('---')
    if e7.get() == '':
        e7.set('---')
    if e8.get() == '':
        e8.set('---')
    if e9.get() == '':
        e9.set('---')
    if e10.get() or e20.get() != '0':
        pass
    if e11.get() or e21.get() != '0':
        pass
    if e12.get() or e22.get() != '0':
        pass
    if e13.get() or e23.get() != '0':
        pass
    if e14.get() or e24.get() != '0':
        pass
    if e15.get() or e25.get() != '0':
        pass
    if e16.get() or e26.get() != '0':
        pass
    if e17.get() or e27.get() != '0':
        pass
    if e18.get() or e28.get() != '0':
        pass
    if e19.get() or e29.get() != '0':
        pass
    a1 = int(e10.get())*int(e20.get())+int(e30.get())+int(e40.get())
    a2 = int(e11.get())*int(e21.get())+int(e31.get())+int(e41.get())
    a3 = int(e12.get())*int(e22.get())+int(e32.get())+int(e42.get())
    a4 = int(e13.get())*int(e23.get())+int(e33.get())+int(e43.get())
    a5 = int(e14.get())*int(e24.get())+int(e34.get())+int(e44.get())
    a6 = int(e15.get())*int(e25.get())+int(e35.get())+int(e45.get())
    a7 = int(e16.get())*int(e26.get())+int(e36.get())+int(e46.get())
    a8 = int(e17.get())*int(e27.get())+int(e37.get())+int(e47.get())
    a9 = int(e18.get())*int(e28.get())+int(e38.get())+int(e48.get())
    a0 = int(e19.get())*int(e29.get())+int(e39.get())+int(e49.get())
    ans = a1+a2+a3+a4+a5+a6+a7+a8+a9+a0
    a10 = int(e10.get())*int(e20.get())
    a11 = int(e11.get())*int(e21.get())
    a12 = int(e12.get())*int(e22.get())
    a13 = int(e13.get())*int(e23.get())
    a14 = int(e14.get())*int(e24.get())
    a15 = int(e15.get())*int(e25.get())
    a16 = int(e16.get())*int(e26.get())
    a17 = int(e17.get())*int(e27.get())
    a18 = int(e18.get())*int(e28.get())
    a19 = int(e19.get())*int(e29.get())
    Label(f1, text = u'購入商品:').pack()
    Label(f1, textvariable = e0).pack()
    Label(f1, textvariable = e1).pack()
    Label(f1, textvariable = e2).pack()
    Label(f1, textvariable = e3).pack()
    Label(f1, textvariable = e4).pack()
    Label(f1, textvariable = e5).pack()
    Label(f1, textvariable = e6).pack()
    Label(f1, textvariable = e7).pack()
    Label(f1, textvariable = e8).pack()
    Label(f1, textvariable = e9).pack()
    Label(f2, text = u'値段').pack()
    Label(f2, textvariable = e10).pack()
    Label(f2, textvariable = e11).pack()
    Label(f2, textvariable = e12).pack()
    Label(f2, textvariable = e13).pack()
    Label(f2, textvariable = e14).pack()
    Label(f2, textvariable = e15).pack()
    Label(f2, textvariable = e16).pack()
    Label(f2, textvariable = e17).pack()
    Label(f2, textvariable = e18).pack()
    Label(f2, textvariable = e19).pack()
    Label(f3, text = u'数量').pack()
    Label(f3, textvariable = e20).pack()
    Label(f3, textvariable = e21).pack()
    Label(f3, textvariable = e22).pack()
    Label(f3, textvariable = e23).pack()
    Label(f3, textvariable = e24).pack()
    Label(f3, textvariable = e25).pack()
    Label(f3, textvariable = e26).pack()
    Label(f3, textvariable = e27).pack()
    Label(f3, textvariable = e28).pack()
    Label(f3, textvariable = e29).pack()
    Label(f4, text = u'商品合計').pack()
    Label(f4, text = u'%d円' % a10).pack()
    Label(f4, text = u'%d円' % a11).pack()
    Label(f4, text = u'%d円' % a12).pack()
    Label(f4, text = u'%d円' % a13).pack()
    Label(f4, text = u'%d円' % a14).pack()
    Label(f4, text = u'%d円' % a15).pack()
    Label(f4, text = u'%d円' % a16).pack()
    Label(f4, text = u'%d円' % a17).pack()
    Label(f4, text = u'%d円' % a18).pack()
    Label(f4, text = u'%d円' % a19).pack()
    Label(f5, text = u'全てを含めた合計').pack()
    Label(f5, text = u'%d円' % a1).pack()
    Label(f5, text = u'%d円' % a2).pack()
    Label(f5, text = u'%d円' % a3).pack()
    Label(f5, text = u'%d円' % a4).pack()
    Label(f5, text = u'%d円' % a5).pack()
    Label(f5, text = u'%d円' % a6).pack()
    Label(f5, text = u'%d円' % a7).pack()
    Label(f5, text = u'%d円' % a8).pack()
    Label(f5, text = u'%d円' % a9).pack()
    Label(f5, text = u'%d円' % a0).pack()
    Label(f6, textvariable = buffe).pack()
    Label(f7, text = u'合計:').pack(side = LEFT)
    Label(f7, text = u'円').pack(side = RIGHT)
    Label(f7, text = '%d' % ans).pack(side = RIGHT)
    Label(f8, text = u'お預かり:').pack(side = LEFT)
    Entry(f8, textvariable = regent).pack(side = RIGHT)
    Button(f8, text = u'計算', command = summ).pack(side = RIGHT)
    f1.pack(side = LEFT)
    f2.pack(side = LEFT)
    f3.pack(side = LEFT)
    f4.pack(side = LEFT)
    f5.pack(side = LEFT)
    f6.pack()
    f7.pack()
    f8.pack(side = BOTTOM)
def erase():
    e0.set('')
    e1.set('')
    e2.set('')
    e3.set('')
    e4.set('')
    e5.set('')
    e6.set('')
    e7.set('')
    e8.set('')
    e9.set('')
    e10.set('0')
    e11.set('0')
    e12.set('0')
    e13.set('0')
    e14.set('0')
    e15.set('0')
    e16.set('0')
    e17.set('0')
    e18.set('0')
    e19.set('0')
    e20.set('0')
    e21.set('0')
    e22.set('0')
    e23.set('0')
    e24.set('0')
    e25.set('0')
    e26.set('0')
    e27.set('0')
    e28.set('0')
    e29.set('0')
    e30.set('0')
    e31.set('0')
    e32.set('0')
    e33.set('0')
    e34.set('0')
    e35.set('0')
    e36.set('0')
    e37.set('0')
    e38.set('0')
    e39.set('0')
    e40.set('0')
    e41.set('0')
    e42.set('0')
    e43.set('0')
    e44.set('0')
    e45.set('0')
    e46.set('0')
    e47.set('0')
    e48.set('0')
    e49.set('0')
def regi():
    global w1
    w1 = Toplevel()
    f0 = Frame(w1)
    f1 = Frame(w1)
    f2 = Frame(w1)
    f3 = Frame(w1)
    f4 = Frame(w1)
    f5 = Frame(w1)
    Label(w1, text = u'会計ソフト').pack()
    Label(f0, text = u'商品名:').pack()
    Entry(f0, textvariable = e0).pack()
    Entry(f0, textvariable = e1).pack()
    Entry(f0, textvariable = e2).pack()
    Entry(f0, textvariable = e3).pack()
    Entry(f0, textvariable = e4).pack()
    Entry(f0, textvariable = e5).pack()
    Entry(f0, textvariable = e6).pack()
    Entry(f0, textvariable = e7).pack()
    Entry(f0, textvariable = e8).pack()
    Entry(f0, textvariable = e9).pack()
    Label(f1, text = u'値段').pack()
    Entry(f1, textvariable = e10).pack()
    Entry(f1, textvariable = e11).pack()
    Entry(f1, textvariable = e12).pack()
    Entry(f1, textvariable = e13).pack()
    Entry(f1, textvariable = e14).pack()
    Entry(f1, textvariable = e15).pack()
    Entry(f1, textvariable = e16).pack()
    Entry(f1, textvariable = e17).pack()
    Entry(f1, textvariable = e18).pack()
    Entry(f1, textvariable = e19).pack()
    Label(f3, text = u'送料').pack()
    Entry(f3, textvariable = e30).pack()
    Entry(f3, textvariable = e31).pack()
    Entry(f3, textvariable = e32).pack()
    Entry(f3, textvariable = e33).pack()
    Entry(f3, textvariable = e34).pack()
    Entry(f3, textvariable = e35).pack()
    Entry(f3, textvariable = e36).pack()
    Entry(f3, textvariable = e37).pack()
    Entry(f3, textvariable = e38).pack()
    Entry(f3, textvariable = e39).pack()
    Label(f2, text = u'数量').pack()
    Entry(f2, textvariable = e20).pack()
    Entry(f2, textvariable = e21).pack()
    Entry(f2, textvariable = e22).pack()
    Entry(f2, textvariable = e23).pack()
    Entry(f2, textvariable = e24).pack()
    Entry(f2, textvariable = e25).pack()
    Entry(f2, textvariable = e26).pack()
    Entry(f2, textvariable = e27).pack()
    Entry(f2, textvariable = e28).pack()
    Entry(f2, textvariable = e29).pack()
    Label(f4, text = u'手数料').pack()
    Entry(f4, textvariable = e40).pack()
    Entry(f4, textvariable = e41).pack()
    Entry(f4, textvariable = e42).pack()
    Entry(f4, textvariable = e43).pack()
    Entry(f4, textvariable = e44).pack()
    Entry(f4, textvariable = e45).pack()
    Entry(f4, textvariable = e46).pack()
    Entry(f4, textvariable = e47).pack()
    Entry(f4, textvariable = e48).pack()
    Entry(f4, textvariable = e49).pack()
    Button(f5, text = u'計算', command = regc).pack()
    Button(f5, text = u'初期化', command = erase).pack()
    f4.pack(side = RIGHT)
    f3.pack(side = RIGHT)
    f2.pack(side = RIGHT)
    f1.pack(side = RIGHT)
    f0.pack(side = RIGHT)
    f5.pack(side = RIGHT)
def normal():
    global w3
    w3 = Toplevel()
    lb = Listbox(w3, width = 50)
    lb.insert(END, 'まずa=raw_input('')とb=input('')についての説明。これはShellにて('')に書かれた解答をaやbに保存する。')
    lb.insert(END, '次にfor文について。使用例がfor y in x(aとbの変数):Tab print y(処理)である。xの内容をyに移して改行・Tabでコロンの中に入るようにして処理を入力。今回はたまたまyを表示にしました。')
    lb.insert(END, '続いてif文。よく使われるもので条件が一致すれば実行する。もしそれ以外の処理があればelse:で処理できる。ただしコロンを忘れずに')
    lb.insert(END, 'そしてwhile。while()の()の中が一致する限り処理を繰り返す。処理を止めるにはbreakを使う')
    lb.insert(END, 'これらの使用例をまとめたプログラムをひとつだけつけておきました。プログラムはプログラムのファイルに入っています。もういくつかほしい方はプログラムパックを購入してください')
    sb1 = Scrollbar(w3, orient = 'v', command = lb.yview)
    sb2 = Scrollbar(w3, orient = 'h', command = lb.xview)
    lb.configure(yscrollcommand = sb1.set)
    lb.configure(xscrollcommand = sb2.set)
    lb.grid(row = 1, column = 0, sticky = 'nsew')
    sb1.grid(row = 1, column = 1, sticky = 'ns')
    sb2.grid(row = 2, column = 0, sticky = 'ew')
def out():
    a = open('etc1.dat', 'r')
    for i in a:
        i == i
    if i == 'able':
        global w3
        w3 = Toplevel()
        lb = Listbox(w3, width = 60)
        lb.insert(END, 'まずウィンドウを出すモジュールとしてTkinterがある。from Tkinter import *と打てば使えるようになる')
        lb.insert(END, '親ウィンドウを作る設定をする。root = Tk()でおｋ')
        lb.insert(END, '次にウィンドウに配置する文字はLabelを使う。Label(root, text = '').pack() textに書きたい文字を書く')
        lb.insert(END, 'ウィンドウにボタンを配置する場合はButton。Button(root, text = '', command = ).pack() commandはボタンを押したときの処理')
        lb.insert(END, '文字入力をさせる場合はEntry。ここでa = StringVar()を作る必要がある。Entry(root, textvariable = a).pack()')
        lb.insert(END, '処理はたいていdefでdef 関数名():Tab 処理となる。')
        lb.insert(END, '.pack()を忘れるとボタンやラベルは表示されない。ボタンやラベルに変数をつけて、変数.pack()でも構わない。')
        lb.insert(END, '最後に必ずroot.mainloop()を入れないとウィンドウすら出てこない。続きはⅡで。')
        sb1 = Scrollbar(w3, orient = 'v', command = lb.yview)
        sb2 = Scrollbar(w3, orient = 'h', command = lb.xview)
        lb.configure(yscrollcommand = sb1.set)
        lb.configure(xscrollcommand = sb2.set)
        lb.grid(row = 1, column = 0, sticky = 'nsew')
        sb1.grid(row = 1, column = 1, sticky = 'ns')
        sb2.grid(row = 2, column = 0, sticky = 'ew')
    else:
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'パックを購入してください',
                      strings = ['OK'], default = 0)
def cal():
    price = 100
    things = 'able'
    a = open('money.dat', 'r')
    g = open('etc1.dat', 'r')
    for ii in g:
        ii == ii
    for i in a:
        i == i
    d = int(i)
    if ii == 'disable':
        if d == price or d > price:
            c = d-price
            b = open('money.dat', 'w')
            b.write(str(c))
            wri = open('etc1.dat', 'w')
            wri.write(things)
            wri.close
            out()
            w1.destroy()
        else:
            Dialog.Dialog(root, title = 'title', bitmap = 'info',
                          text = u'所持金が不足しています',
                          strings = ['OK'], default = 0)
    elif ii == 'able':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'すでに購入済みです',
                      strings = ['OK'], default = 0)
def out2():
    a = open('etc2.dat', 'r')
    for i in a:
        i == i
    if i == 'able':
        global w3
        w3 = Toplevel()
        lb = Listbox(w3, width = 60)
        lb.insert(END, '前回は配置だけだったが、今回は処理について説明：')
        sb1 = Scrollbar(w3, orient = 'v', command = lb.yview)
        sb2 = Scrollbar(w3, orient = 'h', command = lb.xview)
        lb.configure(yscrollcommand = sb1.set)
        lb.configure(xscrollcommand = sb2.set)
        lb.grid(row = 1, column = 0, sticky = 'nsew')
        sb1.grid(row = 1, column = 1, sticky = 'ns')
        sb2.grid(row = 2, column = 0, sticky = 'ew')
    else:
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'パックを購入してください',
                      strings = ['OK'], default = 0)
def lp():
    global w2
    w2 = Toplevel()
    Label(w2, text = 'Learn Python').pack()
    Button(w2, text = u'コンソール版', command = normal).pack()
    Button(w2, text = u'GUIプログラムⅠ', command = out).pack()
    Button(w2, text = u'GUIプログラムⅡ', command = out2).pack()
    Button(w2, text = u'GUIプログラムⅢ').pack()
def pmc():
    global w3
    w3 = Toplevel()
    m = pm1.get()
    n = pm3.get()
    o = pm2.get()
    p = pm4.get()
    if o == '' or n == '0':
        pass
    y = int(m)+int(p)
    x = int(y)-int(n)
    Label(w3, text = u'書き込み内容').pack()
    Label(w3, text = u'今月の小遣い残高:').pack()
    Label(w3, textvariable = pm1).pack()
    Label(w3, text = u'支出内容').pack()
    Label(w3, textvariable = pm2).pack()
    Label(w3, text = u'支出金額').pack()
    Label(w3, textvariable = pm3).pack()
    Label(w3, text = '%d' % x).pack()
    a = open('pm.dat', 'w')
    a.write(str(x))
    b = open('pmt.dat', 'a')
    b.write(o+'\n')
    c = open('pmp.dat', 'a')
    c.write(str(n)+'\n')
def rpmoney():
    global w3
    w3 = Toplevel()
    f1 = LabelFrame(w3)
    f2 = LabelFrame(w3)
    a = open('pmp.dat', 'r')
    b = open('pmt.dat', 'r')
    x = a.readlines()
    y = b.readlines()
    Label(w3, text = u'小遣い使用レポート').pack()
    for aa in y:
        Label(f1, text = '%s+\n' % y).pack()
    for bb in x:
        Label(f2, text = '%s+\n' % x).pack()
    for a2 in y:
        print x,
    print
    for b2 in x:
        print y,
    print
    f1.pack()
    f2.pack()
def poket():
    pm1.set('0')
    pm2.set('')
    pm3.set('0')
    pm4.set('0')
    a = open('pm.dat', 'r')
    for i in a:
        i == i
    pm1.set(i)
def pmoney():
    global w2
    w2 = Toplevel()
    a = open('pm.dat', 'r')
    for i in a:
        i == i
    pm1.set(i)
    Label(w2, text = u'小遣い管理').pack()
    Label(w2, text = u'今月の小遣い残高:').pack()
    Entry(w2, textvariable = pm1).pack()
    Label(w2, text = u'支出内容').pack()
    Entry(w2, textvariable = pm2).pack()
    Label(w2, text = u'支出金額').pack()
    Entry(w2, textvariable = pm3).pack()
    Label(w2, text = u'その他収入').pack()
    Entry(w2, textvariable = pm4).pack()
    Button(w2, text = u'メモにメモる', command = pmc).pack()
    Button(w2, text = u'初期化・更新', command = poket).pack()
    Button(w2, text = u'小遣い使用レポート', command = rpmoney).pack()
def home4():
    global w1
    w1 = Toplevel()
    mb = Menu(w1)
    w1.configure(menu = mb)
    f0 = Frame(w1)
    f4 = Frame(w1)
    f5 = Frame(w1)
    f6 = Frame(w1)
    f7 = Frame(w1)
    ver = 1
    vers = 3
    files = Menu(mb, tearoff = True)
    aco = Menu(mb, tearoff = True)
    mb.add_cascade(label = "File", underline = 0, menu = files)
    mb.add_cascade(label = "Account", underline = 0, menu = aco)
    files.add_command(label = 'Exit', under = 0, command = sys.exit)
    aco.add_command(label = 'Change Acount', under = 0, command = acco)
    ffo = open('id4.dat', 'r')
    for data7 in ffo:
        actname = data7 
    nam = 'Galaxy-OS Universe'
    Label(w1, text = u'%s %d.%d' % (nam, ver, vers)).pack()
    picdata = PhotoImage(width = 64, height = 64)
    label1 = Label(f0, image = picdata).pack()
    Button(f0, text = 'Load', command = loadpic).pack()
    Label(f0, text = u'ユーザー:').pack(in_ = f0, side = LEFT)
    Label(f0, text = '%s' % data7).pack(in_ = f0, side = LEFT)
    f0.pack(fill = BOTH)
    Button(f4, text = 'Account', width = 5, height = 2, command = account4).pack(side = LEFT)
    Label(f5, text = u'アカウント').pack(side = LEFT)
    Button(f4, text = 'Timer', width = 5, height = 2, command = timer).pack(side = LEFT)
    Label(f5, text = u'タイマー').pack(side = LEFT)
    Button(f4, text = u'会計', width = 5, height = 2, command = regi).pack(side = RIGHT)
    Label(f5, text = u'会計ソフト').pack(side = RIGHT)
    Button(f4, text = 'Market', width = 5, height = 2, command = market).pack(side = RIGHT)
    Label(f5, text = u'マーケット').pack(side = RIGHT) 
    Button(f6, text = u'setting', width = 5, height = 2, command = set).pack(side = LEFT)
    Label(f7, text = u'設定').pack(side = LEFT)
    Button(f6, text = 'LP', width = 5, height = 2, command = lp).pack(side = LEFT)
    Label(f7, text = 'Learn Python').pack(side = LEFT)
    Button(f6, text = 'Lock', width = 5, height = 2, command = ru4).pack(side = RIGHT)
    Label(f7, text = u'ロック画面に戻る').pack(side = RIGHT)
    Button(f6, text = u'終了', width = 5, height = 2, command = sys.exit).pack(side = RIGHT)
    f4.pack()
    f5.pack()
    f6.pack()
    f7.pack()
    time()
    homesec4()
def home3():
    global w1
    w1 = Toplevel()
    mb = Menu(w1)
    w1.configure(menu = mb)
    f0 = Frame(w1)
    f4 = Frame(w1)
    f5 = Frame(w1)
    f6 = Frame(w1)
    f7 = Frame(w1)
    ver = 1
    vers = 3
    files = Menu(mb, tearoff = True)
    aco = Menu(mb, tearoff = True)
    mb.add_cascade(label = "File", underline = 0, menu = files)
    mb.add_cascade(label = "Account", underline = 0, menu = aco)
    files.add_command(label = 'Exit', under = 0, command = sys.exit)
    aco.add_command(label = 'Change Acount', under = 0, command = acco)
    ffo = open('id3.dat', 'r')
    for data5 in ffo:
        actname = data5 
    nam = 'Galaxy-OS Universe'
    Label(w1, text = u'%s %d.%d' % (nam, ver, vers)).pack()
    picdata = PhotoImage(width = 64, height = 64)
    label1 = Label(f0, image = picdata).pack()
    Button(f0, text = 'Load', command = loadpic).pack()
    Label(f0, text = u'ユーザー:').pack(in_ = f0, side = LEFT)
    Label(f0, text = '%s' % data5).pack(in_ = f0, side = LEFT)
    f0.pack(fill = BOTH)
    Button(f4, text = 'Account', width = 5, height = 2, command = account3).pack(side = LEFT)
    Label(f5, text = u'アカウント').pack(side = LEFT)
    Button(f4, text = 'Timer', width = 5, height = 2, command = timer).pack(side = LEFT)
    Label(f5, text = u'タイマー').pack(side = LEFT)
    Button(f4, text = u'会計', width = 5, height = 2, command = regi).pack(side = RIGHT)
    Label(f5, text = u'会計ソフト').pack(side = RIGHT)
    Button(f4, text = 'Market', width = 5, height = 2, command = market).pack(side = RIGHT)
    Label(f5, text = u'マーケット').pack(side = RIGHT) 
    Button(f6, text = u'setting', width = 5, height = 2, command = set).pack(side = LEFT)
    Label(f7, text = u'設定').pack(side = LEFT)
    Button(f6, text = 'LP', width = 5, height = 2, command = lp).pack(side = LEFT)
    Label(f7, text = 'Learn Python').pack(side = LEFT)
    Button(f6, text = 'Lock', width = 5, height = 2, command = ru3).pack(side = RIGHT)
    Label(f7, text = u'ロック画面に戻る').pack(side = RIGHT)
    Button(f6, text = u'終了', width = 5, height = 2, command = sys.exit).pack(side = RIGHT)
    f4.pack()
    f5.pack()
    f6.pack()
    f7.pack()
    time()
    homesec3()
def home2():
    global w1
    w1 = Toplevel()
    mb = Menu(w1)
    w1.configure(menu = mb)
    f0 = Frame(w1)
    f4 = Frame(w1)
    f5 = Frame(w1)
    f6 = Frame(w1)
    f7 = Frame(w1)
    ver = 1
    vers = 3
    files = Menu(mb, tearoff = True)
    aco = Menu(mb, tearoff = True)
    mb.add_cascade(label = "File", underline = 0, menu = files)
    mb.add_cascade(label = "Account", underline = 0, menu = aco)
    files.add_command(label = 'Exit', under = 0, command = sys.exit)
    aco.add_command(label = 'Change Acount', under = 0, command = acco)
    ffo = open('id2.dat', 'r')
    for data3 in ffo:
        actname = data3 
    nam = 'Galaxy-OS Universe'
    Label(w1, text = u'%s %d.%d' % (nam, ver, vers)).pack()
    picdata = PhotoImage(width = 64, height = 64)
    label1 = Label(f0, image = picdata).pack()
    Button(f0, text = 'Load', command = loadpic).pack()
    Label(f0, text = u'ユーザー:').pack(in_ = f0, side = LEFT)
    Label(f0, text = '%s' % data3).pack(in_ = f0, side = LEFT)
    f0.pack(fill = BOTH)
    Button(f4, text = 'Account', width = 5, height = 2, command = account2).pack(side = LEFT)
    Label(f5, text = u'アカウント').pack(side = LEFT)
    Button(f4, text = 'Timer', width = 5, height = 2, command = timer).pack(side = LEFT)
    Label(f5, text = u'タイマー').pack(side = LEFT)
    Button(f4, text = u'会計', width = 5, height = 2, command = regi).pack(side = RIGHT)
    Label(f5, text = u'会計ソフト').pack(side = RIGHT)
    Button(f4, text = 'Market', width = 5, height = 2, command = market).pack(side = RIGHT)
    Label(f5, text = u'マーケット').pack(side = RIGHT) 
    Button(f6, text = u'setting', width = 5, height = 2, command = set).pack(side = LEFT)
    Label(f7, text = u'設定').pack(side = LEFT)
    Button(f6, text = 'LP', width = 5, height = 2, command = lp).pack(side = LEFT)
    Label(f7, text = 'Learn Python').pack(side = LEFT)
    Button(f6, text = 'Lock', width = 5, height = 2, command = ru2).pack(side = RIGHT)
    Label(f7, text = u'ロック画面に戻る').pack(side = RIGHT)
    Button(f6, text = u'終了', width = 5, height = 2, command = sys.exit).pack(side = RIGHT)
    f4.pack()
    f5.pack()
    f6.pack()
    f7.pack()
    time()
    homesec2()
def home():
    global w1
    w1 = Toplevel()
    mb = Menu(w1)
    w1.configure(menu = mb)
    f0 = Frame(w1)
    f4 = Frame(w1)
    f5 = Frame(w1)
    f6 = Frame(w1)
    f7 = Frame(w1)
    f8 = Frame(w1)
    f9 = Frame(w1)
    ver = 1
    vers = 3
    files = Menu(mb, tearoff = True)
    aco = Menu(mb, tearoff = True)
    mb.add_cascade(label = "File", underline = 0, menu = files)
    mb.add_cascade(label = "Account", underline = 0, menu = aco)
    files.add_command(label = 'Exit', under = 0, command = sys.exit)
    aco.add_command(label = 'Change Acount', under = 0, command = acco)
    ffo = open('id.dat', 'r')
    for data2 in ffo:
        actname = data2 
    nam = 'Galaxy-OS Universe'
    Label(w1, text = u'%s %d.%d' % (nam, ver, vers)).pack()
    picdata = PhotoImage(width = 64, height = 64)
    Button(f0, text = 'Load', command = loadpic).pack()
    Label(f0, text = u'ユーザー:').pack(in_ = f0, side = LEFT)
    Label(f0, text = '%s' % data2).pack(in_ = f0, side = LEFT)
    f0.pack(fill = BOTH)
    b1 = Button(f4, text = 'Account', width = 5, height = 2, command = account)
    b1.pack(side = LEFT)
    Label(f5, text = u'アカウント').pack(side = LEFT)
    b2 = Button(f4, text = 'Timer', width = 5, height = 2, command = timer).pack(side = LEFT)
    Label(f5, text = u'タイマー').pack(side = LEFT)
    b3 = Button(f4, text = u'会計', width = 5, height = 2, command = regi).pack(side = RIGHT)
    Label(f5, text = u'会計ソフト').pack(side = RIGHT)
    b4 = Button(f4, text = 'Market', width = 5, height = 2, command = market).pack(side = RIGHT)
    Label(f5, text = u'マーケット').pack(side = RIGHT) 
    b5 = Button(f6, text = u'setting', width = 5, height = 2, command = set).pack(side = LEFT)
    Label(f7, text = u'設定').pack(side = LEFT)
    Button(f6, text = 'LP', width = 5, height = 2, command = lp).pack(side = LEFT)
    Label(f7, text = 'Learn Python').pack(side = LEFT)
    b6 = Button(f6, text = 'Lock', width = 5, height = 2, command = ru)
    b6.pack(side = RIGHT)
    b6.bind('<Return>', rus)
    b6.focus_set()
    Label(f7, text = u'ロック画面に戻る').pack(side = RIGHT)
    b7 = Button(f6, text = u'終了', width = 5, height = 2, command = sys.exit)
    b7.pack(side = RIGHT)
    b7.bind('<Return>', sys.exit)
    b7.focus_set()
    Button(f8, text = u'Memo', width = 5, height = 2, command = pmoney).pack()
    Label(f9, text = u'小遣い管理・計算').pack()
    f4.pack()
    f5.pack()
    f6.pack()
    f7.pack()
    f8.pack()
    f9.pack()
    time()
    homesec()
def pok4(event):
    ffo = open('pw4.dat', 'r')
    for data8 in ffo:
        actpw == data8
    if actpwc.get() == data8:
        if op28.get():
            w2.destroy()
            w3.destroy()
            home4()
            actpwc.set('')
        else:
            w1.destroy()
            w3.destroy()
            home4()
            actpwc.set('')
    else:
        Message(w2, text = u'パスワードが違います').pack()
        actpwc.set('')
def pok3(event):
    ffo = open('pw3.dat', 'r')
    for data6 in ffo:
        actpw == data6
    if actpwc.get() == data6:
        if op28.get():
            w2.destroy()
            w3.destroy()
            home3()
            actpwc.set('')
        else:
            w1.destroy()
            w3.destroy()
            home3()
            actpwc.set('')
    else:
        Message(w2, text = u'パスワードが違います').pack()
        actpwc.set('')
def pok2(event):
    ffo = open('pw2.dat', 'r')
    for data4 in ffo:
        actpw == data4
    if actpwc.get() == data4:
        if op28.get():
            w2.destroy()
            w3.destroy()
            home2()
            actpwc.set('')
        else:
            w1.destroy()
            w3.destroy()
            home2()
            actpwc.set('')
    else:
        Message(w2, text = u'パスワードが違います').pack()
        actpwc.set('')
def pok(event):
    ffo = open('pw.dat', 'r')
    for data1 in ffo:
        actpw == data1
    if actpwc.get() == data1:
        if op28.get():
            w2.destroy()
            w3.destroy()
            home()
            actpwc.set('')
        else:
            w1.destroy()
            w3.destroy()
            home()
            actpwc.set('')
    else:
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'パスワードが違います',
                      strings = ['OK'], default = 0)
        actpwc.set('')
def homes():
    w2.destroy()
def hometo():
    root.lift()
    w2.destroy()
def op3gc():
    global w3
    w3 = Toplevel()
    rid = open('id.dat', 'r')
    for data2 in rid:
        data2 == data2
    actpwc.set('')
    Label(w3, text = '%s' % osnam).pack()
    Label(w3, text = u'ユーザー:').pack()
    Label(w3, text = '%s' % data2).pack()
    e = Entry(w3, textvariable = actpwc, show = '*')
    e.pack()
    e.bind('<Return>', pok)
    e.focus_set()
def op4gc():
    global w3
    w3 = Toplevel() 
    id2 = open('id2.dat', 'r')
    for data3 in id2:
        data3 == data3
    actpwc.set('')
    Label(w3, text = '%s' % osnam).pack()
    Label(w3, text = u'ユーザー:').pack()
    Label(w3, text = '%s' % data3).pack()
    e = Entry(w3, textvariable = actpwc, show = '*')
    e.pack()
    e.bind('<Return>', pok2)
    e.focus_set()
def op5gc():
    global w3
    w3 = Toplevel() 
    id3 = open('id3.dat', 'r')
    for data5 in id3:
        data5 == data5
    actpwc.set('')
    Label(w3, text = '%s' % osnam).pack()
    Label(w3, text = u'ユーザー:').pack()
    Label(w3, text = '%s' % data5).pack()
    e = Entry(w3, textvariable = actpwc, show = '*')
    e.pack()
    e.bind('<Return>', pok3)
    e.focus_set()
def op6gc():
    global w3
    id4 = open('id4.dat', 'r')
    for data7 in id4:
        data7 == data7
    actpwc.set('')
    Label(w3, text = '%s' % osnam).pack()
    Label(w3, text = u'ユーザー:').pack()
    Label(w3, text = '%s' % data7).pack()
    e = Entry(w3, textvariable = actpwc, show = '*')
    e.pack()
    e.bind('<Return>', pok4)
    e.focus_set()
def acts():
    global w1
    w1 = Toplevel()
    f1 = Frame(w1)
    rid = open('id.dat', 'r')
    for data2 in rid:
        data2 == data2
    id2 = open('id2.dat', 'r')
    for data3 in id2:
        data3 == data3
    id3 = open('id3.dat', 'r')
    for data5 in id3:
        data5 == data5
    id4 = open('id4.dat', 'r')
    for data7 in id4:
        data7 == data7
    Label(w1, text = '%s' % osnam).pack()
    Label(w1, text = u'ユーザー:').pack()
    b5 = Button(f1, text = u'終了(0)', command = sys.exit)
    b5.pack(side = RIGHT)
    b5.bind('<KeyPress-0>', sys.exit)
    b5.focus_set()
    b4 = Button(f1, text = '%s(4)' % data7, command = op6g)
    b4.pack(side = RIGHT)
    b4.bind('<KeyPress-4>', op6ge)
    b4.focus_set()
    b3 = Button(f1, text = '%s(3)' % data5, command = op5g)
    b3.pack(side = RIGHT)
    b3.bind('<KeyPress-3>', op5ge)
    b3.focus_set()
    b2 = Button(f1, text = '%s(2)' % data3, command = op4g)
    b2.pack(side = RIGHT)
    b2.bind('<KeyPress-2>', op4ge)
    b2.focus_set()
    b1 = Button(f1, text = '%s(1)' % data2, command = op3g)
    b1.pack(side = RIGHT)
    b1.bind('<KeyPress-1>', op3ge)
    b1.focus_set()
    f1.pack()
    root.lower()
def op3ge(event):
    rpw = open('id.dat', 'r')
    for data2 in rpw:
        data2 == data2
    if data2 != 'user1':
        op3gc()
        op10.set(True)
    else:
        op3g()
        op10.set(True)
def op4ge(event):
    rpw = open('id2.dat', 'r')
    for data2 in rpw:
        data2 == data2
    if data2 != 'user2':
        op4gc()
        op11.set(True)
    else:
        op4g()
        op11.set(True)
def op5ge(event):
    rpw = open('id3.dat', 'r')
    for data2 in rpw:
        data2 == data2
    if data2 != 'user3':
        op5gc()
        op12.set(True)
    else:
        op5g()
        op12.set(True)
def op6ge(event):
    rpw = open('id4.dat', 'r')
    for data2 in rpw:
        data2 == data2
    if data2 != 'user4':
        op6gc()
        op13.set(True)
    else:
        op6g()
        op13.set(True)
def op3g():
    rpw = open('id.dat', 'r')
    for data2 in rpw:
        data2 == data2
    if data2 == 'user1':
        global w2
        w2 = Toplevel()
        f1 = Frame(root2)
        f2 = Frame(root2)
        f3 = Frame(root2)
        f4 = Frame(root2)
        Label(root2, text = '%s' % osnam).pack()
        Label(root2, text = u'アカウント作成').pack()
        Entry(f1, textvariable = actname).pack(side = RIGHT)
        Label(f1, text = u'アカウント名').pack(side = LEFT)
        Entry(f2, textvariable = actpw, show = '*').pack(side = RIGHT)
        Label(f2, text = u'パスワード').pack(side = LEFT)
        Entry(f3, textvariable = actpwc, show = '*').pack(side = RIGHT)
        Label(f3, text = u'確認のためもう一度入力').pack(side = LEFT)
        b13 = Button(f4, text = u'作成', command = z)
        b13.pack(side = LEFT)
        b13.bind('<Return>', zz)
        b13.focus_set()
        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()
        op3.set(True)
        op10.set(True)
    else:
        op3gc()
        op10.set(True)
    time()
    root.lower()
def op4g():
    rpw2 = open('id2.dat', 'r')
    for data3 in rpw2:
        data3 == data3
    if data3 == 'user2':
        global w2
        w2 = Toplevel()
        f1 = Frame(w2)
        f2 = Frame(w2)
        f3 = Frame(w2)
        f4 = Frame(w2)
        Label(w2, text = '%s' % osnam).pack()
        Label(w2, text = u'アカウント作成').pack()
        Entry(f1, textvariable = actname).pack(side = RIGHT)
        Label(f1, text = u'アカウント名').pack(side = LEFT)
        Entry(f2, textvariable = actpw, show = '*').pack(side = RIGHT)
        Label(f2, text = u'パスワード').pack(side = LEFT)
        Entry(f3, textvariable = actpwc, show = '*').pack(side = RIGHT)
        Label(f3, text = u'確認のためもう一度入力').pack(side = LEFT)
        b12 = Button(f4, text = u'作成', command = z)
        b12.pack(side = LEFT)
        b12.bind('<Return>', zz)
        b12.focus_set()
        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()
        op4.set(True)
        op11.set(True)
    else:
        op4gc()
        op11.set(True)
    time()
    root.lower()
def op5g():
    w4.wm_attributes("-topmost", 1)
    rpw3 = open('id3.dat','r')
    for data5 in rpw3:
        data5 == data5
    if data5 == 'user3':
        global w2
        w2 = Toplevel()
        f1 = Frame(w2)
        f2 = Frame(w2)
        f3 = Frame(w2)
        f4 = Frame(w2)
        Label(w2, text = '%s' % osnam).pack()
        Label(w2, text = u'アカウント作成').pack()
        Entry(f1, textvariable = actname).pack(side = RIGHT)
        Label(f1, text = u'アカウント名').pack(side = LEFT)
        Entry(f2, textvariable = actpw, show = '*').pack(side = RIGHT)
        Label(f2, text = u'パスワード').pack(side = LEFT)
        Entry(f3, textvariable = actpwc, show = '*').pack(side = RIGHT)
        Label(f3, text = u'確認のためもう一度入力').pack(side = LEFT)
        b11 = Button(f4, text = u'作成', command = z)
        b11.pack(side = LEFT)
        b11.bind('<Return>', zz)
        b11.focus_set()
        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()
        op5.set(True)
        op12.set(True)
    else:
        op5gc()
        op12.set(True)
    time()
    root.lower()
def op6g():
    w4.wm_attributes("-topmost", 1)
    rpw4 = open('id4.dat', 'r')
    for data7 in rpw4:
        data7 == data7
    if data7 == 'user4':
        global w2
        w2 = Toplevel()
        f1 = Frame(w2)
        f2 = Frame(w2)
        f3 = Frame(w2)
        f4 = Frame(w2)
        Label(w2, text = '%s' % osnam).pack()
        Label(w2, text = u'アカウント作成').pack()
        Entry(f1, textvariable = actname).pack(side = RIGHT)
        Label(f1, text = u'アカウント名').pack(side = LEFT)
        Entry(f2, textvariable = actpw, show = '*').pack(side = RIGHT)
        Label(f2, text = u'パスワード').pack(side = LEFT)
        Entry(f3, textvariable = actpwc, show = '*').pack(side = RIGHT)
        Label(f3, text = u'確認のためもう一度入力').pack(side = LEFT)
        b10 = Button(f4, text = u'作成', command = z)
        b10.pack(side = LEFT)
        b10.bind('<Return>', zz)
        b10.focus_set()
        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()
        op6.set(True)
        op13.set(True)
    else:
        op6gc()
        op13.set(True)
    time()
    root.lower()
def time():
    buf.set(strftime('%H:%M:%S'))
    root.after(1000, time)
def homet4():
    a = open('pw4.dat', 'r')
    for i in a:
        i == i
    if i == actpwc.get():
        home4()
        w2.destroy()
        actpwc.set('')
    else:
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'パスワードが違います',
                      strings = ['OK'], default = 0)
        actpwc.set('')
def homet3():
    a = open('pw3.dat', 'r')
    for i in a:
        i == i
    if i == actpwc.get():
        home3()
        w2.destroy()
        actpwc.set('')
    else:
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'パスワードが違います',
                      strings = ['OK'], default = 0)
        actpwc.set('')
def homet2():
    a = open('pw2.dat', 'r')
    for i in a:
        i == i
    if i == actpwc.get():
        home2()
        w2.destroy()
        actpwc.set('')
    else:
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'パスワードが違います',
                      strings = ['OK'], default = 0)
        actpwc.set('')
def homet():
    a = open('pw.dat', 'r')
    for i in a:
        i == i
    if i == actpwc.get():
        home()
        w2.destroy()
        actpwc.set('')
    else:
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'パスワードが違います',
                      strings = ['OK'], default = 0)
        actpwc.set('')
def homett(event):
    if op10.get():
        a = open('pw.dat', 'r')
        for i in a:
            i == i
        if actpwc.get() == i:
            home()
            w2.destroy()
            actpwc.set('')
        else:
            Message(w2, text = u'パスワードが違います').pack()
            actpwc.set('')
    elif op11.get():
        b = open('pw2.dat', 'r')
        for i in b:
            i == i
        if actpwc.get() == i:
            home2()
            w2.destroy()
            actpwc.set('')
        else:
            Message(w2, text = u'パスワードが違います').pack()
            actpwc.set('')
    elif op12.get():
        c = open('pw3.dat', 'r')
        for i in c:
            i == i
        if actpwc.get() == i:
            home3()
            w2.destroy()
            actpwc.set('')
        else:
            Message(w2, text = u'パスワードが違います').pack()
            actpwc.set('')
    elif op13.get():
        d = open('pw4.dat', 'r')
        for i in d:
            i == i
        if actpwc.get() == i:
            home4()
            w2.destroy()
            actpwc.set('')
        else:
            Message(w2, text = u'パスワードが違います').pack()
            actpwc.set('')
def unlock4():
    global w2
    w2 = Toplevel()
    ffo = open('id4.dat', 'r')
    for data2 in ffo:
        data2 == actname
    actpwc.set('')
    w2.wm_attributes("-topmost", 1)
    w2.focus()
    Label(w2, text = '%s' % osnam).pack()
    Label(w2, text = '%s' % data2).pack()
    Entry(w2, textvariable = actpwc, show = '*').pack()
    Label(w2, textvariable = buf).pack()
    b1 = Button(w2, text = u'ログイン', command = homet4)
    b1.pack()
    b1.bind('<Return>', homett)
    b1.focus_set()
    b2 = Button(w2, text = u'ユーザー切り替え', command = act)
    b2.pack()
    b2.bind('<Return>', actss)
    b2.focus_set()
    w1.destroy()
def unlock3():
    global w2
    w2 = Toplevel()
    ffo = open('id3.dat', 'r')
    for data2 in ffo:
        data2 == actname
    actpwc.set('')
    w2.wm_attributes("-topmost", 1)
    w2.focus()
    Label(w2, text = '%s' % osnam).pack()
    Label(w2, text = '%s' % data2).pack()
    Entry(w2, textvariable = actpwc, show = '*').pack()
    Label(w2, textvariable = buf).pack()
    b1 = Button(w2, text = u'ログイン', command = homet3)
    b1.pack()
    b1.bind('<Return>', homett)
    b1.focus_set()
    b2 = Button(w2, text = u'ユーザー切り替え', command = act)
    b2.pack()
    b2.bind('<Return>', actss)
    b2.focus_set()
    w1.destroy()
def unlock2():
    global w2
    w2 = Toplevel()
    ffo = open('id2.dat', 'r')
    for data2 in ffo:
        data2 == actname
    actpwc.set('')
    w2.wm_attributes("-topmost", 1)
    w2.focus()
    Label(w2, text = '%s' % osnam).pack()
    Label(w2, text = '%s' % data2).pack()
    Entry(w2, textvariable = actpwc, show = '*').pack()
    Label(w2, textvariable = buf).pack()
    b1 = Button(w2, text = u'ログイン', command = homet2)
    b1.pack()
    b1.bind('<Return>', homett)
    b1.focus_set()
    b2 = Button(w2, text = u'ユーザー切り替え', command = act)
    b2.pack()
    b2.bind('<Return>', actss)
    b2.focus_set()
    w1.destroy()
def unlock():
    global w2
    w2 = Toplevel()
    ffo = open('id.dat', 'r')
    for data2 in ffo:
        data2 == actname
    actpwc.set('')
    w2.wm_attributes("-topmost", 1)
    w2.focus()
    Label(w2, text = '%s' % osnam).pack()
    Label(w2, text = '%s' % data2).pack()
    Entry(w2, textvariable = actpwc, show = '*').pack()
    Label(w2, textvariable = buf).pack()
    b1 = Button(w2, text = u'ログイン', command = homet)
    b1.pack()
    b1.bind('<Return>', homett)
    b1.focus_set()
    b2 = Button(w2, text = u'ユーザー切り替え', command = act)
    b2.pack()
    b2.bind('<Return>', actss)
    b2.focus_set()
    w1.destroy()
def actss(event):
    acts()
    op10.set(False)
    op11.set(False)
    op12.set(False)
    op13.set(False)
    w2.destroy()
def act():
    acts()
    op10.set(False)
    op11.set(False)
    op12.set(False)
    op13.set(False)
    w2.destroy()
def acco():
    acts()
    op10.set(False)
    op11.set(False)
    op12.set(False)
    op13.set(False)
    w1.destroy()
def myp():
    print actname.get()
    print actpw.get()
    fff = open('id.dat', 'w')
    wpw = open('pw.dat', 'w')
    fff.write(actname.get())
    wpw.write(actpw.get())
    wpw.close
    fff.close
def myp2():
    print actname.get()
    print actpw.get()
    id2 = open('id2.dat', 'w')
    pw2 = open('pw2.dat', 'w')
    id2.write(actname.get())
    pw2.write(actpw.get())
    id2.close
    pw2.close
def myp3():
    print actname.get()
    print actpw.get()
    id3 = open('id3.dat', 'w')
    pw3 = open('pw3.dat', 'w')
    id3.write(actname.get())
    pw3.write(actpw.get())
    id3.close
    pw3.close
def myp4():
    print actname.get()
    print actpw.get()
    id4 = open('id4.dat', 'w')
    pw4 = open('pw4.dat', 'w')
    id4.write(actname.get())
    pw4.write(actpw.get())
    id4.close
    pw4.close
def z():
    if actname.get():
        if actpw.get() == actpwc.get():
            if op3.get():
                myp()
                home()
                w3.destroy()
                w4.destroy()
                actname.set('')
                actpw.set('')
            if op4.get():
                myp2()
                home2()
                w3.destroy()
                w4.destroy()
                actname.set('')
                actpw.set('')
            if op5.get():
                myp3()
                home3()
                w3.destroy()
                w4.destroy()
                actname.set('')
                actpw.set('')
            if op6.get():
                myp4()
                home4()
                w3.destroy()
                w4.destroy()
                actname.set('')
                actpw.set('')
    else:
        Message(w1, text = u'アカウントは４つまでしか作れません').pack()
def zz(event):
    if actname.get():
        if actpw.get() == actpwc.get():
            if op3.get():
                myp()
                home()
                w3.destroy()
                w4.destroy()
                actname.set('')
                actpw.set('')
            if op4.get():
                myp2()
                home2()
                w3.destroy()
                w4.destroy()
                actname.set('')
                actpw.set('')
            if op5.get():
                myp3()
                home3()
                w3.destroy()
                w4.destroy()
                actname.set('')
                actpw.set('')
            if op6.get():
                myp4()
                home4()
                w3.destroy()
                w4.destroy()
                actname.set('')
                actpw.set('')
    else:
        Message(w1, text = u'アカウントは４つまでしか作れません').pack()
def unloc():
    if names.get():
        if pw.get():
            if pw.get() == buffers.get():
                myp()
                unlocks()
                w3.destroy()
        else:
            Message(w3, text = u'ユーザー名が入力されていないかパスワードが違います').pack()
            pw.set('')
            buffers.set('')
def cs():
    global w3
    w3 = Toplevel()
    f1 = Frame(w3)
    f2 = Frame(w3)
    f3 = Frame(w3)
    w3.wm_attributes("-topmost", 1)
    w3.focus()
    Label(w3, text = u'ユーザー登録').pack()
    Entry(f1, textvariable = names).pack(side = RIGHT)
    Label(f1, text = u'ID:').pack(side = LEFT)
    Entry(f2, textvariable = pw, show = '*').pack(side = RIGHT)
    Label(f2, text = u'パスワード:').pack(side = LEFT)
    Entry(f3, textvariable = buffers, show = '*').pack(side = RIGHT)
    Label(f3, text = u'確認のためもう１度入力').pack(side = LEFT)
    f1.pack()
    f2.pack()
    f3.pack()
    Button(w3, text = u'決定', command = unloc).pack()
    time()
    w2.destroy()
root.after(10, acts)
root.wm_attributes("-toolwindow", 1)
Label(root, text = u'私を消さないで').pack()
Label(root, text = u'＊消すとプログラムがお亡くなりになります').pack()
root.mainloop()
