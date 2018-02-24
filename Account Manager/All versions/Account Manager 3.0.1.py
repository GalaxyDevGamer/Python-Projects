# coding:utf-8

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import *
from Crypto.Cipher import AES
from tkinter.scrolledtext import ScrolledText
root = Tk()
import sys
import os
import os.path
import shutil
import subprocess
import sqlite3
import tkinter.dialog
import random
import re
# import webbrowser
root.iconbitmap(default='icon.ico')
root.title("Account Manager")
AccountSearch = StringVar()
NewService = StringVar()
NewID = StringVar()
NewPW = StringVar()
EDIT = 0
SecurityWindow = None
AddWindow = None
GeneratorWindow = None
ManualWindow = None
LicenseWindow = None
ProLicenseW = None
Basedir = os.getcwd()
UserName = StringVar()
UserPW = StringVar()
Path = StringVar()
DataPath = os.getenv('LocalAppData')
login_pw = StringVar()
login_id = StringVar()
ServiceName = StringVar()
AccountID = StringVar()
AccountPW = StringVar()
PWDisabled = BooleanVar()
Base = Frame(root)
MainUI = Frame(Base)
LoginUI = Frame(Base)
account = None
accountDB = None
user_data = None
UserDB = None
AccountKey = None
AccountIV = None
UserKey = None
UserIV = None
Password = None
KeySource = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!"#%&()'
m0 = Menu(root)
root.configure(menu=m0)
m1 = Menu(m0, tearoff=False)
m2 = Menu(m0, tearoff=False)
m3 = Menu(m0, tearoff=False)
m0.add_cascade(label=u'ファイル', under=0, menu=m1)
m0.add_cascade(label=u'設定', under=0, menu=m2)
m0.add_cascade(label=u'ヘルプ', under=0, menu=m3)
#-------------------------ここからがメインのコード----------------------------
def PasswordGenerator():
    # 文字数を指定できるようにしてパスワード生成
    def GeneratePW():
        KeySource = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        try:
            GeneratedPW.set(''.join(random.choice(KeySource)for i in range(int(PWLength.get()))))
        except:
            messagebox.showerror(u'エラー', u'エラーが発生しました。',parent=GeneratorWindow)
    global GeneratorWindow
    GeneratedPW = StringVar()
    if GeneratorWindow is None or not GeneratorWindow.winfo_exists():
        GeneratorWindow = Toplevel()
        Base = Frame(GeneratorWindow)
        Lengths = Frame(Base)
        GeneratorWindow.title(u'パスワード生成ツール')
        Label(GeneratorWindow, text=u"パスワード生成ツール",font=('Meiryo', 14)).pack()
        Label(Lengths, text=u'パスワードの文字数:', font=('Meiryo', 12)).pack(side=LEFT)
        PWLength = Spinbox(Lengths, from_=6, to=32, increment=1, width=3)
        PWLength.pack(side=RIGHT)
        Lengths.pack()
        Entry(Base, textvariable=GeneratedPW, font=('Meiryo', 12)).pack()
        Button(Base, text=u'生成', command=GeneratePW).pack()
        Base.pack()
    else:
        GeneratorWindow.deiconify()
def update_account():
    update_DB(2)
    global EDIT
    EDIT = 1

def update_DB(Mode):
    # UserKeyからAccountKeyを復号化して、AccountKeyで暗号化する
    Aobj = AES.new(AccountKey, AES.MODE_CBC, AccountIV)
    if Mode == 1:
        d = (NewService.get(),Aobj.encrypt(ManagePlain(NewID.get())), Aobj.encrypt(ManagePlain(NewPW.get())))
        accountDB.execute('insert into account(Service, id,PW) values (?,?,?)', d)
    elif Mode == 2:
        d = (Aobj.encrypt(ManagePlain(AccountID.get())), Aobj.encrypt(ManagePlain(AccountPW.get())), ServiceName.get())
        accountDB.execute("update account set id=?, PW=? where Service=?", d)

def search2(event):
    searchsys()

