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
st1 = StringVar()
st2 = StringVar()
st3 = StringVar()
st4 = StringVar()
st5 = StringVar()
st6 = StringVar()
tota = StringVar()
moneyval = StringVar()
val = IntVar()
chec = BooleanVar()
loginw = StringVar()
kane = StringVar()
kane.set(0)
xyz = []
selecti = IntVar()
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
f1 = Frame(root)
i_d = PhotoImage(file = 'tradebox.gif', width = 100, height = 80)
a2 = 'empty'
b2 = 'empty'
c2 = 'empty'
dd2 = 'empty'
e2 = 'empty'
F2 = 'empty'
g2 = 'empty'
h2 = 'empty'
ii2 = 'empty'
j2 = 'empty'
k2 = 0
l2 = 0
m2 = 0
n2 = 0
o2 = 0
p2 = 0
q2 = 0
r2 = 0
s2 = 0
t2 = 0
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
def shori():
    if selecti.get() == 1:
        f = open('item1pr.dat', 'r')
        fr = codecs.open('item1.dat', 'r', 'shift-jis')
        for item in fr:
            item == item
        n = '1'
        con = R1
        Lco = L1
        Pco = P1
    if selecti.get() == 2:
        f = open('item2pr.dat', 'r')
        fr = codecs.open('item2.dat', 'r', 'shift-jis')
        for item in fr:
            item == item
        n = '2'
        con = R2
        Lco = L2
        Pco = P2
    if selecti.get() == 3:
        f = open('item3pr.dat', 'r')
        fr = codecs.open('item3.dat', 'r', 'shift-jis')
        for item in fr:
            item == item
        n = '3'
        con = R3
        Lco = L3
        Pco = P3
    if selecti.get() == 4:
        f = open('item4pr.dat', 'r')
        fr = codecs.open('item4.dat', 'r', 'shift-jis')
        for item in fr:
            item == item
        n = '4'
        con = R4
        Lco = L4
        Pco = P4
    if selecti.get() == 5:
        f = open('item5pr.dat', 'r')
        fr = codecs.open('item5.dat', 'r', 'shift-jis')
        for item in fr:
            item == item
        n = '5'
        con = R5
        Lco = L5
        Pco = P5
    if selecti.get() == 6:
        f = open('item6pr.dat', 'r')
        fr = codecs.open('item6.dat', 'r', 'shift-jis')
        for item in fr:
            item == item
        n = '6'
        con = R6
        Lco = L6
        Pco = P6
    if selecti.get() == 7:
        f = open('item7pr.dat', 'r')
        fr = codecs.open('item7.dat', 'r', 'shift-jis')
        for item in fr:
            item == item
        n = '7'
        con = R7
        Lco = L7
        Pco = P7
    if selecti.get() == 8:
        f = open('item8pr.dat', 'r')
        fr = codecs.open('item8.dat', 'r', 'shift-jis')
        for item in fr:
            item == item
        n = '8'
        con = R8
        Lco = L8
        Pco = P8
    if selecti.get() == 9:
        f = open('item9pr.dat', 'r')
        fr = codecs.open('item9.dat', 'r', 'shift-jis')
        for item in fr:
            item == item
        n = '9'
        con = R9
        Lco = L9
        Pco = P9
    if selecti.get() == 10:
        f = open('item10pr.dat', 'r')
        fr = codecs.open('item10.dat', 'r', 'shift-jis')
        for item in fr:
            item == item
        n = '10'
        con = R10
        Lco = L10
        Pco = P10
    if item == 'empty':
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                  text = u'商品が入っていません',
                  strings = ['OK'], default = 0)
        selecti.set('0')
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
                selecti.set('0')
            else:
                x = int(i)-int(p1)
                moneyval.set(str(x))
                wallet.append(x)
                chargem.append(x)
                codecs.open('item%s.dat' % n, 'w', 'shift-jis').write('empty')
                open('item%spr.dat' % n, 'w').write('0')
                open('wallet.dat', 'w').write(str(x))
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
                selecti.set('0')
                con.configure(state = 'disabled')
                Lco.configure(text = 'empty')
                Pco.configure(text = int(0))
        else:
            for p2 in f:
                p2==p2
            for ii in pri:
                ii == ii
            if ii<int(p2):
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お金が不足しています',
                              strings = ['OK'], default = 0)
                selecti.set('0')
            else:
                ii-=int(p2)
                to1.configure(text = int(ii))
                pri.append(ii)
                codecs.open('item%s.dat' % n, 'w', 'shift-jis').write('empty')
                open('item%spr.dat' % n, 'w').write('0')
                Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                              text = u'お買い上げありがとうございました',
                              strings = ['OK'], default = 0)
                selecti.set('0')
                con.configure(state = 'disabled')
                Lco.configure(text = 'empty')
                Pco.configure(text = int(0))
def manyen2():
    price = 10000
    for countm in chargem:
        countm+=price
    kane.set(countm)
    chargem.append(countm)
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
def gohyaku():
    price = 500
    for countm in chargem:
        countm+=price
    kane.set(countm)
    chargem.append(countm)
