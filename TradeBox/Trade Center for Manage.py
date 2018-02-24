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
st1 = StringVar()
st2 = StringVar()
st3 = StringVar()
st4 = StringVar()
st5 = StringVar()
st6 = StringVar()
st7 = StringVar()
st8 = StringVar()
regcon = StringVar()
tota = StringVar()
moneyval = StringVar()
val = IntVar()
chec = BooleanVar()
NS1 = IntVar()
loginw = StringVar()
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
selecti = IntVar()
registi = IntVar()
geti = IntVar()
chp = IntVar()
ii = 0
pri = []
pri.append(ii)
wallet = []
chargem = []
skeyobj = []
bb = 0
countm = 0
chargem.append(countm)
wallet.append(bb)
kina = []
calcu = []
calcula = 0
calcu.append(calcula)
curd = os.getcwd()
a = codecs.open('item1.dat', 'r', 'shift-jis')
b = codecs.open('item2.dat', 'r', 'shift-jis')
c = codecs.open('item3.dat', 'r', 'shift-jis')
d = codecs.open('item4.dat', 'r', 'shift-jis')
e = codecs.open('item5.dat', 'r', 'shift-jis')
f = codecs.open('item6.dat', 'r', 'shift-jis')
g = codecs.open('item7.dat', 'r', 'shift-jis')
h = codecs.open('item8.dat', 'r', 'shift-jis')
i = codecs.open('item9.dat', 'r', 'shift-jis')
j = codecs.open('item10.dat', 'r', 'shift-jis')
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

def itemr():
    if registi.get() == 1:
        n=1
        L1.configure(text = item1st.get())
        P1.configure(text = item1pr.get())
        R1.configure(state = 'normal')
        registi.set('0')
    if registi.get() == 2:
        n=2
        L2.configure(text = item2st.get())
        P2.configure(text = item2pr.get())
        R2.configure(state = 'normal')
        registi.set('0')
    if registi.get() == 3:
        n=3
        L3.configure(text = item3st.get())
        P3.configure(text = item3pr.get())
        R3.configure(state = 'normal')
        registi.set('0')
    if registi.get() == 4:
        n=4
        L4.configure(text = item4st.get())
        P4.configure(text = item4pr.get())
        R4.configure(state = 'normal')
        registi.set('0')
    if registi.get() == 5:
        n=5
        L5.configure(text = item5st.get())
        P5.configure(text = item5pr.get())
        R5.configure(state = 'normal')
        registi.set('0')
    if registi.get() == 6:
        n=6
        L6.configure(text = item6st.get())
        P6.configure(text = item6pr.get())
        R6.configure(state = 'normal')
        registi.set('0')
    if registi.get() == 7:
        n=7
        L7.configure(text = item7st.get())
        P7.configure(text = item7pr.get())
        R7.configure(state = 'normal')
        registi.set('0')
    if registi.get() == 8:
        n=8
        L8.configure(text = item8st.get())
        P8.configure(text = item8pr.get())
        R8.configure(state = 'normal')
        registi.set('0')
    if registi.get() == 9:
        n=9
        L9.configure(text = item9st.get())
        P9.configure(text = item9pr.get())
        R9.configure(state = 'normal')
        registi.set('0')
    if registi.get() == 10:
        n=10
        L10.configure(text = item10st.get())
        P10.configure(text = item10pr.get())
        R10.configure(state = 'normal')
        registi.set('0')
    if NS1.get() == 1:
        ns = 'and'
    elif NS1.get() == 2:
        ns = 'not'
    elif NS1.get() == 0:
        ns = 'disable'
    f1 = codecs.open('item%d.dat' % n, 'w', 'shift-jis')
    f2 = open('item%dpr.dat' % n, 'w')
    f1.write(item1st.get())
    f2.write(item1pr.get())
    f1.close()
    f2.close()
    w3.destroy()
    w4.destroy()
