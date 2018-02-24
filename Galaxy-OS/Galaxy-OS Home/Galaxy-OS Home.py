# -*- coding:shift-jis-*-

from Tkinter import *
from time import *
from tkFileDialog import *
from ScrolledText import *
import tkFileDialog as dialog

import datetime
import Dialog
import sys
import os
import shutil
import ctypes
import sys, os.path
import time
import Crypto.Cipher.DES
import tkMessageBox
import codecs
import tkFileDialog as D
import os, zipfile
import zipfile
import stat
path = 'C://Users//Galaxy//Desktop//Galaxy-OS Universe 1.7 Personal'
enckey = Crypto.Cipher.DES.new("galaxygi", Crypto.Cipher.DES.MODE_ECB)
enckey2 = Crypto.Cipher.DES.new("kudoukey", Crypto.Cipher.DES.MODE_ECB)
w1 = None
w2 = None
w3 = None
w4 = None
w5 = None
w6 = None
w7 = None
w8 = None
w9 = None
w10 = None
w11 = None
w12 = None
w13 = None
w14 = None
w15 = None
w16 = None

root = Tk()
aaa = StringVar()
bbb = StringVar()
ccc = StringVar()
ddd = StringVar()
sysfop1 = BooleanVar()
sysfop2 = BooleanVar()
sysfop3 = BooleanVar()
sysfop4 = BooleanVar()
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
ender.set(False)
buf = StringVar()
buf.set('')
regent = StringVar()
actname = StringVar()
actname.set('')
actpw = StringVar()
actpw.set('')
actpwc = StringVar()
actpwc.set('')
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
idfill = StringVar()
todayd = datetime.datetime.today()
textfill = []
ccd = StringVar()
osnam = 'Galaxy-OS Universe'
buttons = []
pmbf = []
sf = []
file_name=None
timestr = StringVar()
pwcon = StringVar()
TIME = 60*3
time = '0'
ttime = []
ttime.append(time)
ids = os.environ.get("USERNAME")
currentdir = os.getcwd()
lst1 = StringVar()
lst2 = StringVar()
lst3 = StringVar()
lst4 = StringVar()
piccon = []
try:
    p = open('Path.dat', 'r')
except IOError:
    pass
else:
    for Paths in p:
        Paths == Paths
def unzip():
    os.chdir(currentdir)
    try:
        zf = zipfile.ZipFile("back up.zip", "r")
    except IOError:
        pwcon.set(u'バックアップファイルが見つかりません')
    else:
        for name in zf.namelist():
            try:
                uzf = file(name, "wb")
                uzf.write(zf.read(name))
                uzf.close()
            except IOError:
                pwcon.set(u'権限がないため復元できません')
            zf.close()
            pwcon.set(u'復元が完了しました')
def recf():
    if sysfop1.get():
        a = open('money.dat', 'w')
        a.write(str(0))
        a.close()
        sysfop1.set(False)
        aaa.set(u'すでに存在します')
    else:
        aaa.set(u'復元するファイルを選択してください')
def rysysf():
    global w5
    if w5 is None or not w5.winfo_exists():
        w5 = Toplevel()
        f1 = Frame(w5)
        f2 = Frame(w5)
        f3 = Frame(w5)
        f4 = Frame(w5)
        f5 = Frame(w5)
        os.chdir("%s\\Users\\Admin\\Market" % Paths)
        try:
            open('money.dat', 'r')
        except IOError:
            aaa.set(u'復元が必要です')
        else:
            aaa.set(u'異常なし')
        os.chdir(Paths)
        Label(w5, text = u'バックアップデータがなく、紛失又は破損したシステムファイルを復元しますが、初期化された状態での復元になります。').pack()
        Checkbutton(f1, text = u'マーケット用ファイル', variable = sysfop1).pack(side = LEFT)
        Label(f1, textvariable = aaa).pack(side = RIGHT)
        Button(f5, text = u'復元', command = recf).pack()
        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()
        f5.pack()
    else:
        w5.deiconify()
def resetpwm():
    pwtitle.set('')
    pwids.set('')
    pwpw.set('')
def savepwm():
    try:
        os.mkdir("%s" % pwtitle.get())
    except WindowsError:
        os.chdir("%s\%s" % (Paths, pwtitle.get()))
    a = open('sysf1.dat', 'w')
    a.write(pwids.get())
    a.close()
    b = open('sysf2.dat', 'w')
    b.write(pwpw.get())
    b.close()
    pwmcon.set(u'保存完了')
    os.chdir(Paths)
def searchsys():
    try:
        os.chdir('%s\\%s' % (Paths, pwsearch.get()))
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
        os.chdir(Paths)
