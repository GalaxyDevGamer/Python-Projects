# coding:shift-jis

#�\�Ȍ�������͏����Ă������B������������Ȃ��ӏ��͎��ۂɎ��s���Ē��ׂĂ���B

#�ŏ��ɕK�v�ȃ��W���[���̃C���|�[�g��ϐ��̒�`
from Tkinter import *
from ttk import *
root = Tk()
import sys
import os
import sys, os.path
import shutil
import subprocess
import sqlite3
import Dialog
import tkMessageBox
import webbrowser
root.iconbitmap(default='account manager.ico')
note = Notebook(root)
#�����p�e�L�X�g�{�b�N�X
pwsearch = StringVar()
#�T�C�g���p
pwtitle = StringVar()
#ID�p
pwid = StringVar()
#�p�X���[�h�p
pwpw = StringVar()
#�G���[�⏈�������Ȃǂ̒ʒm�p�B����Ɍ����Ă̓e�L�X�g�{�b�N�X�Ƃ��Ă̗��p�͂Ȃ�
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
w5 = None
#�ۑ��E�����E�ꗗ�Ȃǂ�؂�ւ��邽�߂̃^�u
tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)
tab4 = Frame(note)
lb = Listbox(tab3, width = 20, height = 5, state = 'normal')
deletelb = Listbox(tab4, width = 20, height = 5, state = 'normal')
b = []
ad = StringVar()
#�����Ő�ɃJ�����g�f�B���N�g�����擾���Ă����B
currentdir = os.getcwd()
user_id = StringVar()
user_pw = StringVar()
#���O�C���֐��p�e�L�X�g�{�b�N�X
login_pw = StringVar()
login_id = StringVar()
r_title = StringVar()
r_id = StringVar()
r_pw = StringVar()
l_title = StringVar()
l_id = StringVar()
l_pw = StringVar()
add_name = StringVar()
add_pw = StringVar()
add_login = IntVar()
add_authority = IntVar()
#------------------------�����܂ł��K�v�ȕϐ��̐錾----------------------------
#��������֐��̒�`

#�܂��ŏ��ɃA�J�E���g���⃆�[�U�����i�[����f�B���N�g���̑��݂̊m�F
#�f�B���N�g�������݂���΃f�[�^�x�[�X�ɐڑ��A�Ȃ���΃f�[�^�x�[�X�܂߁A�S�Ẵf�[�^���쐬
#���̏����͈�ԉ�
try:
    os.mkdir("bin")
except WindowsError:
    os.chdir("bin")
    curd = os.getcwd()
    if not os.path.exists("rqd02.db") or not os.path.exists("rqd01.db"):
        Dialog.Dialog(root, title = 'error', bitmap = 'info',
                          text = u'�K�v�ȃt�@�C�����s�����Ă��邽�ߋN���ł��܂���',
                          strings = ['OK'], default = 0)
        sys.exit()
    else:        
        con = sqlite3.connect("rqd01.db", isolation_level='EXCLUSIVE')
        cur = con.cursor()
        cur.execute("BEGIN EXCLUSIVE")
        user = sqlite3.connect("rqd02.db", isolation_level='EXCLUSIVE')
        user_data = user.cursor()
        user_data.execute("BEGIN EXCLUSIVE")
else:
    os.chdir("bin")
    con = sqlite3.connect("rqd01.db", isolation_level='EXCLUSIVE')
    cur = con.cursor()
    cur.execute("BEGIN EXCLUSIVE")
    cur.execute("""create table account (
                id TEXT,
                pw TEXT,
                site TEXT
                url TEXT)""")         
    con.commit()
    user = sqlite3.connect("rqd02.db", isolation_level='EXCLUSIVE')
    user_data = user.cursor()
    user_data.execute("BEGIN EXCLUSIVE")
    user_data.execute("""create table user (
                            id TEXT,
                            pw TEXT,
                            login TEXT,
                            root TEXT,
                            authority TEXT)""")
    user_data.execute('insert into user (login, root, authority) values ("off", "yes", "yes")')
    user.commit()
