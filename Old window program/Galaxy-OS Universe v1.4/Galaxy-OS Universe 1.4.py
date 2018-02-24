# -*- coding:utf-8-*-

from Tkinter import *
from time import *
from tkFileDialog import *
import datetime
import Dialog
import sys
import os
import ctypes
import sys, os.path
import time

path = '/home/desktop'

w1 = None
w2 = None
w3 = None
w4 = None

root = Tk()

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
op29 = BooleanVar()
ender = BooleanVar()
ender.set(True)
buf = StringVar()
buf.set('')
regent = StringVar()
actname = StringVar()
actname.set('')
actpw = StringVar()
actpw.set('')
actpwc = StringVar()
actpwc.set('')
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
pmc1 = StringVar()
pmc2 = StringVar()
pmc3 = StringVar()
pmc4 = StringVar()
pmc5 = StringVar()
pmcb = BooleanVar()
val1 = IntVar()
a1 = IntVar()
a2 = IntVar()
a3 = IntVar()
a4 = IntVar()
a5 = IntVar()
ans = 0
todayd = datetime.datetime.today()

osnam = 'Galaxy-OS Universe'
buttons = []
pmbf = []

def c_s():
    if op1.get():
        new_state = 'normal'
    else:
        new_state = 'disabled'
        a1.set('0')
    for rb in buttons:
        rb.configure(state = new_state)
def sleep():
    global w3
    w3 = Toplevel()
    cb = Checkbutton(w3, text = u'自動ロックを有効にする', variable = op1, command = c_s)
    Label(w3, text = u'作業中でもスリープモード（ロック画面）に入ってしまうのでご注意ください').pack()
    Label(w3, text = u'設定はホームから一度ロック画面に戻らないと適用されません').pack()
    Label(w3, text = u'放置すると無限にウィンドウが増え続けます').pack()
    f = LabelFrame(w3, labelwidget = cb)
    for x in (1, 3, 5, 10, 30, 60, 90, 120):
        rb = Radiobutton(f, text = u'%d分' % x, value = x, variable = a1, state = 'disabled')
        rb.pack()
        buttons.append(rb)
    f.pack(padx = 5, pady = 5)
def homesec():
    if a1.get() == 120:
        root.after(12000000, way2unlock)
    elif a1.get() == 90:
        root.after(9000000, way2unlock)
    elif a1.get() == 60:
        root.after(6000000, way2unlock)
    elif a1.get() == 30:
        root.after(1800000, way2unlock)
    elif a1.get() == 1:
        root.after(60000, way2unlock)
    elif a1.get() == 3:
        root.after(180000, way2unlock)
    elif a1.get() == 5:
        root.after(300000, way2unlock)
    elif a1.get() == 10:
        root.after(600000, way2unlock)
def done():
    if actname.get():
        if actpw.get() == actpwc.get():
            a = open('%spw.dat' % actname.get(), 'w')
            b = open('actlist.dat', 'w')
            a.write(actpw.get())
            actpwc.set('')
            w4.destroy()
        else:
            Message(w4, text = u'パスワードが違います').pack()
            actpw.set('')
            actpwc.set('')
def cna():
    global w4
    w4 = Toplevel()
    try:
        a = open('%spw.dat' % actname.get(), 'r')
    except IOError:
        Dialog.Dialog(root, title = 'error', bitmap = 'info',
                      text = u'入力したIDが存在しないかパスワードが違います',
                      strings = ['OK'], default = 0)
        actpwc.set('')
    else:
        for i in a:
            i == i
        if actpwc.get() == i:
            actpwc.set('')
            actpw.set('')
            Label(w4, text = u'新しいパスワードを入力').pack()
            Entry(w4, textvariable = actpw, show = '*').pack()
            Label(w4, text = u'確認のためもう一度入力').pack()
            Entry(w4, textvariable = actpwc, show = '*').pack()
            Button(w4, text = u'変更する', command = done).pack()
            w3.destroy()
def pca():
    global w3
    w3 = Toplevel()
    actpwc.set('')
    Label(w3, text = u'確認のためにログイン').pack()
    Label(w3, text = '%s' % actname.get()).pack()
    Entry(w3, textvariable = actpwc, show = '*').pack()
    Button(w3, text = u'次へ', command = cna).pack()
    w2.destroy()
