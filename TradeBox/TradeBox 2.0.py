# coding:shift-jis

from Tkinter import *
import sys
import Dialog
import Crypto.Cipher.DES
import codecs
import os
key = Crypto.Cipher.DES.new("TBACTENC", Crypto.Cipher.DES.MODE_ECB)

root = Tk()

w1 = None
w2 = None
w3 = None
w4 = None
st1 = StringVar()
st2 = StringVar()
st3 = StringVar()
st4 = StringVar()
st5 = StringVar()
tota = StringVar()
moneyval = StringVar()
val = IntVar()
chec = BooleanVar()
kane = StringVar()
kane.set(0)
item1st = StringVar()
item1pr = StringVar()
item2st = StringVar()
item2pr = StringVar()
item3st = StringVar()
item3pr = StringVar()
item4st = StringVar()
item4pr = StringVar()
item5st = StringVar()
item5pr = StringVar()
item6st = StringVar()
item6pr = StringVar()
item7st = StringVar()
item7pr = StringVar()
item8st = StringVar()
item8pr = StringVar()
item9st = StringVar()
item9pr = StringVar()
item10st = StringVar()
item10pr = StringVar()
cid = StringVar()
cpw = StringVar()
xyz = []

ii = 0
pri = []
pri.append(ii)
wallet = []
chargem = []
bb = 0
countm = 0
chargem.append(countm)
wallet.append(bb)
kina = []
calcu = []
calcula = 0
calcu.append(calcula)
curd = os.getcwd()
a = open('item1.dat', 'r')
b = open('item2.dat', 'r')
c = open('item3.dat', 'r')
d = open('item4.dat', 'r')
e = open('item5.dat', 'r')
f = open('item6.dat', 'r')
g = open('item7.dat', 'r')
h = open('item8.dat', 'r')
i = open('item9.dat', 'r')
j = open('item10.dat', 'r')
k = open('item1pr.dat', 'r')
l = open('item2pr.dat', 'r')
m = open('item3pr.dat', 'r')
n = open('item4pr.dat', 'r')
o = open('item5pr.dat', 'r')
p = open('item6pr.dat', 'r')
q = open('item7pr.dat', 'r')
r = open('item8pr.dat', 'r')
s = open('item9pr.dat', 'r')
t = open('item10pr.dat', 'r')
for a2 in a:
    a2 == a2
for b2 in b:
    b2 == b2
for c2 in c:
    c2 == c2
for dd2 in d:
    dd2 == dd2
for e2 in e:
    e2 == e2
for F2 in f:
    F2 == F2
for g2 in g:
    g2 == g2
for h2 in h:
    h2 == h2
for ii2 in i:
    ii2 == ii2
for j2 in j:
    j2 == j2
for k2 in k:
    k2 == k2
for l2 in l:
    l2 == l2
for m2 in m:
    m2 == m2
for n2 in n:
    n2 == n2
for o2 in o:
    o2 == o2
for p2 in p:
    p2 == p2
for q2 in q:
    q2 == q2
for r2 in r:
    r2 == r2
for s2 in s:
    s2 == s2
for t2 in t:
    t2 == t2

def item1r():
    f1 = open('item1.dat', 'w')
    f2 = open('item1pr.dat', 'w')
    f1.write(item1st.get())
    f2.write(item1pr.get())
    f1.close()
    f2.close()
    w3.destroy()
    w4.destroy()
    L1.configure(text = item1st.get())
    P1.configure(text = item1pr.get())
def item2r():
    f1 = open('item2.dat', 'w')
    f2 = open('item2pr.dat', 'w')
    f1.write(item2st.get())
    f2.write(item2pr.get())
    f1.close()
    f2.close()
    w3.destroy()
    w4.destroy()
    L2.configure(text = item2st.get())
    P2.configure(text = item2pr.get())
def item3r():
    f1 = open('item3.dat', 'w')
    f2 = open('item3pr.dat', 'w')
    f1.write(item3st.get())
    f2.write(item3pr.get())
    f1.close()
    f2.close()
    w3.destroy()
    w4.destroy()
    L3.configure(text = item3st.get())
    P3.configure(text = item3pr.get())
def item4r():
    f1 = open('item4.dat', 'w')
    f2 = open('item4pr.dat', 'w')
    f1.write(item4st.get())
    f2.write(item4pr.get())
    f1.close()
    f2.close()
    w3.destroy()
    w4.destroy()
    L4.configure(text = item4st.get())
    P4.configure(text = item4pr.get())
def item5r():
    f1 = open('item5.dat', 'w')
    f2 = open('item5pr.dat', 'w')
    f1.write(item5st.get())
    f2.write(item5pr.get())
    f1.close()
    f2.close()
    w3.destroy()
    w4.destroy()
    L5.configure(text = item5st.get())
    P5.configure(text = item5pr.get())
def item6r():
    f1 = open('item6.dat', 'w')
    f2 = open('item6pr.dat', 'w')
    f1.write(item6st.get())
    f2.write(item6pr.get())
    f1.close()
    f2.close()
    w3.destroy()
    w4.destroy()
    L6.configure(text = item6st.get())
    P6.configure(text = item6pr.get())
def item7r():
    f1 = open('item7.dat', 'w')
    f2 = open('item7pr.dat', 'w')
    f1.write(item7st.get())
    f2.write(item7pr.get())
    f1.close()
    f2.close()
    w3.destroy()
    w4.destroy()
    L7.configure(text = item7st.get())
    P7.configure(text = item7pr.get())
def item8r():
    f1 = open('item8.dat', 'w')
    f2 = open('item8pr.dat', 'w')
    f1.write(item8st.get())
    f2.write(item8pr.get())
    f1.close()
    f2.close()
    w3.destroy()
    w4.destroy()
    L8.configure(text = item8st.get())
    P8.configure(text = item8pr.get())