def item():
    global w4
    if w4 is None or not w4.winfo_exists():
        w4 = Toplevel()
        Label(w4, text = u'商品名').pack()
        Entry(w4, text = item1st).pack()
        Label(w4, text = u'値段').pack()
        Entry(w4, text = item1pr).pack()
        Radiobutton(w4, text = u'通信販売も行う', variable = NS1, value = 1).pack()
        Radiobutton(w4, text = u'通信販売のみ', variable = NS1, value = 2).pack()
        Radiobutton(w4, text = u'通信販売は行わない', variable = NS1, value = 0).pack()
        Button(w4, text = u'出品', command = itemr).pack()
    else:
        w4.deiconify()
def price():
    global w3
    if w3 is None or not w3.winfo_exists():
        w3 = Toplevel()
        f1 = Frame(w3)
        f2 = Frame(w3)
        r1 = Radiobutton(f1, text = 'item1', variable = registi, value = 1, command = item)
        r1.pack()
        r2 = Radiobutton(f1, text = 'item2', variable = registi, value = 2, command = item)
        r2.pack()
        r3 = Radiobutton(f1, text = 'item3', variable = registi, value = 3, command = item)
        r3.pack()
        r4 = Radiobutton(f1, text = 'item4', variable = registi, value = 4, command = item)
        r4.pack()
        r5 = Radiobutton(f1, text = 'item5', variable = registi, value = 5, command = item)
        r5.pack()
        r6 = Radiobutton(f1, text = 'item6', variable = registi, value = 6, command = item)
        r6.pack()
        r7 = Radiobutton(f1, text = 'item7', variable = registi, value = 7, command = item)
        r7.pack()
        r8 = Radiobutton(f1, text = 'item8', variable = registi, value = 8, command = item)
        r8.pack()
        r9 = Radiobutton(f1, text = 'item9', variable = registi, value = 9, command = item)
        r9.pack()
        r10 = Radiobutton(f1, text = 'item10', variable = registi, value = 10, command = item)
        r10.pack()
        F1 = codecs.open("item1.dat", 'r', 'shift-jis')
        F2 = codecs.open("item2.dat", 'r', 'shift-jis')
        F3 = codecs.open("item3.dat", 'r', 'shift-jis')
        F4 = codecs.open("item4.dat", 'r', 'shift-jis')
        F5 = codecs.open("item5.dat", 'r', 'shift-jis')
        F6 = codecs.open("item6.dat", 'r', 'shift-jis')
        F7 = codecs.open("item7.dat", 'r', 'shift-jis')
        F8 = codecs.open("item8.dat", 'r', 'shift-jis')
        F9 = codecs.open("item9.dat", 'r', 'shift-jis')
        F10 = codecs.open("item10.dat", 'r', 'shift-jis')
        for i1 in F1:
            if i1 != 'empty':
                r1.configure(state = 'disabled')
        for i2 in F2:
            if i2 != 'empty':
                r2.configure(state = 'disabled')
        for i3 in F3:
            if i3 != 'empty':
                r3.configure(state = 'disabled')
        for i4 in F4:
            if i4 != 'empty':
                r4.configure(state = 'disabled')
        for i5 in F5:
            if i5 != 'empty':
                r5.configure(state = 'disabled')
        for i6 in F6:
            if i6 != 'empty':
                r6.configure(state = 'disabled')
        for i7 in F7:
            if i7 != 'empty':
                r7.configure(state = 'disabled')
        for i8 in F8:
            if i8 != 'empty':
                r8.configure(state = 'disabled')
        for i9 in F9:
            if i9 != 'empty':
                r9.configure(state = 'disabled')
        for i10 in F10:
            if i10 != 'empty':
                r10.configure(state = 'disabled')
        f1.pack(side = LEFT)
        f2.pack(side = RIGHT)
    else:
        w3.deiconify()
