#coding:utf-8
import MySQLdb
import Crypto.Cipher.Blowfish
key = Crypto.Cipher.Blowfish.new('BlowfishSecret', Crypto.Cipher.Blowfish.MODE_ECB)
con = MySQLdb.connect(host="192.168.0.6", db="user", user="client", passwd="galaxygin")
cur = con.cursor()

#最初に必要なモジュールのインポートや変数の定義
from Tkinter import *
from ttk import *
root = Tk()
import sys
import os
import sys, os.path
import shutil
import subprocess
import Dialog
import tkMessageBox
import webbrowser
root.iconbitmap(default='account manager.ico')
note = Notebook(root)
#検索用テキストボックス
pwsearch = StringVar()
#サイト名用
pwtitle = StringVar()
#ID用
pwid = StringVar()
#パスワード用
pwpw = StringVar()
#エラーや処理完了などの通知用。これに限ってはテキストボックスとしての利用はない
su = StringVar()
con = StringVar()
i1 = IntVar()
i2 = IntVar()
i2.set('0')
cb1 = BooleanVar()
w1 = None
w2 = None
w3 = None
w4 = None
#保存・検索・一覧などを切り替えるためのタブ
tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)
tab4 = Frame(note)
lb = Listbox(tab3, width = 20, height = 5, state = 'normal')
deletelb = Listbox(tab4, width = 20, height = 5, state = 'normal')
b = []
ad = StringVar()
#ここで先にカレントディレクトリを取得しておく。
currentdir = os.getcwd()
user_id = StringVar()
user_pw = StringVar()
#ログイン関数用テキストボックス
login_pw = StringVar()
login_id = StringVar()
r_title = StringVar()
r_id = StringVar()
r_pw = StringVar()
l_title = StringVar()
l_id = StringVar()
l_pw = StringVar()
#------------------------ここまでが必要な変数の宣言----------------------------
#ここから関数の定義

#まず最初にアカウント情報やユーザ情報を格納するディレクトリの存在の確認
#ディレクトリが存在すればデータベースに接続、なければデータベース含め、全てのデータを作成
#次の処理は一番下
try:
    os.mkdir("bin")
except WindowsError:
    os.chdir("bin")
    curd = os.getcwd()
    if not os.path.exists("rqd02.db") or not os.path.exists("rqd01.db"):
        Dialog.Dialog(root, title = 'error', bitmap = 'info',
                          text = u'必要なファイルが不足しているため起動できません',
                          strings = ['OK'], default = 0)
        sys.exit()
else:
    os.chdir("bin")
#セキュリティ設定でログインを求めるを選択した場合に行うログイン認証。オブジェクト関数を
#削除するため、関数内関数にし、有効範囲を広くしている。
def login():
    def check():
        cur.execute("select uid, pw from user where uid = '%s'" % login_id.get())
        for id, pw in cur.fetchall():
            print login_id.get()
            print id
            pwe = key.encrypt('4869gin ')
            print pwe
        if pw == pwe:
            print login_id.get(), id, pwe, pw
            Dialog.Dialog(root, title = 'error', bitmap = 'info',
                          text = u'ID又はパスワードが違います',
                          strings = ['OK'], default = 0)
        else:
            print pw
            print pwe
            l1.pack_forget()
            llf.pack_forget()
            llf2.pack_forget()
            llf3.pack_forget()
            note.pack()
            m2.entryconfigure(u'セキュリティ', state = 'normal')
            cur.execute("select site from account")
            for site in cur.fetchall():
                lb.insert('end', site)
                deletelb.insert('end', site)
    llf = Frame(root)
    llf2 = Frame(root)
    llf3 = Frame(root)
    l1 = Label(root, text = u'セキュリティ認証')
    l1.pack()
    Label(llf, text = 'ID:').pack(side = LEFT)
    Entry(llf, textvariable = login_id).pack(side = RIGHT)
    Label(llf2, text = 'PW:').pack(side = LEFT)
    Entry(llf2, textvariable = login_pw, show = '*').pack(side = RIGHT)
    Button(llf3, text = u'ログイン', command = check).pack(side = LEFT)
    Button(llf3, text = u'終了', command = sys.exit).pack(side = RIGHT)
    llf.pack()
    llf2.pack()
    llf3.pack()
    cb1.set(True)