def item9r():
    f1 = open('item9.dat', 'w')
    f2 = open('item9pr.dat', 'w')
    f1.write(item9st.get())
    f2.write(item9pr.get())
    f1.close()
    f2.close()
    w3.destroy()
    w4.destroy()
    L9.configure(text = item9st.get())
    P9.configure(text = item9pr.get())
def item10r():
    f1 = open('item10.dat', 'w')
    f2 = open('item10pr.dat', 'w')
    f1.write(item10st.get())
    f2.write(item10pr.get())
    f1.close()
    f2.close()
    w3.destroy()
    w4.destroy()
    L10.configure(text = item10st.get())
    P10.configure(text = item10pr.get())
def item1():
    global w4
    w4 = Toplevel()
    Label(w4, text = '商品名(ローマ字)').pack()
    Entry(w4, text = item1st).pack()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item1pr).pack()
    Button(w4, text = '出品', command = item1r).pack()
def item2():
    global w4
    w4 = Toplevel()
    Label(w4, text = '商品名(ローマ字)').pack()
    Entry(w4, text = item2st).pack()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item2pr).pack()
    Button(w4, text = '出品', command = item2r).pack()
def item3():
    global w4
    w4 = Toplevel()
    Label(w4, text = '商品名(ローマ字)').pack()
    Entry(w4, text = item3st).pack()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item3pr).pack()
    Button(w4, text = '出品', command = item3r).pack()
def item4():
    global w4
    w4 = Toplevel()
    Label(w4, text = '商品名(ローマ字)').pack()
    Entry(w4, text = item4st).pack()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item4pr).pack()
    Button(w4, text = '出品', command = item4r).pack()
def item5():
    global w4
    w4 = Toplevel()
    Label(w4, text = '商品名(ローマ字)').pack()
    Entry(w4, text = item5st).pack()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item5pr).pack()
    Button(w4, text = '出品', command = item5r).pack()
def item6():
    global w4
    w4 = Toplevel()
    Label(w4, text = '商品名(ローマ字)').pack()
    Entry(w4, text = item6st).pack()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item6pr).pack()
    Button(w4, text = '出品', command = item6r).pack()
def item7():
    global w4
    w4 = Toplevel()
    Label(w4, text = '商品名(ローマ字)').pack()
    Entry(w4, text = item7st).pack()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item7pr).pack()
    Button(w4, text = '出品', command = item7r).pack()
def item8():
    global w4
    w4 = Toplevel()
    Label(w4, text = '商品名(ローマ字)').pack()
    Entry(w4, text = item8st).pack()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item8pr).pack()
    Button(w4, text = '出品', command = item8r).pack()
def item9():
    global w4
    w4 = Toplevel()
    Label(w4, text = '商品名(ローマ字)').pack()
    Entry(w4, text = item9st).pack()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item9pr).pack()
    Button(w4, text = '出品', command = item9r).pack()
def item10():
    global w4
    w4 = Toplevel()
    Label(w4, text = '商品名(ローマ字)').pack()
    Entry(w4, text = item10st).pack()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item10pr).pack()
    Button(w4, text = '出品', command = item10r).pack()
def price():
    global w3
    w3 = Toplevel()
    f1 = Frame(w3)
    f2 = Frame(w3)
    Button(f1, text = 'item1', command = item1).pack()
    Button(f1, text = 'item2', command = item2).pack()
    Button(f1, text = 'item3', command = item3).pack()
    Button(f1, text = 'item4', command = item4).pack()
    Button(f1, text = 'item5', command = item5).pack()
    Button(f1, text = 'item6', command = item6).pack()
    Button(f1, text = 'item7', command = item7).pack()
    Button(f1, text = 'item8', command = item8).pack()
    Button(f1, text = 'item9', command = item9).pack()
    Button(f1, text = 'item10', command = item10).pack()
    f1.pack(side = LEFT)
    f2.pack(side = RIGHT)
def i1r():
    f2 = open('item1pr.dat', 'w')
    f2.write(item1pr.get())
    f2.close()
    w3.destroy()
    w4.destroy()
    P1.configure(text = item1pr.get())
def i2r():
    f2 = open('item2pr.dat', 'w')
    f2.write(item2pr.get())
    f2.close()
    w3.destroy()
    w4.destroy()
    P2.configure(text = item2pr.get())
def i3r():
    f2 = open('item3pr.dat', 'w')
    f2.write(item3pr.get())
    f2.close()
    w3.destroy()
    w4.destroy()
    P3.configure(text = item3pr.get())
def i4r():
    f2 = open('item4pr.dat', 'w')
    f2.write(item4pr.get())
    f2.close()
    w3.destroy()
    w4.destroy()
    P4.configure(text = item4pr.get())
def i5r():
    f2 = open('item5pr.dat', 'w')
    f2.write(item5pr.get())
    f2.close()
    w3.destroy()
    w4.destroy()
    P5.configure(text = item5pr.get())
def i6r():
    f2 = open('item6pr.dat', 'w')
    f2.write(item6pr.get())
    f2.close()
    w3.destroy()
    w4.destroy()
    P6.configure(text = item6pr.get())
def i7r():
    f2 = open('item7pr.dat', 'w')
    f2.write(item7pr.get())
    f2.close()
    w3.destroy()
    w4.destroy()
    P7.configure(text = item7pr.get())
def i8r():
    f2 = open('item8pr.dat', 'w')
    f2.write(item8pr.get())
    f2.close()
    w3.destroy()
    w4.destroy()
    P8.configure(text = item8pr.get())