def i1r():
    if chp.get() == 1:
        n=1
        Pco = P1.configure(text = item1pr.get())
    if chp.get() == 2:
        n=2
        Pco = P2.configure(text = item2pr.get())
    if chp.get() == 3:
        n=3
        Pco = P3.configure(text = item3pr.get())
    if chp.get() == 4:
        n=4
        Pco = P4.configure(text = item4pr.get())
    if chp.get() == 5:
        n=5
        Pco = P5.configure(text = item5pr.get())
    if chp.get() == 6:
        n=6
        Pco = P6.configure(text = item6pr.get())
    if chp.get() == 7:
        n=7
        Pco = P7.configure(text = item7pr.get())
    if chp.get() == 8:
        n=8
        Pco = P8.configure(text = item8pr.get())
    if chp.get() == 9:
        n=9
        Pco = P9.configure(text = item9pr.get())
    if chp.get() == 10:
        n=10
        Pco = P10.configure(text = item10pr.get())
    f2 = open('item%dpr.dat' % n, 'w')
    f2.write(item1pr.get())
    f2.close()
    w6.destroy()
    w7.destroy()
    chp.set('0')
def cpn():
    global w6
    if w6 is None or not w6.winfo_exists():
        w6 = Toplevel()
        Label(w6, text = u'値段').pack()
        Entry(w6, text = item1pr).pack()
        Button(w6, text = u'出品', command = i1r).pack()
    else:
        w6.deiconify()
def cp():
    global w7
    if w7 is None or not w7.winfo_exists():
        w7 = Toplevel()
        f1 = Frame(w7)
        r1 = Radiobutton(f1, text = 'item1', variable = chp, value = 1, command = cpn)
        r1.pack()
        r2 = Radiobutton(f1, text = 'item2', variable = chp, value = 2, command = cpn)
        r2.pack()
        r3 = Radiobutton(f1, text = 'item3', variable = chp, value = 3, command = cpn)
        r3.pack()
        r4 = Radiobutton(f1, text = 'item4', variable = chp, value = 4, command = cpn)
        r4.pack()
        r5 = Radiobutton(f1, text = 'item5', variable = chp, value = 5, command = cpn)
        r5.pack()
        r6 = Radiobutton(f1, text = 'item6', variable = chp, value = 6, command = cpn)
        r6.pack()
        r7 = Radiobutton(f1, text = 'item7', variable = chp, value = 7, command = cpn)
        r7.pack()
        r8 = Radiobutton(f1, text = 'item8', variable = chp, value = 8, command = cpn)
        r8.pack()
        r9 = Radiobutton(f1, text = 'item9', variable = chp, value = 9, command = cpn)
        r9.pack()
        r10 = Radiobutton(f1, text = 'item10', variable = chp, value = 10, command = cpn)
        r10.pack()
        f1.pack()
        F1 = codecs.open("item1.dat", 'r', 'shift-jis')
        F2 = codecs.open("item2.dat", 'r', 'shift-jis')
        F3 = codecs.open("item3.dat", 'r', 'shift-jis')
        F4 = codecs.open("item4.dat", 'r', 'shift-jis')
        F5 = codecs.open("item5.dat", 'r', 'shift-jis')
        F6 = codecs.open("item6.dat", 'r', 'shift-jis')
        F7 = codecs.open("item7.dat", 'r', 'shift-jis')
        F8 = codecs.open("item8.dat", 'r', 'shift-jis')
        F9 = codecs.open("item9.dat", 'r', 'shift-jis')
        F10 = codecs.open("item10.dat", 'r', 'shift-jis')
        for i1 in F1:
            if i1 != 'empty':
                r1.configure(state = 'normal')
            else:
                r1.configure(state = 'disabled')
        for i2 in F2:
            if i2 != 'empty':
                r2.configure(state = 'normal')
            else:
                r2.configure(state = 'disabled')
        for i3 in F3:
            if i3 != 'empty':
                r3.configure(state = 'normal')
            else:
                r3.configure(state = 'disabled')
        for i4 in F4:
            if i4 != 'empty':
                r4.configure(state = 'normal')
            else:
                r4.configure(state = 'disabled')
        for i5 in F5:
            if i5 != 'empty':
                r5.configure(state = 'normal')
            else:
                r5.configure(state = 'disabled')
        for i6 in F6:
            if i6 != 'empty':
                r6.configure(state = 'normal')
            else:
                r6.configure(state = 'disabled')
        for i7 in F7:
            if i7 != 'empty':
                r7.configure(state = 'normal')
            else:
                r7.configure(state = 'disabled')
        for i8 in F8:
            if i8 != 'empty':
                r8.configure(state = 'normal')
            else:
                r8.configure(state = 'disabled')
        for i9 in F9:
            if i9 != 'empty':
                r9.configure(state = 'normal')
            else:
                r9.configure(state = 'disabled')
        for i10 in F10:
            if i10 != 'empty':
                r10.configure(state = 'normal')
            else:
                r10.configure(state = 'disabled')
    else:
        w7.deiconify()
