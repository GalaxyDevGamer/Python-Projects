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
os.chmod("Galaxy-OS Universe 1.7 Personal.py", 0755)
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
        pwcon.set(u'�o�b�N�A�b�v�t�@�C����������܂���')
    else:
        for name in zf.namelist():
            try:
                uzf = file(name, "wb")
                uzf.write(zf.read(name))
                uzf.close()
            except IOError:
                pwcon.set(u'�������Ȃ����ߕ����ł��܂���')
            zf.close()
            pwcon.set(u'�������������܂���')
def recf():
    if sysfop1.get():
        a = open('money.dat', 'w')
        a.write(str(0))
        a.close()
        sysfop1.set(False)
        aaa.set(u'���łɑ��݂��܂�')
    else:
        aaa.set(u'��������t�@�C����I�����Ă�������')
def rysysf():
    global w5
    if w5 is None or not w5.winfo_exists():
        w5 = Toplevel()
        f1 = Frame(w5)
        f2 = Frame(w5)
        f3 = Frame(w5)
        f4 = Frame(w5)
        f5 = Frame(w5)
        os.chdir("%s\Market" % Paths)
        try:
            open('money.dat', 'r')
        except IOError:
            aaa.set(u'�������K�v�ł�')
        else:
            aaa.set(u'�ُ�Ȃ�')
        os.chdir(Paths)
        Label(w5, text = u'�o�b�N�A�b�v�f�[�^���Ȃ��A�������͔j�������V�X�e���t�@�C���𕜌����܂����A���������ꂽ��Ԃł̕����ɂȂ�܂��B').pack()
        Checkbutton(f1, text = u'�}�[�P�b�g�p�t�@�C��', variable = sysfop1).pack(side = LEFT)
        Label(f1, textvariable = aaa).pack(side = RIGHT)
        Button(f5, text = u'����', command = recf).pack()
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
    pwmcon.set(u'�ۑ�����')
    os.chdir(Paths)