def i9r():
    f2 = open('item9pr.dat', 'w')
    f2.write(item9pr.get())
    f2.close()
    w3.destroy()
    w4.destroy()
    P9.configure(text = item9pr.get())
def i10r():
    f2 = open('item10pr.dat', 'w')
    f2.write(item10pr.get())
    f2.close()
    w3.destroy()
    w4.destroy()
    P10.configure(text = item10pr.get())
def i1():
    global w4
    w4 = Toplevel()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item1pr).pack()
    Button(w4, text = '出品', command = i1r).pack()
def i2():
    global w4
    w4 = Toplevel()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item2pr).pack()
    Button(w4, text = '出品', command = i2r).pack()
def i3():
    global w4
    w4 = Toplevel()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item3pr).pack()
    Button(w4, text = '出品', command = i3r).pack()
def i4():
    global w4
    w4 = Toplevel()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item4pr).pack()
    Button(w4, text = '出品', command = i4r).pack()
def i5():
    global w4
    w4 = Toplevel()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item5pr).pack()
    Button(w4, text = '出品', command = i5r).pack()
def i6():
    global w4
    w4 = Toplevel()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item6pr).pack()
    Button(w4, text = '出品', command = i6r).pack()
def i7():
    global w4
    w4 = Toplevel()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item7pr).pack()
    Button(w4, text = '出品', command = i7r).pack()
def i8():
    global w4
    w4 = Toplevel()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item8pr).pack()
    Button(w4, text = '出品', command = i8r).pack()
def i9():
    global w4
    w4 = Toplevel()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item9pr).pack()
    Button(w4, text = '出品', command = i9r).pack()
def i10():
    global w4
    w4 = Toplevel()
    Label(w4, text = '値段').pack()
    Entry(w4, text = item10pr).pack()
    Button(w4, text = '出品', command = i10r).pack()
def cp():
    global w3
    w3 = Toplevel()
    f1 = Frame(w3)
    f2 = Frame(w3)
    Button(f1, text = 'item1', command = i1).pack()
    Button(f1, text = 'item2', command = i2).pack()
    Button(f1, text = 'item3', command = i3).pack()
    Button(f1, text = 'item4', command = i4).pack()
    Button(f1, text = 'item5', command = i5).pack()
    Button(f1, text = 'item6', command = i6).pack()
    Button(f1, text = 'item7', command = i7).pack()
    Button(f1, text = 'item8', command = i8).pack()
    Button(f1, text = 'item9', command = i9).pack()
    Button(f1, text = 'item10', command = i10).pack()
    f1.pack(side = LEFT)
    f2.pack(side = RIGHT)
def d1():
    f1 = open('item1.dat', 'w')
    f2 = open('item1pr.dat', 'w')
    f1.write('empty')
    f2.write('0')
    L1.configure(text = 'empty')
    P1.configure(text = int(0))
    Dialog.Dialog(root, title = 'done', bitmap = 'info',
                  text = '商品を回収しました',
                  strings = ['OK'], default = 0)
    w3.destroy()
def d2():
    f1 = open('item2.dat', 'w')
    f2 = open('item2pr.dat', 'w')
    f1.write('empty')
    f2.write('0')
    L2.configure(text = 'empty')
    P2.configure(text = int(0))
    Dialog.Dialog(root, title = 'done', bitmap = 'info',
                  text = '商品を回収しました',
                  strings = ['OK'], default = 0)
    w3.destroy()
def d3():
    f1 = open('item3.dat', 'w')
    f2 = open('item3pr.dat', 'w')
    f1.write('empty')
    f2.write('0')
    L3.configure(text = 'empty')
    P3.configure(text = int(0))
    Dialog.Dialog(root, title = 'done', bitmap = 'info',
                  text = '商品を回収しました',
                  strings = ['OK'], default = 0)
    w3.destroy()
def d4():
    f1 = open('item4.dat', 'w')
    f2 = open('item4pr.dat', 'w')
    f1.write('empty')
    f2.write('0')
    L4.configure(text = 'empty')
    P4.configure(text = int(0))
    Dialog.Dialog(root, title = 'done', bitmap = 'info',
                  text = '商品を回収しました',
                  strings = ['OK'], default = 0)
    w3.destroy()
def d5():
    f1 = open('item5.dat', 'w')
    f2 = open('item5pr.dat', 'w')
    f1.write('empty')
    f2.write('0')
    L5.configure(text = 'empty')
    P5.configure(text = int(0))
    Dialog.Dialog(root, title = 'done', bitmap = 'info',
                  text = '商品を回収しました',
                  strings = ['OK'], default = 0)
    w3.destroy()
def d6():
    f1 = open('item6.dat', 'w')
    f2 = open('item6pr.dat', 'w')
    f1.write('empty')
    f2.write('0')
    L6.configure(text = 'empty')
    P6.configure(text = int(0))
    Dialog.Dialog(root, title = 'done', bitmap = 'info',
                  text = '商品を回収しました',
                  strings = ['OK'], default = 0)
    w3.destroy()
def d7():
    f1 = open('item7.dat', 'w')
    f2 = open('item7pr.dat', 'w')
    f1.write('empty')
    f2.write('0')
    L7.configure(text = 'empty')
    P7.configure(text = int(0))
    Dialog.Dialog(root, title = 'done', bitmap = 'info',
                  text = '商品を回収しました',
                  strings = ['OK'], default = 0)
    w3.destroy()
def d8():
    f1 = open('item8.dat', 'w')
    f2 = open('item8pr.dat', 'w')
    f1.write('empty')
    f2.write('0')
    L8.configure(text = 'empty')
    P8.configure(text = int(0))
    Dialog.Dialog(root, title = 'done', bitmap = 'info',
                  text = '商品を回収しました',
                  strings = ['OK'], default = 0)
    w3.destroy()
