# coding:shift-jis

from Tkinter import *
from ScrolledText import *
from tkFileDialog import *
root= Tk()
import tkFileDialog as D
import shutil
import os
import sys
import Dialog
import codecs
w1 = None
w2 = None
w3 = None
w4 = None
w5 = None
w6 = None
st1 = StringVar()
st2 = StringVar()
st3 = StringVar()
st4 = StringVar()
st5 = StringVar()
st6 = StringVar()
st7 = StringVar()
st8 = StringVar()
st9 = StringVar()
st10 = StringVar()
st11 = StringVar()
st12 = StringVar()
st13 = StringVar()
st14 = StringVar()
st15 = StringVar()
st16 = StringVar()
st17 = StringVar()
st18 = StringVar()
st19 = StringVar()
st20 = StringVar()
st21 = StringVar()
st22 = StringVar()
st23 = StringVar()
st24 = StringVar()
st25 = StringVar()
st26 = StringVar()
st27 = StringVar()
st28 = StringVar()
st29 = StringVar()
st30 = StringVar()
st31 = StringVar()
st32 = StringVar()
st33 = StringVar()
st34 = StringVar()
st35 = StringVar()
st36 = StringVar()
st37 = StringVar()
st38 = StringVar()
st39 = StringVar()
st40 = StringVar()
st41 = StringVar()
st42 = StringVar()
st43 = StringVar()
st44 = StringVar()
st45 = StringVar()
st46 = StringVar()
st47 = StringVar()
st48 = StringVar()
st49 = StringVar()
st50 = StringVar()
altcon = StringVar()
rescon = StringVar()
rescon2 = StringVar()
fn = ""
sf = []
sf.append(fn)
currentdir = os.getcwd()
def fileanddir():
    global w4
    if w4 is None or not w4.winfo_exists():
        w4 = Toplevel()
        f1 = Frame(w4)
        f2 = Frame(w4)
        f3 = Frame(w4)
        Label(w4, textvariable = rescon).pack()
        Label(f1, text = u'       科目名:').pack(side = LEFT)
        Entry(f1, textvariable = st48).pack(side = RIGHT)
        Label(f2, text = u'講義のタイトル:').pack(side = LEFT)
        Entry(f2, textvariable = st49).pack(side = RIGHT)
        Button(f3, text = 'OK', command = load_file).pack()
        f1.pack()
        f2.pack()
        f3.pack()
    else:
        w4.deiconify()
def fileanddir2():
    global w5
    if w5 is None or not w5.winfo_exists():
        w5 = Toplevel()
        f1 = Frame(w5)
        f2 = Frame(w5)
        Label(w5, textvariable = rescon2).pack()
        Label(f1, text = u'       科目名:').pack(side = LEFT)
        Entry(f1, textvariable = st50).pack(side = RIGHT)
        Button(f2, text = 'OK', command = listoflesson).pack()
        f1.pack()
        f2.pack()
    else:
        w5.deiconify()
def new_memo():
    st46.set('')
    st47.set('')
    t0.delete('1.0', 'end')
def savekougi():
    data = t0.get('1.0', END)
    if st47.get() == '' or st46.get() == '':
        altcon.set(u'科目又はタイトルが入力されていません')
    else:
        try:
            endata = data.encode('shift-jis')
        except UnicodeEncodeError:
            altcon.set(u'使用できない文字が含まれています')
        else:
            if os.path.isfile("%s\\Lectures\\%s\\%s" % (currentdir, st46.get(), st47.get())):
                try:
                    os.chdir("%s\\Lectures\\%s" % (currentdir, st47.get()))
                except WindowsError:
                    altcon.set(u'エラーが発生したため、保存できませんでした')
                else:
                    f = open(st46.get() + '.txt', 'w')
                    f.write(endata)
                    f.close()
                    os.chdir(currentdir)
                    altcon.set(u'保存完了')
            elif not os.path.isfile("%s\\Lectures\\%s\\%s" % (currentdir, st46.get(), st47.get())):
                try:
                    os.path.exists("%s\\Lecture\\%s" % (currentdir, st47.get()))
                except WindowsError:
                    altcon.set(u'登録されてない科目です')
                else:
                    try:
                        os.chdir("%s\\Lectures\\%s" % (currentdir, st47.get()))
                    except WindowsError:
                        altcon.set(u'エラーが発生したため、保存できませんでした')
                        os.chdir(currentdir)
                    else:
                        f = open(st46.get() + '.txt', 'w')
                        f.write(endata)
                        f.close()
                        os.chdir(currentdir)
                        altcon.set(u'保存完了')
            else:
                altcon.set(u'不明なエラー：保存できませんでした')
