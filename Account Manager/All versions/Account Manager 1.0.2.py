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
w1 = None
w2 = None
w3 = None
w4 = None
b = []
ad = StringVar()
def resetpwm():
    pwtitle.set('')
    pwids.set('')
    pwpw.set('')
def savepwm():
    if i1.get() == 1:
        try:
            os.mkdir("%s\\%s" % (ad.get(), pwtitle.get()))
        except WindowsError:
            pwmcon.set(u'ディレクトリが無効です')
        else:
            a = open('sysf1.dat', 'w')
            a.write(pwids.get())
            a.close()
            shutil.move("sysf1.dat", "%s\\%s" % (ad.get(), pwtitle.get()))
            b = open('sysf2.dat', 'w')
            b.write(pwpw.get())
            b.close()
            shutil.move("sysf2.dat", "%s\\%s" % (ad.get(), pwtitle.get()))
            pwmcon.set(u'保存完了')
    if i1.get() == 0:
        try:
            os.mkdir("C:\\Users\\%s\\Desktop\\PW Manager 1.0.2\\%s" % (su.get(), pwtitle.get()))
        except WindowsError:
            pwmcon.set(u'ユーザー名が正しく設定されてないか、ディレクトリに問題があります')
        a = open('sysf1.dat', 'w')
        a.write(pwids.get())
        a.close()
        shutil.move("sysf1.dat", "%s" % pwtitle.get())
        b = open('sysf2.dat', 'w')
        b.write(pwpw.get())
        b.close()
        shutil.move("sysf2.dat", "%s" % pwtitle.get())
        pwmcon.set(u'保存完了')
def searchsys():
    if i1.get() == 1:
        try:
            os.chdir("%s\\%s" % (ad.get(), pwsearch.get()))
        except WindowsError:
            pwmcon.set(u'入力された情報のデータは存在しません。')
        try:
            a = open('sysf1.dat', 'r')
            b = open('sysf2.dat', 'r')
        except IOError:
            pwmcon.set(u'ファイルが見つかりません')
        else:
            for i in a:
                pwids.set(i)
            for t in b:
                pwpw.set(t)
            pwtitle.set(pwsearch.get())
            pwmcon.set('')
            os.chdir('%s' % ad.get())
    if i1.get() == 0:
        try:
            os.chdir("%s" % pwsearch.get())
        except WindowsError:
            pwmcon.set(u'入力された情報のデータは存在しません。')
        try:
            a = open('sysf1.dat', 'r')
            b = open('sysf2.dat', 'r')
        except IOError:
            pwmcon.set(u'ファイルが見つかりません')
        else:
            for i in a:
                pwids.set(i)
            for t in b:
                pwpw.set(t)
            pwtitle.set(pwsearch.get())
            pwmcon.set('')
            os.chdir('C:\\Users\\%s\\Desktop\\PW manager 1.0.2' % su.get())
def setu():
    if su.get() == '':
        con.set(u'ユーザー名を入力してください')
    else:
        f = open('user.dat', 'w')
        f.write(su.get())
        f.close()
        w1.destroy()
        pwmcon.set('')
def cu():
    global w1
    w1 = Toplevel()
    f1 = Frame(w1)
    f2 = Frame(w1)
    con.set('')
    try:
        f = open('user.dat', 'r')
        for i in f:
            su.set(i)
    except IOError:
        pass
    Label(w1, textvariable = con).pack()
    Label(f1, text = u'このソフトを利用するコンピュータのユーザー名を入力').pack(side = LEFT)
    Entry(f1, textvariable = su).pack(side = RIGHT)
    Button(f2, text = 'OK', command = setu).pack(side = LEFT)
    Button(f2, text = 'Cancel', command = w1.destroy).pack(side = RIGHT)
    f1.pack()
    f2.pack()
def decide():
    if i1.get() == 1:
        if ad.get() == '':
            con.set(u'パスを入力してください')
        else:
            f = open('Pathad.dat', 'w')
            f.write(ad.get())
            f.close()
            w2.destroy()
            pwmcon.set('')
    if i1.get() == 0:
        w2.destroy()