#�Z�L�����e�B�ݒ�Ń��O�C�������߂��I�������ꍇ�ɍs�����O�C���F�؁B�I�u�W�F�N�g�֐���
#�폜���邽�߁A�֐����֐��ɂ��A�L���͈͂��L�����Ă���B
def login():
    def check():
        user_data.execute("select id, pw from user")
        for id, pw in user_data.fetchall():
            pass
        if login_id.get() == id and login_pw.get() == pw:
            l1.pack_forget()
            llf.pack_forget()
            llf2.pack_forget()
            llf3.pack_forget()
            note.pack()
            m2.entryconfigure(u'�Z�L�����e�B', state = 'normal')
            m2.entryconfigure(u'���[�U�[�Ǘ�', state = 'normal')
            cur.execute("select site from account")
            for site in cur.fetchall():
                lb.insert('end', site)
                deletelb.insert('end', site)
        else:
            Dialog.Dialog(root, title = 'error', bitmap = 'info',
                          text = u'ID���̓p�X���[�h���Ⴂ�܂�',
                          strings = ['OK'], default = 0)
    llf = Frame(root)
    llf2 = Frame(root)
    llf3 = Frame(root)
    l1 = Label(root, text = u'�Z�L�����e�B�F��')
    l1.pack()
    Label(llf, text = 'ID:').pack(side = LEFT)
    Entry(llf, textvariable = login_id).pack(side = RIGHT)
    Label(llf2, text = 'PW:').pack(side = LEFT)
    Entry(llf2, textvariable = login_pw, show = '*').pack(side = RIGHT)
    Button(llf3, text = u'���O�C��', command = check).pack(side = LEFT)
    Button(llf3, text = u'�I��', command = sys.exit).pack(side = RIGHT)
    llf.pack()
    llf2.pack()
    llf3.pack()
    cb1.set(True)
#���j���[ ���̑� �L���łւ̃O���[�h�A�b�v�����N
def browser():
    webbrowser.open_new_tab('http://galaxy-development.info/product.php')
#�V�K�쐬�̂��߂̃��Z�b�g
def reset():
    pwtitle.set('')
    pwid.set('')
    pwpw.set('')
#�A�J�E���g�ۑ��֐�
def save():
    cur.execute('insert into account values ("%s", "%s", "%s")' % (pwid.get(), pwpw.get(), pwtitle.get()))
    con.commit()
    os.chdir(currentdir)
    update()
    Dialog.Dialog(root, title = 'error', bitmap = 'info',
                          text = u'�ۑ����܂���',
                          strings = ['OK'], default = 0)
#ENTER�������Č��������ꍇ�̏���
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
                          text = u'��v����A�J�E���g������܂���',
                          strings = ['OK'], default = 0)
    os.chdir(currentdir)
#�����{�^�����������ꍇ�̏���
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
                          text = u'��v����A�J�E���g������܂���',
                          strings = ['OK'], default = 0)
    os.chdir(currentdir)
#�������ʂ̃N���A
def clear():
    try:
        rf2.pack_forget()
        rf3.pack_forget()
        rf4.pack_forget()
    except:
        pass
#�Z�L�����e�B�ݒ��OK�������ꂽ�Ƃ��̏����B���O�C������Ȃ����ۑ����A���Ȃ��Ȃ�t�@�C��
#���폜����
def sec2():
    if cb1.get():
        if user_id.get() and user_pw.get():
            user_data.execute("update user set id='%s', pw='%s', login='on'" % (user_id.get(), user_pw.get()))
            user.commit()
            w1.destroy()
        else:
            Dialog.Dialog(root, title = 'error', bitmap = 'info',
                          text = u'ID����PW�����͂���Ă��܂���',
                          strings = ['OK'], default = 0)
    else:
        user_data.execute("update user set id='', pw='', login='off'")
        user.commit()
        w1.destroy()
#���j���[�̃Z�L�����e�B�ݒ�            
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
        Label(w1, text = u'�Z�L�����e�B�ݒ�').pack()
        c1 = Checkbutton(w1, text = u'�v���O�����N�����Ƀ��O�C�������߂�', variable = cb1, command = change_state).pack()
        Label(f1, text = 'ID:').pack(side = LEFT)
        ID = Entry(f1, textvariable = user_id, state = 'disabled')
        ID.pack(side = RIGHT)
        Label(f2, text = u'�p�X���[�h:').pack(side = LEFT)
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
#���j���[�̂��̑��̎g����
def htu():
    global w3
    if w3 is None or not w3.winfo_exists():
        w3 = Toplevel()
        Label(w3, text = u'1. �T�C�g�EID�EPW����͂��A�ۑ�����B').pack()
        Label(w3, text = u'2. 1�ɂĕۑ������T�C�g���������{�b�N�X�ł������悤�ɓ���').pack()
    else:
        w3.deiconify()