def d9():
    f1 = open('item9.dat', 'w')
    f2 = open('item9pr.dat', 'w')
    f1.write('empty')
    f2.write('0')
    L9.configure(text = 'empty')
    P9.configure(text = int(0))
    Dialog.Dialog(root, title = 'done', bitmap = 'info',
                  text = '商品を回収しました',
                  strings = ['OK'], default = 0)
    w3.destroy()
def d10():
    f1 = open('item10.dat', 'w')
    f2 = open('item10pr.dat', 'w')
    f1.write('empty')
    f2.write('0')
    L10.configure(text = 'empty')
    P10.configure(text = int(0))
    Dialog.Dialog(root, title = 'done', bitmap = 'info',
                  text = '商品を回収しました',
                  strings = ['OK'], default = 0)
    w3.destroy()
def tt():
    global w3
    w3 = Toplevel()
    f1 = Frame(w3)
    f2 = Frame(w3)
    Button(f1, text = 'item1', command = d1).pack()
    Button(f1, text = 'item2', command = d2).pack()
    Button(f1, text = 'item3', command = d3).pack()
    Button(f1, text = 'item4', command = d4).pack()
    Button(f1, text = 'item5', command = d5).pack()
    Button(f1, text = 'item6', command = d6).pack()
    Button(f1, text = 'item7', command = d7).pack()
    Button(f1, text = 'item8', command = d8).pack()
    Button(f1, text = 'item9', command = d9).pack()
    Button(f1, text = 'item10', command = d10).pack()
    f1.pack(side = LEFT)
    f2.pack(side = RIGHT)
def dopw():
    f = open('pw.dat', 'w')
    f.write(cpw.get())
    f.close()
    w3.destroy()
def doid():
    f = open('owner.dat', 'w')
    f.write(cid.get())
    f.close()
    w3.destroy()
def changepw():
    global w3
    w3 = Toplevel()
    Label(w3, text = 'PWを入力').pack()
    Entry(w3, textvariable = cpw).pack()
    Button(w3, text = '変更する', command = dopw).pack()
def changeid():
    global w3
    w3 = Toplevel()
    Label(w3, text = 'IDを入力').pack()
    Entry(w3, textvariable = cid).pack()
    Button(w3, text = '変更する', command = doid).pack()
def menu():
    global w2
    w2 = Toplevel()
    Label(w2, text = '管理者メニュー').pack()
    Button(w2, text = '管理者を変更する', command = changeid).pack()
    Button(w2, text = 'PWを変更する', command = changepw).pack()
    Button(w2, text = '出品する', command = price).pack()
    Button(w2, text = '商品を回収する', command = tt).pack()
    Button(w2, text = '値段を変更する', command = cp).pack()
    Button(w2, text = '終了', command = w2.destroy).pack()
def security():
    if st1.get() and st2.get():
        fo1 = open('owner.dat', 'r')
        for i in fo1:
            de = key.decrypt(i)
            strip = de.rstrip()
        fo2 = open('pw.dat', 'r')
        for ii in fo2:
            ii == ii
            de2 = key.encrypt(ii)
            strip2 = de.rstrip()
        if st1.get() == strip and st2.get() == strip2:
            menu()
            st2.set('')
            w1.destroy()
        else:
            Message(w1, text = '管理者名又はパスワードが違います').pack()
    else:
        Message(w1, text = 'ログイン情報を正しく入力してください').pack()
def register():
    if st1.get() and st2.get():
        ids = len(st1.get())
        if 8 >= ids:
            pri = 8-ids
            text = ' '*pri
        pws = len(st2.get())
        if 8 >= pws:
            prp = 8 - pws
            text2 = ' '*prp
        elif 16 >= pws and pws >= 9:
            prp = 16-pws
            text2 = ' '*prp
        key1 = key.encrypt(st1.get() + text)
        key2 = key.encrypt(st2.get() + text2)
        fo1 = open('owner.dat', 'w')
        fo1.write(key1)
        fo2 = open('pw.dat', 'w')
        fo2.write(key2)
        menu()
        st1.set('')
        st2.set('')
        w1.destroy()
    else:
        Message(w1, text = '管理者情報を正しく入力してください').pack()
def owner():
    global w1
    w1 = Toplevel()
    if not os.path.isfile("owner.dat") and not os.path.isfile("pw.dat"):
        Label(w1, text = '管理者登録').pack()
        Label(w1, text = 'Owner:').pack()
        Entry(w1, textvariable = st1).pack()
        Label(w1, text = 'Password(16以内):').pack()
        Entry(w1, textvariable = st2, show='*').pack()
        Button(w1, text = '登録', command = register).pack()
    else:
        Label(w1, text = 'Owner:').pack()
        Entry(w1, textvariable = st1).pack()
        Label(w1, text = 'Password:').pack()
        Entry(w1, textvariable = st2, show='*').pack()
        Button(w1, text = 'ログイン', command = security).pack()
        