pwsearch = StringVar()
pwtitle = StringVar()
pwids = StringVar()
pwpw = StringVar()
pwmcon = StringVar()
def pwmanage():
    global w6
    if w6 is None or not w6.winfo_exists():
        w6 = Toplevel()
        f1 = Frame(w6)
        f2 = Frame(w6)
        f3 = Frame(w6)
        f4 = Frame(w6)
        f5 = Frame(w6)
        f6 = Frame(w6)
        f7 = Frame(w6)
        f8 = Frame(w6)
        pwmcon.set('')
        Label(w6, text = 'PW Manager', font = ('New Times Roman', 18)).pack()
        Label(w6, text = u'あらゆるサイト・ゲーム・その他のアカウントのユーザー名/パスワードを保存していつでも確認できるようにします').pack()
        Label(f1, text = u'ユーザー名:').pack(side = LEFT)
        Label(f1, textvariable = ids).pack(side = RIGHT)
        Entry(f3, textvariable = pwsearch).pack(side = LEFT)
        Button(f3, text = u'検索', command = searchsys).pack(side = RIGHT)
        Label(f8, textvariable = pwmcon).pack()
        Label(f4, text = u'サイト名：').pack(side = LEFT)
        Entry(f4, textvariable = pwtitle).pack(side = RIGHT)
        Label(f5, text = 'ID:').pack(side = LEFT)
        Entry(f5, textvariable = pwids).pack(side = RIGHT)
        Label(f6, text = 'Password:').pack(side = LEFT)
        Entry(f6, textvariable = pwpw, show = '*').pack(side = RIGHT)
        Button(f7, text = u'保存', command = savepwm).pack(side = LEFT)
        Button(f7, text = u'新規作成', command = resetpwm).pack(side = RIGHT)
        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()
        f5.pack()
        f6.pack()
        f7.pack()
        f8.pack()
    else:
        w6.deiconify()
def makepwm():
    os.chdir("%s\Users" % Paths)
    f1 = open('user.dat', 'r')
    f2 = open('pw.dat', 'r')
    for i in f1:
        i == i
    for ii in f2:
        de = enckey.decrypt(ii)
    os.chdir(Paths)
    if actname.get() == i and actpw.get() == de:
        if actpw.get() != actpwc.get():
            try:
                e1 = enckey.encrypt(actpwc.get())
            except ValueError:
                pwcon.set(u'パスワードは8文字にしてください')
            else:
                if actname.get() and actpw.get() and actpwc.get() and actpw.get() != actpwc.get():
                    f = open('sysfile1.dat', 'w')
                    f.write(e1)
                    f.close()
                    actpwc.set('')
                    w7.destroy()
                    pwmanage()
                    pwcon.set('')
        else:
            pwcon.set(u'ログイン用パスワードと管理用パスワードは別にしてください')
    else:
        pwcon.set(u'アカウント名又はパスワードが違います')
def pwml():
    try:
        open('sysfile1.dat', 'r')
    except IOError:
        Message(w5, text = 'Error:file not found').pack()
    else:
        f = open('sysfile1.dat', 'r')
        for i in f:
            de = enckey.decrypt(i)
            if de == actpwc.get():
                pwmanage()
                actpwc.set('')
                w7.destroy()
                pwcon.set('')
            else:
                pwcon.set(u'パスワードが違います')
def pwcheck():
    global w7
    if w7 is None or not w7.winfo_exists():
        w7 = Toplevel()
        os.chdir(currentdir)
        try:
            open('sysfile1.dat', 'r')
        except IOError:
            f1 = Frame(w7)
            f2 = Frame(w7)
            f3 = Frame(w7)
            f4 = Frame(w7)
            Label(w7, text = u'セキュリティ強化のため、アカウント情報を入力してパスワード管理用の専用のパスワードを作成してください。').pack()
            Label(w7, textvariable = pwmcon).pack()
            Entry(f1, textvariable = actname).pack(side = RIGHT)
            Label(f1, text = u'アカウント名').pack(side = LEFT)
            Entry(f2, textvariable = actpw, show = '*').pack(side = RIGHT)
            Label(f2, text = u'パスワード(8文字)').pack(side = LEFT)
            Entry(f3, textvariable = actpwc, show = '*').pack(side = RIGHT)
            Label(f3, text = u'管理用パスワード(8文字)').pack(side = LEFT)
            b13 = Button(f4, text = u'作成', command = makepwm)
            b13.pack(side = LEFT)
            b13.bind('<Return>')
            b13.focus_set()
            f1.pack()
            f2.pack()
            f3.pack()
            f4.pack()
        else:
            Label(w7, text = u'管理用パスワード').pack()
            Label(w7, textvariable = pwcon).pack()
            Entry(w7, textvariable = actpwc, show = '*').pack()
            Button(w7, text = u'ログイン', command = pwml).pack()
    else:
        w7.deiconify()
