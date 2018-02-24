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

osnam = 'Galaxy-OS Universe'
f0 = Frame(root)
buttons = []
        
if op2.get():
    op3 = op13
    op4 = op14
    op5 = op15
    op6 = op16
    op7 = op17
    op8 = op18
    op9 
    op10 
    op11 
    op12 
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
def ru():
    root.lower()
    unlock()
    op28.set(True)
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
def idc():
    fff = open('id.dat', 'w')
    fff.write(actname.get())
    fff.close
    w4.destroy()
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
def done():
    if actpw.get() == actpwc.get():
        wpw = open('pw.dat', 'w')
        wpw.write(actpw.get())
        wpw.close
        w4.destroy()
    else:
        Message(w4, text = u'パスワードが違います').pack()
        pw.set('')
        buffers.set('')
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
        buffer.set('')
def pca():
    global w3
    w3 = Toplevel()
    actpwc.set('')
    Label(w3, text = u'古いパスワードを入力').pack()
    Entry(w3, textvariable = actpwc, show = '*').pack()
    Button(w3, text = u'次へ', command = cna).pack()
    w2.destroy()
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
    fn = askopenfilename(filetypes = [('All Files', '*'),
                                      ('JPG Files', '.jpg'),
                                      ('PPM FIles', '.ppm')],initialdir = path)
    if fn != '':
            path = os.path.dirname(fn)
            picdata = Tkinter.PhotoImage(file = fn)
            label.configure(image = picdata)
def home():
    f4 = Frame(root)
    ver = 2
    vers = 1
    ffo = open('id.dat', 'r')
    for data2 in ffo:
        actname = data2 
    nam = 'Galaxy-OS Universe'
    Label(root, text = u'%s %d.%d' % (nam, ver, vers)).pack()
    picdata = PhotoImage(width = 64, height = 64)
    label1 = Label(f0, image = picdata).pack()
    Button(f0, text = 'Load', command = loadpic).pack()
    Label(f0, text = u'ユーザー:').pack(in_ = f0, side = LEFT)
    Label(f0, text = '%s' % data2).pack(in_ = f0, side = LEFT)
    f0.pack(fill = BOTH)
    Button(f4, text = 'A', command = account).pack(fill = BOTH)
    Label(f4, text = u'アカウント').pack(fill = BOTH)
    Button(f4, text = u'†', command = set).pack(fill = BOTH)
    Label(f4, text = u'設定').pack(fill = BOTH)
    Button(f4, text = 'L', command = ru).pack(fill = BOTH)
    Label(f4, text = u'ロック画面に戻る').pack(fill = BOTH)
    buttons.append(f0)
    buttons.append(root)
    buttons.append(f4)
    f4.pack()
    time()

def pok():
    global w3
    ffo = open('pw.dat', 'r')
    for data1 in ffo:
        actpw == data1
    if actpwc.get() == data1:
        if op28.get():
            w2.destroy()
            w1.destroy()
            root.lift()
            buffe.set('')
        else:
            w2.destroy()
            w1.destroy()
            home()
            buffe.set('')
    else:
        Message(w2, text = u'パスワードが違います').pack()
        buffe.set('')
def homes():
    w2.destroy()
def hometo():
    root.lift()
    w2.destroy()
        
def sc():
    global w2
    w2 = Toplevel()
    rpw = open('id.dat', 'r')
    for data2 in rpw:
        actname == data2
    actpwc.set('')
    w2.wm_attributes("-topmost", 1)
    Label(w2, text = '%s' % osnam).pack()
    Label(w2, text = '%s' % data2).pack()
    Entry(w2, textvariable = actpwc, show = '*').pack()
    Button(w2, text = u'決定', command = pok).pack()
    w1.destroy()
def time():
    buf.set(strftime('%H:%M:%S'))
    root.after(1000, time)
def unlock():
    global w1
    w1 = Toplevel()
    ffo = open('id.dat', 'r')
    for data2 in ffo:
        data2 == actname
    actpwc.set('')
    w1.wm_attributes("-topmost", 1)
    Label(w1, text = '%s' % osnam).pack()
    Label(w1, text = '%s' % data2).pack()
    Entry(w1, textvariable = actpwc, show = '*').pack()
    Label(w1, textvariable = buf).pack()
    Button(w1, text = u'ログイン', command = w1.destroy).pack()
def myp():
    print actname.get()
    print actpw.get()
    fff = open('id.dat', 'w')
    wpw = open('pw.dat', 'w')
    fff.write(actname.get())
    wpw.write(actpw.get())
    wpw.close
    fff.close
def z():
    if actname.get():
        if actpw.get() == actpwc.get():
            myp()
            home()
            w1.destroy()
def unlocks():
    global w1
    w1 = Toplevel()
    mypr()
    f1 = Frame(w1)
    f2 = Frame(w1)
    f3 = Frame(w1)
    f4 = Frame(w1)
    w1.wm_attributes("-topmost", 1)
    Label(w1, text = '%s' % osnam).pack()
    Label(w1, text = u'アカウント作成').pack()
    Entry(f1, textvariable = actname).pack(side = RIGHT)
    Label(f1, text = u'アカウント名').pack(side = LEFT)
    Entry(f2, textvariable = actpw, show = '*').pack(side = RIGHT)
    Label(f2, text = u'パスワード').pack(side = LEFT)
    Entry(f3, textvariable = actpwc, show = '*').pack(side = RIGHT)
    Label(f3, text = u'確認のためもう一度入力').pack(side = LEFT)
    Button(f4, text = u'すでにアカウントを持ってる場合', command = sc).pack(side = RIGHT)
    Button(f4, text = u'作成', command = z).pack(side = LEFT)
    f1.pack()
    f2.pack()
    f3.pack()
    f4.pack()
    time()
    root.lower()
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
            buffer.set('')
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
def mypr():
    ffo = open('pw.dat', 'r')
    rpw = open('id.dat', 'r')
    for data1 in ffo:
        print data1
        actpw == data1
    for data2 in rpw:
        print data2
        actname == data2
root.after(10, unlocks)


root.mainloop()