def account():
    global w2
    w2 = Toplevel()
    Button(w2, text = u'パスワードをを変更する', command = pca).pack()
    Label(w2, text = u'＊IDは変更できません').pack()
    Button(w2, text = u'閉じる', command = w2.destroy).pack()
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
    global w2
    w2 = Toplevel()
    f1 = Frame(w2)
    f2 = Frame(w2)
    f3 = LabelFrame(w2)
    b = open('%smoney.dat' % actname.get(), 'r')
    for i in b:
        i == i
    Label(f1, text = 'Galaxy Store').pack(side = LEFT)
    Label(f2, text = '%s' % actname.get()).pack(side = LEFT)
    Label(f2, text = u'クレジット %s円' % i).pack(side = RIGHT)
    Label(f3, text = u'アプリ一覧：').pack()
TIME = 60*3
def timer():   
    time = 0
    timestr =  StringVar()
    timestr.set("03:00")
    l = Label(self, textvariable = self.timestr)
    b1 = Button(self, text = 'Start', command = self.countdown)
    b2 = Button(self, text = 'Quit', command = self.master.destroy)
    for obj, sideparam in ((l,TOP),(b1,LEFT),(b2,RIGHT)):
        obj.pack(side = sideparam)
    self.pack()
def countdown(self):
    if self.time == 0:
        self.time = time.time()
    timeleft = max(TIME-(time.time()-self.time), 0)
    min,sec = (timeleft) / 60, timeleft % 60
    timestr.set("%02d:%02d" % (min,sec))
    root.after(1000, countdown)
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
    ans = a1+a2+a3+a4+a5+a6+a7+a8+a9+a0
    o = int(z)
    Label(w3, text = u'合計金額').pack()
    Label(w3, text = '%d' % ans).pack()
    Label(w3, text = u'お預かり').pack()
    Label(w3, text = '%d' % o).pack()
    Button(w3, text = u'閉じる', command = w3.destroy).pack()
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
    for i in (e0, e1, e2, e3, e4, e5, e6, e7, e8, e9):
        Label(f1, textvariable = i).pack()
    Label(f2, text = u'値段').pack()
    for x in (e10, e11, e12, e13, e14, e15, e16, e17, e18, e19):
        Label(f2, textvariable = x).pack()
    Label(f3, text = u'数量').pack()
    for y in (e20, e21, e22, e23, e24, e25, e26, e27, e28, e29):
        Label(f3, textvariable = y).pack()
    Label(f4, text = u'商品合計').pack()
    for H in (a10, a11, a12, a13, a14, a15, a16, a17, a18, a19):
        Label(f4, text = u'%d円' % H).pack()
    Label(f5, text = u'全てを含めた合計').pack()
    for SP in (a1, a2, a3, a4, a5, a6, a7, a8, a9, a0):
        Label(f5, text = u'%d円' % SP).pack()
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
    for i in (e0, e1, e2, e3, e4, e5, e6, e7, e8, e9):
        i.set('')
    for x in (e10, e11, e12, e13, e14, e15, e16, e17, e18, e19,e30, e31, e32, e33, e34, e35, e36, e37, e38, e39, e40, e41, e42, e43, e44, e45, e46, e47, e48, e49):
        x.set('0')
    for y in (e20, e21, e22, e23, e24, e25, e26, e27, e28, e29):
        y.set('1')
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
    for i in (e0, e1, e2, e3, e4, e5, e6, e7, e8, e9):
        Entry(f0, textvariable = i).pack()
    Label(f1, text = u'値段').pack()
    for x in (e10, e11, e12, e13, e14, e15, e16, e17, e18, e19):
        Entry(f1, textvariable = x).pack()
    Label(f3, text = u'送料').pack()
    for y in (e30, e31, e32, e33, e34, e35, e36, e37, e38, e39):
        Entry(f3, textvariable = y).pack()
    Label(f2, text = u'数量').pack()
    for H in (e20, e21, e22, e23, e24, e25, e26, e27, e28, e29):
        H.set('1')
        Entry(f2, textvariable = H).pack()
    Label(f4, text = u'手数料').pack()
    for SP in (e40, e41, e42, e43, e44, e45, e46, e47, e48, e49):
        Entry(f4, textvariable = SP).pack()
    Button(f5, text = u'計算', command = regc).pack()
    Button(f5, text = u'初期化', command = erase).pack()
    Button(f5, text = u'閉じる', command = w1.destroy).pack()
    f4.pack(side = RIGHT)
    f3.pack(side = RIGHT)
    f2.pack(side = RIGHT)
    f1.pack(side = RIGHT)
    f0.pack(side = RIGHT)
    f5.pack(side = RIGHT)
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
    a = open('%spm.dat' % actname.get(), 'w')
    a.write(str(x))
    b = open('%spmt.dat' % actname.get(), 'a')
    b.write(o+'\n')
    c = open('%spmp.dat' % actname.get(), 'a')
    c.write(str(n)+'\n')
