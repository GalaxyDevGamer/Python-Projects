# coding:shift-jis

from Tkinter import *
root = Tk()
import sys
import os
import sys, os.path
import shutil
import subprocess
pwsearch = StringVar()
pwtitle = StringVar()
pwids = StringVar()
pwpw = StringVar()
pwmcon = StringVar()
su = StringVar()
con = StringVar()
i1 = IntVar()
i2 = IntVar()
i2.set('0')
cb1 = BooleanVar()
cb2 = BooleanVar()
w1 = None
w2 = None
w3 = None
w4 = None
b = []
ad = StringVar()
currentdir = os.getcwd()
ids = StringVar()
pws = StringVar()
loginst = StringVar()
loginst2 = StringVar()
logincon = StringVar()
secobj1 = []
secobj2 = []
try:
    os.mkdir("dir")
except WindowsError:
    os.chdir("dir")
    curd = os.getcwd()
else:
    os.chdir("dir")
    curd = os.getcwd()
def tyuu():
    f1 = open('ID.dat', 'r')
    f2 = open('PW.dat', 'r') 
    for i in f1:
        i==i
    for ii in f2:
        ii==ii
    if loginst.get() == i and loginst2.get() == ii:
        new_state = 'normal'
        e1.configure(state = new_state)
        sb1.configure(state = new_state)
        se1.configure(state = new_state)
        ie1.configure(state = new_state)
        pe1.configure(state = new_state)
        sb2.configure(state = new_state)
        sb3.configure(state = new_state)
        w2.destroy()
    else:
        logincon.set(u'ID又はパスワードが違います')
def ninsyou():
    global w2
    w2 = Toplevel()
    llf = Frame(w2)
    llf2 = Frame(w2)
    llf3 = Frame(w2)
    Label(w2, text = u'セキュリティ認証').pack()
    Label(w2, textvariable = logincon).pack()
    Label(llf, text = 'ID:').pack(side = LEFT)
    Entry(llf, textvariable = loginst).pack(side = RIGHT)
    Label(llf2, text = 'PW:').pack(side = LEFT)
    Entry(llf2, textvariable = loginst2, show = '*').pack(side = RIGHT)
    Button(llf3, text = u'ログイン', command = tyuu).pack(side = LEFT)
    Button(llf3, text = u'終了', command = sys.exit).pack(side = RIGHT)
    llf.pack()
    llf2.pack()
    llf3.pack()
    cb1.set(True)
def resetpwm():
    pwtitle.set('')
    pwids.set('')
    pwpw.set('')
def savepwm():
    os.chdir(curd)
    try:
        os.mkdir(pwtitle.get())
    except WindowsError:
        pwmcon.set(u'原因不明のエラーが発生しました')
    a = open('sysf1.dat', 'w')
    a.write(pwids.get())
    a.close()
    shutil.move("sysf1.dat", "%s" % pwtitle.get())
    b = open('sysf2.dat', 'w')
    b.write(pwpw.get())
    b.close()
    shutil.move("sysf2.dat", "%s" % pwtitle.get())
    pwmcon.set(u'保存完了')
def search2(event):
    os.chdir(curd)
    try:
        os.chdir(pwsearch.get())
    except WindowsError:
        pwmcon.set(u'入力されたアカウント情報が見つかりませんでした。')
    else:
        try:
            a = open('sysf1.dat', 'r')
            b = open('sysf2.dat', 'r')
        except IOError:
            pwmcon.set(u'ファイルが見つかりません')
            os.chdir("%s\\dir" % curd)
        else:
            for i in a:
                pwids.set(i)
            for t in b:
                pwpw.set(t)
            pwtitle.set(pwsearch.get())
            pwmcon.set('')
            os.chdir(curd)
def searchsys():
    os.chdir(curd)
    try:
        os.chdir(pwsearch.get())
    except WindowsError:
        pwmcon.set(u'入力されたアカウント情報が見つかりませんでした。')
    else:
        try:
            a = open('sysf1.dat', 'r')
            b = open('sysf2.dat', 'r')
        except IOError:
            pwmcon.set(u'ファイルが見つかりません')
            os.chdir(curd)
        else:
            for i in a:
                pwids.set(i)
            for t in b:
                pwpw.set(t)
            pwtitle.set(pwsearch.get())
            pwmcon.set('')
            os.chdir(curd)
def sec2():
    if cb1.get():
        if ids.get() and pws.get():
            f1 = open('ID.dat', 'w')
            f2 = open('PW.dat', 'w')
            f1.write(ids.get())
            f2.write(pws.get())
            f1.close()
            f2.close()
            w1.destroy()
        else:
            Message(w1, text = u'ID又はPWが入力されていません').pack()
    else:
        try:
            os.remove("ID.dat")
            os.remove("PW.dat")
        except WindowsError:
            pass
        w1.destroy()