def load_file():
    try:
        os.chdir("Lectures")
    except WindowsError:
        rescon.set(u'データが見つかりません')
        os.chdir(currentdir)
    else:
        try:
            os.chdir(st48.get())
        except WindowsError:
            rescon.set(u'データが見つかりません')
            os.chdir(currentdir)
        else:
            fi = open(st49.get() + '.txt')
            t0.delete('1.0', 'end')
            for x in fi:
                t0.insert('end', x.decode('shift-jis'))
            fi.close()
            st47.set(st48.get())
            st46.set(st49.get())
            os.chdir(currentdir)
            w4.destroy()
def kougi():
    try:
        os.chdir("Lectures")
    except WindowsError:
        st2.set(u'不明のエラー：登録できませんでした')
        os.chdir(currentdir)
    else:
        os.mkdir(st1.get())
        os.chdir(currentdir)
        w1.destroy()
        
def register():
    global w1
    if w1 is None or not w1.winfo_exists():
        w1 = Toplevel()
        Label(w1, text = u'受講する講義名を入力').pack()
        Label(w1, textvariable = st2).pack()
        Entry(w1, textvariable = st1).pack()
        Button(w1, text = 'OK', command = kougi).pack()
    else:
        w1.deiconify()
def lists():
    global w2
    if w2 is None or not w2.winfo_exists():
        try:
            os.chdir("%s\\Lectures" % currentdir)
        except WindowsError:
            Dialog.Dialog(root, title = u'エラー', bitmap = 'info',
                          text = u'講義が登録されてないか、フォルダが見つかりません',
                          strings = ['OK'], default = 0)
        else:
            w2 = Toplevel()
            list1 = os.listdir("%s\\Lectures" % currentdir)
            for i in list1:
                shi = i.decode('shift-jis')
                Label(w2, text = shi).pack()
            os.chdir(currentdir)
def listoflesson():
    global w6
    if w6 is None or not w6.winfo_exists():
        try:
            os.chdir("%s\\Lectures\\%s" % (currentdir, st50.get()))
        except WindowsError:
            rescon2.set(u'データが見つかりません')
            os.chdir(currentdir)
        else:
            w6 = Toplevel()
            list1 = os.listdir("%s\\Lectures\\%s" % (currentdir, st50.get()))
            for i in list1:
                Label(w6, text = i).pack()
                w5.destroy()
            os.chdir(currentdir)
    else:
        w6.deiconify()