def rpmoney():
    global w3
    w3 = Toplevel()
    f1 = LabelFrame(w3)
    f2 = LabelFrame(w3)
    a = open('%spmp.dat' % actname.get(), 'r')
    b = open('%spmt.dat' % actname.get(), 'r')
    x = a.readlines()
    y = b.readlines()
    Label(w3, text = u'小遣い使用レポート').pack()
    for aa in y:
        Label(f1, text = '%s' % aa).pack()
    for bb in x:
        Label(f2, text = '%s' % bb).pack()
    f1.pack()
    f2.pack()
def poket():
    pm2.set('')
    pm3.set('0')
    pm4.set('0')
    a = open('%spm.dat' % actname.get(), 'r')
    for i in a:
        i == i
    pm1.set(i)
def pmoney():
    global w2
    w2 = Toplevel()
    a = open('%spm.dat' % actname.get(), 'r')
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
    Button(w2, text = u'閉じる', command = w2.destroy).pack()
def poweropt():
    if val1.get() == 0:
        w2.destroy()
    elif val1.get() == 1:
        w2.destroy()
        unlock()
    elif val1.get() == 2:
        sys.exit()
    elif val1.get() == 3:
        os.system('shutdown -s -f')
        sys.exit()
    elif val1.get() == 4:
        os.system('shutdown -r -f')
        sys.exit()
    elif val1.get() == 5:
        ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)
        w2.destroy()
    elif val2.get() == 6:
        ctypes.windll.PowrProf.SetSuspendState(1, 1, 0)
        w2.destroy()
def power():
    global w2
    w2 = Toplevel()
    Label(w2, text = u'ユーザー：%s' % actname.get()).pack()
    Label(w2, text = u'電源オプション').pack()
    lf1 = LabelFrame(w2)
    lf2 = LabelFrame(w2)
    Label(lf1, text = u'プログラムを').pack()
    Radiobutton(lf1, text = u'ログオフ/ユーザー切り替え', variable = val1, value = 1).pack()
    Radiobutton(lf1, text = u'終了', variable = val1, value = 2).pack()
    Label(lf2, text = u'コンピュータを').pack()
    Radiobutton(lf2, text = u'シャットダウン', variable = val1, value = 3).pack()
    Radiobutton(lf2, text = u'再起動', variable = val1, value = 4).pack()
    Radiobutton(lf2, text = u'スリープ', variable = val1, value = 5).pack()
    Radiobutton(lf2, text = u'休止', variable = val1, value = 6).pack()
    Radiobutton(w2, text = u'キャンセル', variable = val1, value = 0).pack()
    Button(w2, text = u'決定', command = poweropt).pack()
    lf1.pack()
    lf2.pack()
def about():
    global w2
    w2 = Toplevel()
    Label(w2, text = u'ソフトウェア情報').pack()
    Label(w2, text = u'ソフトウェア名:Galaxy-OS Universe').pack()
    Label(w2, text = u'バージョン:1.4').pack()
    Label(w2, text = u'ライセンス:完全版').pack()
    Label(w2, text = u'開発者:Galaxy-OS Universe Dev Team').pack()
    Button(w2, text = u'閉じる', command = w2.destroy).pack()
def asisuto():    
    if a4.get() == 3:
        new_state = 'normal'
    else:
        new_state = 'disabled'
    for b in pmbf:
        b.configure(state = new_state)
