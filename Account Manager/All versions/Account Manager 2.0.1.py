# coding:shift-jis

#�\�Ȍ�������͏����Ă������B������������Ȃ��ӏ��͎��ۂɎ��s���Ē��ׂĂ���B

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
#AES�𗘗p�����A�J�E���g���̈Í����̂��߂̔閧��
key = Crypto.Cipher.AES.new("GalaxyMarkTatuya", Crypto.Cipher.AES.MODE_ECB)
#���������[�U���̈Í����̂��߂̔閧��
user = Crypto.Cipher.AES.new("AMSEDEVCXx86-x64", Crypto.Cipher.AES.MODE_ECB)
#�����p�e�L�X�g�{�b�N�X
pwsearch = StringVar()
#�T�C�g���p
pwtitle = StringVar()
#ID�p
pwid = StringVar()
#�p�X���[�h�p
pwpw = StringVar()
#�G���[�⏈�������Ȃǂ̒ʒm�p�B����Ɍ����Ă̓e�L�X�g�{�b�N�X�Ƃ��Ă̗��p�͂Ȃ�
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
#�ۑ��E�����E�ꗗ�Ȃǂ�؂�ւ��邽�߂̃^�u
tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)
lb = Listbox(tab3, width = 20, height = 5)
b = []
ad = StringVar()
#�����Ő�ɃJ�����g�f�B���N�g�����擾���Ă����B
currentdir = os.getcwd()
user_id = StringVar()
user_pw = StringVar()
#���O�C���֐��p�e�L�X�g�{�b�N�X
login_pw = StringVar()
login_id = StringVar()
logincon = StringVar()
secobj1 = []
secobj2 = []
#------------------------�����܂ł��K�v�ȕϐ��̐錾----------------------------

#�܂��ŏ��ɃA�J�E���g���⃆�[�U�����i�[����f�B���N�g���̑��݂̊m�F
#�f�B���N�g�������݂���΃f�[�^�x�[�X�ɐڑ��A�Ȃ���΃f�[�^�x�[�X�܂߁A�S�Ẵf�[�^���쐬
#���̏����͈�ԉ�
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
#�Z�L�����e�B�ݒ�Ń��O�C�������߂��I�������ꍇ�ɍs�����O�C���F��
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
            logincon.set(u'ID���̓p�X���[�h���Ⴂ�܂�')
    global w2
    w2 = Toplevel()
    llf = Frame(w2)
    llf2 = Frame(w2)
    llf3 = Frame(w2)
    Label(w2, text = u'�Z�L�����e�B�F��').pack()
    Label(w2, textvariable = logincon).pack()
    Label(llf, text = 'ID:').pack(side = LEFT)
    Entry(llf, textvariable = login_id).pack(side = RIGHT)
    Label(llf2, text = 'PW:').pack(side = LEFT)
    Entry(llf2, textvariable = login_id, show = '*').pack(side = RIGHT)
    Button(llf3, text = u'���O�C��', command = check).pack(side = LEFT)
    Button(llf3, text = u'�I��', command = sys.exit).pack(side = RIGHT)
    llf.pack()
    llf2.pack()
    llf3.pack()
    cb1.set(True)
#�V�K�쐬�̂��߂̃��Z�b�g
def reset():
    pwtitle.set('')
    pwid.set('')
    pwpw.set('')
#�A�J�E���g�ۑ��֐�
def save():
    if len(pwpw.get())>48:
        Dialog.Dialog(root, title='too much strings', bitmap='info',
                      text=u'48�����ȏ�̃p�X���[�h�͓o�^�ł��܂���',
                      strings=['OK'], default = 0)
    if len(pwid.get())>16:
        Dialog.Dialog(root, title='too much strings', bitmap='info',
                      text=u'16�����ȏ��ID�͓o�^�ł��܂���',
                      strings=['OK'], default = 0)
    else:
        #���͂��ꂽ�p�X���[�h�̒������擾
        pw_length = len(pwpw.get())
        #������16�{���ŏ���
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
        #�Í���
        ID = key.encrypt(pwid.get()+id_blank)
        pw = key.encrypt(pwpw.get()+pw_blank)
        cur.execute('insert into account values (u"%s", u"%s", u"%s")' % (ID, pw, pwtitle.get()))
        con.commit()
        os.chdir(currentdir)
        pwmcon.set(u'�ۑ�����')
#ENTER�������Č��������ꍇ�̏���
def search2(event):
    cur.execute("select id, pw from account where site like '%s%'" % pwtitle.get())
    for id, pw in cur.fetchall():
        pwid.set(id)
        pwpw.set(pw)
    pwtitle.set(pwsearch.get())
    pwmcon.set('')
    os.chdir(currentdir)
#�����{�^�����������ꍇ�̏���
def searchsys():
    cur.execute("select id, pw from account where site like '%s%'" % pwtitle.get())
    for id, pw in cur.fetchall():
        pwid.set(id)
        pwpw.set(pw)
    pwtitle.set(pwsearch.get())
    pwmcon.set('')
    print pwtitle.get()
    os.chdir(currentdir)