def save():
    os.chdir(currentdir) 
    try:
        os.chdir("Timetable")
    except WindowsError:
        Dialog.Dialog(root, title = u'エラー', bitmap = 'info',
                          text = u'時間割のデータが見つかりません',
                          strings = ['OK'], default = 0)
    else:
        if st3.get() == '':
            st3.set(u'タイトルがありません')
        f1 = codecs.open('title.dat', 'w', 'shift-jis')
        f1.write(st3.get())
        f1.close()
        if st4.get() == '':
            st4.set(' ')
        f2 = codecs.open('time of lesson1.dat', 'w', 'shift-jis')
        f2.write(st4.get())
        f2.close()
        if st5.get() == '':
            st5.set(' ')
        f3 = codecs.open('time of lesson2.dat', 'w', 'shift-jis')
        f3.write(st5.get())
        f3.close()
        if st6.get() == '':
            st6.set(' ')
        f4 = codecs.open('time of lesson3.dat', 'w', 'shift-jis')
        f4.write(st6.get())
        f4.close()
        if st7.get() == '':
            st7.set(' ')
        f5 = codecs.open('time of lesson4.dat', 'w', 'shift-jis')
        f5.write(st7.get())
        f5.close()
        if st8.get() == '':
            st8.set(' ')
        f6 = codecs.open('time of lesson5.dat', 'w', 'shift-jis')
        f6.write(st8.get())
        f6.close()
        if st9.get() == '':
            st9.set(' ')
        f7 = codecs.open('time of lesson6.dat', 'w', 'shift-jis')
        f7.write(st9.get())
        f7.close()
        if st10.get() == '':
            st10.set(' ')
        f8 = codecs.open('Monper1.dat', 'w', 'shift-jis')
        f8.write(st10.get())
        f8.close()
        if st11.get() == '':
            st11.set(' ')
        f9 = codecs.open('Monper2.dat', 'w', 'shift-jis')
        f9.write(st11.get())
        f9.close()
        if st12.get() == '':
            st12.set(' ')
        f10 = codecs.open('Monper3.dat', 'w', 'shift-jis')
        f10.write(st12.get())
        f10.close()
        if st13.get() == '':
            st13.set(' ')
        f11 = codecs.open('Monper4.dat', 'w', 'shift-jis')
        f11.write(st13.get())
        f11.close()
        if st14.get() == '':
            st14.set(' ')
        f12 = codecs.open('Monper5.dat', 'w', 'shift-jis')
        f12.write(st14.get())
        f12.close()
        if st15.get() == '':
            st15.set(' ')
        f13 = codecs.open('Monper6.dat', 'w', 'shift-jis')
        f13.write(st15.get())
        f13.close()
        if st16.get() == '':
            st16.set(' ')
        f14 = codecs.open('Tueper1.dat', 'w', 'shift-jis')
        f14.write(st16.get())
        f14.close()
        if st17.get() == '':
            st17.set(' ')
        f15 = codecs.open('Tueper2.dat', 'w', 'shift-jis')
        f15.write(st17.get())
        f15.close()
        if st18.get() == '':
            st18.set(' ')
        f16 = codecs.open('Tueper3.dat', 'w', 'shift-jis')
        f16.write(st18.get())
        f16.close()
        if st19.get() == '':
            st19.set(' ')
        f17 = codecs.open('Tueper4.dat', 'w', 'shift-jis')
        f17.write(st19.get())
        f17.close()
        if st20.get() == '':
            st20.set(' ')
        f18 = codecs.open('Tueper5.dat', 'w', 'shift-jis')
        f18.write(st20.get())
        f18.close()
        if st21.get() == '':
            st21.set(' ')
        f19 = codecs.open('Tueper6.dat', 'w', 'shift-jis')
        f19.write(st21.get())
        f19.close()
        if st22.get() == '':
            st22.set(' ')
        f20 = codecs.open('Wedper1.dat', 'w', 'shift-jis')
        f20.write(st22.get())
        f20.close()
        if st23.get() == '':
            st23.set(' ')
        f21 = codecs.open('Wedper2.dat', 'w', 'shift-jis')
        f21.write(st23.get())
        f21.close()
        if st24.get() == '':
            st24.set(' ')
        f22 = codecs.open('Wedper3.dat', 'w', 'shift-jis')
        f22.write(st24.get())
        f22.close()
        if st25.get() == '':
            st25.set(' ')
        f23 = codecs.open('Wedper4.dat', 'w', 'shift-jis')
        f23.write(st25.get())
        f23.close()
        if st26.get() == '':
            st26.set(' ')
        f24 = codecs.open('Wedper5.dat', 'w', 'shift-jis')
        f24.write(st26.get())
        f24.close()
        if st27.get() == '':
            st27.set(' ')
        f25 = codecs.open('Wedper6.dat', 'w', 'shift-jis')
        f25.write(st27.get())
        f25.close()
        if st28.get() == '':
            st28.set(' ')
        f26 = codecs.open('Thuper1.dat', 'w', 'shift-jis')
        f26.write(st28.get())
        f26.close()
        if st29.get() == '':
            st29.set(' ')
        f27 = codecs.open('Thuper2.dat', 'w', 'shift-jis')
        f27.write(st29.get())
        f27.close()
        if st30.get() == '':
            st30.set(' ')
        f28 = codecs.open('Thuper3.dat', 'w', 'shift-jis')
        f28.write(st30.get())
        f28.close()
        if st31.get() == '':
            st31.set(' ')
        f29 = codecs.open('Thuper4.dat', 'w', 'shift-jis')
        f29.write(st31.get())
        f29.close()
        if st32.get() == '':
            st32.set(' ')
        f30 = codecs.open('Thuper5.dat', 'w', 'shift-jis')
        f30.write(st32.get())
        f30.close()
        if st33.get() == '':
            st33.set(' ')
        f31 = codecs.open('Thuper6.dat', 'w', 'shift-jis')
        f31.write(st33.get())
        f31.close()
        if st34.get() == '':
            st34.set(' ')
        f32 = codecs.open('Friper1.dat', 'w', 'shift-jis')
        f32.write(st34.get())
        f32.close()
        if st35.get() == '':
            st35.set(' ')
        f33 = codecs.open('Friper2.dat', 'w', 'shift-jis')
        f33.write(st35.get())
        f33.close()
        if st36.get() == '':
            st36.set(' ')
        f34 = codecs.open('Friper3.dat', 'w', 'shift-jis')
        f34.write(st36.get())
        f34.close()
        if st37.get() == '':
            st37.set(' ')
        f35 = codecs.open('Friper4.dat', 'w', 'shift-jis')
        f35.write(st37.get())
        f35.close()
        if st38.get() == '':
            st38.set(' ')
        f36 = codecs.open('Friper5.dat', 'w', 'shift-jis')
        f36.write(st38.get())
        f36.close()
        if st39.get() == '':
            st39.set(' ')
        f37 = codecs.open('Friper6.dat', 'w', 'shift-jis')
        f37.write(st39.get())
        f37.close()
        if st40.get() == '':
            st40.set(' ')
        f38 = codecs.open('Satper1.dat', 'w', 'shift-jis')
        f38.write(st40.get())
        f38.close()
        if st41.get() == '':
            st41.set(' ')
        f39 = codecs.open('Satper2.dat', 'w', 'shift-jis')
        f39.write(st40.get())
        f39.close()
        if st42.get() == '':
            st42.set(' ')
        f40 = codecs.open('Satper3.dat', 'w', 'shift-jis')
        f40.write(st42.get())
        f40.close()
        if st43.get() == '':
            st43.set(' ')
        f41 = codecs.open('Satper4.dat', 'w', 'shift-jis')
        f41.write(st43.get())
        f41.close()
        if st44.get() == '':
            st44.set(' ')
        f42 = codecs.open('Satper5.dat', 'w', 'shift-jis')
        f42.write(st42.get())
        f42.close()
        if st45.get() == '':
            st45.set(' ')
        f43 = codecs.open('Satper6.dat', 'w', 'shift-jis')
        f43.write(st45.get())
        f43.close()
        os.chdir(currentdir)