def searchsys():
    # try: rf2.pack_forget()
    # except: pass
    Aobj = AES.new(AccountKey, AES.MODE_CBC, AccountIV)
    accountDB.execute('select count (*) from account where Service like "%s"' % AccountSearch.get())
    for count in accountDB.fetchone():
        if count > 0:
            accountDB.execute('select id, PW, Service from account where Service like "%s"' % AccountSearch.get())
            for id, pw, Service in accountDB.fetchall():
                AccountID.set(Aobj.decrypt(id).strip().decode('utf-8'))
                AccountPW.set(Aobj.decrypt(pw).strip().decode('utf-8'))
                ServiceName.set(Service)
            editB.configure(state='normal')
            hide.configure(state='normal')
            delete.configure(state='normal')
        else:
            messagebox.showerror(u'エラー', u'一致するアカウントがありませんでした')
    os.chdir(Basedir)

def UserSetting():
    def chIDState():
        global IDState
        if IDState == False:
            UserIDForm.configure(state='normal')
            IDLabel.set(u'完了')
            IDState = True
        elif IDState == True:
            if Check_UserFormError() != True:
                #一つしか引数がない場合、後ろに,を忘れるとエラーになる
                UserDB.execute("update user set UserName=?", (UserName.get(),))
                UserIDForm.configure(state='disabled')
                IDLabel.set(u'変更')
                IDState = False
    def chPWState():
        global PWState
        if PWState == False:
            UserPWForm.configure(state='normal')
            PWLabel.set(u'完了')
            PWState = True
        elif PWState == True:
            if Check_PWFormError() != True:
                if UserPW.get() == '':
                    UserDB.execute("update user set PW=?", ('',))
                else:
                    UserDB.execute("update user set PW=?", (Uobj.encrypt(ManagePlain(UserPW.get())),))
                UserPWForm.configure(state='disabled')
                PWLabel.set(u'変更')
                PWState = False
    global SecurityWindow, PWState, IDState
    if SecurityWindow is None or not SecurityWindow.winfo_exists():
        PWState = BooleanVar()
        PWState = False
        PWLabel = StringVar()
        PWLabel.set(u'変更')
        IDState = BooleanVar()
        IDState = False
        IDLabel = StringVar()
        IDLabel.set(u'変更')
        Progress = StringVar()
        UserDB.execute("select UserKey, UserIV from user")
        for key, iv in UserDB.fetchall():
            Uobj = AES.new(key, AES.MODE_CBC, iv)
        SecurityWindow = Toplevel(root)
        SecurityWindow.minsize(400, 150)
        Base = Frame(SecurityWindow)
        Form = Frame(Base)
        Labels = Frame(Form)
        Insert = Frame(Form)
        Edits = Frame(Form)
        SecurityWindow.title(u"設定")
        Label(SecurityWindow, text=u'ユーザー設定', font=('Meiryo', 12)).pack()
        Label(Labels, text=u'ユーザー名:', font=('Meiryo', 12)).pack(anchor='e')
        AbleID = Button(Edits, textvariable=IDLabel, command=chIDState)
        AbleID.pack()
        UserIDForm = Entry(Insert, textvariable=UserName, font=('Meiryo', 12), state='disabled')
        UserIDForm.pack()
        Label(Labels, text=u'パスワード：', font=('Meiryo', 12)).pack(anchor='e')
        AblePW = Button(Edits, textvariable=PWLabel, command=chPWState)
        AblePW.pack()
        UserPWForm = Entry(Insert, textvariable=UserPW, font=('Meiryo', 12), show='*', state='disabled')
        UserPWForm.pack()
        Labels.pack(side=LEFT)
        Edits.pack(side=RIGHT)
        Insert.pack(side=RIGHT)
        Form.pack()
        Base.pack()
    else:
        SecurityWindow.deiconify()