#�Z�L�����e�B�ݒ��OK�������ꂽ�Ƃ��̏����B���O�C������Ȃ����ۑ����A���Ȃ��Ȃ�t�@�C��
#���폜����
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
            Message(w1, text = u'ID����PW�����͂���Ă��܂���').pack()
    else:
        try:
            os.remove("ID.dat")
            os.remove("PW.dat")
        except WindowsError:
            pass
        w1.destroy()
#�Z�L�����e�B�ݒ荀�ڂ̃e�L�X�g�{�b�N�X�̏�Ԃ�؂�ւ���
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
#���j���[�̃Z�L�����e�B�ݒ�            
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
        Label(w1, text = u'�Z�L�����e�B�ݒ�').pack()
        c1 = Checkbutton(w1, text = u'�v���O�����N�����Ƀ��O�C�������߂�', variable = cb1, command = seccs).pack()
        Label(f1, text = 'ID:').pack(side = LEFT)
        sece1 = Entry(f1, textvariable = user_id, state = 'disabled')
        sece1.pack(side = RIGHT)
        Label(f2, text = 'PW:').pack(side = LEFT)
        sece2 = Entry(f2, textvariable = user_pw, show = '*', state = 'disabled')
        sece2.pack(side = RIGHT)
        c2 = Checkbutton(f3, text = u'�A�J�E���g�͏�ɈÍ������ĕۑ�', variable = cb2).pack()
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
#���j���[�̃w���v
def htu():
    global w3
    w3 = Toplevel()
    Label(w3, text = u'1. �T�C�g�EID�EPW����͂��A�ۑ�����B').pack()
    Label(w3, text = u'2. 1�ɂĕۑ������T�C�g���������{�b�N�X�ł������悤�ɓ���').pack()
#�e�E�B���h�E�ɕ\�����郉�x����e�L�X�g�{�b�N�X�B�Z�L�����e�B�̂��߁A�ŏ��͉����ł��Ȃ��悤
#�ɂ��Ă��邪�A���O�C�����Ȃ��ꍇ�͈�ԉ��ŏ�Ԃ���������B
#��L�̊֐��ւ�Button�֐���command�ŌĂяo��
m0 = Menu(root)
root.configure(menu = m0)
m1 = Menu(m0, tearoff = False)
m2 = Menu(m0, tearoff = False)
m3 = Menu(m0, tearoff = False)
m0.add_cascade(label = u'�t�@�C��', under = 0, menu = m1)
m1.add_cascade(label = u'�I��', command = sys.exit)
m0.add_cascade(label = u'�ݒ�', under = 0, menu = m2)
m2.add_command(label = u'�Z�L�����e�B', command = security)
m0.add_cascade(label = 'HELP', under = 0, menu = m3)
m3.add_command(label = u'�g����', command = htu)
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
Label(root, text = u'������T�C�g�E�Q�[���E���̑��̃A�J�E���g�̃��[�U�[��/�p�X���[�h��ۑ����Ă��ł��m�F�ł���悤�ɂ��܂�').pack()
note.add(tab1, text = u'�ۑ�')
note.add(tab2, text = u'����')
note.add(tab3, text = u'�ꗗ')
note.pack()
Label(tab2, text = u'�ۑ������A�J�E���g������').pack()
e1 = Entry(tab2, textvariable = pwsearch, state = 'disabled')
e1.pack(side = LEFT)
e1.bind('<Return>', search2)
sb1 = Button(tab2, text = u'����', command = searchsys, state = 'disabled')
sb1.pack(side = RIGHT)
Label(f8, textvariable = pwmcon).pack()
Label(f3, text = u'�A�J�E���g�̕ۑ��y�ѕۑ������A�J�E���g�̕\��').pack()
Label(f4, text = u'�T�C�g��(�S�p)�F').pack(side = LEFT)
se1 = Entry(f4, textvariable = pwtitle, state = 'disabled')
se1.pack(side = RIGHT)
Label(f5, text = '                 ID:').pack(side = LEFT)
ie1 = Entry(f5, textvariable = pwid, state = 'disabled')
ie1.pack(side = RIGHT)
Label(f6, text = '       Password:').pack(side = LEFT)
pe1 = Entry(f6, textvariable = pwpw, show = '*', state = 'disabled')
pe1.pack(side = RIGHT)
sb2 = Button(f7, text = u'�ۑ�', command = save, state = 'disabled')
sb2.pack(side = LEFT)
Button(f7, text = u'�I��', command = sys.exit).pack(side = RIGHT)
sb3 = Button(f7, text = u'�V�K�쐬', command = reset, state = 'disabled')
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
#2��ڂɍs�������B���O�C���p�f�[�^������΃��O�C���֐��ցA�Ȃ���Γ��͏�Ԃ�L���ɂ��邾��
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