def seccs():
    if cb1.get() or os.path.isfile("ID.dat") and os.path.isfile("PW.dat"):
        new_state = 'normal'
    else:
        new_state = 'disabled'
    for sece1 in secobj1:
        try:
            sece1.configure(state = new_state)
        except TclError:
            pass
    for sece2 in secobj2:
        try:
            sece2.configure(state = new_state)
        except TclError:
            pass
            
def security():
    global w1
    if w1 is None or not w1.winfo_exists():
        try:
            f1 = open('ID.dat', 'r')
            f2 = open('PW.dat', 'r')
        except IOError:
            pass
        else:
            for x in f1:
                ids.set(x)
            for y in f2:
                pws.set(y)
        w1 = Toplevel()
        f1 = Frame(w1)
        f2 = Frame(w1)
        f3 = Frame(w1)
        f4 = Frame(w1)
        Label(w1, text = u'セキュリティ設定').pack()
        c1 = Checkbutton(w1, text = u'プログラム起動時にログインを求める', variable = cb1, command = seccs).pack()
        Label(f1, text = 'ID:').pack(side = LEFT)
        sece1 = Entry(f1, textvariable = ids, state = 'disabled')
        sece1.pack(side = RIGHT)
        Label(f2, text = 'PW:').pack(side = LEFT)
        sece2 = Entry(f2, textvariable = pws, show = '*', state = 'disabled')
        sece2.pack(side = RIGHT)
        c2 = Checkbutton(f3, text = u'アカウントを暗号化して保存する', variable = cb2).pack()
        Button(f4, text = 'OK', command = sec2).pack()
        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()
        secobj1.append(sece1)
        secobj2.append(sece2)
        seccs()
    else:
        w1.deiconify()
def htu():
    global w3
    w3 = Toplevel()
    Label(w3, text = u'1. サイト・ID・PWを入力し、保存する。').pack()
    Label(w3, text = u'2. 1にて保存したサイト名を検索ボックスでも同じように入力').pack()
m0 = Menu(root)
root.configure(menu = m0)
m1 = Menu(m0, tearoff = False)
m2 = Menu(m0, tearoff = False)
m0.add_cascade(label = u'設定', under = 0, menu = m1)
m1.add_command(label = u'セキュリティ', command = security)
m0.add_cascade(label = 'HELP', under = 0, menu = m2)
m2.add_command(label = u'使い方', command = htu)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)
f7 = Frame(root)
f8 = Frame(root)
lf1 = LabelFrame(root)
lf2 = LabelFrame(root)
root.title("Account Manager")
Label(root, text = 'Account Manager', font = ('New Times Roman', 18)).pack()
Label(root, text = u'あらゆるサイト・ゲーム・その他のアカウントのユーザー名/パスワードを保存していつでも確認できるようにします').pack()
Label(lf1, text = u'保存したアカウントを検索').pack()
e1 = Entry(lf1, textvariable = pwsearch, state = 'disabled')
e1.pack(side = LEFT)
e1.bind('<Return>', search2)
sb1 = Button(lf1, text = u'検索', command = searchsys, state = 'disabled')
sb1.pack(side = RIGHT)
Label(f8, textvariable = pwmcon).pack()
Label(f3, text = u'アカウントの保存及び保存したアカウントの表示').pack()
Label(f4, text = u'サイト名(全角)：').pack(side = LEFT)
se1 = Entry(f4, textvariable = pwtitle, state = 'disabled')
se1.pack(side = RIGHT)
Label(f5, text = '                 ID:').pack(side = LEFT)
ie1 = Entry(f5, textvariable = pwids, state = 'disabled')
ie1.pack(side = RIGHT)
Label(f6, text = '       Password:').pack(side = LEFT)
pe1 = Entry(f6, textvariable = pwpw, show = '*', state = 'disabled')
pe1.pack(side = RIGHT)
sb2 = Button(f7, text = u'保存', command = savepwm, state = 'disabled')
sb2.pack(side = LEFT)
Button(f7, text = u'終了', command = sys.exit).pack(side = RIGHT)
sb3 = Button(f7, text = u'新規作成', command = resetpwm, state = 'disabled')
sb3.pack(side = RIGHT)
lf1.pack()
f8.pack()
f3.pack()
f4.pack()
f5.pack()
f6.pack()
f7.pack()
try:
    open('ID.dat', 'r')
    open('PW.dat', 'r')
except IOError:
    new_state = 'normal'
    e1.configure(state = new_state)
    sb1.configure(state = new_state)
    se1.configure(state = new_state)
    ie1.configure(state = new_state)
    pe1.configure(state = new_state)
    sb2.configure(state = new_state)
    sb3.configure(state = new_state)
else:
    ninsyou()
root.mainloop()