def searchsys():
    try:
        os.chdir('%s\\%s' % (Paths, pwsearch.get()))
    except WindowsError:
        pwmcon.set(u'���͂��ꂽ���̃f�[�^�͑��݂��܂���B')
    try:
        a = open('sysf1.dat', 'r')
        b = open('sysf2.dat', 'r')
    except IOError:
        pwmcon.set(u'�t�@�C����������܂���')
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
        Label(w6, text = u'������T�C�g�E�Q�[���E���̑��̃A�J�E���g�̃��[�U�[��/�p�X���[�h��ۑ����Ă��ł��m�F�ł���悤�ɂ��܂�').pack()
        Label(f1, text = u'���[�U�[��:').pack(side = LEFT)
        Label(f1, textvariable = ids).pack(side = RIGHT)
        Entry(f3, textvariable = pwsearch).pack(side = LEFT)
        Button(f3, text = u'����', command = searchsys).pack(side = RIGHT)
        Label(f8, textvariable = pwmcon).pack()
        Label(f4, text = u'�T�C�g���F').pack(side = LEFT)
        Entry(f4, textvariable = pwtitle).pack(side = RIGHT)
        Label(f5, text = 'ID:').pack(side = LEFT)
        Entry(f5, textvariable = pwids).pack(side = RIGHT)
        Label(f6, text = 'Password:').pack(side = LEFT)
        Entry(f6, textvariable = pwpw, show = '*').pack(side = RIGHT)
        Button(f7, text = u'�ۑ�', command = savepwm).pack(side = LEFT)
        Button(f7, text = u'�V�K�쐬', command = resetpwm).pack(side = RIGHT)
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
                pwcon.set(u'�p�X���[�h��8�����ɂ��Ă�������')
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
            pwcon.set(u'���O�C���p�p�X���[�h�ƊǗ��p�p�X���[�h�͕ʂɂ��Ă�������')
    else:
        pwcon.set(u'�A�J�E���g�����̓p�X���[�h���Ⴂ�܂�')
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
                pwcon.set(u'�p�X���[�h���Ⴂ�܂�')
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
            Label(w7, text = u'�Z�L�����e�B�����̂��߁A�A�J�E���g������͂��ăp�X���[�h�Ǘ��p�̐�p�̃p�X���[�h���쐬���Ă��������B').pack()
            Label(w7, textvariable = pwmcon).pack()
            Entry(f1, textvariable = actname).pack(side = RIGHT)
            Label(f1, text = u'�A�J�E���g��').pack(side = LEFT)
            Entry(f2, textvariable = actpw, show = '*').pack(side = RIGHT)
            Label(f2, text = u'�p�X���[�h(8����)').pack(side = LEFT)
            Entry(f3, textvariable = actpwc, show = '*').pack(side = RIGHT)
            Label(f3, text = u'�Ǘ��p�p�X���[�h(8����)').pack(side = LEFT)
            b13 = Button(f4, text = u'�쐬', command = makepwm)
            b13.pack(side = LEFT)
            b13.bind('<Return>')
            b13.focus_set()
            f1.pack()
            f2.pack()
            f3.pack()
            f4.pack()
        else:
            Label(w7, text = u'�Ǘ��p�p�X���[�h').pack()
            Label(w7, textvariable = pwcon).pack()
            Entry(w7, textvariable = actpwc, show = '*').pack()
            Button(w7, text = u'���O�C��', command = pwml).pack()
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
        pwcon.set(u'�o�b�N�A�b�v���������܂���')
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
        w3.title(u'�ݒ�')
        Label(w3, text = u'�V�X�e��:').pack()
        Button(w3, text = u'�V�X�e�����', width = 15, height = 1, command = about).pack()
        Label(w3, text = u'������A�J�E���g��ID�EPW�̊Ǘ�:').pack()
        Button(w3, text = 'PW Manager', command = pwcheck).pack()
        Label(w3, text = u'�j�����͕��������V�X�e���t�@�C���𕜌�:').pack()
        Button(w3, text = u'�V�X�e���t�@�C������', command = rysysf).pack()
        Label(w3, text = u'�w�i�̕ύX').pack()
        Button(w3, text = u'�ǎ�', command = cw).pack()
        Label(w3, textvariable = pwcon).pack()
        Label(w3, text = u'�o�b�N�A�b�v�ƕ����F').pack()
        Button(w3, text = u'�o�b�N�A�b�v�̍쐬', width = 30, height = 1, command = zipdirectory).pack()
        Button(w3, text = u'�o�b�N�A�b�v����t�@�C���𕜌�', width = 30, height = 1, command = unzip).pack()
    else:
        w3.deiconify()
def done():
    if actname.get():
        if actpw.get() == actpwc.get():
            os.chdir('%s\Users' % Paths)
            try:
                enckey.encrypt(actpw.get())
            except ValueError:
                pwcon.set(u'�p�X���[�h��8�����ɂ��Ă�������')
            else:
                a = open('pw.dat', 'w')
                e1 = enckey.encrypt(actpw.get())
                a.write(e1)
                actpwc.set('')
                pwcon.set('')
                w8.destroy()
            os.chdir(Paths)
        else:
            Message(w4, text = u'�p�X���[�h����v���܂���').pack()
            actpw.set('')
            actpwc.set('')
def cna():
    global w8
    if w8 is None or not w8.winfo_exists():
        w8 = Toplevel()
        os.chdir('%s\Users' % Paths)
        a = open('pw.dat', 'r')
        for i in a:
            de = enckey.decrypt(i)
        if actpwc.get() == de:
            actpwc.set('')
            actpw.set('')
            pwcon.set('')
            Label(w8, textvariable = pwcon).pack()
            Label(w8, text = u'�V�����p�X���[�h�����').pack()
            Entry(w8, textvariable = actpw, show = '*').pack()
            Label(w8, text = u'�m�F�̂��߂�����x����').pack()
            Entry(w8, textvariable = actpwc, show = '*').pack()
            Button(w8, text = u'�ύX����', command = done).pack()
            w9.destroy()
            os.chdir(Paths)
        else:
            pwcon.set(u'�p�X���[�h���Ⴂ�܂�')
    else:
        w8.deiconify()