def ahelp():
    global w3
    w3 = Toplevel()
    Label(w3, textvariable = pmc1).pack()
    if a2.get() == 2:
        Label(w3, text = u'まず、本当に必要でない物は買わないほうがいいでしょう').pack()
        if a3.get() == 1:
            if int(pmc4.get()) > int(pmc3.get()):
                i = int(pmc4.get()) - int(pmc3.get())
                if i < 1000:
                    Label(w3, text = u'予算からすると安い買い物とは思えません').pack()
                elif i < 3000:
                    Label(w3, text = u'予算からしてそこそこの金額は残るみたいですが').pack()
                elif i > 3000:
                    Label(w3, text = u'確かに予算からしたら安い買い物かもしれませんが').pack()
                Label(w3, text = u'安い物には安物買いの銭失いになる可能性があるので注意してください').pack()
        if a3.get() == 2:
            if int(pmc4.get()) > int(pmc3.get()):
                i = int(pmc4.get()) - int(pmc3.get())
                if i < 1000:
                    Label(w3, text = u'将来に備えるにしても予算からして安い買い物では無いと思いますのでよく考えてください').pack()
                elif i < 3000:
                    Label(w3, text = u'将来に備えるなら予算からしてそこそこの金額は残るみたいなので買うのもありかもしれません').pack()
                elif i > 3000:
                    Label(w3, text = u'確かに予算からしたら安い買い物だと思いますので将来に備えるための購入なら良いんじゃないでしょうか？').pack()
                Label(w3, text = u'いざというときにはそういう関連のものは入手困難になりやすいので、予算が許すのであれば購入するのもありでしょう').pack()
        if a3.get() == 3:
            Label(w3, text = u'物にもよりますが、今は人気があるといってもいずれは人気が無くなるので、欲しいだけなら購入を控えることを強くお勧めします').pack()
            if int(pmc4.get()) - int(pmc3.get()) > 3000:
                Label(w3, text = u'予算的に余裕はあるみたいですが必要でなければ買わないほうが良いでしょう').pack()
            elif int(pmc4.get()) - int(pmc3.get()) < 3000:
                Label(w3, text = u'予算的な余裕もあまりないみたいなので買わないほうが良いと思います').pack()
        if a3.get() == 4:
            Label(w3, text = u'確かに新商品はかなり気になりますので予算が許すのであれば購入もいいんじゃないですか？ただ、商品のレビューは見てからのほうがいいでしょう').pack()
        if a4.get() == 5:
            Label(w3, text = u'予算が許すならば普段使うものへの出費は可だと思います。').pack()
    if a2.get() == 1:
        Label(w3, text = u'必要なら買っておくべきでしょう').pack()
def pm():
    global w2
    w2 = Toplevel()
    lf1 = LabelFrame(w2)
    lf2 = LabelFrame(w2)
    lf3 = LabelFrame(w2)
    lf4 = LabelFrame(w2)
    Label(w2, text = u'無駄遣い防止').pack()
    Label(w2, text = u'この機能は何か物を買おうとして迷っているとき、それが本当に必要かを考え').pack()
    Label(w2, text = u'理由を具体的に述べて無駄遣いをしないように「助ける」ものです。機能アシ').pack()
    Label(w2, text = u'ストの性能はまだ低いので、あくまでも参考程度にしてください。全項目入力').pack()
    Label(lf1, text = u'買おうか迷っているもの:').pack()
    Entry(lf1, textvariable = pmc1).pack()
    Label(lf1, text = u'値段:').pack()
    Entry(lf1, textvariable = pmc3).pack()
    Label(lf1, text = u'予算:').pack()
    Entry(lf1, textvariable = pmc4).pack()
    Label(lf2, text = u'買おうとしている理由:').pack()
    Checkbutton(lf2, text = u'安い', variable = pmcb).pack()
    Radiobutton(lf2, text = u'安くて興味がある', variable = a3, value = 1).pack()
    Radiobutton(lf2, text = u'安いからいざというときに備える', variable = a3, value = 2).pack()
    Radiobutton(lf2, text = u'人気がある', variable = a3, value = 3).pack()
    Radiobutton(lf2, text = u'新商品だから', variable = a3, value = 4).pack()
    Radiobutton(lf2, text = u'実用性があり、普段の使用に最適', variable = a3, value = 5).pack()
    Radiobutton(lf2, text = u'その他:', variable = a3, value = 6).pack()
    Entry(lf2, textvariable = pmc2).pack()
    Label(lf3, text = u'それは「必要」な物？「欲しい」物？').pack()
    Radiobutton(lf3, text = u'必要な物', variable = a2, value = 1).pack()
    Radiobutton(lf3, text = u'欲しい物', variable = a2, value = 2).pack()
    Label(lf4, text = u'上記をもう１度確認して').pack()
    Radiobutton(lf4, text = u'欲しい/必要なので買う', variable = a4, value = 1, command = asisuto).pack()
    Radiobutton(lf4, text = u'やっぱりいらないので買わない', variable = a4, value = 2, command = asisuto).pack()
    Radiobutton(lf4, text = u'決まらないので機能アシストに相談', variable = a4, value = 3, command = asisuto).pack()
    b = Button(lf4, text = u'機能アシスト', state = 'disabled', command = ahelp)
    b.pack()
    pmbf.append(b)
    lf1.pack()
    lf2.pack()
    lf3.pack()
    lf4.pack()