#メニュー その他 有料版へのグレードアップリンク
def browser():
    webbrowser.open_new_tab('http://galaxy-development.info/product.php')
#新規作成のためのリセット
def reset():
    pwtitle.set('')
    pwid.set('')
    pwpw.set('')
#アカウント保存関数
def save():
    cur.execute('insert into account values ("%s", "%s", "%s")' % (pwid.get(), pwpw.get(), pwtitle.get()))
    con.commit()
    os.chdir(currentdir)
    update()
    Dialog.Dialog(root, title = 'error', bitmap = 'info',
                          text = u'保存しました',
                          strings = ['OK'], default = 0)
#ENTERを押して検索した場合の処理
def search2(event):
    try:
        rf2.pack_forget()
        rf3.pack_forget()
        rf4.pack_forget()
    except:
        pass
    cur.execute('select count (*) from account where site like "%s"' % pwsearch.get())
    for count in cur.fetchone():
        if count > 0:
            cur.execute('select id, pw, site from account where site like "%s"' % pwsearch.get())
            for id, pw, site in cur.fetchall():
                r_id.set(id)
                r_pw.set(pw)
                r_title.set(site)
                rf2.pack()
                rf3.pack()
                rf4.pack()
        else:
            Dialog.Dialog(root, title = 'error', bitmap = 'info',
                          text = u'一致するアカウントがありません',
                          strings = ['OK'], default = 0)
    os.chdir(currentdir)
#検索ボタンを押した場合の処理
def searchsys():
    try:
        rf2.pack_forget()
        rf3.pack_forget()
        rf4.pack_forget()
    except:
        pass
    cur.execute('select count (*) from account where site like "%s"' % pwsearch.get())
    for count in cur.fetchone():
        if count > 0:
            cur.execute('select id, pw, site from account where site like "%s"' % pwsearch.get())
            for id, pw, site in cur.fetchall():
                r_id.set(id)
                r_pw.set(pw)
                r_title.set(site)
                rf2.pack()
                rf3.pack()
                rf4.pack()
        else:
            Dialog.Dialog(root, title = 'error', bitmap = 'info',
                          text = u'一致するアカウントがありません',
                          strings = ['OK'], default = 0)
    os.chdir(currentdir)
#検索結果のクリア
def clear():
    try:
        rf2.pack_forget()
        rf3.pack_forget()
        rf4.pack_forget()
    except:
        pass
#セキュリティ設定でOKが押されたときの処理。ログインするなら情報を保存し、しないならファイル
#を削除する
def sec2():
    if cb1.get():
        if user_id.get() and user_pw.get():
            user_data.execute("update user set id='%s', pw='%s', login='on'" % (user_id.get(), user_pw.get()))
            user.commit()
            w1.destroy()
        else:
            Dialog.Dialog(root, title = 'error', bitmap = 'info',
                          text = u'ID又はPWが入力されていません',
                          strings = ['OK'], default = 0)
    else:
        user_data.execute("update user set id='', pw='', login='off'")
        user.commit()
        w1.destroy()