def zipdirectory():
    os.chdir(currentdir)
    try:
        os.remove("back up.zip")
    except WindowsError:
        pass
    zf = zipfile.ZipFile("back up.zip", 'w')
    zf.writestr("back up" + '/', '')
    for dirp, dirn, filen in os.walk(currentdir):
        for dn in dirn:
            for fn in filen:
                zf.write(dirp + '/' + fn + '/' + dn, '')
        pwcon.set(u'バックアップが完了しました')
    zf.close()
def cw():
    os.chdir(currentdir)
    i_d6 = PhotoImage(file = 'moon.gif', height = 650, width = 1500)
    for L1 in piccon:
        L1.configure(image = i_d6)
def setting():
    global w3
    if w3 is None or not w3.winfo_exists():
        os.chmod(currentdir, stat.S_IREAD | stat.S_IWRITE)
        w3 = Toplevel()
        pwcon.set('')
        w3.title(u'設定')
        Label(w3, text = u'アカウントを作成やパスワードの変更').pack()
        Button(w3, text = u'アカウント', command = account).pack()
        Label(w3, text = u'システム:').pack()
        Button(w3, text = u'システム情報', width = 15, height = 1, command = about).pack()
        Label(w3, text = u'あらゆるアカウントのID・PWの管理:').pack()
        Button(w3, text = 'PW Manager', command = pwcheck).pack()
        Label(w3, text = u'破損又は紛失したシステムファイルを復元:').pack()
        Button(w3, text = u'システムファイル復元', command = rysysf).pack()
        Label(w3, text = u'背景の変更').pack()
        Button(w3, text = u'壁紙', command = cw).pack()
        Label(w3, textvariable = pwcon).pack()
        Label(w3, text = u'バックアップと復元：').pack()
        Button(w3, text = u'バックアップの作成', width = 30, height = 1, command = zipdirectory).pack()
        Button(w3, text = u'バックアップからファイルを復元', width = 30, height = 1, command = unzip).pack()
    else:
        w3.deiconify()
def done():
    if actname.get():
        if actpw.get() == actpwc.get():
            os.chdir('%s\\Users\\Admin\\ad' % Paths)
            try:
                enckey.encrypt(actpw.get())
            except ValueError:
                pwcon.set(u'パスワードは8文字にしてください')
            else:
                a = open('pw.dat', 'w')
                e1 = enckey.encrypt(actpw.get())
                a.write(e1)
                actpwc.set('')
                pwcon.set('')
                w8.destroy()
            os.chdir(Paths)
        else:
            Message(w4, text = u'パスワードが一致しません').pack()
            actpw.set('')
            actpwc.set('')
def cna():
    global w8
    if w8 is None or not w8.winfo_exists():
        w8 = Toplevel()
        os.chdir('%s\\Users\\Admin\\ad' % Paths)
        a = open('pw.dat', 'r')
        for i in a:
            de = enckey.decrypt(i)
        if actpwc.get() == de:
            actpwc.set('')
            actpw.set('')
            pwcon.set('')
            Label(w8, textvariable = pwcon).pack()
            Label(w8, text = u'新しいパスワードを入力').pack()
            Entry(w8, textvariable = actpw, show = '*').pack()
            Label(w8, text = u'確認のためもう一度入力').pack()
            Entry(w8, textvariable = actpwc, show = '*').pack()
            Button(w8, text = u'変更する', command = done).pack()
            w9.destroy()
            os.chdir(Paths)
        else:
            pwcon.set(u'パスワードが違います')
    else:
        w8.deiconify()
def pca():
    global w9
    if w9 is None or not w9.winfo_exists():
        w9 = Toplevel()
        actpwc.set('')
        Label(w9, text = u'確認のためにログイン').pack()
        Label(w9, textvariable = pwcon).pack()
        Label(w9, text = '%s' % actname.get()).pack()
        Entry(w9, textvariable = actpwc, show = '*').pack()
        Button(w9, text = u'次へ', command = cna).pack()
        w10.destroy()
    else:
        w9.deiconify()