def home():
    root.wm_attributes('-fullscreen', 1)
    a = actname.get()
    f0 = Frame(root)
    f4 = Frame(root)
    f5 = Frame(root)
    f6 = Frame(root)
    f7 = Frame(root)
    nam = 'Galaxy-OS Universe'
    b1 = Button(f4, text = 'Account', width = 5, height = 2, command = account)
    b1.pack()
    Label(f4, text = u'アカウント').pack()
    b2 = Button(f4, text = 'Timer', width = 5, height = 2, command = timer).pack()
    Label(f4, text = u'タイマー').pack()
    b3 = Button(f4, text = u'会計', width = 5, height = 2, command = regi).pack()
    Label(f4, text = u'会計ソフト').pack()
    b4 = Button(f4, text = 'Market', width = 5, height = 2, command = market).pack()
    Label(f4, text = u'マーケット').pack()
    b5 = Button(f4, text = u'setting', width = 5, height = 2, command = sleep).pack()
    Label(f4, text = u'設定').pack()
    Button(f4, text = 'MEMO', width = 5, height = 2, command = pmoney).pack()
    Label(f4, text = u'小遣い管理・計算').pack()
    Button(f4, text = u'無駄', width = 5, height = 2, command = pm).pack()
    Label(f4, text = u'無駄遣い防止').pack()
    Button(f4, text = 'About', width = 5, height = 2, command = about).pack()
    Label(f4, text = u'ソフト情報').pack()
    Label(f6, text = 'Galaxy-OS Universe', font = ('New Times Roman', 48), width = 80, height = 10).pack()
    Button(f7, text = 'Galaxy', command = power).pack(side = LEFT)
    Label(f7, text = '%s/%s/%s' % (todayd.year, todayd.month, todayd.day)).pack(side = RIGHT)
    Label(f7, textvariable = buf).pack(side = RIGHT)
    f7.pack(padx = 20, pady = 20,side = BOTTOM)
    f4.pack(side = LEFT)
    f5.pack(side = LEFT)
    f6.pack()
    time()
    homesec()
def makeid():
    if actname.get() and actpw.get() and actpwc.get() and actpw.get() == actpwc.get():
        try:
            y = open('%s.dat' % actname.get(), 'r')
        except IOError:
            a = open('%s.dat' % actname.get(), 'w')
            c = open('%smoney.dat' % actname.get(), 'w')
            f = open('%spm.dat' % actname.get(), 'w')
            g = open('%spmp.dat' % actname.get(), 'w')
            h = open('%spmt.dat' % actname.get(), 'w')
            i = open('%spw.dat' % actname.get(), 'w')
            b = open('actlist.dat', 'a')
            a.write(actname.get()+'\n')
            i.write(actpw.get())
            b.write(actname.get()+'\n')
            c.write(str(0))
            f.write(str(0))
            a.close()
            b.close()
            c.close()
            f.close()
            g.close()
            h.close()
            i.close()
            actpwc.set('')
            home()
            w3.destroy()
        else:
            Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                          text = u'入力されたIDは常に登録されています',
                          strings = ['OK'], default = 0)
    else:
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'アカウント情報を入力してください',
                      strings = ['OK'], default = 0)  
def one():
    global w3
    w3 = Toplevel()
    f1 = Frame(w3)
    f2 = Frame(w3)
    f3 = Frame(w3)
    f4 = Frame(w3)
    Label(w2, text = '%s' % osnam).pack()
    Label(w2, text = u'アカウント作成').pack()
    Entry(f1, textvariable = actname).pack(side = RIGHT)
    Label(f1, text = u'アカウント名(変更不可)').pack(side = LEFT)
    Entry(f2, textvariable = actpw, show = '*').pack(side = RIGHT)
    Label(f2, text = u'パスワード').pack(side = LEFT)
    Entry(f3, textvariable = actpwc, show = '*').pack(side = RIGHT)
    Label(f3, text = u'確認のためもう一度入力').pack(side = LEFT)
    b13 = Button(f4, text = u'作成', command = makeid)
    b13.pack(side = LEFT)
    b13.bind('<Return>')
    b13.focus_set()
    f1.pack()
    f2.pack()
    f3.pack()
    f4.pack()
    w2.destroy()