def pca():
    global w9
    if w9 is None or not w9.winfo_exists():
        w9 = Toplevel()
        actpwc.set('')
        Label(w9, text = u'�m�F�̂��߂Ƀ��O�C��').pack()
        Label(w9, textvariable = pwcon).pack()
        Label(w9, text = '%s' % actname.get()).pack()
        Entry(w9, textvariable = actpwc, show = '*').pack()
        Button(w9, text = u'����', command = cna).pack()
        w10.destroy()
    else:
        w9.deiconify()
def account():
    global w10
    if w10 is None or not w10.winfo_exists():
        w10 = Toplevel()
        Button(w10, text = u'�p�X���[�h��ύX����', command = pca).pack()
        Label(w10, text = u'��ID�͕ύX�ł��܂���').pack()
        Button(w10, text = u'����', command = w2.destroy).pack()
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
        os.chdir('%s\Market' % Paths)
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
        Label(f2, text = u'�N���W�b�g %s�~' % i).pack(side = RIGHT)
        Label(f3, text = u'�A�v���ꗗ�F').pack()
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
        b1 = Button(w14, text = u'�X�^�[�g', command = countdown)
        b2 = Button(w14, text = u'�I��', command = w14.destroy)
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
        os.chdir('%s\\Users' % Paths)
        a = open('user.dat', 'r')
        for i in a:
            i == i
        os.chdir(Paths)
        w12 = Toplevel()
        lf3 = LabelFrame(w12)
        Label(lf3, text = u'���ׂẴv���O����').pack()
        Button(lf3, text = u'�R���s���[�^', width = 20, command = Mycomputer).pack()
        Button(lf3, text = u'�A�J�E���g', width = 20, command = account).pack()
        Button(lf3, text = u'������', width = 20, command = memo).pack()
        Button(lf3, text = u'�^�C�}�[', width = 20, command = timer).pack()
        Button(lf3, text = u'�}�[�P�b�g', width = 20, command = market).pack()
        Button(lf3, text = u'�V�X�e�����', width = 20, command = about).pack()
        Button(lf3, text = u'�ݒ�', width = 20, command = setting).pack()
        lf1 = LabelFrame(w12)
        Label(lf1, text = u'���[�U�[�F%s' % i).pack()
        Label(lf1, text = '').pack()
        Label(lf1, text = u'�v���O����', font = ('New Times Roman', 18)).pack()
        Radiobutton(lf1, text = u'���O�I�t/���[�U�[�؂�ւ�', variable = val1, value = 1).pack()
        Radiobutton(lf1, text = u'�I��', variable = val1, value = 2).pack()
        Label(lf1, text = '').pack()
        Label(lf1, text = u'�R���s���[�^', font = ('New Times Roman', 18)).pack()
        Radiobutton(lf1, text = u'�V���b�g�_�E��', variable = val1, value = 3).pack()
        Radiobutton(lf1, text = u'�ċN��', variable = val1, value = 4).pack()
        Radiobutton(lf1, text = u'�X���[�v', variable = val1, value = 5).pack()
        Radiobutton(lf1, text = u'�x�~', variable = val1, value = 6).pack()
        Radiobutton(lf1, text = u'�L�����Z��', variable = val1, value = 0).pack()
        Label(lf1, text = '').pack()
        Button(lf1, text = u'����', command = poweropt).pack()
        lf3.pack(side = LEFT)
        lf1.pack()
    else:
        w12.deiconify()