def createid():
    os.chdir(Paths)
    if not os.path.exists("%s\\Users\\user2" % Paths):
        if actname.get() and actpw.get() and actpwc.get() != "":
            if actpw.get() == actpwc.get():
                try:
                    e1 = enckey.encrypt(actpw.get())
                except ValueError:
                    pwcon.set(u'パスワードは8文字で入力してください')
                else:
                    if actpw.get() and actpwc.get() and actpw.get() == actpwc.get():
                        idf = ids
                        os.chdir("Users")
                        os.mkdir("user2")
                        os.chdir("user2")
                        os.mkdir("ad")
                        os.mkdir("Market")
                        os.mkdir("Memo")
                        a = open('user.dat', 'w')
                        c = open('money.dat', 'w')
                        i = open('pw.dat', 'w')
                        a.write(actname.get())
                        e1 = enckey.encrypt(actpw.get())
                        i.write(e1)
                        c.write(str(0))
                        a.close()
                        c.close()
                        i.close()
                        try:
                            shutil.move("user.dat", "ad")
                        except WindowsError:
                            pass
                        try:
                            shutil.move("money.dat", "Market")
                        except WindowsError:
                            pass
                        try:
                            shutil.move("pw.dat", "ad")
                        except WindowsError:
                            pass
                        Dialog.Dialog(root, title = 'done', bitmap = 'info',
                                      text = u'設定を適用するには再起動してください',
                                      strings = ['OK'], default = 0)
                    else:
                        pwcon.set(u'アカウント情報を正しく入力してください')
            else:
                pwcon.set(u'アカウント情報を正しく入力してください')
        else:
            pwcon.set(u'アカウント情報を入力してください')
    elif not os.path.exists("%s\\Users\\user3" % Paths):
        if actname.get() and actpw.get() and actpwc.get() != "":
            if actpw.get() == actpwc.get():
                try:
                    e1 = enckey.encrypt(actpw.get())
                except ValueError:
                    pwcon.set(u'パスワードは8文字で入力してください')
                else:
                    if actpw.get() and actpwc.get() and actpw.get() == actpwc.get():
                        idf = ids
                        os.chdir("Users")
                        os.mkdir("user3")
                        os.chdir("user3")
                        os.mkdir("ad")
                        os.mkdir("Market")
                        os.mkdir("Memo")
                        a = open('user.dat', 'w')
                        c = open('money.dat', 'w')
                        i = open('pw.dat', 'w')
                        a.write(actname.get())
                        e1 = enckey.encrypt(actpw.get())
                        i.write(e1)
                        c.write(str(0))
                        a.close()
                        c.close()
                        i.close()
                        try:
                            shutil.move("user.dat", "ad")
                        except WindowsError:
                            pass
                        try:
                            shutil.move("money.dat", "Market")
                        except WindowsError:
                            pass
                        try:
                            shutil.move("pw.dat", "ad")
                        except WindowsError:
                            pass
                        Dialog.Dialog(root, title = 'done', bitmap = 'info',
                                      text = u'設定を適用するには再起動してください',
                                      strings = ['OK'], default = 0)
                    else:
                        pwcon.set(u'アカウント情報を正しく入力してください')
            else:
                pwcon.set(u'アカウント情報を正しく入力してください')
        else:
            pwcon.set(u'アカウント情報を入力してください')
    elif not os.path.exists("%s\\Users\\user4" % Paths):
        if actname.get() and actpw.get() and actpwc.get() != "":
            if actpw.get() == actpwc.get():
                try:
                    e1 = enckey.encrypt(actpw.get())
                except ValueError:
                    pwcon.set(u'パスワードは8文字で入力してください')
                else:
                    if actpw.get() and actpwc.get() and actpw.get() == actpwc.get():
                        idf = ids
                        os.chdir("Users")
                        os.mkdir("user4")
                        os.chdir("user4")
                        os.mkdir("ad")
                        os.mkdir("Market")
                        os.mkdir("Memo")
                        a = open('user.dat', 'w')
                        c = open('money.dat', 'w')
                        i = open('pw.dat', 'w')
                        a.write(actname.get())
                        e1 = enckey.encrypt(actpw.get())
                        i.write(e1)
                        c.write(str(0))
                        a.close()
                        c.close()
                        i.close()
                        try:
                            shutil.move("user.dat", "ad")
                        except WindowsError:
                            pass
                        try:
                            shutil.move("money.dat", "Market")
                        except WindowsError:
                            pass
                        try:
                            shutil.move("pw.dat", "ad")
                        except WindowsError:
                            pass
                        Dialog.Dialog(root, title = 'done', bitmap = 'info',
                                      text = u'設定を適用するには再起動してください',
                                      strings = ['OK'], default = 0)
                        sys.exit()
                    else:
                        pwcon.set(u'アカウント情報を正しく入力してください')
            else:
                pwcon.set(u'アカウント情報を正しく入力してください')
        else:
            pwcon.set(u'アカウント情報を入力してください')
    else:
        pwcon.set(u'作成可能なアカウントが最大です')
def createa():
    global w14
    if w14 is None or not w14.winfo_exists():
        w14 = Toplevel()
        f1 = Frame(w14)
        f2 = Frame(w14)
        f3 = Frame(w14)
        f4 = Frame(w14)
        pwcon.set('')
        actname.set('')
        w14.title(u"アカウント作成")
        Label(w14, textvariable = pwcon).pack()
        Entry(f1, textvariable = actname).pack(side = RIGHT)
        Label(f1, text = u'アカウント名').pack(side = LEFT)
        Entry(f2, textvariable = actpw, show = '*').pack(side = RIGHT)
        Label(f2, text = u'パスワード(8文字)').pack(side = LEFT)
        Entry(f3, textvariable = actpwc, show = '*').pack(side = RIGHT)
        Label(f3, text = u'確認のためもう一度入力').pack(side = LEFT)
        Button(f4, text = u'作成', command = createid).pack(side = LEFT)
        Button(f4, text = u'キャンセル', command = w14.destroy).pack(side = RIGHT)
        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()
    else:
        w14.deiconify()
