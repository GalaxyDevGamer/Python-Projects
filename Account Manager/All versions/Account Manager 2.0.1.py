# coding:shift-jis

#可能な限り説明は書いておいた。処理が分からない箇所は実際に実行して調べてくれ。

from Tkinter import *
from ttk import *
root = Tk()
import sys
import os
import sys, os.path
import shutil
import subprocess
import sqlite3
import Crypto.Cipher.AES
import Dialog
import tkMessageBox
note = Notebook(root)
#AESを利用したアカウント情報の暗号化のための秘密鍵
key = Crypto.Cipher.AES.new("GalaxyMarkTatuya", Crypto.Cipher.AES.MODE_ECB)
#同じくユーザ情報の暗号化のための秘密鍵
user = Crypto.Cipher.AES.new("AMSEDEVCXx86-x64", Crypto.Cipher.AES.MODE_ECB)
#検索用テキストボックス
pwsearch = StringVar()
#サイト名用
pwtitle = StringVar()
#ID用
pwid = StringVar()
#パスワード用
pwpw = StringVar()
#エラーや処理完了などの通知用。これに限ってはテキストボックスとしての利用はない
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
#保存・検索・一覧などを切り替えるためのタブ
tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)
lb = Listbox(tab3, width = 20, height = 5)
b = []
ad = StringVar()
#ここで先にカレントディレクトリを取得しておく。
currentdir = os.getcwd()
user_id = StringVar()
user_pw = StringVar()
#ログイン関数用テキストボックス
login_pw = StringVar()
login_id = StringVar()
logincon = StringVar()
secobj1 = []
secobj2 = []
#------------------------ここまでが必要な変数の宣言----------------------------

#まず最初にアカウント情報やユーザ情報を格納するディレクトリの存在の確認
#ディレクトリが存在すればデータベースに接続、なければデータベース含め、全てのデータを作成
#次の処理は一番下
try:
    os.mkdir("dir")
except WindowsError:
    os.chdir("dir")
    curd = os.getcwd()
    con = sqlite3.connect("data.db", isolation_level='EXCLUSIVE')
    cur = con.cursor()
    cur.execute("BEGIN EXCLUSIVE")
    cur.execute("""select * from account""")
    for sq in cur.fetchall():
        print sq
else:
    os.chdir("dir")
    con = sqlite3.connect("data.db", isolation_level='EXCLUSIVE')
    cur = con.cursor()
    cur.execute("BEGIN EXCLUSIVE")
    cur.execute("""create table account (
                id blob,
                pw blob,
                site TEXT)""")         
    con.commit()
#セキュリティ設定でログインを求めるを選択した場合に行うログイン認証
def login():
    def check():
        f1 = open('ID.dat', 'r')
        f2 = open('PW.dat', 'r') 
        for i in f1:
            i==i
        for ii in f2:
            ii==ii
        if login_id.get() == i and login_pw.get() == ii:
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
    global w2
    w2 = Toplevel()
    llf = Frame(w2)
    llf2 = Frame(w2)
    llf3 = Frame(w2)
    Label(w2, text = u'セキュリティ認証').pack()
    Label(w2, textvariable = logincon).pack()
    Label(llf, text = 'ID:').pack(side = LEFT)
    Entry(llf, textvariable = login_id).pack(side = RIGHT)
    Label(llf2, text = 'PW:').pack(side = LEFT)
    Entry(llf2, textvariable = login_id, show = '*').pack(side = RIGHT)
    Button(llf3, text = u'ログイン', command = check).pack(side = LEFT)
    Button(llf3, text = u'終了', command = sys.exit).pack(side = RIGHT)
    llf.pack()
    llf2.pack()
    llf3.pack()
    cb1.set(True)
#新規作成のためのリセット
def reset():
    pwtitle.set('')
    pwid.set('')
    pwpw.set('')
#アカウント保存関数
def save():
    if len(pwpw.get())>48:
        Dialog.Dialog(root, title='too much strings', bitmap='info',
                      text=u'48文字以上のパスワードは登録できません',
                      strings=['OK'], default = 0)
    if len(pwid.get())>16:
        Dialog.Dialog(root, title='too much strings', bitmap='info',
                      text=u'16文字以上のIDは登録できません',
                      strings=['OK'], default = 0)
    else:
        #入力されたパスワードの長さを取得
        pw_length = len(pwpw.get())
        #長さを16倍数で処理
        if pw_length <= 16:
            pw_blank = 16-pw_length
            pw_blank = ' '*pw_blank
        elif pw_length > 16 and pw_length <= 32:
            pw_blank = 32-pw_length
            pw_blank = ' '*pw_blank
        elif pw_length > 32 and pw_length <= 48:
            pw_blank = 48-pw_length
            pw_blank = ' '*pw_blank
        id_blank = 16-len(pwid.get())
        id_blank = ' '*id_blank
        #暗号化
        ID = key.encrypt(pwid.get()+id_blank)
        pw = key.encrypt(pwpw.get()+pw_blank)
        cur.execute('insert into account values (u"%s", u"%s", u"%s")' % (ID, pw, pwtitle.get()))
        con.commit()
        os.chdir(currentdir)
        pwmcon.set(u'保存完了')