def gitem():
    if geti.get() == 1:
        n=1
        con1 = L1
        con2 = L1
    if geti.get() == 2:
        n=2
        con1 = L2
        con2 = P2
    if geti.get() == 3:
        n=3
        con1 = L3
        con2 = P3
    if geti.get() == 4:
        n=4
        con1 = L4
        con2 = P4
    if geti.get() == 5:
        n=5
        con1 = L5
        con2 = P5
    if geti.get() == 6:
        n=6
        con1 = L6
        con2 = P6
    if geti.get() == 7:
        n=7
        con1 = L7
        con2 = P7
    if geti.get() == 8:
        n=8
        con1 = L8
        con2 = P8
    if geti.get() == 9:
        n=9
        con1 = L9
        con2 = P9
    if geti.get() == 10:
        n=10
        con1 = L10
        con2 = P10
    f1 = codecs.open('item%d.dat' % n, 'w', 'shift-jis')
    f2 = open('item%dpr.dat' % n, 'w')
    f1.write('empty')
    f2.write('0')
    Dialog.Dialog(root, title = 'done', bitmap = 'info',
                  text = u'商品を回収しました',
                  strings = ['OK'], default = 0)
    w5.destroy()
    geti.set('0')
    con1.configure(text = 'empty')
    con2.configure(text = int(0))
def tt():
    global w5
    if w5 is None or not w5.winfo_exists():
        w5 = Toplevel()
        f1 = Frame(w5)
        r1 = Radiobutton(f1, text = 'item1', variable = geti, value = 1, command = gitem)
        r1.pack()
        r2 = Radiobutton(f1, text = 'item2', variable = geti, value = 2, command = gitem)
        r2.pack()
        r3 = Radiobutton(f1, text = 'item3', variable = geti, value = 3, command = gitem)
        r3.pack()
        r4 = Radiobutton(f1, text = 'item4', variable = geti, value = 4, command = gitem)
        r4.pack()
        r5 = Radiobutton(f1, text = 'item5', variable = geti, value = 5, command = gitem)
        r5.pack()
        r6 = Radiobutton(f1, text = 'item6', variable = geti, value = 6, command = gitem)
        r6.pack()
        r7 = Radiobutton(f1, text = 'item7', variable = geti, value = 7, command = gitem)
        r7.pack()
        r8 = Radiobutton(f1, text = 'item8', variable = geti, value = 8, command = gitem)
        r8.pack()
        r9 = Radiobutton(f1, text = 'item9', variable = geti, value = 9, command = gitem)
        r9.pack()
        r10 = Radiobutton(f1, text = 'item10', variable = geti, value = 10, command = gitem)
        r10.pack()
        f1.pack()
        F1 = codecs.open("item1.dat", 'r', 'shift-jis')
        F2 = codecs.open("item2.dat", 'r', 'shift-jis')
        F3 = codecs.open("item3.dat", 'r', 'shift-jis')
        F4 = codecs.open("item4.dat", 'r', 'shift-jis')
        F5 = codecs.open("item5.dat", 'r', 'shift-jis')
        F6 = codecs.open("item6.dat", 'r', 'shift-jis')
        F7 = codecs.open("item7.dat", 'r', 'shift-jis')
        F8 = codecs.open("item8.dat", 'r', 'shift-jis')
        F9 = codecs.open("item9.dat", 'r', 'shift-jis')
        F10 = codecs.open("item10.dat", 'r', 'shift-jis')
        for i1 in F1:
            if i1 == 'empty':
                r1.configure(state = 'disabled')
        for i2 in F2:
            if i2 == 'empty':
                r2.configure(state = 'disabled')
        for i3 in F3:
            if i3 == 'empty':
                r3.configure(state = 'disabled')
        for i4 in F4:
            if i4 == 'empty':
                r4.configure(state = 'disabled')
        for i5 in F5:
            if i5 == 'empty':
                r5.configure(state = 'disabled')
        for i6 in F6:
            if i6 == 'empty':
                r6.configure(state = 'disabled')
        for i7 in F7:
            if i7 == 'empty':
                r7.configure(state = 'disabled')
        for i8 in F8:
            if i8 == 'empty':
                r8.configure(state = 'disabled')
        for i9 in F9:
            if i9 == 'empty':
                r9.configure(state = 'disabled')
        for i10 in F10:
            if i10 == 'empty':
                r10.configure(state = 'disabled')
    else:
        w5.deiconify()