def filecheck():
    try:
        c = open('%smoney.dat' % actname.get(), 'r')
        f = open('%spm.dat' % actname.get(), 'r')
        g = open('%spmp.dat' % actname.get(), 'r')
        h = open('%spmt.dat' % actname.get(), 'r')
    except IOError:
        c = open('%smoney.dat' % actname.get(), 'w')
        f = open('%spm.dat' % actname.get(), 'w')
        g = open('%spmp.dat' % actname.get(), 'w')
        h = open('%spmt.dat' % actname.get(), 'w')
        c.write(str(0))
        f.write(str(0))
        c.close()
        f.close()
        g.close()
        h.close()
        print u'必要なファイルを追加しました'
        home()
    else:
        c.close()
        f.close()
        g.close()
        h.close()
        home()
def login():
    aa = actname.get()
    bb = actpwc.get()
    try:
        a = open('%spw.dat' % aa, 'r')
    except IOError:
        Dialog.Dialog(root, title = 'error', bitmap = 'info',
                      text = u'入力したIDが存在しないかパスワードが違います',
                      strings = ['OK'], default = 0)
        actpwc.set('')
    else:
        for i in a:
            i == i
        if aa and bb == i:
                filecheck()
                actpwc.set('')
                w2.destroy()
                a.close()
def actlog():
    global w2
    w2 = Toplevel()
    w2.wm_attributes('-fullscreen', 1)
    Label(w2, text = u'ID').pack()
    Entry(w2, textvariable = actname).pack()
    Label(w2, text = u'パスワード').pack()
    Entry(w2, textvariable = actpwc, show = '*').pack()
    Button(w2, text = u'ログイン', command = login).pack()
    Button(w2, text = u'もしくはアカウント作成', command = one).pack()
    Button(w2, text = u'終了', command = sys.exit).pack()
def time():
    buf.set(strftime('%H:%M:%S'))
    root.after(1000, time)
def homet():
    try:
        a = open('%spw.dat' % actname.get(), 'r')
    except IOError:
        Dialog.Dialog(root, title = 'error', bitmap = 'info',
                      text = u'入力したIDが存在しないかパスワードが違います',
                      strings = ['OK'], default = 0)
        actpwc.set('')
    else:
        for i in a:
            i == i
        if actname.get() and actpwc.get() == i:
            w2.destroy()
            actpwc.set('')
            a.close()
def homett(event):
    try:
        a = open('%spw.dat' % actname.get(), 'r')
    except IOError:
        Dialog.Dialog(root, title = 'error', bitmap = 'info',
                      text = u'入力したIDが存在しないかパスワードが違います',
                      strings = ['OK'], default = 0)
        actpwc.set('')
    else:
        for i in a:
            i == i
        if actname.get() and actpwc.get() == i:
            w2.destroy()
            actpwc.set('')
            a.close()
def way2unlock():
    if ender.get():
        root.lower()
        unlock()
def unlock():
    global w2
    w2 = Toplevel()
    w2.wm_attributes('-fullscreen', 1)
    Label(w2, text = '%s' % osnam).pack()
    Label(w2, text = u'＊他のアカウントにもログインできます').pack()
    Entry(w2, textvariable = actname).pack()
    Entry(w2, textvariable = actpwc, show = '*').pack()
    Label(w2, textvariable = buf).pack()
    b1 = Button(w2, text = u'ログイン', command = homet)
    b1.pack()
    b1.bind('<Return>', homett)
    b1.focus_set()
    Button(w2, text = u'終了', command = sys.exit).pack()
try:
    of = open('License.dat', 'r')
except IOError:
    Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                  text = u'ライセンス認証プログラムでライセンス認証されていないため、本ソフトを起動できませんでした。終了します',
                  strings = ['OK'], default = 0)
    sys.exit()
else:
    for of2 in of:
        of2 == of2
    if of2 == 'disable':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                  text = u'ライセンス認証プログラムでライセンス認証されていないため、本ソフトを起動できませんでした。終了します',
                  strings = ['OK'], default = 0)
        sys.exit()
    elif of2 == 'able':
        actlog()
root.mainloop()