def choose_account(event):
    a = [int(x) for x in lb.curselection()]
    Aobj = AES.new(AccountKey, AES.MODE_CBC, AccountIV)
    accountDB.execute("select Service, id, PW from account limit 1 offset %d" % a[0])
    for Service, id, pw in accountDB.fetchall():
        try:
            AccountID.set(Aobj.decrypt(id).strip().decode('utf-8'))
            AccountPW.set(Aobj.decrypt(pw).strip().decode('utf-8'))
        except:
            messagebox.showerror(u'エラー', u'データの読み込みに失敗しました -004')
        else:
            ServiceName.set(Service)
            editB.configure(state='normal')
            hide.configure(state='normal')
            delete.configure(state='normal')

def delete_account():
    if messagebox.askyesno(u'確認', u'%sを削除しますか?' % ServiceName.get()):
        a = [int(x) for x in lb.curselection()]
        accountDB.execute("select Service from account limit 1 offset %d" % a[0])
        for sites in accountDB.fetchall():
            accountDB.execute("delete from account where Service = '%s'" % sites)
        ServiceName.set('')
        AccountID.set('')
        AccountPW.set('')
        update_list()
        messagebox.showinfo(u'完了', u'削除しました')
        CloseInfo()

def update_list():
    lb.delete(0, 300)
    try:
        accountDB.execute("select Service from account")
    except:
        messagebox.showerror(u'エラー', u'データを読み込めません。データが破損している可能性があります。')
    else:
        for Service in accountDB.fetchall():
            lb.insert('end', '%s' % Service)

def add():
    def check():
        if NewService.get() == '' or NewID.get() == '' or NewPW.get() == '':
            messagebox.showerror(u'エラー', u'正常なアカウントではありません',parent=AddWindow)
        elif isJapanese(NewID.get()) == None or isJapanese(NewPW.get()) == None:
            messagebox.showerror(u'エラー', u'使用できない文字列が含まれています',parent=AddWindow)
        else:
            save()
    def save():
        # 重複チェックをしてから暗号化をして保存
        accountDB.execute('select count (*) from account where Service like "%s"' % NewService.get())
        for count in accountDB.fetchone():
            if count == 0:
                update_DB(1)
                update_list()
                reset()
                messagebox.showinfo(u'完了', u'追加しました',parent=AddWindow)
                AddWindow.destroy()
            else:
                messagebox.showerror(u'エラー', u'既に追加されているアカウントです',parent=AddWindow)
    def reset():
        NewService.set('')
        NewID.set('')
        NewPW.set('')
    global AddWindow
    if AddWindow is None or not AddWindow.winfo_exists():
        AddWindow = Toplevel()
        f1 = Frame(AddWindow)
        Labels = Frame(f1)
        Insert = Frame(f1)
        AddWindow.title("Add")
        Label(AddWindow, text=u'アカウントの追加', font=('Meiryo', 12)).pack()
        Label(Labels, text=u'アカウント名：', font=('Meiryo', 12)).pack(anchor='e')
        Entry(Insert, textvariable=NewService, font=('Meiryo', 10)).pack()
        Label(Labels, text='ID：', font=('Meiryo', 12)).pack(anchor='e')
        Entry(Insert, textvariable=NewID, font=('Meiryo', 10)).pack()
        Label(Labels, text=u'パスワード：', font=('Meiryo', 12)).pack(anchor='e')
        Entry(Insert, textvariable=NewPW, show='*', font=('Meiryo', 10)).pack()
        Labels.pack(side=LEFT)
        Insert.pack(side=RIGHT)
        f1.pack()
        Button(AddWindow, text=u'追加', command=check).pack()
    else:
        AddWindow.deiconify()