def account():
    global w10
    if w10 is None or not w10.winfo_exists():
        w10 = Toplevel()
        Button(w10, text = u'パスワードを変更', command = pca).pack()
        Button(w10, text = u'アカウントを作成', command = createa).pack()
        Button(w10, text = u'閉じる', command = w2.destroy).pack()
    else:
        w10.deiconify()
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
    global w11
    if w11 is None or not w11.winfo_exists():
        os.chdir('%s\\Users\\Admin\\Market' % Paths)
        b = open('money.dat', 'r')
        for i in b:
            i==i
        os.chdir(Paths)
        w11 = Toplevel()
        f1 = Frame(w11)
        f2 = Frame(w11)
        f3 = LabelFrame(w11)
        Label(f1, text = 'Galaxy Store').pack(side = LEFT)
        Label(f2, text = '%s' % actname.get()).pack(side = LEFT)
        Label(f2, text = u'クレジット %s円' % i).pack(side = RIGHT)
        Label(f3, text = u'アプリ一覧：').pack()
        f1.pack()
        f2.pack()
        f3.pack()
    else:
        w11.deiconify()
def timer():
    global w14
    if w14 is None or not w14.winfo_exists():
        w14 = Toplevel()
        timestr.set("03:00")
        l = Label(w14, textvariable = timestr)
        b1 = Button(w14, text = u'スタート', command = countdown)
        b2 = Button(w14, text = u'終了', command = w14.destroy)
        for obj, sideparam in ((l,TOP),(b1,LEFT),(b2,RIGHT)):
            obj.pack(side = sideparam)
    else:
        w14.deiconify()
def countdown():
    time = time.time()
    timeleft = max(TIME-(time.time()-time), 0)
    min,sec = (timeleft) / 60, timeleft % 60
    timestr.set("%02d:%02d" % (min,sec))
    root.after(1000, countdown)
def poweropt():
    if val1.get() == 0:
        w12.destroy()
    elif val1.get() == 1:
        w12.destroy()
        ender.set(True)
        actlog()
        root.iconify()
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
    global w12
    if w12 is None or not w12.winfo_exists():        
        os.chdir('%s\\Users\\Admin\\ad' % Paths)
        a = open('user.dat', 'r')
        for i in a:
            i == i
        os.chdir(Paths)
        w12 = Toplevel()
        lf3 = LabelFrame(w12)
        Label(lf3, text = u'すべてのプログラム').pack()
        Button(lf3, text = u'コンピュータ', width = 20, command = Mycomputer).pack()
        Button(lf3, text = u'メモ帳', width = 20, command = memo).pack()
        Button(lf3, text = u'タイマー', width = 20, command = timer).pack()
        Button(lf3, text = u'マーケット', width = 20, command = market).pack()
        Button(lf3, text = u'システム情報', width = 20, command = about).pack()
        Button(lf3, text = u'設定', width = 20, command = setting).pack()
        lf1 = LabelFrame(w12)
        Label(lf1, text = u'ユーザー：%s' % i).pack()
        Label(lf1, text = '').pack()
        Label(lf1, text = u'プログラム', font = ('New Times Roman', 18)).pack()
        Radiobutton(lf1, text = u'ログオフ/ユーザー切り替え', variable = val1, value = 1).pack()
        Radiobutton(lf1, text = u'終了', variable = val1, value = 2).pack()
        Label(lf1, text = '').pack()
        Label(lf1, text = u'コンピュータ', font = ('New Times Roman', 18)).pack()
        Radiobutton(lf1, text = u'シャットダウン', variable = val1, value = 3).pack()
        Radiobutton(lf1, text = u'再起動', variable = val1, value = 4).pack()
        Radiobutton(lf1, text = u'スリープ', variable = val1, value = 5).pack()
        Radiobutton(lf1, text = u'休止', variable = val1, value = 6).pack()
        Radiobutton(lf1, text = u'キャンセル', variable = val1, value = 0).pack()
        Label(lf1, text = '').pack()
        Button(lf1, text = u'決定', command = poweropt).pack()
        lf3.pack(side = LEFT)
        lf1.pack()
    else:
        w12.deiconify()
def about():
    global w2
    if w2 is None or not w2.winfo_exists():
        w2 = Toplevel()
        Label(w2, text = u'ソフトウェア情報').pack()
        Label(w2, text = u'ソフトウェア:Galaxy-OS Home').pack()
        Label(w2, text = u'バージョン:1.0').pack()
        Label(w2, text = u'ライセンス:Home').pack()
        Label(w2, text = u'開発者:Galaxy-OS Universe Dev Team').pack()
        Button(w2, text = u'閉じる', command = w2.destroy).pack()
    else:
        w2.deiconify()