#メニューのセキュリティ設定            
def security():
    def change_state():
        if cb1.get() or user_data == 'on':
            new_state = 'normal'
        else:
            new_state = 'disabled'
        try:
            ID.configure(state = new_state)
            PW.configure(state = new_state)
        except:
            pass
    global w1
    try:
        os.chdir("dir")
    except:
        pass
    if w1 is None or not w1.winfo_exists():
        user_data.execute("select login from user")
        if user_login == 'on':
            user_data.execute("select id, pw from user")
            for id, pw in user_data.fetchall():
                user_id.set(id)
                user_pw.set(pw)
        else:
            pass
        w1 = Toplevel()
        f1 = Frame(w1)
        f2 = Frame(w1)
        f3 = Frame(w1)
        f4 = Frame(w1)
        Label(w1, text = u'セキュリティ設定').pack()
        c1 = Checkbutton(w1, text = u'プログラム起動時にログインを求める', variable = cb1, command = change_state).pack()
        Label(f1, text = 'ID:').pack(side = LEFT)
        ID = Entry(f1, textvariable = user_id, state = 'disabled')
        ID.pack(side = RIGHT)
        Label(f2, text = u'パスワード:').pack(side = LEFT)
        PW = Entry(f2, textvariable = user_pw, show = '*', state = 'disabled')
        PW.pack(side = RIGHT)
        Button(f4, text = 'OK', command = sec2).pack()
        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()
        change_state()
    else:
        w1.deiconify()
#メニューのその他の使い方
def htu():
    global w3
    if w3 is None or not w3.winfo_exists():
        w3 = Toplevel()
        Label(w3, text = u'1. サイト・ID・PWを入力し、保存する。').pack()
        Label(w3, text = u'2. 1にて保存したサイト名を検索ボックスでも同じように入力').pack()
    else:
        w3.deiconify()
#一覧タブのリストボックスから選択されたアカウントを表示する処理
def choose_account(event):
    try:
        li1.pack_forget()
        li2.pack_forget()
        li3.pack_forget()
    except:
        pass
    a = [int(x) for x in lb.curselection()]
    cur.execute("select id, pw, site from account limit 1 offset %d" % a[0])
    for id, pw, site in cur.fetchall():
        l_id.set(id)
        l_pw.set(pw)
        l_title.set(site)
        li1.pack()
        li2.pack()
        li3.pack()
#削除タブのリストボックスから選択されたアカウントを削除する処理
def delete_account(event):
    ask = tkMessageBox.askyesno(u'確認',u'選択したアカウントを削除しますか?')
    if ask:
        a = [int(x) for x in deletelb.curselection()]
        cur.execute("select site from account limit 1 offset %d" % a[0])
        for sites in cur.fetchall():
            cur.execute("delete from account where site = '%s'" % sites)
        con.commit()
        update()
        Dialog.Dialog(root, title = 'error', bitmap = 'info',
                              text = u'削除しました',
                              strings = ['OK'], default = 0)
#リストボックスの更新
def update():
    lb.delete(0, 300)
    deletelb.delete(0, 300)
    cur.execute("select site from account")
    for site in cur.fetchall():
        lb.insert('end', site)
        deletelb.insert('end', site)
#バージョン情報
def version():
    global w4
    if w4 is None or not w4.winfo_exists():
        w4 = Toplevel()
        Label(w4, text = u'Account Manager\nバージョン：2.0.2\nライセンス：個人での使用に限り無料\n開発元：Galaxyチーム\nCopyright (C) 2012-2013 Galaxy All Rights Reserved.').pack()
    else:
        w4.deiconify()
