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
            pwmcon.set(u'�f�B���N�g���������ł�')
        else:
            a = open('sysf1.dat', 'w')
            a.write(pwids.get())
            a.close()
            shutil.move("sysf1.dat", "%s\\%s" % (ad.get(), pwtitle.get()))
            b = open('sysf2.dat', 'w')
            b.write(pwpw.get())
            b.close()
            shutil.move("sysf2.dat", "%s\\%s" % (ad.get(), pwtitle.get()))
            pwmcon.set(u'�ۑ�����')
    if i1.get() == 0:
        try:
            os.mkdir("C:\\Users\\%s\\Desktop\\PW Manager 1.0.2\\%s" % (su.get(), pwtitle.get()))
        except WindowsError:
            pwmcon.set(u'���[�U�[�����������ݒ肳��ĂȂ����A�f�B���N�g���ɖ�肪����܂�')
        a = open('sysf1.dat', 'w')
        a.write(pwids.get())
        a.close()
        shutil.move("sysf1.dat", "%s" % pwtitle.get())
        b = open('sysf2.dat', 'w')
        b.write(pwpw.get())
        b.close()
        shutil.move("sysf2.dat", "%s" % pwtitle.get())
        pwmcon.set(u'�ۑ�����')
def searchsys():
    if i1.get() == 1:
        try:
            os.chdir("%s\\%s" % (ad.get(), pwsearch.get()))
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
            os.chdir('%s' % ad.get())
    if i1.get() == 0:
        try:
            os.chdir("%s" % pwsearch.get())
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
            os.chdir('C:\\Users\\%s\\Desktop\\PW manager 1.0.2' % su.get())
def setu():
    if su.get() == '':
        con.set(u'���[�U�[������͂��Ă�������')
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
    Label(f1, text = u'���̃\�t�g�𗘗p����R���s���[�^�̃��[�U�[�������').pack(side = LEFT)
    Entry(f1, textvariable = su).pack(side = RIGHT)
    Button(f2, text = 'OK', command = setu).pack(side = LEFT)
    Button(f2, text = 'Cancel', command = w1.destroy).pack(side = RIGHT)
    f1.pack()
    f2.pack()
def decide():
    if i1.get() == 1:
        if ad.get() == '':
            con.set(u'�p�X����͂��Ă�������')
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
    r1 = Radiobutton(f1, text = u'�t���p�X�ŏꏊ���w��(�㋉�Ҍ���)', variable = i1, value = 1)
    r1.pack(side = LEFT)
    e1 = Entry(f1, textvariable = ad)
    e1.pack(side = RIGHT)
    r2 = Radiobutton(f2, text = u'�f�t�H���g�Ɏw��', variable = i1, value = 0)
    r2.pack()
    Button(f3, text = 'OK', command = decide).pack()
    f1.pack()
    f4.pack()
    f2.pack()
    f3.pack()
def htu():
    global w3
    w3 = Toplevel()
    Label(w3, text = u'1.[�ݒ�]�ɂă��[�U�[����o�^�B�ς�ł�ꍇ��2��').pack()
    Label(w3, text = u'2.[�ݒ�]�ɂĕۑ��ꏊ��ݒ肷��B�f�t�H���g�ł����ꍇ3��').pack()
    Label(w3, text = u'�t���p�X�w�肷��ꍇ�̓p�X���Ԉ���Ă���Ɛ������ۑ�����Ȃ��Ȃ�܂�').pack()
    Label(w3, text = u'3.�T�C�g�EID�EPW����͂��A�ۑ�����B').pack()
    Label(w3, text = u'4.3�ɂĕۑ������T�C�g���������{�b�N�X�ł������悤�ɓ���').pack()
def sup():
    global w4
    w4 = Toplevel()
    Label(w4, text = u'Q.�t���p�X�ŃA�J�E���g��ۑ������̂ŕۑ��ꏊ���f�t�H���g��').pack()
    Label(w4, text = u'�߂�����ۑ������A�J�E���g��ǂݍ��߂Ȃ��Ȃ��Ă��܂����B').pack()
    Label(w4, text = u'A.�ݒ肵���t���p�X�Ɉړ����A�t�H���_���f�X�N�g�b�v�Ɉڂ���').pack()
    Label(w4, text = u'�ۑ��ꏊ���t���p�X�ɐݒ肵�A�Č������Ă�������').pack()
m0 = Menu(root)
root.configure(menu = m0)
m1 = Menu(m0, tearoff = False)
m2 = Menu(m0, tearoff = False)
m0.add_cascade(label = u'�ݒ�', under = 0, menu = m1)
m0.add_cascade(label = 'HELP', under = 0, menu = m2)
m1.add_command(label = u'���[�U�[����ݒ�', command = cu)
m1.add_command(label = u'�ۑ��ꏊ��ݒ�', command = changed)
m2.add_command(label = u'�g����', command = htu)
m2.add_command(label = u'�������Ƃ���', command = sup)
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
Label(root, text = u'������T�C�g�E�Q�[���E���̑��̃A�J�E���g�̃��[�U�[��/�p�X���[�h��ۑ����Ă��ł��m�F�ł���悤�ɂ��܂�').pack()
Label(lf1, text = u'�����{�b�N�X').pack()
Entry(lf1, textvariable = pwsearch).pack(side = LEFT)
Button(lf1, text = u'����', command = searchsys).pack(side = RIGHT)
Label(f8, textvariable = pwmcon).pack()
Label(f3, text = u'�A�J�E���g��ۑ�').pack()
Label(f4, text = u'�T�C�g��(�S�p)�F').pack(side = LEFT)
Entry(f4, textvariable = pwtitle).pack(side = RIGHT)
Label(f5, text = 'ID:').pack(side = LEFT)
Entry(f5, textvariable = pwids).pack(side = RIGHT)
Label(f6, text = 'Password:').pack(side = LEFT)
Entry(f6, textvariable = pwpw, show = '*').pack(side = RIGHT)
Button(f7, text = u'�ۑ�', command = savepwm).pack(side = LEFT)
Button(f7, text = u'�I��', command = sys.exit).pack(side = RIGHT)
Button(f7, text = u'�V�K�쐬', command = resetpwm).pack(side = RIGHT)
lf1.pack()
f8.pack()
f3.pack()
f4.pack()
f5.pack()
f6.pack()
f7.pack()
root.mainloop()