f1 = Frame(root)
i_d = PhotoImage(file = 'tradebox.gif', width = 100, height = 80)
I1 = Label(f1, image = i_d)
I1.pack()
L1 = Label(f1, text = a2)
L1.pack()
P1 = Label(f1, text = k2, bg = 'white')
P1.pack()
I2 = Label(f1, image = i_d)
I2.pack()
L2 = Label(f1, text = b2)
L2.pack()
P2 = Label(f1, text = l2, bg = 'white')
P2.pack()
I3 = Label(f1, image = i_d)
I3.pack()
L3 = Label(f1, text = c2)
L3.pack()
P3 = Label(f1, text = m2, bg = 'white')
P3.pack()
I4 = Label(f1, image = i_d)
I4.pack()
L4 = Label(f1, text = dd2)
L4.pack()
P4 = Label(f1, text = n2, bg = 'white')
P4.pack()
I5 = Label(f1, image = i_d)
I5.pack()
L5 = Label(f1, text = e2)
L5.pack()
P5 = Label(f1, text = o2, bg = 'white')
P5.pack()
f2 = Frame(root)
i_d2 = PhotoImage(file = 'tradebox.gif', width = 100, height = 80)
I6 = Label(f2, image = i_d2)
I6.pack()
L6 = Label(f2, text = F2)
L6.pack()
P6 = Label(f2, text = p2, bg = 'white')
P6.pack()
I7 = Label(f2, image = i_d2)
I7.pack()
L7 = Label(f2, text = g2)
L7.pack()
P7 = Label(f2, text = q2, bg = 'white')
P7.pack()
I8 = Label(f2, image = i_d2)
I8.pack()
L8 = Label(f2, text = h2)
L8.pack()
P8 = Label(f2, text = r2, bg = 'white')
P8.pack()
I9 = Label(f2, image = i_d2)
I9.pack()
L9 = Label(f2, text = ii2)
L9.pack()
P9 = Label(f2, text = s2, bg = 'white')
P9.pack()
I10 = Label(f2, image = i_d2)
I10.pack()
L10 = Label(f2, text = j2)
L10.pack()
P10 = Label(f2, text = t2, bg = 'white')
P10.pack()

def B1():
    f = open('item1pr.dat', 'r')
    fr = open('item1.dat', 'r')
    for item in fr:
        item == item
    if item == 'empty':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                  text = '商品が入っていません',
                  strings = ['OK'], default = 0)
    else:
        if chec.get():
            ff = open('wallet.dat', 'r')
            for i in ff:
                i == i
            for p1 in f:
                p1==p1
            if int(i)<int(p1):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                x = int(i)-int(p1)
                moneyval.set(str(x))
                wallet.append(x)
                chargem.append(x)
                open('item1.dat', 'w').write('empty')
                open('item1pr.dat', 'w').write('0')
                open('wallet.dat', 'w').write(str(x))
                L1.configure(text = 'empty')
                P1.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
        else:
            for p1 in f:
                p1==p1
            for ii in pri:
                ii==ii
            if ii<int(p1):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                ii-=int(p1)
                to1.configure(text = int(ii))
                pri.append(ii)
                open('item1.dat', 'w').write('empty')
                open('item1pr.dat', 'w').write('0')
                L1.configure(text = 'empty')
                P1.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
def B2():
    f = open('item2pr.dat', 'r')
    fr = open('item2.dat', 'r')
    for item in fr:
        item == item
    if item == 'empty':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                  text = '商品が入っていません',
                  strings = ['OK'], default = 0)
    else:
        if chec.get():
            ff = open('wallet.dat', 'r')
            for i in ff:
                i == i
            for p1 in f:
                p1==p1
            if int(i)<int(p1):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                x = int(i)-int(p1)
                moneyval.set(str(x))
                wallet.append(x)
                chargem.append(x)
                open('item2.dat', 'w').write('empty')
                open('item2pr.dat', 'w').write('0')
                open('wallet.dat', 'w').write(str(x))
                L1.configure(text = 'empty')
                P1.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
        else:
            for p2 in f:
                p2==p2
            for ii in pri:
                ii == ii
            if ii<int(p2):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                ii-=int(p2)
                to1.configure(text = int(ii))
                pri.append(ii)
                open('item2.dat', 'w').write('empty')
                open('item2pr.dat', 'w').write('0')
                L2.configure(text = 'empty')
                P2.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
def B3():
    f = open('item3pr.dat', 'r')
    fr = open('item3.dat', 'r')
    for item in fr:
        item == item
    if item == 'empty':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                  text = '商品が入っていません',
                  strings = ['OK'], default = 0)
    else:
        if chec.get():
            ff = open('wallet.dat', 'r')
            for i in ff:
                i == i
            for p1 in f:
                p1==p1
            if int(i)<int(p1):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                x = int(i)-int(p1)
                moneyval.set(str(x))
                wallet.append(x)
                chargem.append(x)
                open('item3.dat', 'w').write('empty')
                open('item3pr.dat', 'w').write('0')
                open('wallet.dat', 'w').write(str(x))
                L1.configure(text = 'empty')
                P1.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
        else:
            for p2 in f:
                p2==p2
            for ii in pri:
                ii == ii
            if ii<int(p2):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                ii-=int(p2)
                to1.configure(text = int(ii))
                pri.append(ii)
                open('item3.dat', 'w').write('empty')
                open('item3pr.dat', 'w').write('0')
                L3.configure(text = 'empty')
                P3.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
def B4():
    f = open('item4pr.dat', 'r')
    fr = open('item4.dat', 'r')
    for item in fr:
        item == item
    if item == 'empty':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                  text = '商品が入っていません',
                  strings = ['OK'], default = 0)
    else:
        if chec.get():
            ff = open('wallet.dat', 'r')
            for i in ff:
                i == i
            for p1 in f:
                p1==p1
            if int(i)<int(p1):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                x = int(i)-int(p1)
                moneyval.set(str(x))
                wallet.append(x)
                chargem.append(x)
                open('item4.dat', 'w').write('empty')
                open('item4pr.dat', 'w').write('0')
                open('wallet.dat', 'w').write(str(x))
                L1.configure(text = 'empty')
                P1.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
        else:
            for p2 in f:
                p2==p2
            for ii in pri:
                ii == ii
            if ii<int(p2):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                ii-=int(p2)
                to1.configure(text = int(ii))
                pri.append(ii)
                open('item4.dat', 'w').write('empty')
                open('item4pr.dat', 'w').write('0')
                L4.configure(text = 'empty')
                P4.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