def dopw():
    f = open('pw.dat', 'w')
    f.write(cpw.get())
    f.close()
    w8.destroy()
def doid():
    f = open('owner.dat', 'w')
    f.write(cid.get())
    f.close()
    w9.destroy()
def changepw():
    global w8
    if w8 is None or not w8.winfo_exists():
        w8 = Toplevel()
        Label(w8, text = u'PWを入力').pack()
        Entry(w8, textvariable = cpw).pack()
        Button(w8, text = u'変更する', command = dopw).pack()
    else:
        w8.deiconify()
def changeid():
    global w9
    if w9 is None or not w9.winfo_exists():
        w9 = Toplevel()
        Label(w9, text = u'IDを入力').pack()
        Entry(w9, textvariable = cid).pack()
        Button(w9, text = u'変更する', command = doid).pack()
    else:
        w9.deiconify()
def adinfo():
    global w14
    if w14 is None or not w14.winfo_exists():
        w14 = Toplevel()
        Button(w14, text = u'管理者名を変更する', command = changeid).pack()
        Button(w14, text = u'パスワードを変更する', command = changepw).pack()
        Button(w14, text = u'住所を変更する').pack()
        Button(w14, text = u'メールアドレスを変更する').pack()
        Button(w14, text = u'セキュリティキーを変更する').pack()
    else:
        w14.deiconify()
def menu():
    global w10
    if w10 is None or not w10.winfo_exists():
        w10 = Toplevel()
        Label(w10, text = u'管理者メニュー').pack()
        Button(w10, text = u'管理者情報を変更する', command = adinfo).pack()
        Button(w10, text = u'出品する', command = price).pack()
        Button(w10, text = u'商品を回収する', command = tt).pack()
        Button(w10, text = u'値段を変更する', command = cp).pack()
        Button(w10, text = u'終了', command = w10.destroy).pack()
    else:
        w10.deiconify()
def security():
    if st1.get() and st2.get():
        fo1 = open('owner.dat', 'r')
        for i in fo1:
            de = key.decrypt(i)
            strip = de.rstrip()
        fo2 = open('pw.dat', 'r')
        for ii in fo2:
            ii == ii
            de2 = key.decrypt(ii)
            strip2 = de2.rstrip()
        if st1.get() == strip and st2.get() == strip2:
            menu()
            st2.set('')
            w1.destroy()
        else:
            Message(w1, text = u'管理者名又はパスワードが違います').pack()
    else:
        Message(w1, text = u'ログイン情報を正しく入力してください').pack()