def update_state():
    global EDIT
    if EDIT == 0:
        new_state = 'normal'
        EDIT = 1
        editB.configure(text=u'完了')
        delete.configure(state='disabled')
        hide.configure(state='disabled')
    else:
        # updateが押されたら、doneと同じ状態にしてrecentも書き換える
        if AccountID.get() == '' or AccountPW.get() == '':
            messagebox.showerror(u'エラー', u'正常なアカウントではありません')
        elif isJapanese(AccountID.get()) == None or isJapanese(AccountPW.get()) == None:
            messagebox.showerror(u'エラー', u'使用できない文字列が含まれています')
        else:
            update_account()
            new_state = 'readonly'
            EDIT = 0
            editB.configure(text=u'編集')
            delete.configure(state='normal')
            hide.configure(state='normal')
            messagebox.showinfo(u'完了', u'情報を更新しました')
    try:
        EditID.configure(state=new_state)
        EditPW.configure(state=new_state)
        editB.configure(state='normal')
    except:
        pass

def CloseInfo():
    hide.configure(state='disabled')
    EditID.configure(state='readonly')
    EditPW.configure(state='readonly')
    editB.configure(state='disabled')
    delete.configure(state='disabled')
    AccountID.set('')
    AccountPW.set('')
    ServiceName.set('')
    AccountSearch.set('')
def UserManual():
    global ManualWindow
    if ManualWindow is None or not ManualWindow.winfo_exists():
        try:
            f = open('説明書.txt')
        except:
            messagebox.showerror(u'エラー', u'ファイルが見つかりませんでした。')
        else:
            ManualWindow = Toplevel()
            ManualWindow.title(u"説明書.txt")
            Manual = ScrolledText(ManualWindow)
            data = f.read()
            f.close()
            Manual.insert('end', data)
            Manual.pack()
    else:
        ManualWindow.deiconify()
def License():
    global LicenseWindow
    if LicenseWindow is None or not LicenseWindow.winfo_exists():
        try:
            f = open('License.txt')
        except:
            messagebox.showerror(u'エラー', u'ファイルが見つかりませんでした。')
        else:
            LicenseWindow = Toplevel()
            ST = ScrolledText(LicenseWindow)
            LicenseWindow.title("License.txt")
            data = f.read()
            f.close()
            ST.insert('end', data)
            ST.pack()
    else:
        LicenseWindow.deiconify()
def ProLicense():
    global ProLicenseW
    if ProLicenseW is None or not ProLicenseW.winfo_exists():
        try:
            f = open('License for Pro.txt')
        except:
            messagebox.showerror(u'エラー', u'ファイルが見つかりませんでした。')
        else:
            ProLicenseW = Toplevel()
            ST = ScrolledText(ProLicenseW)
            ProLicenseW.title("License for Pro.txt")
            data = f.read()
            f.close()
            ST.insert('end', data)
            ST.pack()
    else:
        ProLicenseW.deiconify()
def OpenWindow():
    dir = os.path.join(DataPath, 'Account Manager')
    os.popen('start explorer "%s" ' % dir)