def B5():
    f = open('item5pr.dat', 'r')
    fr = open('item5.dat', 'r')
    for item in fr:
        item == item
    if item == 'empty':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                  text = '商品が入っていません',
                  strings = ['OK'], default = 0)
    else:
        if chec.get():
            ff = open('wallet.dat', 'r')
            for i in ff:
                i == i
            for p1 in f:
                p1==p1
            if int(i)<int(p1):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                x = int(i)-int(p1)
                moneyval.set(str(x))
                wallet.append(x)
                chargem.append(x)
                open('item5.dat', 'w').write('empty')
                open('item5pr.dat', 'w').write('0')
                open('wallet.dat', 'w').write(str(x))
                L1.configure(text = 'empty')
                P1.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
        else:
            for p2 in f:
                p2==p2
            for ii in pri:
                ii == ii
            if ii<int(p2):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                ii-=int(p2)
                to1.configure(text = int(ii))
                pri.append(ii)
                open('item5.dat', 'w').write('empty')
                open('item5pr.dat', 'w').write('0')
                L5.configure(text = 'empty')
                P5.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = 'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
def B6():
    f = open('item6pr.dat', 'r')
    fr = open('item6.dat', 'r')
    for item in fr:
        item == item
    if item == 'empty':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                  text = u'商品が入っていません',
                  strings = ['OK'], default = 0)
    else:
        if chec.get():
            ff = open('wallet.dat', 'r')
            for i in ff:
                i == i
            for p1 in f:
                p1==p1
            if int(i)<int(p1):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                x = int(i)-int(p1)
                moneyval.set(str(x))
                wallet.append(x)
                chargem.append(x)
                open('item6.dat', 'w').write('empty')
                open('item6pr.dat', 'w').write('0')
                open('wallet.dat', 'w').write(str(x))
                L1.configure(text = 'empty')
                P1.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
        else:
            for p2 in f:
                p2==p2
            for ii in pri:
                ii == ii
            if ii<int(p2):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                ii-=int(p2)
                to1.configure(text = int(ii))
                pri.append(ii)
                open('item6.dat', 'w').write('empty')
                open('item6pr.dat', 'w').write('0')
                L6.configure(text = 'empty')
                P6.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
def B7():
    f = open('item7pr.dat', 'r')
    fr = open('item7.dat', 'r')
    for item in fr:
        item == item
    if item == 'empty':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                  text = u'商品が入っていません',
                  strings = ['OK'], default = 0)
    else:
        if chec.get():
            ff = open('wallet.dat', 'r')
            for i in ff:
                i == i
            for p1 in f:
                p1==p1
            if int(i)<int(p1):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                x = int(i)-int(p1)
                moneyval.set(str(x))
                wallet.append(x)
                chargem.append(x)
                open('item7.dat', 'w').write('empty')
                open('item7pr.dat', 'w').write('0')
                open('wallet.dat', 'w').write(str(x))
                L1.configure(text = 'empty')
                P1.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
        else:
            for p2 in f:
                p2==p2
            for ii in pri:
                ii == ii
            if ii<int(p2):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                ii-=int(p2)
                to1.configure(text = int(ii))
                pri.append(ii)
                open('item7.dat', 'w').write('empty')
                open('item7pr.dat', 'w').write('0')
                L7.configure(text = 'empty')
                P7.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
def B8():
    f = open('item8pr.dat', 'r')
    fr = open('item8.dat', 'r')
    for item in fr:
        item == item
    if item == 'empty':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                  text = u'商品が入っていません',
                  strings = ['OK'], default = 0)
    else:
        if chec.get():
            ff = open('wallet.dat', 'r')
            for i in ff:
                i == i
            for p1 in f:
                p1==p1
            if int(i)<int(p1):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                x = int(i)-int(p1)
                moneyval.set(str(x))
                wallet.append(x)
                chargem.append(x)
                open('item8.dat', 'w').write('empty')
                open('item8pr.dat', 'w').write('0')
                open('wallet.dat', 'w').write(str(x))
                L1.configure(text = 'empty')
                P1.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
        else:
            for p2 in f:
                p2==p2
            for ii in pri:
                ii == ii
            if ii<int(p2):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                ii-=int(p2)
                to1.configure(text = int(ii))
                pri.append(ii)
                open('item8.dat', 'w').write('empty')
                open('item8pr.dat', 'w').write('0')
                L8.configure(text = 'empty')
                P8.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
def B9():
    f = open('item9pr.dat', 'r')
    fr = open('item9.dat', 'r')
    for item in fr:
        item == item
    if item == 'empty':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                  text = u'商品が入っていません',
                  strings = ['OK'], default = 0)
    else:
        if chec.get():
            ff = open('wallet.dat', 'r')
            for i in ff:
                i == i
            for p1 in f:
                p1==p1
            if int(i)<int(p1):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                x = int(i)-int(p1)
                moneyval.set(str(x))
                wallet.append(x)
                chargem.append(x)
                open('item9.dat', 'w').write('empty')
                open('item9pr.dat', 'w').write('0')
                open('wallet.dat', 'w').write(str(x))
                L1.configure(text = 'empty')
                P1.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
        else:
            for p2 in f:
                p2==p2
            for ii in pri:
                ii == ii
            if ii<int(p2):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                ii-=int(p2)
                to1.configure(text = int(ii))
                pri.append(ii)
                open('item9.dat', 'w').write('empty')
                open('item9pr.dat', 'w').write('0')
                L9.configure(text = 'empty')
                P9.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