def asisuto():    
    if a4.get() == 3:
        new_state = 'normal'
    else:
        new_state = 'disabled'
    for b in pmbf:
        b.configure(state = new_state)
def save(w1, text):
    try:
        os.chdir('%s\\Memo' % Paths)
    except WindowsError:
        try:
            os.chdir('%s\Memo' % Paths)
        except WindowsError:
            Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                          text = u'保存先が見つからず、保存できません',
                          strings = ['OK'], default = 0)
    for t0 in textfill:
        data = t0.get('1.0', END)
    for fn in sf:
        fn==fn
    if fn != "":
        f = open(fn, 'w')
        f.write(data.encode('shift-jis'))
        f.close()
        os.chdir(Paths)
    else:
        fn = D.asksaveasfilename(filetypes=[('Text', '*.txt')], title=u'名前を付けて保存...')
        f = open(fn, 'w')
        f.write(data.encode('shift-jis'))
        f.close()
        w1.title(fn)
        os.chdir(Paths)
def load_File(w1):
    try:
        os.chdir('%s\\Memo' % Paths)
    except WindowsError:
        os.mkdir("Memo")
        os.chdir('%s\\Memo' % Paths)
    fn = D.askopenfilename(filetypes = [('Text Files', ('*.txt'))])
    if fn:
        fi = open(fn)
        for t0 in textfill:
            t0==t0
        t0.delete('1.0', 'end')
        for x in fi:
            t0.insert('end', x.decode('shift_jis'))
        fi.close()
        sf.append(fn)
        w1.title(fn)
        t0.focus_set()
        os.chdir(Paths)
def new_memo(w1):
    fn = ""
    sf.append(fn)
    w1.title(os.name=='posix' and 'untitled' or u'無題')
    for t0 in textfill:
        t0.delete('1.0', 'end')
def close(w1):
    w1.destroy()
def memo():
    global w1
    if w1 is None or not w1.winfo_exists():
        w1 = Toplevel()
        t0 = ScrolledText(w1)
        t0.pack()
        fn = ""
        sf.append(fn)
        w1.title(os.name=='posix' and 'untitled' or u'無題')
        textfill.append(t0)
        menubar = Menu(w1)
        filemenu = Menu(menubar)
        filemenu.add_command(label=u'新規作成', command=lambda : new_memo(w1))
        filemenu.add_command(label=u'保存', command=lambda : save(w1, t0))
        filemenu.add_command(label=u'開く', command=lambda : load_File(w1))
        filemenu.add_command(label=u'閉じる', command=lambda : close(w1))

        menubar.add_cascade(label=u'ファイル', menu=filemenu)
        w1.config(menu=menubar)
    else:
        w1.deiconify()
def Mycomputer():
    global w13
    if w13 is None or not w13.winfo_exists():
        w13 = Toplevel()
        Label(w13, text = u'ドライブ:').pack()
        win32api.GetDiskFreeSpaceEx('C:')
        for i in win32api.GetDiskFreeSpaceEx():
            print i / (1024 ** 3), "GB"
    else:
        w13.deiconify()
try:
    os.chdir('%s\\images' % currentdir)
    M_C = PhotoImage(file = 'mycomputer.gif', width = 60, height = 60)
    i_d2 = PhotoImage(file = 'timer.gif', width = 60, height = 60)
    i_d4 = PhotoImage(file = 'market.gif', width = 60, height = 50)
    i_d5 = PhotoImage(file = 'setting.gif', width = 60, height = 60)
    i_d6 = PhotoImage(file = 'gos.gif', width = 1500, height = 800)
    os.chdir(currentdir)
except WindowsError:
    pass
def home():
    root.deiconify()
    root.wm_attributes('-fullscreen', 1)
    a = actname.get()
    f0 = Frame(root)
    f4 = Frame(root)
    f5 = Frame(root)
    f6 = Frame(root)
    lf = LabelFrame(root)
    nam = 'Galaxy-OS Universe'
    Button(f4, image = M_C, command = Mycomputer).pack()
    Label(f4, text = u'コンピューター').pack()
    b6 = Button(f4, text = 'Memo', command = memo).pack()
    Label(f4, text = u'メモ帳').pack()
    b2 = Button(f4, image = i_d2, command = timer).pack()
    Label(f4, text = u'タイマー').pack()
    b4 = Button(f4, image = i_d4, command = market).pack()
    Label(f4, text = u'マーケット').pack()
    b5 = Button(f4, image = i_d5, command = setting).pack()
    Label(f4, text = u'設定').pack()
    L1 = Label(f6, image = i_d6)
    L1.pack()
    piccon.append(L1)
    Label(lf, text = 'Galaxy-OS Home', font = ('New Times Roman', 20), width = 30, height = 2).pack(side = LEFT)
    Button(lf, text = 'Galaxy', state = 'active', command = power).pack(side = LEFT)
    Label(lf, text = '%s/%s/%s' % (todayd.year, todayd.month, todayd.day)).pack(side = LEFT)
    Label(lf, textvariable = buf).pack(side = LEFT)
    lf.pack(padx = 20, pady = 20,side = BOTTOM)
    f4.pack(side = LEFT)
    f5.pack(side = LEFT)
    f6.pack()
    time()