#---------------------------ここからがメインUIの定義---------------------------
# ここからがUIの定義。設置は上記のログイン又は登録で行う
m3.add_command(label=u'ユーザーマニュアル', command=UserManual)
m3.add_command(label=u'License', command=License)
m3.add_command(label=u'Pro License', command=ProLicense)
root.minsize(400, 230)
SearchBox = Frame(MainUI)
Box = Frame(MainUI)
ListBox = Frame(Box)
InfoBox = Frame(Box)
EditBox = Frame(InfoBox)
Resault = Frame(InfoBox)
Labels = Frame(InfoBox)
Label(MainUI, text="Account Manager", font=('Meiryo', 18)).pack()
e1 = Entry(SearchBox, textvariable=AccountSearch, font=('Meiryo', 10))
e1.pack(side=LEFT)
e1.bind('<Return>', search2)
Button(SearchBox, text=u'検索', command=searchsys).pack(side=RIGHT)
SearchBox.pack()
lb = Listbox(ListBox, width=10, font=('Meiryo', 13), height=5, state='normal')
tate = Scrollbar(ListBox, orient='v', command=lb.yview)
yoko = Scrollbar(ListBox, orient='h', command=lb.xview)
lb.configure(yscrollcommand=tate.set)
lb.configure(xscrollcommand=yoko.set)
lb.pack(side=LEFT)
lb.bind("<Double-1>", choose_account)
ListBox.pack(side=LEFT)
hide = Button(EditBox, text=u'閉じる', command=CloseInfo, state='disabled')
hide.pack(side=LEFT)
editB = Button(EditBox, text=u'編集', command=update_state, state='disabled')
editB.pack(side=LEFT)
delete = Button(EditBox, text=u'削除', state='disabled', command=delete_account)
delete.pack(side=RIGHT)
EditBox.pack()
Label(Labels, text=u'サービス名：', font=('Meiryo', 13)).pack(anchor='e')
EditName = Label(Resault, textvariable=ServiceName, font=('Meiryo', 11))
EditName.pack()
Label(Labels, text='ID：', font=('Meiryo', 13)).pack(anchor='e')
EditID = Entry(Resault, textvariable=AccountID, font=('Meiryo', 11), state='readonly')
EditID.pack()
Label(Labels, text=u'パスワード：', font=('Meiryo', 13)).pack(anchor='e')
EditPW = Entry(Resault, textvariable=AccountPW, font=('Meiryo', 11), state='readonly')
EditPW.pack()
Resault.pack(side=RIGHT)
Labels.pack(side=LEFT)
InfoBox.pack(side=RIGHT)
Box.pack()
Label(root, text='Version: 3β1.1 © 2012-2016 Galaxy',font=('Meiryo', 8)).pack(side=BOTTOM)
#------------------------ここからSetup・ログイン用のコード----------------------
# まず最初にユーザー設定とデータ保存用のパスを設定させる
# ユーザー設定ファイルが存在しなければ、ここが真っ先に実行される。
def load_UI():
    m1.add_command(label=u'アカウントの追加', command=add)
    m1.add_command(label=u'パスワード生成ツール', command=PasswordGenerator)
    m1.add_separator()
    m1.add_command(label=u'データフォルダを開く', command = OpenWindow)
    m1.add_separator()
    m1.add_command(label=u'終了', command=sys.exit)
    m2.add_command(label=u'設定', command=UserSetting)
    MainUI.pack()
    update_list()

def isJapanese(Text):
    # ひらがな・カタカナ判定 re.search(u'[ぁ-んァ-ヴ]', text)
    # 英数字判定 isalnum()
    # re.search('abcdefghijklmnopqrstuvwxyz0123456789', Text)
    #keys = re.compile(r'^[0-9A-Za-z]+$')

    #re.compile("[!-/:-@[-`{-~]") 全ての半角記号
    #str = "!/"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[//]^_abcdefghijklmnopqrstuvwxyz{|}~"
    #print re.sub(re.compile("[!-/:-@[-`{-~]"), '', str)  半角記号だけを除去する
    # 半角英数字記号以外の文字列があればNoneが返される
    keys = re.compile("[!-~]")
    return keys.search(Text)

def login():
    def check(event):
        if UserPW.get() == Password:
            LoginUI.pack_forget()
            load_UI()
        else:
            ipw.configure(text=u'パスワードが違います')
    if os.path.exists('%s/Account Manager/data/data2.db' % DataPath) == False:
        createServiceDB()
    ConnectDB()
    if Password == '':
        load_UI()
    else:
        Base = Frame(LoginUI)
        Form = Frame(Base)
        Buttons = Frame(Base)
        Label(LoginUI, text=u'ログイン', font=('Meiryo', 14)).pack()
        Label(LoginUI, textvariable=UserName, font=('Meiryo', 20)).pack(anchor='center')
        ipw = Label(LoginUI, font=('Meiryo', 10))
        ipw.pack(anchor='center')
        Label(Form, text=u'パスワード：', font=('Meiryo', 14)).pack(side=LEFT)
        login = Entry(Form, textvariable=UserPW, font=('Meiryo', 13), show='*')
        login.pack(side=RIGHT)
        login.bind('<Return>', check)
        b = Button(Buttons, text=u'ログイン')
        b.pack(side=LEFT)
        b.bind('<Button-1>', check)
        Button(Buttons, text=u'終了', command=sys.exit).pack(side=RIGHT)
        Base.pack()
        Form.pack()
        Buttons.pack()
        LoginUI.pack()