def B10():
    f = open('item10pr.dat', 'r')
    fr = open('item10.dat', 'r')
    for item in fr:
        item == item
    if item == 'empty':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                  text = u'商品が入っていません',
                  strings = ['OK'], default = 0)
    else:
        if chec.get():
            ff = open('wallet.dat', 'r')
            for i in ff:
                i == i
            for p1 in f:
                p1==p1
            if int(i)<int(p1):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                x = int(i)-int(p1)
                moneyval.set(str(x))
                wallet.append(x)
                chargem.append(x)
                open('item10.dat', 'w').write('empty')
                open('item10pr.dat', 'w').write('0')
                open('wallet.dat', 'w').write(str(x))
                L1.configure(text = 'empty')
                P1.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
        else:
            for p2 in f:
                p2==p2
            for ii in pri:
                ii == ii
            if ii<int(p2):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お金が不足しています',
                              strings = ['OK'], default = 0)
            else:
                ii-=int(p2)
                to1.configure(text = int(ii))
                pri.append(ii)
                open('item10.dat', 'w').write('empty')
                open('item10pr.dat', 'w').write('0')
                L10.configure(text = 'empty')
                P10.configure(text = int(0))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
def manyen2():
    price = 10000
    for countm in chargem:
        countm+=price
    kane.set(countm)
    chargem.append(countm)
def manyen():
    price = 10000
    for ii in pri:
        ii+=price
    pri.append(ii)
    to1.configure(text = ii)
def gosenyen():
    price = 5000
    for ii in pri:
        ii+=price
    pri.append(ii)
    to1.configure(text = ii)
def gosenyen2():
    price = 5000
    for countm in chargem:
        countm+=price
    kane.set(countm)
    chargem.append(countm)
def senyen2():
    price = 1000
    for countm in chargem:
        countm+=price
    kane.set(countm)
    chargem.append(countm)
def senyen():
    price = 1000
    for ii in pri:
        ii+=price
    pri.append(ii)
    to1.configure(text = ii)
def gohyaku():
    price = 500
    for countm in chargem:
        countm+=price
    kane.set(countm)
    chargem.append(countm)
def gohyakuyen():
    price = 500
    for ii in pri:
        ii+=price
    pri.append(ii)
    to1.configure(text = ii)
def hyaku2():
    price = 100
    for countm in chargem:
        countm+=price
    kane.set(countm)
    chargem.append(countm)
def hyakuyen():
    price = 100
    for ii in pri:
        ii+=price
    pri.append(ii)
    to1.configure(text = ii)
def gojyu2():
    price = 50
    for countm in chargem:
        countm+=price
    kane.set(countm)
    chargem.append(countm)
def gojyuuyen():
    price = 50
    for ii in pri:
        ii+=price
    pri.append(ii)
    to1.configure(text = ii)
def jyuu2():
    price = 10
    for countm in chargem:
        countm+=price
    kane.set(countm)
    chargem.append(countm)
def jyuuyen():
    price = 10
    for ii in pri:
        ii+=price
    pri.append(ii)
    to1.configure(text = ii)
def reset():
    kane.set(0)
    chargem.append(0)
def cdone():
    w2.destroy()
    w3.destroy()
    wuf = open('wallet.dat', 'r')
    for wufi in wuf:
        wufi = int(wufi)
    wuf.close()
    calcu.append(wufi)
    for calcula in calcu:
        calcula == calcula
    for countm in chargem:
        countm == countm
    calcula+=countm
    wallet.append(calcula)
    moneyval.set(calcula)
    countm = 0
    chargem.append(countm)
    kane.set(0)
    f = open('wallet.dat', 'w')
    f.write(str(calcula))
    f.close()
def charge():
    global w3
    w3 = Toplevel()
    for countm in chargem:
        countm == countm
    Label(w3, text = u'確認').pack()
    Label(w3, text = countm).pack()
    if val.get() == 1:
        Label(w3, text = u'クレジットカード').pack()
    elif val.get() == 2:
        Label(w3, text = u'コンビニ支払い').pack()
    elif val.get() == 3:
        Label(w3, text = u'Webmoney').pack()
    Button(w3, text = u'チャージ', command = cdone).pack()
    Button(w3, text = u'戻る', command = w3.destroy).pack()
def walletmenu():
    global w2
    w2 = Toplevel()
    wuf = open('wallet.dat', 'r')
    for wufi in wuf:
        wufi = int(wufi)
        xyz.append(wufi)
    if wufi != '0' or '':
        wallet.append(wufi)
    if wufi != '0':
        for i in xyz:
            moneyval.set(i)
    Label(w2, text = u'チャージする金額と支払い方法を選択').pack()
    kin = Label(w2, textvariable = kane)
    kin.pack()
    Button(w2, text = u'1万円', command = manyen2).pack(side = LEFT)
    Button(w2, text = u'5千円', command = gosenyen2).pack(side = LEFT)
    Button(w2, text = u'千円', command = senyen2).pack(side = LEFT)
    Button(w2, text = u'500円', command = gohyaku).pack(side = LEFT)
    Button(w2, text = u'100円', command = hyaku2).pack(side = LEFT)
    Button(w2, text = u'50円', command = gojyu2).pack(side = LEFT)
    Button(w2, text = u'10円', command = jyuu2).pack(side = LEFT)
    Button(w2, text = u'訂正', command = reset).pack()
    Radiobutton(w2, text = u'クレジットカード', variable = val, value = 1).pack()
    Radiobutton(w2, text = u'コンビニ支払い', variable = val, value = 2).pack()
    Radiobutton(w2, text = u'Webmoney', variable = val, value = 3).pack()
    Button(w2, text = u'確認する', command = charge).pack()
    Button(w2, text = u'チャージを行わないで終了', command = w2.destroy).pack()