def about():
    global w2
    if w2 is None or not w2.winfo_exists():
        w2 = Toplevel()
        Label(w2, text = u'�\�t�g�E�F�A���').pack()
        Label(w2, text = u'�\�t�g�E�F�A��:Galaxy-OS Universe').pack()
        Label(w2, text = u'�o�[�W����:1.7').pack()
        Label(w2, text = u'���C�Z���X:Personal').pack()
        Label(w2, text = u'�J����:Galaxy-OS Universe Dev Team').pack()
        Button(w2, text = u'����', command = w2.destroy).pack()
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
                          text = u'�ۑ��悪�����炸�A�ۑ��ł��܂���',
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
        fn = D.asksaveasfilename(filetypes=[('Text', '*.txt')], title=u'���O��t���ĕۑ�...')
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
    w1.title(os.name=='posix' and 'untitled' or u'����')
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
        w1.title(os.name=='posix' and 'untitled' or u'����')
        textfill.append(t0)
        menubar = Menu(w1)
        filemenu = Menu(menubar)
        filemenu.add_command(label=u'�V�K�쐬', command=lambda : new_memo(w1))
        filemenu.add_command(label=u'�ۑ�', command=lambda : save(w1, t0))
        filemenu.add_command(label=u'�J��', command=lambda : load_File(w1))
        filemenu.add_command(label=u'����', command=lambda : close(w1))

        menubar.add_cascade(label=u'�t�@�C��', menu=filemenu)
        w1.config(menu=menubar)
    else:
        w1.deiconify()
def Mycomputer():
    global w13
    if w13 is None or not w13.winfo_exists():
        w13 = Toplevel()
        Label(w13, text = u'�h���C�u:').pack()
        win32api.GetDiskFreeSpaceEx('C:')
        for i in win32api.GetDiskFreeSpaceEx():
            print i / (1024 ** 3), "GB"
    else:
        w13.deiconify()
try:
    os.chdir('%s\\images' % currentdir)
    M_C = PhotoImage(file = 'mycomputer.gif', width = 60, height = 60)
    i_d = PhotoImage(file = 'account.gif', width = 60, height = 60)
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
    Label(f4, text = u'�R���s���[�^�[').pack()
    b1 = Button(f4, image = i_d, command = account).pack()
    Label(f4, text = u'�A�J�E���g').pack()
    b6 = Button(f4, text = 'Memo', command = memo).pack()
    Label(f4, text = u'������').pack()
    b2 = Button(f4, image = i_d2, command = timer).pack()
    Label(f4, text = u'�^�C�}�[').pack()
    b4 = Button(f4, image = i_d4, command = market).pack()
    Label(f4, text = u'�}�[�P�b�g').pack()
    b5 = Button(f4, image = i_d5, command = setting).pack()
    Label(f4, text = u'�ݒ�').pack()
    L1 = Label(f6, image = i_d6)
    L1.pack()
    piccon.append(L1)
    Label(lf, text = 'Galaxy-OS Universe 1.7 Personal', font = ('New Times Roman', 20), width = 30, height = 2).pack(side = LEFT)
    Button(lf, text = 'Galaxy', command = power).pack(side = LEFT)
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
                pwcon.set(u'�p�X���[�h��8�����œ��͂��Ă�������')
            else:
                if actpw.get() and actpwc.get() and actpw.get() == actpwc.get():
                    idf = ids
                    os.mkdir("Users")
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
                        shutil.move("user.dat", "Users")
                    except WindowsError:
                        pass
                    try:
                        shutil.move("money.dat", "Market")
                    except WindowsError:
                        pass
                    try:
                        shutil.move("pw.dat", "Users")
                    except WindowsError:
                        pass
                    Dialog.Dialog(root, title = 'done', bitmap = 'info',
                                  text = u'�ݒ��K�p���邽�߂ɍċN�����Ă�������',
                                  strings = ['OK'], default = 0)
                    sys.exit()
                else:
                    pwcon.set(u'�A�J�E���g���𐳂������͂��Ă�������')
        else:
            pwcon.set(u'�A�J�E���g���𐳂������͂��Ă�������')
    else:
        pwcon.set(u'�A�J�E���g������͂��Ă�������')