#�ꗗ�^�u�̃��X�g�{�b�N�X����I�����ꂽ�A�J�E���g��\�����鏈��
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
#�폜�^�u�̃��X�g�{�b�N�X����I�����ꂽ�A�J�E���g���폜���鏈��
def delete_account(event):
    ask = tkMessageBox.askyesno(u'�m�F',u'�I�������A�J�E���g���폜���܂���?')
    if ask:
        a = [int(x) for x in deletelb.curselection()]
        cur.execute("select site from account limit 1 offset %d" % a[0])
        for sites in cur.fetchall():
            cur.execute("delete from account where site = '%s'" % sites)
        con.commit()
        update()
        Dialog.Dialog(root, title = 'error', bitmap = 'info',
                              text = u'�폜���܂���',
                              strings = ['OK'], default = 0)
#���X�g�{�b�N�X�̍X�V
def update():
    lb.delete(0, 300)
    deletelb.delete(0, 300)
    cur.execute("select site from account")
    for site in cur.fetchall():
        lb.insert('end', site)
        deletelb.insert('end', site)
#�o�[�W�������
def version():
    global w4
    if w4 is None or not w4.winfo_exists():
        w4 = Toplevel()
        Label(w4, text = u'Account Manager\n�o�[�W�����F2.0.2\n���C�Z���X�F�l�ł̎g�p�Ɍ��薳��\n�J�����FGalaxy�`�[��\nCopyright (C) 2012-2013 Galaxy All Rights Reserved.').pack()
    else:
        w4.deiconify()
#���[�U�[�Ǘ�
def user_manage():
    global w5
    if w5 is None or not w5.winfo_exists():
        w5 = Toplevel()
        Label(w5, text = u'���[�U�[�Ǘ�').pack()
        add = LabelFrame(w5)
        lists = LabelFrame(w5)
        name = Frame(add)
        pw = Frame(add)
        login = Frame(add)
        authority = Frame(add)
        b = Frame(add)
        user_list = Listbox(lists, width = 20, height = 5, state = 'normal')
        Label(add, text = u'���[�U�[�ǉ�').pack()
        Label(lists, text = u'���[�U�[�ꗗ').pack()
        Label(name, text = u'���[�U�[���y��ID:').pack(side = LEFT)
        Entry(name, textvariable = add_name).pack(side = RIGHT)
        Label(pw, text = u'�p�X���[�h(���ݒ��):').pack(side = LEFT)
        Entry(pw, textvariable = add_pw).pack(side = RIGHT)
        Label(login, text = u'���O�C��:').pack(side = LEFT)
        Radiobutton(login, text = u'���Ȃ�', variable = add_login, value = 2).pack(side = RIGHT)
        Radiobutton(login, text = u'����', variable = add_login, value = 1).pack(side = RIGHT)
        Label(authority, text = u'�Ǘ��Ҍ���:').pack(side = LEFT)
        Radiobutton(authority, text = u'�������Ȃ�', variable = add_authority, value = 2).pack(side = RIGHT)
        Radiobutton(authority, text = u'��������', variable = add_authority, value = 1).pack(side = RIGHT)
        Button(b, text = u'�ǉ�').pack()
        add.pack(side = LEFT)
        lists.pack(side = RIGHT)
        user_list.pack(side = RIGHT)
        name.pack()
        pw.pack()
        login.pack()
        authority.pack()
    else:
        w5.deiconify()