def choose_dir():
    dir = os.path.join(DataPath, 'Account Manager/backup')
    Path.set(filedialog.askdirectory(title = u'バックアップファイルがあるディレクトリを選択', parent=root,initialdir=dir))

def ManagePlain(PlainText):
    plain_length = len(PlainText)
    # 長さを16倍数で処理
    if plain_length <= 16:
        plain_blank = 16 - plain_length
        plain_blank = ' ' * plain_blank
    elif plain_length > 16 and plain_length <= 32:
        plain_blank = 32 - plain_length
        plain_blank = ' ' * plain_blank
    Plain = PlainText + plain_blank
    return Plain

def Check_UserFormError():
    if UserName.get() == '' or UserName.get().isspace() == True:
        messagebox.showerror(u'エラー', u'ユーザー名は空白に出来ません')
        return True
    elif len(UserName.get()) > 16:
        messagebox.showerror(u'エラー', u'文字数制限を超えています')
        return True
def Check_PWFormError():
    if isJapanese(UserPW.get()) == None or UserPW.get().isspace() == True:
        if UserPW.get() != '':
            messagebox.showerror(u'エラー', u'パスワードに設定出来るのは半角英数字のみです')
            return True
    elif len(UserPW.get()) > 32:
        messagebox.showerror(u'エラー', u'文字数制限を超えています')
        return True
def ConnectDB():
    try:
        global account, accountDB, user_data, UserDB, Password, AccountKey, AccountIV, UserKey, UserIV
        account = sqlite3.connect('%s/Account Manager/data/data2.db' % DataPath, isolation_level=None)
        accountDB = account.cursor()
        user_data = sqlite3.connect('%s/Account Manager/data/data1.db' % DataPath, isolation_level=None)
        UserDB = user_data.cursor()
        UserDB.execute("select UserName, PW, AccountKey,AccountIV,UserKey, UserIV from user")
        for name, pw, akey, aiv,Key, IV in UserDB.fetchall():
            UserName.set(name)
            obj = AES.new(Key, AES.MODE_CBC, IV)
            Password = obj.decrypt(pw).strip().decode('utf-8')
            AccountKey = akey
            AccountIV = aiv
            UserKey = Key
            UserIV = IV
    except:
        messagebox.showerror(u'エラー', u'データ取得に失敗しました')
        sys.exit()
def createServiceDB():
    try:
        global account, accountDB
        account = sqlite3.connect('%s/Account Manager/data/data2.db' % DataPath, isolation_level=None)
        accountDB = account.cursor()
        accountDB.execute('create table account (No integer primary key,Service TEXT, id,PW)')
    except:
        messagebox.showerror(u'エラー', u'データの構成に失敗しました')
        sys.exit()