#---------------------------ここまでが関数の定義---------------------------------
#ここからがUIの定義。設置はしないので注意。最後の行に設置するための.pack()関数はあるが
#今回は全てタブ内定義なので、あとでタブを設置する処理を1行書くだけでいいようにしてある。
m0 = Menu(root)
root.configure(menu = m0)
m1 = Menu(m0, tearoff = False)
m2 = Menu(m0, tearoff = False)
m3 = Menu(m0, tearoff = False)
m0.add_cascade(label = u'ファイル', under = 0, menu = m1)
m1.add_cascade(label = u'終了', command = sys.exit)
m0.add_cascade(label = u'設定', under = 0, menu = m2)
m2.add_command(label = u'セキュリティ', command = security, state = 'disabled')
m0.add_cascade(label = u'その他', under = 0, menu = m3)
m3.add_command(label = u'使い方', command = htu)
m3.add_command(label = u'Account Stationへグレードアップ', command = browser)
m3.add_command(label = u'バージョン情報', command = version)
f3 = Frame(tab1)
f4 = Frame(tab1)
f5 = Frame(tab1)
f6 = Frame(tab1)
f7 = Frame(tab1)
f8 = Frame(tab1)
lf1 = LabelFrame(tab1)
lf2 = LabelFrame(tab1)
#ソフト名が分かるようにタイトルと説明だけは設置するようにしてある。
root.title("Account Station")
Label(root, text = 'Account Station', font = ('New Times Roman', 18)).pack()
Label(root, text = u'あらゆるサイト・ゲーム・その他のアカウントのユーザー名/パスワードを保存していつでも確認できるようにします').pack()
#ここがタブ
note.add(tab1, text = u'保存')
note.add(tab2, text = u'検索')
note.add(tab3, text = u'一覧')
note.add(tab4, text = u'削除')
Label(f3, text = u'アカウントの保存').pack()
Label(f4, text = u'サイト名：').pack(side = LEFT)
Entry(f4, textvariable = pwtitle).pack(side = RIGHT)
#IDやPW枠に空白がたくさんあるのは見栄えを良くする為の調整
Label(f5, text = '                 ID:').pack(side = LEFT)
Entry(f5, textvariable = pwid).pack(side = RIGHT)
Label(f6, text = '       Password:').pack(side = LEFT)
Entry(f6, textvariable = pwpw, show = '*').pack(side = RIGHT)
Button(f7, text = u'保存', command = save).pack(side = LEFT)
Button(f7, text = u'新規作成', command = reset).pack(side = RIGHT)
tate = Scrollbar(tab3, orient = 'v', command = lb.yview)
yoko = Scrollbar(tab3, orient = 'h', command = lb.xview)
lb.configure(yscrollcommand = tate.set)
lb.configure(xscrollcommand = yoko.set)
Label(tab4, text = u'一覧から削除するアカウントをダブルクリック').pack()
tate2 = Scrollbar(tab4, orient = 'v', command = deletelb.yview)
yoko2 = Scrollbar(tab4, orient = 'h', command = deletelb.xview)
deletelb.configure(yscrollcommand = tate2.set)
deletelb.configure(xscrollcommand = yoko2.set)
lb.pack(side = LEFT)
lb.bind("<Double-1>", choose_account)
deletelb.pack()
deletelb.bind("<Double-1>", delete_account)
lf1.pack()
f3.pack()
f4.pack()
f5.pack()
f6.pack()
f7.pack()
rf1 = Frame(tab2)
rf2 = Frame(tab2)
rf3 = Frame(tab2)
rf4 = Frame(tab2)
Label(tab2, text = u'保存したアカウントを検索').pack()
e1 = Entry(rf1, textvariable = pwsearch)
e1.pack(side = LEFT)
e1.bind('<Return>', search2)
Button(rf1, text = u'検索', command = searchsys).pack(side = RIGHT)
Button(rf1, text = u'検索結果をクリア', command = clear).pack(side = RIGHT)
Label(rf2, text = u'サイト名：').pack(side = LEFT)
Label(rf2, textvariable = r_title).pack(side = RIGHT)
Label(rf3, text = 'ID:').pack(side = LEFT)
Label(rf3, textvariable = r_id).pack(side = RIGHT)
Label(rf4, text = 'Password:').pack(side = LEFT)
Label(rf4, textvariable = r_pw).pack(side = RIGHT)
rf1.pack()
li1 = Frame(tab3)
li2 = Frame(tab3)
li3 = Frame(tab3)
Label(tab3, text = u'一覧から表示するアカウントをダブルクリック').pack()
Label(li1, text = u'サイト名：').pack(side = LEFT)
Label(li1, textvariable = l_title).pack(side = RIGHT)
Label(li2, text = 'ID:').pack(side = LEFT)
Label(li2, textvariable = l_id).pack(side = RIGHT)
Label(li3, text = 'Password:').pack(side = LEFT)
Label(li3, textvariable = l_pw).pack(side = RIGHT)
#--------------------------------ここまでがUIの定義------------------------------
login()
root.mainloop()