def register():
    if st1.get() and st2.get() and st6.get() and st7.get() and len(st8.get()) == 8:
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
        ads = len(st6.get())
        adp = 64-ads
        text3 = ' '*adp
        ead = len(st7.get())
        edp = 48-ead
        text4 = ' '*edp
        skey = Crypto.Cipher.DES.new(st8.get(), Crypto.Cipher.DES.MODE_ECB)
        key1 = skey.encrypt(st1.get() + text)
        key2 = skey.encrypt(st2.get() + text2)
        key3 = skey.encrypt(st6.get() + text3)
        key4 = skey.encrypt(st7.get() + text4)
        fo1 = open('owner.dat', 'w')
        fo1.write(key1)
        fo1.close()
        fo2 = open('pw.dat', 'w')
        fo2.write(key2)
        fo2.close()
        fo3 = codecs.open('address.dat', 'r', 'shift-jis')
        fo3.write(key3)
        fo3.close()
        fo4 = codecs.open('email.dat', 'r', 'shift-jis')
        fo4.write(key4)
        fo4.close()
        skeyobj.append(skey)
        menu()
        st1.set('')
        st2.set('')
        w1.destroy()
    else:
        Message(w1, text = u'未入力又は正しく入力されていない項目があります').pack()
def owner():
    global w1
    if w1 is None or not w1.winfo_exists():
        w1 = Toplevel()
        f1 = Frame(w1)
        f2 = Frame(w1)
        f3 = Frame(w1)
        f4 = Frame(w1)
        if not os.path.isfile("owner.dat") and not os.path.isfile("pw.dat"):
            Label(w1, text = u'管理者登録').pack()
            Label(w1, textvariable = regcon).pack()
            Label(w1, text = u'全て入力必須です。').pack()
            Label(w1, text = 'Owner:').pack()
            Entry(w1, textvariable = st1).pack()
            Label(w1, text = u'Password(16以内):').pack()
            Entry(w1, textvariable = st2, show='*').pack()
            Checkbutton(w1, text = u'通信販売を利用しない。※登録しないと通販での商品の売買ができなくなります').pack()
            Label(f1, text = u'住所:').pack(side = LEFT)
            Entry(f1, textvariable = st6).pack(side = RIGHT)
            Label(f2, text = u'メールアドレス:').pack(side = LEFT)
            Entry(f2, textvariable = st7).pack(side = RIGHT)
            Label(f3, text = u'セキュリティキー(8文字):').pack(side = LEFT)
            Entry(f3, textvariable = st8).pack(side = RIGHT)
            Button(f4, text = u'登録', command = register).pack()
            f1.pack()
            f2.pack()
            f3.pack()
            f4.pack()
        else:
            Label(w1, text = 'Owner:').pack()
            Entry(w1, textvariable = st1).pack()
            Label(w1, text = 'Password:').pack()
            Entry(w1, textvariable = st2, show='*').pack()
            Button(w1, text = u'ログイン', command = security).pack()
    else:
        w1.deiconify()
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
def reset():
    kane.set(0)
    chargem.append(0)
def cdone():
    w11.destroy()
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
    global w11
    if w11 is None or not w11.winfo_exists():
        if val.get() != 0:
            w11 = Toplevel()
            for countm in chargem:
                countm == countm
            Label(w11, text = u'確認').pack()
            Label(w11, text = countm).pack()
            if val.get() == 1:
                Label(w11, text = u'クレジットカード').pack()
            elif val.get() == 2:
                Label(w11, text = u'コンビニ支払い').pack()
            elif val.get() == 3:
                Label(w11, text = u'Webmoney').pack()
            Button(w11, text = u'チャージ', command = cdone).pack()
            Button(w11, text = u'戻る', command = w11.destroy).pack()
        else:
            Message(w12, text = u'お支払い方法を選択してください').pack()
    else:
        w11.deiconify()
def pfw():
    if loginw.get() == 'login':
        pass
    else:
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'ウォレットを利用するにはログインしてください',
                      strings = ['OK'], default = 0)
        chec.set(False)