def makeid():
    if actpw.get() and actpwc.get() != "":
        if actpw.get() == actpwc.get():
            try:
                e1 = enckey.encrypt(actpw.get())
            except ValueError:
                pwcon.set(u'パスワードは8文字で入力してください')
            else:
                if actpw.get() and actpwc.get() and actpw.get() == actpwc.get():
                    idf = ids
                    os.mkdir("Users")
                    os.chdir("Users")
                    os.mkdir("Admin")
                    os.chdir("Admin")
                    os.mkdir("ad")
                    os.mkdir("Market")
                    os.mkdir("Memo")
                    a = open('user.dat', 'w')
                    c = open('money.dat', 'w')
                    i = open('pw.dat', 'w')
                    p = open('Path.dat', 'w')
                    x = open('License.dat', 'w')
                    x.write(ugoku)
                    p.write(currentdir)
                    a.write(idf)
                    e1 = enckey.encrypt(actpw.get())
                    i.write(e1)
                    c.write(str(0))
                    a.close()
                    x.close()
                    c.close()
                    i.close()
                    try:
                        shutil.move("user.dat", "ad")
                    except WindowsError:
                        pass
                    try:
                        shutil.move("money.dat", "Market")
                    except WindowsError:
                        pass
                    try:
                        shutil.move("pw.dat", "ad")
                    except WindowsError:
                        pass
                    Dialog.Dialog(root, title = 'done', bitmap = 'info',
                                  text = u'設定を適用するために動してください',
                                  strings = ['OK'], default = 0)
                    sys.exit()
                else:
                    pwcon.set(u'アカウント情報を正しく入力してください')
        else:
            pwcon.set(u'アカウント情報を正しく入力してください')
    else:
        pwcon.set(u'アカウント情報を入力してください')
def login():
    try:
        os.chdir('%s\\Users\\Admin\\ad' % Paths)
    except WindowsError:
        pwcon.set(u'フォルダが見つかりません')
    else:
        try:
            a = open('pw.dat', 'r')
        except IOError:
            pwcon.set('file not found')
        else:
            for i in a:
                de = enckey.decrypt(i)
            if lst1.get() == de:
                if ender.get():
                    w2.destroy()
                    lst1.set('')
                    pwcon.set('')
                    os.chdir(Paths)
                    root.deiconify()
                else:
                    home()
                    lst1.set('')
                    w2.destroy()
                    a.close()
                    pwcon.set('')
            else:
                pwcon.set(u'パスワードが違います')
def login2():
    try:
        os.chdir('%s\\Users\\user2\\ad' % Paths)
    except WindowsError:
        pwcon.set(u'フォルダが見つかりません')
    else:
        try:
            a = open('pw.dat', 'r')
        except IOError:
            pwcon.set('file not found')
            lst2.set('')
        else:
            for i in a:
                de = enckey.decrypt(i)
            if lst2.get() == de:
                if ender.get():
                    w2.destroy()
                    lst2.set('')
                    pwcon.set('')
                    os.chdir(Paths)
                    root.deiconify()
                else:
                    home()
                    lst2.set('')
                    w2.destroy()
                    a.close()
                    pwcon.set('')
            else:
                pwcon.set(u'パスワードが違います')
labox = []
try:
    os.chdir('%s\images' % currentdir)
    i_d7 = PhotoImage(file = 'gos.gif', height = 560)
    os.chdir(currentdir)
except WindowsError:
    pass
def stc():
    if not os.path.exists("%s\\Users\\user2\\ad" % Paths):
        ns = 'disabled'
        for b in stb:
            b.configure(state = ns)
    if not os.path.exists("%s\\Users\\user3\\ad" % Paths):
        ns = 'disabled'
        for b2 in stb2:
            b2.configure(state = ns)
    if not os.path.exists("%s\\Users\\user4\\ad" % Paths):
        ns = 'disabled'
        for b3 in stb3:
            b3.configure(state = ns)