def changed():
    try:
        f = open('Pathad.dat', 'r')
    except IOError:
        pass
    else:
        i1.set('1')
        for i in f:
            ad.set(i)
    global w2
    con.set('')
    w2 = Toplevel()
    f1 = Frame(w2)
    f2 = Frame(w2)
    f3 = Frame(w2)
    f4 = Frame(w2)
    Label(w2, textvariable = con).pack()
    r1 = Radiobutton(f1, text = u'フルパスで場所を指定(上級者向け)', variable = i1, value = 1)
    r1.pack(side = LEFT)
    e1 = Entry(f1, textvariable = ad)
    e1.pack(side = RIGHT)
    r2 = Radiobutton(f2, text = u'デフォルトに指定', variable = i1, value = 0)
    r2.pack()
    Button(f3, text = 'OK', command = decide).pack()
    f1.pack()
    f4.pack()
    f2.pack()
    f3.pack()
def htu():
    global w3
    w3 = Toplevel()
    Label(w3, text = u'1.[設定]にてユーザー名を登録。済んでる場合は2へ').pack()
    Label(w3, text = u'2.[設定]にて保存場所を設定する。デフォルトでいい場合3へ').pack()
    Label(w3, text = u'フルパス指定する場合はパスが間違っていると正しく保存されなくなります').pack()
    Label(w3, text = u'3.サイト・ID・PWを入力し、保存する。').pack()
    Label(w3, text = u'4.3にて保存したサイト名を検索ボックスでも同じように入力').pack()
def sup():
    global w4
    w4 = Toplevel()
    Label(w4, text = u'Q.フルパスでアカウントを保存したので保存場所をデフォルトに').pack()
    Label(w4, text = u'戻したら保存したアカウントを読み込めなくなってしまった。').pack()
    Label(w4, text = u'A.設定したフルパスに移動し、フォルダをデスクトップに移すか').pack()
    Label(w4, text = u'保存場所をフルパスに設定し、再検索してください').pack()
m0 = Menu(root)
root.configure(menu = m0)
m1 = Menu(m0, tearoff = False)
m2 = Menu(m0, tearoff = False)
m0.add_cascade(label = u'設定', under = 0, menu = m1)
m0.add_cascade(label = 'HELP', under = 0, menu = m2)
m1.add_command(label = u'ユーザー名を設定', command = cu)
m1.add_command(label = u'保存場所を設定', command = changed)
m2.add_command(label = u'使い方', command = htu)
m2.add_command(label = u'困ったときは', command = sup)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)
f7 = Frame(root)
f8 = Frame(root)
lf1 = LabelFrame(root)
lf2 = LabelFrame(root)
root.title("Account Manager 1.0.2")
Label(root, text = 'Account Manager', font = ('New Times Roman', 18)).pack()
Label(root, text = u'あらゆるサイト・ゲーム・その他のアカウントのユーザー名/パスワードを保存していつでも確認できるようにします').pack()
Label(lf1, text = u'検索ボックス').pack()
Entry(lf1, textvariable = pwsearch).pack(side = LEFT)
Button(lf1, text = u'検索', command = searchsys).pack(side = RIGHT)
Label(f8, textvariable = pwmcon).pack()
Label(f3, text = u'アカウントを保存').pack()
Label(f4, text = u'サイト名(全角)：').pack(side = LEFT)
Entry(f4, textvariable = pwtitle).pack(side = RIGHT)
Label(f5, text = 'ID:').pack(side = LEFT)
Entry(f5, textvariable = pwids).pack(side = RIGHT)
Label(f6, text = 'Password:').pack(side = LEFT)
Entry(f6, textvariable = pwpw, show = '*').pack(side = RIGHT)
Button(f7, text = u'保存', command = savepwm).pack(side = LEFT)
Button(f7, text = u'終了', command = sys.exit).pack(side = RIGHT)
Button(f7, text = u'新規作成', command = resetpwm).pack(side = RIGHT)
lf1.pack()
f8.pack()
f3.pack()
f4.pack()
f5.pack()
f6.pack()
f7.pack()
root.mainloop()