def Setup():
    def Agree_state():
        if Agree.get():
            Finish.configure(state='normal')
        else:
            Finish.configure(state='disabled')
    def PW_state():
        if PWDisabled.get():
            pw.configure(state='disabled')
            UserPW.set('')
        else:
            pw.configure(state='enabled')
    def change_state():
        if SetupOpt.get() == 0:
            name.configure(state = 'enabled')
            if PWDisabled.get() == False:
                pw.configure(state = 'enabled')
            PATH.configure(state = 'disabled')
            pathb.configure(state = 'disabled')
        else:
            name.configure(state = 'disabled')
            pw.configure(state = 'disabled')
            PATH.configure(state = 'readonly')
            pathb.configure(state = 'enabled')
    def process():
        if SetupOpt.get() == 0:
            if Check_UserFormError() != True and Check_PWFormError() != True:
            # KeySourceからランダムで文字を選び、rangeの回数を繰り返して、''(空白)で繋げる
                UKey = ''.join(random.choice(KeySource) for i in range(32))
                UIV = ''.join(random.choice(KeySource) for i in range(16))
                uobj = AES.new(UKey, AES.MODE_CBC, UIV)
                if UserPW.get() != '':
                    EPW = uobj.encrypt(ManagePlain(UserPW.get()))
                else:
                    EPW = ''
                EKey = ''.join(random.choice(KeySource) for i in range(32))
                EIV = ''.join(random.choice(KeySource) for i in range(16))
                d = (UserName.get(), EPW, EKey, EIV, UKey, UIV)
                sqlite3.connect('%s/Account Manager/data/data1.db' % DataPath, isolation_level=None).cursor().execute('create table user (UserName Text, PW, AccountKey, AccountIV, UserKey, UserIV)')
                sqlite3.connect('%s/Account Manager/data/data1.db' % DataPath, isolation_level=None).cursor().execute('insert into user values (?, ?, ?, ?, ?, ?)', d)
                createServiceDB()
                ConnectDB()
                SetupUI.pack_forget()
                load_UI()
        elif SetupOpt.get() == 1:
            if os.path.exists("%s/data1.db" % Path.get()) == False or os.path.exists("%s/data2.db" % Path.get()) == False:
                messagebox.showerror(u'エラー', u'バックアップファイルが見つかりませんでした。')
            else:
                try:
                    shutil.copy2("%s/data1.db" % Path.get(), '%s/Account Manager/data/data1.db' % DataPath)
                    shutil.copy2("%s/data2.db" % Path.get(), '%s/Account Manager/data/data2.db' % DataPath)
                except:
                    messagebox.showerror(u'エラー',u'復元に失敗しました。')
                else:
                    messagebox.showinfo(u'完了', u'復元が完了しました。')
                    SetupUI.pack_forget()
                    login()
    Agree = BooleanVar()
    SetupOpt = IntVar()
    SetupOpt.set(0)
    SetupUI = Frame(Base)
    UserInfo = Frame(SetupUI)
    UserLabel = Frame(UserInfo)
    UserForm = Frame(UserInfo)
    PathBox = Frame(SetupUI)
    Label(SetupUI, text="Account Manager Setup", font=('Meiryo', 18)).pack()
    Radiobutton(SetupUI, text=u"Account Manager用のアカウントを作成", variable = SetupOpt, value = 0, command = change_state).pack(anchor = "w")
    Label(UserLabel, text=u'ユーザー名(16文字以内):', font=('Meiryo', 12)).pack()
    name = Entry(UserForm, textvariable=UserName, font=('Meiryo', 12))
    name.pack()
    Label(UserLabel, text=u'パスワード(32文字以内):', font=('Meiryo', 12)).pack()
    Checkbutton(UserLabel, text=u'パスワードを設定しない',variable=PWDisabled, command=PW_state).pack()
    pw = Entry(UserForm, textvariable=UserPW, font=('Meiryo', 12), show='*')
    pw.pack()
    UserLabel.pack(side=LEFT)
    UserForm.pack(side=RIGHT)
    UserInfo.pack()
    Radiobutton(SetupUI, text=u'バックアップから復元', variable = SetupOpt, value = 1, command = change_state).pack(anchor ='w')
    PATH = Entry(PathBox, textvariable=Path, font=('Meiryo', 12), width=30, state = 'disabled')
    PATH.pack(side='left')
    pathb = Button(PathBox, text=u'..', command=choose_dir, state = 'disabled')
    pathb.pack(side ='right')
    PathBox.pack()
    Checkbutton(SetupUI, text=u'ヘルプに書いてある全てを理解しました',variable=Agree, command=Agree_state).pack()
    Finish = Button(SetupUI, text=u'始める', state='disabled', command=process)
    Finish.pack()
    SetupUI.pack()
if os.path.exists("%s/Account Manager/data" %DataPath) == False:
    try:
        os.makedirs("%s/Account Manager/data" %DataPath)
    except:
        messagebox.showerror(u'エラー',u'データフォルダの作成に失敗しました')
        sys.exit()
if os.path.exists('%s/Account Manager/data/data1.db' % DataPath) == False:
    Setup()
else:
    login()
Base.pack()
root.mainloop()