def login():
    bb = actpwc.get()
    try:
        os.chdir('%s\\Users' % Paths)
    except WindowsError:
        pwcon.set(u'�t�H���_��������܂���')
    else:
        try:
            a = open('pw.dat', 'r')
        except IOError:
            pwcon.set('file not found')
            actpwc.set('')
        else:
            for i in a:
                de = enckey.decrypt(i)
            if bb == de:
                if ender.get():
                    w2.destroy()
                    actpwc.set('')
                    pwcon.set('')
                    os.chdir(Paths)
                    root.deiconify()
                else:
                    home()
                    actpwc.set('')
                    w2.destroy()
                    a.close()
                    pwcon.set('')
            else:
                pwcon.set(u'�p�X���[�h���Ⴂ�܂�')
def login2(event):
    bb = actpwc.get()
    try:
        os.chdir('%s\\Users' % Paths)
    except WindowsError:
        pwcon.set(u'�t�H���_��������܂���')
    else:
        try:
            a = open('pw.dat', 'r')
        except IOError:
            pwcon.set('file not found')
            actpwc.set('')
        else:
            for i in a:
                de = enckey.decrypt(i)
            if bb == de:
                if ender.get():
                    w2.destroy()
                    actpwc.set('')
                    pwcon.set('')
                    os.chdir(Paths)
                    root.deiconify()
                else:
                    home()
                    actpwc.set('')
                    w2.destroy()
                    a.close()
                    pwcon.set('')
            else:
                pwcon.set(u'�p�X���[�h���Ⴂ�܂�')
labox = []
try:
    os.chdir('%s\images' % currentdir)
    i_d7 = PhotoImage(file = 'gos.gif', height = 560)
    os.chdir(currentdir)
except WindowsError:
    pass
def actlog():
    global w2
    w2 = Toplevel()
    w2.wm_attributes('-fullscreen', 1)
    lf = Frame(w2)
    lf2 = Frame(w2)
    os.chdir('%s\Users' % Paths)
    a = open('user.dat', 'r')
    for i in a:
        i == i
    os.chdir(Paths)
    pwcon.set('')
    Label(lf2, image = i_d7).pack()
    Label(lf, text = i, font = ('New Times Roman', 18)).pack()
    Label(lf, textvariable = pwcon).pack()
    Label(lf, text = u'�p�X���[�h').pack()
    e = Entry(lf, textvariable = actpwc, show = '*')
    e.pack()
    Button(lf, text = u'���O�C��', command = login).pack()
    Button(lf, text = u'�I��', command = sys.exit).pack()
    e.bind('<Return>', login2)
    la1 = Label(w2, text = 'Galaxy-OS Universe 1.7 Personal', font = ('New Times Roman', 24))
    la1.pack(side = BOTTOM)
    lf2.pack()
    lf.pack()
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
                              text = u'�v���O�����t�@�C����������܂���B%s' % i,
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
        Label(w3, text = u'���̃R���s���[�^�𑀍삷��A�J�E���g�̍쐬').pack()
        Label(w3, textvariable = pwcon).pack()
        Label(f1, textvariable = actname).pack(side = RIGHT)
        Label(f1, text = u'���̃R���s���[�^�̃��[�U�[��').pack(side = LEFT)
        Entry(f2, textvariable = actpw, show = '*').pack(side = RIGHT)
        Label(f2, text = u'�p�X���[�h(8����)').pack(side = LEFT)
        Entry(f3, textvariable = actpwc, show = '*').pack(side = RIGHT)
        Label(f3, text = u'�m�F�̂��߂�����x����').pack(side = LEFT)
        Button(f4, text = u'�쐬', command = makeid).pack(side = LEFT)
        Button(f4, text = u'�L�����Z��', command = sys.exit).pack(side = RIGHT)
        f1.pack()
        f2.pack()
        f3.pack()
        f4.pack()
        root.lower()
    else:
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'���C�Z���X�F�؂���Ă��Ȃ����߁A�{�\�t�g���N���ł��܂���ł���',
                      strings = ['OK'], default = 0)
        sys.exit()
ek1 = 'activate'
dousa = 'ugoitaze'
ugoku = enckey2.encrypt(dousa)
eke = enckey2.encrypt(ek1)
defaultcheck()
root.mainloop()