#ENTERを押して検索した場合の処理
def search2(event):
    cur.execute("select id, pw from account where site like '%s%'" % pwtitle.get())
    for id, pw in cur.fetchall():
        pwid.set(id)
        pwpw.set(pw)
    pwtitle.set(pwsearch.get())
    pwmcon.set('')
    os.chdir(currentdir)
#検索ボタンを押した場合の処理
def searchsys():
    cur.execute("select id, pw from account where site like '%s%'" % pwtitle.get())
    for id, pw in cur.fetchall():
        pwid.set(id)
        pwpw.set(pw)
    pwtitle.set(pwsearch.get())
    pwmcon.set('')
    print pwtitle.get()
    os.chdir(currentdir)
#セキュリティ設定でOKが押されたときの処理。ログインするなら情報を保存し、しないならファイル
#を削除する
def sec2():
    if cb1.get():
        if ids.get() and pws.get():
            f1 = open('ID.dat', 'w')
            f2 = open('PW.dat', 'w')
            f1.write(user_id.get())
            f2.write(user_pw.get())
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
#セキュリティ設定項目のテキストボックスの状態を切り替える
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
#メニューのセキュリティ設定            
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
        sece1 = Entry(f1, textvariable = user_id, state = 'disabled')
        sece1.pack(side = RIGHT)
        Label(f2, text = 'PW:').pack(side = LEFT)
        sece2 = Entry(f2, textvariable = user_pw, show = '*', state = 'disabled')
        sece2.pack(side = RIGHT)
        c2 = Checkbutton(f3, text = u'アカウントは常に暗号化して保存', variable = cb2).pack()
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
#メニューのヘルプ
def htu():
    global w3
    w3 = Toplevel()
    Label(w3, text = u'1. サイト・ID・PWを入力し、保存する。').pack()
    Label(w3, text = u'2. 1にて保存したサイト名を検索ボックスでも同じように入力').pack()
#親ウィンドウに表示するラベルやテキストボックス。セキュリティのため、最初は何もできないよう
#にしてあるが、ログインしない場合は一番下で状態を解除する。
#上記の関数へはButton関数のcommandで呼び出す
m0 = Menu(root)
root.configure(menu = m0)
m1 = Menu(m0, tearoff = False)
m2 = Menu(m0, tearoff = False)
m3 = Menu(m0, tearoff = False)
m0.add_cascade(label = u'ファイル', under = 0, menu = m1)
m1.add_cascade(label = u'終了', command = sys.exit)
m0.add_cascade(label = u'設定', under = 0, menu = m2)
m2.add_command(label = u'セキュリティ', command = security)
m0.add_cascade(label = 'HELP', under = 0, menu = m3)
m3.add_command(label = u'使い方', command = htu)
f3 = Frame(tab1)
f4 = Frame(tab1)
f5 = Frame(tab1)
f6 = Frame(tab1)
f7 = Frame(tab1)
f8 = Frame(tab1)
lf1 = LabelFrame(tab1)
lf2 = LabelFrame(tab1)
root.title("Account Manager 2.0.1")
Label(root, text = 'Account Manager', font = ('New Times Roman', 18)).pack()
Label(root, text = u'あらゆるサイト・ゲーム・その他のアカウントのユーザー名/パスワードを保存していつでも確認できるようにします').pack()
note.add(tab1, text = u'保存')
note.add(tab2, text = u'検索')
note.add(tab3, text = u'一覧')
note.pack()
Label(tab2, text = u'保存したアカウントを検索').pack()
e1 = Entry(tab2, textvariable = pwsearch, state = 'disabled')
e1.pack(side = LEFT)
e1.bind('<Return>', search2)
sb1 = Button(tab2, text = u'検索', command = searchsys, state = 'disabled')
sb1.pack(side = RIGHT)
Label(f8, textvariable = pwmcon).pack()
Label(f3, text = u'アカウントの保存及び保存したアカウントの表示').pack()
Label(f4, text = u'サイト名(全角)：').pack(side = LEFT)
se1 = Entry(f4, textvariable = pwtitle, state = 'disabled')
se1.pack(side = RIGHT)
Label(f5, text = '                 ID:').pack(side = LEFT)
ie1 = Entry(f5, textvariable = pwid, state = 'disabled')
ie1.pack(side = RIGHT)
Label(f6, text = '       Password:').pack(side = LEFT)
pe1 = Entry(f6, textvariable = pwpw, show = '*', state = 'disabled')
pe1.pack(side = RIGHT)
sb2 = Button(f7, text = u'保存', command = save, state = 'disabled')
sb2.pack(side = LEFT)
Button(f7, text = u'終了', command = sys.exit).pack(side = RIGHT)
sb3 = Button(f7, text = u'新規作成', command = reset, state = 'disabled')
sb3.pack(side = RIGHT)
scb1 = Scrollbar(tab3, orient = 'v', command = lb.yview)
scb2 = Scrollbar(tab3, orient = 'h', command = lb.xview)
lb.configure(yscrollcommand = scb1.set)
lb.configure(xscrollcommand = scb2.set)
lb.pack()
lb.bind("<Double-1>")
lf1.pack()
f8.pack()
f3.pack()
f4.pack()
f5.pack()
f6.pack()
f7.pack()
#2回目に行う処理。ログイン用データがあればログイン関数へ、なければ入力状態を有効にするだけ
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
    login()
root.mainloop()