def wlogin():
    a = open('userwallet.dat', 'r')
    b = open('walletpw.dat', 'r')
    for i in a:
        de = key.decrypt(i)
        strip = de.rstrip()
    for ii in b:
        de2 = key.decrypt(ii)
        strip2 = de2.rstrip()
    if st3.get()==strip and st4.get()==strip2:
        walletmenu()
        w1.destroy()
        st4.set('')
    else:
        Message(w1, text = u'ID又はパスワードが違います').pack()
def regist():
    if st3.get() and st4.get():
        ids = len(st3.get())
        if 8 >= ids:
            pri = 8-ids
            text = ' '*pri
        pws = len(st4.get())
        if 8 >= pws:
            prp = 8-pws
            text2 = ' '*prp
        elif 16 >= pws and pws >= 9:
            prp = 16-pws
            text2 = ' '*prp
        key1 = key.encrypt(st3.get() + text)
        key2 = key.encrypt(st4.get() + text2)
        f1 = open('userwallet.dat', 'w')
        f1.write(key1)
        f2 = open('walletpw.dat', 'w')
        f2.write(key2)
        f = open('wallet.dat', 'w')
        f.write('0')
        f.close()
        f1.close()
        f2.close()
        walletmenu()
        w1.destroy()
        st3.set('')
        st4.set('')
    else:
        Message(w1, text = u'アカウント情報を正しく入力してください').pack()
def wallets():
    global w1
    w1 = Toplevel()
    if not os.path.isfile("userwallet.dat") and not os.path.isfile("walletpw.dat"):
        Label(w1, text = u'ウォレット登録').pack()
        Label(w1, text = u'ID:').pack()
        Entry(w1, textvariable = st3).pack()
        Label(w1, text = u'パスワード').pack()
        Entry(w1, textvariable = st4, show = '*').pack()
        Button(w1, text = u'登録', command = regist).pack()
    else:
        Label(w1, text = u'ログイン').pack()
        Label(w1, text = u'ID:').pack()
        Entry(w1, textvariable = st3).pack()
        Label(w1, text = u'パスワード').pack()
        Entry(w1, textvariable = st4, show = '*').pack()
        Button(w1, text = u'ログイン', command = wlogin).pack()
        
        
f4 = Frame(root)
Button(f4, text = '1', width = 7, height = 7, command = B1).pack()
Button(f4, text = '2', width = 7, height = 7, command = B2).pack()
Button(f4, text = '3', width = 7, height = 7, command = B3).pack()
Button(f4, text = '4', width = 7, height = 7, command = B4).pack()
Button(f4, text = '5', width = 7, height = 7, command = B5).pack()
f5 = Frame(root)
Button(f5, text = '6', width = 7, height = 7, command = B6).pack()
Button(f5, text = '7', width = 7, height = 7, command = B7).pack()
Button(f5, text = '8', width = 7, height = 7, command = B8).pack()
Button(f5, text = '9', width = 7, height = 7, command = B9).pack()
Button(f5, text = '10', width = 7, height = 7, command = B10).pack()
f3 = Frame(root)
Label(f3, text = u'TradeBox 2', font = ('New Times Roman', 24)).pack()
Label(f3, text = u'利用方法:').pack()
Label(f3, text = u'1.購入する商品の値段分のお金を投入').pack()
Label(f3, text = u'2.商品のボタンを押す').pack()
Label(f3, text = u'3.ロッカーが開くので商品を取り出す').pack()
f6 = Frame(root)
Label(f6, text = u'合計金額:').pack(side = LEFT)
to1 = Label(f6, text = ii, font = ('New Times Roman', 18), bg = 'white')
to1.pack(side = RIGHT)
f8 = Frame(root)
i_d3 = PhotoImage(file = 'coinbillpic.gif')
i_d4 = PhotoImage(file = 'suica.gif')
Label(f8, image = i_d4).pack(side = LEFT)
Label(f8, image = i_d3).pack(side = RIGHT)
f9 = Frame(root)
Label(f9, text = u'所持額:').pack(side = LEFT)
Mon = Label(f9, textvariable = moneyval).pack(side = RIGHT)
f10 = Frame(root)
i_d5 = PhotoImage(file = '10000yen.gif')
i_d6 = PhotoImage(file = '5000yen.gif')
i_d7 = PhotoImage(file = '1000yen.gif')
i_d8 = PhotoImage(file = '500yen.gif')
i_d9 = PhotoImage(file = '100yen.gif')
i_d10 = PhotoImage(file = '50yen.gif')
i_d11 = PhotoImage(file = '10yen.gif')
Label(f10, text = u'＊ボタンを押してお金を投入してください', font = ('New Times Roman', 18), bg = 'red').pack()
Checkbutton(f10, text = u'ウォレットで支払う', variable = chec).pack()
Button(f10, image = i_d5, command = manyen).pack(side = LEFT)
Button(f10, image = i_d6, command = gosenyen).pack(side = LEFT)
Button(f10, image = i_d7, command = senyen).pack(side = LEFT)
Button(f10, image = i_d8, command = gohyakuyen).pack(side = LEFT)
Button(f10, image = i_d9, command = hyakuyen).pack(side = LEFT)
Button(f10, image = i_d10, command = gojyuuyen).pack(side = LEFT)
Button(f10, image = i_d11, command = jyuuyen).pack(side = LEFT)
f11 = Frame(root)
Button(f11, text = u'取引終了', command = sys.exit).pack()
Button(f11, text = u'管理(管理者のみ)', command = owner).pack()
Button(f11, text = u'ウォレット：チャージ/ログインして利用する', command = wallets).pack()

f4.pack(side = LEFT)
f1.pack(side = LEFT)
f5.pack(side = RIGHT)
f2.pack(side = RIGHT)
f3.pack(fill = BOTH)
f6.pack()
f8.pack()
f9.pack()
f10.pack()
f11.pack()
root.mainloop()