def hyaku2():
    price = 100
    for countm in chargem:
        countm+=price
    kane.set(countm)
    chargem.append(countm)
def gojyu2():
    price = 50
    for countm in chargem:
        countm+=price
    kane.set(countm)
    chargem.append(countm)
def jyuu2():
    price = 10
    for countm in chargem:
        countm+=price
    kane.set(countm)
    chargem.append(countm)
def pfw():
    if loginw.get() == 'login':
        pass
    else:
        Dialog.Dialog(root, title = 'alert', bitmap = 'info',
                      text = u'ウォレットを利用するにはログインしてください',
                      strings = ['OK'], default = 0)
        chec.set(False)
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
        wuf = open('wallet.dat', 'r')
        for wufi in wuf:
            wufi = int(wufi)
            xyz.append(wufi)
        if wufi != '0' or '':
            wallet.append(wufi)
        if wufi != '0':
            for i in xyz:
                moneyval.set(i)
        loginw.set('login')
    else:
        Message(w1, text = u'ID又はパスワードが違います').pack()
def wallets():
    global w3
    if w3 is None or not w3.winfo_exists():
        w3 = Toplevel()
        Label(w3, text = u'ログイン').pack()
        Label(w3, text = u'ID:').pack()
        Entry(w3, textvariable = st3).pack()
        Label(w3, text = u'パスワード').pack()
        Entry(w3, textvariable = st4, show = '*').pack()
        Button(w3, text = u'ログイン', command = wlogin).pack()
    else:
        w3.deiconify()
f4 = Frame(root)
R1 = Radiobutton(f4, text = '1', width = 7, height = 7, variable = selecti, value = 1, state = 'disabled', command = shori)
R1.pack()
R2 = Radiobutton(f4, text = '2', width = 7, height = 7, variable = selecti, value = 2, state = 'disabled', command = shori)
R2.pack()
R3 = Radiobutton(f4, text = '3', width = 7, height = 7, variable = selecti, value = 3, state = 'disabled', command = shori)
R3.pack()
R4 = Radiobutton(f4, text = '4', width = 7, height = 7, variable = selecti, value = 4, state = 'disabled', command = shori)
R4.pack()
R5 = Radiobutton(f4, text = '5', width = 7, height = 7, variable = selecti, value = 5, state = 'disabled', command = shori)
R5.pack()
f5 = Frame(root)
R6 = Radiobutton(f5, text = '6', width = 7, height = 7, variable = selecti, value = 6, state = 'disabled', command = shori)
R6.pack()
R7 = Radiobutton(f5, text = '7', width = 7, height = 7, variable = selecti, value = 7, state = 'disabled', command = shori)
R7.pack()
R8 = Radiobutton(f5, text = '8', width = 7, height = 7, variable = selecti, value = 8, state = 'disabled', command = shori)
R8.pack()
R9 = Radiobutton(f5, text = '9', width = 7, height = 7, variable = selecti, value = 9, state = 'disabled', command = shori)
R9.pack()
R10 = Radiobutton(f5, text = '10', width = 7, height = 7, variable = selecti, value = 10, state = 'disabled', command = shori)
R10.pack()
f3 = Frame(root)
Label(f3, text = u'Trade Center for Web', font = ('New Times Roman', 24)).pack()
Label(f3, text = u'利用方法:').pack()
Label(f3, text = u'1.商品を検索').pack()
Label(f3, text = u'2.その商品を売っているユーザー名を入力').pack()
Label(f3, text = u'3.ウォレットへログイン').pack()
Label(f3, text = u'4.商品のボタンを押す').pack()
Label(f3, text = u'5.商品注文メールが出品者に送信されるので、到着を待つ').pack()
Label(f3, text = u'6.必要であれば、出品者にメールにて連絡を取る').pack()
f7 = Frame(root)
Label(f7, text = u'ユーザー名：').pack(side = LEFT)
Entry(f7, textvariable = st6).pack(side = RIGHT)
f6 = Frame(root)
Label(f6, text = u'合計金額:').pack(side = LEFT)
to1 = Label(f6, text = ii, font = ('New Times Roman', 18), bg = 'white')
to1.pack(side = RIGHT)
f9 = Frame(root)
Label(f9, text = u'所持額:').pack(side = LEFT)
Mon = Label(f9, textvariable = moneyval).pack(side = RIGHT)
f10 = Frame(root)
Checkbutton(f10, text = u'ウォレットで支払う', variable = chec, command = pfw).pack()
f11 = Frame(root)
Button(f11, text = u'終了', command = sys.exit).pack()
Button(f11, text = u'ウォレットへログイン', command = wallets).pack()

f4.pack(side = LEFT)
f1.pack(side = LEFT)
f5.pack(side = RIGHT)
f2.pack(side = RIGHT)
f3.pack(fill = BOTH)
f7.pack()
f6.pack()
f9.pack()
f10.pack()
f11.pack()
root.mainloop()