def walletmenu():
    global w12
    if w12 is None or not w12.winfo_exists():
        w12 = Toplevel()
        wuf = open('wallet.dat', 'r')
        for wufi in wuf:
            wufi = int(wufi)
            xyz.append(wufi)
        if wufi != '0' or '':
            wallet.append(wufi)
        if wufi != '0':
            for i in xyz:
                moneyval.set(i)
        Label(w12, text = u'チャージする金額と支払い方法を選択').pack()
        kin = Label(w12, textvariable = kane)
        kin.pack()
        loginw.set('login')
        Button(w12, text = u'1万円', command = manyen2).pack(side = LEFT)
        Button(w12, text = u'5千円', command = gosenyen2).pack(side = LEFT)
        Button(w12, text = u'千円', command = senyen2).pack(side = LEFT)
        Button(w12, text = u'500円', command = gohyaku).pack(side = LEFT)
        Button(w12, text = u'100円', command = hyaku2).pack(side = LEFT)
        Button(w12, text = u'50円', command = gojyu2).pack(side = LEFT)
        Button(w12, text = u'10円', command = jyuu2).pack(side = LEFT)
        Button(w12, text = u'訂正', command = reset).pack()
        Radiobutton(w12, text = u'クレジットカード', variable = val, value = 1).pack()
        Radiobutton(w12, text = u'コンビニ支払い', variable = val, value = 2).pack()
        Radiobutton(w12, text = u'Webmoney', variable = val, value = 3).pack()
        Button(w12, text = u'確認する', command = charge).pack()
        Button(w12, text = u'チャージを行わないで終了', command = w12.destroy).pack()
    else:
        w12.deiconify()
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
        w13.destroy()
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
        w13.destroy()
        st3.set('')
        st4.set('')
    else:
        Message(w1, text = u'アカウント情報を正しく入力してください').pack()
def wallets():
    global w13
    if w13 is None or not w13.winfo_exists():
        w13 = Toplevel()
        if not os.path.isfile("userwallet.dat") and not os.path.isfile("walletpw.dat"):
            Label(w13, text = u'ウォレット登録').pack()
            Label(w13, text = u'ID:').pack()
            Entry(w13, textvariable = st3).pack()
            Label(w13, text = u'パスワード').pack()
            Entry(w13, textvariable = st4, show = '*').pack()
            Button(w13, text = u'登録', command = regist).pack()
        else:
            Label(w13, text = u'ログイン').pack()
            Label(w13, text = u'ID:').pack()
            Entry(w13, textvariable = st3).pack()
            Label(w13, text = u'パスワード').pack()
            Entry(w13, textvariable = st4, show = '*').pack()
            Button(w13, text = u'ログイン', command = wlogin).pack()
    else:
        w13.deiconify()
f4 = Frame(root)
Label(f4, text = '1', width = 7, height = 7).pack()
Label(f4, text = '2', width = 7, height = 7).pack()
Label(f4, text = '3', width = 7, height = 7).pack()
Label(f4, text = '4', width = 7, height = 7).pack()
Label(f4, text = '5', width = 7, height = 7).pack()
f5 = Frame(root)
Label(f5, text = '6', width = 7, height = 7).pack()
Label(f5, text = '7', width = 7, height = 7).pack()
Label(f5, text = '8', width = 7, height = 7).pack()
Label(f5, text = '9', width = 7, height = 7).pack()
Label(f5, text = '10', width = 7, height = 7).pack()
f3 = Frame(root)
Label(f3, text = u'Trade Center(管理用)', font = ('New Times Roman', 24)).pack()
f9 = Frame(root)
Label(f9, text = u'所持額:').pack(side = LEFT)
Mon = Label(f9, textvariable = moneyval).pack(side = RIGHT)
f11 = Frame(root)
Button(f11, text = u'終了', command = sys.exit).pack()
Button(f11, text = u'管理', command = owner).pack()
Button(f11, text = u'ウォレット：チャージ/ログイン', command = wallets).pack()
f4.pack(side = LEFT)
f1.pack(side = LEFT)
f5.pack(side = RIGHT)
f2.pack(side = RIGHT)
f3.pack(fill = BOTH)
f9.pack()
f11.pack()
root.mainloop()