stb = []
stb2 = []
stb3 = []
def actlog():
    global w2
    w2 = Toplevel()
    w2.wm_attributes('-fullscreen', 1)
    lf = Frame(w2)
    lf2 = Frame(w2)
    lf3 = Frame(w2)
    os.chdir("%s\\Users\\Admin\\ad" % Paths)
    a = open('user.dat', 'r')
    for i in a:
        i == i
    os.chdir(Paths)
    try:
        os.chdir("%s\\Users\\user2\\ad" % Paths)
    except WindowsError:
        i2 = 'No user'
    else:
        b = open('user.dat', 'r')
        for i2 in b:
            i2 == i2
        os.chdir(Paths)
    try:
        os.chdir("%s\\Users\\user3\\ad" % Paths)
    except WindowsError:
        i3 = 'No user'
    else:
        c = open('user.dat', 'r')
        for i3 in c:
            i3 == i3
        os.chdir(Paths)
    try:
        os.chdir("%s\\Users\\user4\\ad" % Paths)
    except WindowsError:
        i4 = 'No user'
    else:
        d = open('user.dat', 'r')
        for i4 in d:
            i4 == i4
        os.chdir(Paths)
    pwcon.set('')
    Label(w2, text = '', height = 18).pack()
    Label(w2, text = u'ログインするアカウントのパスワードを入力し、ボタンを押してください').pack()
    Label(w2, textvariable = pwcon).pack()
    Button(lf, text = i, width = 8, height = 3, command = login).pack(side = LEFT)
    Label(lf, text = '', width = 10).pack(side = LEFT)
    b=Button(lf, text = i2, width = 8, height = 3, state = 'normal', command = login2)
    b.pack(side = LEFT)
    stb.append(b)
    Label(lf, text = '', width = 10).pack(side = LEFT)
    b2=Button(lf, text = i3, width = 8, height = 3)
    b2.pack(side = LEFT)
    stb2.append(b2)
    Label(lf, text = '', width = 10).pack(side = LEFT)
    b3=Button(lf, text = i4, width = 8, height = 3)
    b3.pack(side = LEFT)
    stb3.append(b3)
    Entry(lf2, textvariable = lst1, show = '*', width = 8).pack(side = LEFT)
    Label(lf2, text = '', width = 10).pack(side = LEFT)
    Entry(lf2, textvariable = lst2, show = '*', width = 8).pack(side = LEFT)
    Label(lf2, text = '', width = 10).pack(side = LEFT)
    Entry(lf2, textvariable = lst3, show = '*', width = 8).pack(side = LEFT)
    Label(lf2, text = '', width = 10).pack(side = LEFT)
    Entry(lf2, textvariable = lst4, show = '*', width = 8).pack(side = LEFT)
    Button(lf3, text = u'終了', command = sys.exit).pack()
    la1 = Label(w2, text = 'Galaxy-OS Home', font = ('New Times Roman', 24))
    la1.pack(side = BOTTOM)
    stc()
    lf.pack()
    lf2.pack()
    lf3.pack()
    root.lower()
def time():
    buf.set(strftime('%H:%M:%S'))
    root.after(1000, time)
def defaultcheck():
    global w3
    w3 = Toplevel()
    w3.wm_attributes('-fullscreen', 1)
    of = open('License.dat', 'r')
    for of2 in of:
        of2==of2
    root.iconify()
    if of2 == ugoku:
        p = open('Path.dat', 'r')
        for i in p:
            if not os.path.exists(i):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'プログラムファイルが見つかりません。%s' % i,
                              strings = ['OK'], default = 0)
                sys.exit()
            else:
                actlog()
                w3.destroy()
    elif of2 == eke:
        actname.set(ids)
        os.chdir(currentdir)
        f1 = Frame(w3)
        f2 = Frame(w3)
        f3 = Frame(w3)
        f4 = Frame(w3)
        Label(w3, text = '%s' % osnam).pack()
        t0 = ScrolledText(w3)
        t0.pack()
        fi = open('README.txt')
        t0.delete('1.0', 'end')
        for x in fi:
            t0.insert('end', x.decode('shift_jis'))
        fi.close()
        t0.focus_set()
        Label(w3, text = u'管理者登録').pack()
        Label(w3, textvariable = pwcon).pack()
        Label(f1, textvariable = actname).pack(side = RIGHT)
        Label(f1, text = u'管理者名').pack(side = LEFT)
        Entry(f2, textvariable = actpw, show = '*').pack(side = RIGHT)
        Label(f2, text = u'パスワード(8文字)').pack(side = LEFT)
        Entry(f3, textvariable = actpwc, show = '*').pack(side = RIGHT)
        Label(f3, text = u'確認のためもう一度入力').pack(side = LEFT)
        Button(f4, text = u'作成', command = makeid).pack(side = LEFT)
        Button(f4, text = u'キャンセル', command = sys.exit).pack(side = RIGHT)
        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()
        root.lower()
    else:
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'ライセンス認証されていないため、本ソフトを起動できませんでした',
                      strings = ['OK'], default = 0)
        sys.exit()
ek1 = 'activate'
dousa = 'ugoitaze'
ugoku = enckey2.encrypt(dousa)
eke = enckey2.encrypt(ek1)
defaultcheck()
root.mainloop()