def timetable():
    global w3
    if w3 is None or not w3.winfo_exists():
        try:
            os.chdir("Timetable")
        except WindowsError:
            pass
        else:
            try:
                f1 = codecs.open('title.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i1 in f1:
                    st3.set(i1)
            try:
                f2 = codecs.open('time of lesson1.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i2 in f2:
                    st4.set(i2)
            try:
                f3 = codecs.open('time of lesson2.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i3 in f3:
                    st5.set(i3)
            try:
                f4 = codecs.open('time of lesson3.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i4 in f4:
                    st6.set(i4)
            try:
                f5 = codecs.open('time of lesson4.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i5 in f5:
                    st7.set(i5)
            try:
                f6 = codecs.open('time of lesson5.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i6 in f6:
                    st8.set(i6)
            try:
                f7 = codecs.open('time of lesson6.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i7 in f7:
                    st9.set(i7)
            try:
                f8 = codecs.open('Monper1.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i8 in f8:
                    st10.set(i8)
            try:
                f9 = codecs.open('Monper2.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i9 in f9:
                    st11.set(i9)
            try:
                f10 = codecs.open('Monper3.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i10 in f10:
                    st12.set(i10)
            try:
                f11 = codecs.open('Monper4.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i11 in f11:
                    st13.set(i11)
            try:
                f12 = codecs.open('Monper5.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i12 in f12:
                    st14.set(i12)
            try:
                f13 = codecs.open('Monper6.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i13 in f13:
                    st15.set(i13)
            try:
                f14 = codecs.open('Tueper1.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i14 in f14:
                    st16.set(i14)
            try:
                f15 = codecs.open('Tueper2.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i15 in f15:
                    st17.set(i15)
            try:
                f16 = codecs.open('Tueper3.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i16 in f16:
                    st18.set(i16)
            try:
                f17 = codecs.open('Tueper4.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i17 in f17:
                    st19.set(i17)
            try:
                f18 = codecs.open('Tueper5.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i18 in f18:
                    st20.set(i18)
            try:
                f19 = codecs.open('Tueper6.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i19 in f19:
                    st21.set(i19)
            try:
                f20 = codecs.open('Wedper1.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i20 in f20:
                    st22.set(i20)
            try:
                f21 = codecs.open('Wedper2.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i21 in f21:
                    st23.set(i21)
            try:
                f22 = codecs.open('Wedper3.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i22 in f22:
                    st24.set(i22)
            try:
                f23 = codecs.open('Wedper4.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i23 in f23:
                    st25.set(i23)
            try:
                f24 = codecs.open('Wedper5.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i24 in f24:
                    st26.set(i24)
            try:
                f25 = codecs.open('Wedper6.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i25 in f25:
                    st27.set(i25)
            try:
                f26 = codecs.open('Thuper1.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i26 in f26:
                    st28.set(i26)
            try:
                f27 = codecs.open('Thuper2.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i27 in f27:
                    st29.set(i27)
            try:
                f28 = codecs.open('Thuper3.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i28 in f28:
                    st30.set(i28)
            try:
                f29 = codecs.open('Thuper4.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i29 in f29:
                    st31.set(i29)
            try:
                f30 = codecs.open('Thuper5.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i30 in f30:
                    st32.set(i30)
            try:
                f31 = codecs.open('Thuper6.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i31 in f31:
                    st33.set(i31)
            try:
                f32 = codecs.open('Friper1.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i32 in f32:
                    st34.set(i32)
            try:
                f33 = codecs.open('Friper2.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i33 in f33:
                    st35.set(i33)
            try:
                f34 = codecs.open('Friper3.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i34 in f34:
                    st36.set(i34)
            try:
                f35 = codecs.open('Friper4.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i35 in f35:
                    st37.set(i35)
            try:
                f36 = codecs.open('Friper5.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i36 in f36:
                    st38.set(i36)
            try:
                f37 = codecs.open('Friper6.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i37 in f37:
                    st39.set(i37)
            try:
                f38 = codecs.open('Satper1.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i38 in f38:
                    st40.set(i38)
            try:
                f39 = codecs.open('Satper2.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i39 in f39:
                    st41.set(i39)
            try:
                f40 = codecs.open('Satper3.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i40 in f40:
                    st42.set(i40)
            try:
                f41 = codecs.open('Satper4.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i41 in f41:
                    st43.set(i41)
            try:
                f42 = codecs.open('Satper5.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i42 in f42:
                    st44.set(i42)
            try:
                f43 = codecs.open('Satper6.dat', 'r', 'shift-jis')
            except IOError:
                pass
            else:
                for i43 in f43:
                    st45.set(i43)
            os.chdir(currentdir)
        w3 = Toplevel()
        lf1 = LabelFrame(w3)
        lf2 = LabelFrame(w3)
        lf3 = LabelFrame(w3)
        lf4 = LabelFrame(w3)
        lf5 = LabelFrame(w3)
        lf6 = LabelFrame(w3)
        lf7 = LabelFrame(w3)
        lf8 = LabelFrame(w3)
        Label(lf2, text = u'学部・学年・学期：').pack(side = LEFT)
        Entry(lf2, textvariable = st3).pack(side = LEFT)
        Button(lf2, text = u'保存', command = save).pack(side = RIGHT)
        Label(lf1, text = u'時間').pack(side = LEFT)
        Label(lf1, text = u'1時限:').pack(side = LEFT)
        Entry(lf1, textvariable = st4).pack(side = LEFT)
        Label(lf1, text = u'2時限:').pack(side = LEFT)
        Entry(lf1, textvariable = st5).pack(side = LEFT)
        Label(lf1, text = u'3時限:').pack(side = LEFT)
        Entry(lf1, textvariable = st6).pack(side = LEFT)
        Label(lf1, text = u'4時限:').pack(side = LEFT)
        Entry(lf1, textvariable = st7).pack(side = LEFT)
        Label(lf1, text = u'5時限:').pack(side = LEFT)
        Entry(lf1, textvariable = st8).pack(side = LEFT)
        Label(lf1, text = u'6時限:').pack(side = LEFT)
        Entry(lf1, textvariable = st9).pack(side = LEFT)
        Label(lf3, text = u'月曜').pack(side = LEFT)
        Label(lf3, text = u'1時限:').pack(side = LEFT)
        Entry(lf3, textvariable = st10).pack(side = LEFT)
        Label(lf3, text = u'2時限:').pack(side = LEFT)
        Entry(lf3, textvariable = st11).pack(side = LEFT)
        Label(lf3, text = u'3時限:').pack(side = LEFT)
        Entry(lf3, textvariable = st12).pack(side = LEFT)
        Label(lf3, text = u'4時限:').pack(side = LEFT)
        Entry(lf3, textvariable = st13).pack(side = LEFT)
        Label(lf3, text = u'5時限:').pack(side = LEFT)
        Entry(lf3, textvariable = st14).pack(side = LEFT)
        Label(lf3, text = u'6時限:').pack(side = LEFT)
        Entry(lf3, textvariable = st15).pack(side = LEFT)
        Label(lf4, text = u'火曜').pack(side = LEFT)
        Label(lf4, text = u'1時限:').pack(side = LEFT)
        Entry(lf4, textvariable = st16).pack(side = LEFT)
        Label(lf4, text = u'2時限:').pack(side = LEFT)
        Entry(lf4, textvariable = st17).pack(side = LEFT)
        Label(lf4, text = u'3時限:').pack(side = LEFT)
        Entry(lf4, textvariable = st18).pack(side = LEFT)
        Label(lf4, text = u'4時限:').pack(side = LEFT)
        Entry(lf4, textvariable = st19).pack(side = LEFT)
        Label(lf4, text = u'5時限:').pack(side = LEFT)
        Entry(lf4, textvariable = st20).pack(side = LEFT)
        Label(lf4, text = u'6時限:').pack(side = LEFT)
        Entry(lf4, textvariable = st21).pack(side = LEFT)
        Label(lf5, text = u'水曜').pack(side = LEFT)
        Label(lf5, text = u'1時限:').pack(side = LEFT)
        Entry(lf5, textvariable = st22).pack(side = LEFT)
        Label(lf5, text = u'2時限:').pack(side = LEFT)
        Entry(lf5, textvariable = st23).pack(side = LEFT)
        Label(lf5, text = u'3時限:').pack(side = LEFT)
        Entry(lf5, textvariable = st24).pack(side = LEFT)
        Label(lf5, text = u'4時限:').pack(side = LEFT)
        Entry(lf5, textvariable = st25).pack(side = LEFT)
        Label(lf5, text = u'5時限:').pack(side = LEFT)
        Entry(lf5, textvariable = st26).pack(side = LEFT)
        Label(lf5, text = u'6時限:').pack(side = LEFT)
        Entry(lf5, textvariable = st27).pack(side = LEFT)
        Label(lf6, text = u'木曜').pack(side = LEFT)
        Label(lf6, text = u'1時限:').pack(side = LEFT)
        Entry(lf6, textvariable = st28).pack(side = LEFT)
        Label(lf6, text = u'2時限:').pack(side = LEFT)
        Entry(lf6, textvariable = st29).pack(side = LEFT)
        Label(lf6, text = u'3時限:').pack(side = LEFT)
        Entry(lf6, textvariable = st30).pack(side = LEFT)
        Label(lf6, text = u'4時限:').pack(side = LEFT)
        Entry(lf6, textvariable = st31).pack(side = LEFT)
        Label(lf6, text = u'5時限:').pack(side = LEFT)
        Entry(lf6, textvariable = st32).pack(side = LEFT)
        Label(lf6, text = u'6時限:').pack(side = LEFT)
        Entry(lf6, textvariable = st33).pack(side = LEFT)
        Label(lf7, text = u'金曜').pack(side = LEFT)
        Label(lf7, text = u'1時限:').pack(side = LEFT)
        Entry(lf7, textvariable = st34).pack(side = LEFT)
        Label(lf7, text = u'2時限:').pack(side = LEFT)
        Entry(lf7, textvariable = st35).pack(side = LEFT)
        Label(lf7, text = u'3時限:').pack(side = LEFT)
        Entry(lf7, textvariable = st36).pack(side = LEFT)
        Label(lf7, text = u'4時限:').pack(side = LEFT)
        Entry(lf7, textvariable = st37).pack(side = LEFT)
        Label(lf7, text = u'5時限:').pack(side = LEFT)
        Entry(lf7, textvariable = st38).pack(side = LEFT)
        Label(lf7, text = u'6時限:').pack(side = LEFT)
        Entry(lf7, textvariable = st39).pack(side = LEFT)
        Label(lf8, text = u'土曜').pack(side = LEFT)
        Label(lf8, text = u'1時限:').pack(side = LEFT)
        Entry(lf8, textvariable = st40).pack(side = LEFT)
        Label(lf8, text = u'2時限:').pack(side = LEFT)
        Entry(lf8, textvariable = st41).pack(side = LEFT)
        Label(lf8, text = u'3時限:').pack(side = LEFT)
        Entry(lf8, textvariable = st42).pack(side = LEFT)
        Label(lf8, text = u'4時限:').pack(side = LEFT)
        Entry(lf8, textvariable = st43).pack(side = LEFT)
        Label(lf8, text = u'5時限:').pack(side = LEFT)
        Entry(lf8, textvariable = st44).pack(side = LEFT)
        Label(lf8, text = u'6時限:').pack(side = LEFT)
        Entry(lf8, textvariable = st45).pack(side = LEFT)
        lf2.pack()
        lf1.pack()
        lf3.pack()
        lf4.pack()
        lf5.pack()
        lf6.pack()
        lf7.pack()
        lf8.pack()
    else:
        w3.deiconify()
m0 = Menu(root)
root.configure(menu = m0)
m1 = Menu(m0, tearoff = False)
m2 = Menu(m0, tearoff = False)
m0.add_cascade(label = u'ファイル', under = 0, menu = m1)
m1.add_command(label = u'終了', command = sys.exit)
F1 = LabelFrame(root)
F2 = Frame(root)
F3 = LabelFrame(root)
F4 = Frame(root)
t0 = ScrolledText(root)
root.title("MLU")
Label(root, text = u'大学講義マネージャー', font = ['New Times Roman', 18]).pack()
Label(root, text = u'講義内容の表示・編集ができます').pack()
Button(F1, text = u'科目の登録    ', command = register).pack(side = LEFT)
Button(F1, text = u'登録した科目の一覧', command = lists).pack(side = LEFT)
Button(F1, text = u'保存した講義の一覧', command = fileanddir2).pack(side = LEFT)
Button(F1, text = u'時間割', command = timetable).pack(side = LEFT)
Label(F2, textvariable = altcon).pack()
Label(F4, text = 'Title:').pack(side = LEFT)
Entry(F4, textvariable = st46).pack(side = LEFT)
Label(F4, text = u'科目:').pack(side = LEFT)
Entry(F4, textvariable = st47).pack(side = LEFT)
Button(F4, text = u'新規作成', command = new_memo).pack(side = LEFT)
Button(F4, text = u'保存', command = savekougi).pack(side = LEFT)
Button(F4, text = u'保存した講義を開く', command = fileanddir).pack(side = LEFT)
F1.pack()
F2.pack()
F3.pack()
F4.pack(fill = BOTH)
t0.pack()
root.mainloop()