#---------------------------�����܂ł��֐��̒�`---------------------------------
#�������炪UI�̒�`�B�ݒu�͂��Ȃ��̂Œ��ӁB�Ō�̍s�ɐݒu���邽�߂�.pack()�֐��͂��邪
#����͑S�ă^�u����`�Ȃ̂ŁA���ƂŃ^�u��ݒu���鏈����1�s���������ł����悤�ɂ��Ă���B
m0 = Menu(root)
root.configure(menu = m0)
m1 = Menu(m0, tearoff = False)
m2 = Menu(m0, tearoff = False)
m3 = Menu(m0, tearoff = False)
m0.add_cascade(label = u'�t�@�C��', under = 0, menu = m1)
m1.add_cascade(label = u'�I��', command = sys.exit)
m0.add_cascade(label = u'�ݒ�', under = 0, menu = m2)
m2.add_command(label = u'���[�U�[�Ǘ�', command = user_manage, state = 'disabled')
m2.add_command(label = u'�Z�L�����e�B', command = security, state = 'disabled')
m0.add_cascade(label = u'���̑�', under = 0, menu = m3)
m3.add_command(label = u'�g����', command = htu)
m3.add_command(label = u'Account Station�փO���[�h�A�b�v', command = browser)
m3.add_command(label = u'�o�[�W�������', command = version)
f3 = Frame(tab1)
f4 = Frame(tab1)
f5 = Frame(tab1)
f6 = Frame(tab1)
f7 = Frame(tab1)
f8 = Frame(tab1)
lf1 = LabelFrame(tab1)
lf2 = LabelFrame(tab1)
#�\�t�g����������悤�Ƀ^�C�g���Ɛ��������͐ݒu����悤�ɂ��Ă���B
root.title("Account Station 1.0.1")
Label(root, text = 'Account Station', font = ('New Times Roman', 18)).pack()
Label(root, text = u'������T�C�g�E�Q�[���E���̑��̃A�J�E���g�̃��[�U�[��/�p�X���[�h��ۑ����Ă��ł��m�F�ł���悤�ɂ��܂�').pack()
#�������^�u
note.add(tab1, text = u'�ۑ�')
note.add(tab2, text = u'����')
note.add(tab3, text = u'�ꗗ')
note.add(tab4, text = u'�폜')
Label(f3, text = u'�A�J�E���g�̕ۑ�').pack()
Label(f4, text = u'�T�C�g���F').pack(side = LEFT)
Entry(f4, textvariable = pwtitle).pack(side = RIGHT)
#ID��PW�g�ɋ󔒂��������񂠂�̂͌��h����ǂ�����ׂ̒���
Label(f5, text = '                 ID:').pack(side = LEFT)
Entry(f5, textvariable = pwid).pack(side = RIGHT)
Label(f6, text = '       Password:').pack(side = LEFT)
Entry(f6, textvariable = pwpw, show = '*').pack(side = RIGHT)
Button(f7, text = u'�ۑ�', command = save).pack(side = LEFT)
Button(f7, text = u'�V�K�쐬', command = reset).pack(side = RIGHT)
tate = Scrollbar(tab3, orient = 'v', command = lb.yview)
yoko = Scrollbar(tab3, orient = 'h', command = lb.xview)
lb.configure(yscrollcommand = tate.set)
lb.configure(xscrollcommand = yoko.set)
Label(tab4, text = u'�ꗗ����폜����A�J�E���g���_�u���N���b�N').pack()
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
Label(tab2, text = u'�ۑ������A�J�E���g������').pack()
e1 = Entry(rf1, textvariable = pwsearch)
e1.pack(side = LEFT)
e1.bind('<Return>', search2)
Button(rf1, text = u'����', command = searchsys).pack(side = RIGHT)
Button(rf1, text = u'�������ʂ��N���A', command = clear).pack(side = RIGHT)
Label(rf2, text = u'�T�C�g���F').pack(side = LEFT)
Label(rf2, textvariable = r_title).pack(side = RIGHT)
Label(rf3, text = 'ID:').pack(side = LEFT)
Label(rf3, textvariable = r_id).pack(side = RIGHT)
Label(rf4, text = 'Password:').pack(side = LEFT)
Label(rf4, textvariable = r_pw).pack(side = RIGHT)
rf1.pack()
li1 = Frame(tab3)
li2 = Frame(tab3)
li3 = Frame(tab3)
Label(tab3, text = u'�ꗗ����\������A�J�E���g���_�u���N���b�N').pack()
Label(li1, text = u'�T�C�g���F').pack(side = LEFT)
Label(li1, textvariable = l_title).pack(side = RIGHT)
Label(li2, text = 'ID:').pack(side = LEFT)
Label(li2, textvariable = l_id).pack(side = RIGHT)
Label(li3, text = 'Password:').pack(side = LEFT)
Label(li3, textvariable = l_pw).pack(side = RIGHT)
#--------------------------------�����܂ł�UI�̒�`------------------------------
#2��ڂ̏���:�ȉ��Ń��O�C���ݒ肪�L���Ȃ烍�O�C���A���Ȃ���΃^�u�y�у^�u���̒�`��ݒu
user_data.execute("select login from user")
for user_login in user_data.fetchall():
    user_login =  user_login[0]
if user_login == 'on':
    login()
else:
#����.pack()�őS�̂�UI���ݒu�����
    note.pack()
    m2.entryconfigure(u'�Z�L�����e�B', state = 'normal')
    m2.entryconfigure(u'���[�U�[�Ǘ�', state = 'normal')
    cur.execute("select site from account")
    for site in cur.fetchall():
        lb.insert('end', site)
        deletelb.insert('end', site)
root.mainloop()
