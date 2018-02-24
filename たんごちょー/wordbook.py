# coding:shift-jis
from Tkinter import *
from ScrolledText import *
import os
import random
import shutil
import codecs
root = Tk()
w1 = None
w2 = None
w3 = None
w4 = None
cb1 = BooleanVar()
curd = os.getcwd()
tangoc = StringVar()
con1 = StringVar()
tanr = StringVar()
tango = StringVar()
con2 = StringVar()
con3 = StringVar()
st1 = StringVar()
st2 = StringVar()
def wordlist():
    global w1
    if w1 is None or not w1.winfo_exists():
        l1 = os.listdir("%s\\words" % curd)
        w1 = Toplevel()
        for i in l1:
            ni = i.decode('shift-jis')
            Label(w1, text = i).pack()
    else:
        w1.deiconify()
def sw():
    if tanr.get() == '':
        con2.set(u'単語入力しないとか、一体何がしたい？')
    else:
        try:
            os.chdir("%s\\words" % curd)
        except WindowsError:
            con2.set(u'システム故障')
        else:
            try:
                fo = open('%s' % tanr.get() + '.txt', 'r')
            except IOError:
                con2.set(u'そんな単語入ってねぇーぞ')
            else:
                t0.delete('1.0', 'end')
                for i in fo:
                    t0.insert('end', i.decode('shift-jis'))
                fo.close()
                tango.set(tanr.get())
                w2.destroy()
                os.chdir("%s\\Keyword" % curd)
                try:
                    os.path.isfile(tanr.get() + '.dat')
                except WindowsError:
                    con2.get(u'キーワードが見つからん')
                else:
                    f = codecs.open(tanr.get() + 'kw.dat', 'r', 'shift-jis')
                    for i in f:
                        st2.set(i)
def seeword():
    global w2
    if w2 is None or not w2.winfo_exists():
        w2 = Toplevel()
        F1 = Frame(w2)
        F2 = Frame(w2)
        Label(w2, textvariable = con2).pack()
        Label(F1, text = u'単語を検索:').pack(side = LEFT)
        Entry(F1, textvariable = tanr).pack(side = RIGHT)
        Button(F2, text = 'OK', command = sw).pack()
        F1.pack()
        F2.pack()
    else:
        w2.deiconify()
def savetango():
    data = t0.get('1.0', END)
    if tango.get() == '':
        con1.set(u'ちゃんと入力しろ！！')
    else:
        try:
            endata = data.encode('shift-jis')
        except UnicodeEncodeError:
            con1.set(u'使えねぇ文字がはいってっぞ！ちゃんと確認しろ！')
        else:
            try:
                os.chdir("%s\\words" % curd)
            except WindowsError:
                con1.set(u'トラブル発生!?一体何をした!?')
            else:
                if st2.get() == '':
                    con1.set(u'キーワードがないの！？')
                else:
                    k = codecs.open(tango.get() + 'kw.dat', 'w', 'shift-jis')
                    f = open(tango.get() + '.txt', 'w')
                    f.write(endata)
                    k.write(st2.get())
                    k.close()
                    f.close()
                    shutil.move(tango.get() + 'kw.dat', "%s\\Keyword" % curd)
                    con1.set(u'保存しといたぞー')
def newword():
    tango.set('')
    t0.delete('1.0', 'end')
def notame():
    if cb1 == True:
        con3.set('')
    else:
        con3.set(u'タメ口が嫌なら金払ってアップグレードしなさい')
def setting():
    global w3
    if w3 is None or w3.winfo_exists():
        w3 = Toplevel()
        Label(w3, textvariable = con3).pack()
        Checkbutton(w3, text = u'タメ口で通知をしない', variable = cb1, command = notame).pack()
    else:
        w3.deiconify()
def shori():
    times = 1
    os.chdir("%s\\Keyword" % curd)
    for r1 in ans:
        w = r1.strip('.txt')
    f = open(w + 'kw.dat', 'r')
    for i in f:
        print i
        os.chdir(curd)
        if st1.get() != i:
            print 'wrong'
        elif st1.get() == i:
            for score in scorec:
                score+=times
            scorec.append(score)
            st1.set('')
            print 'correct', score
    ten()
def ten():
    for cnt in cntc:
        cnt==cnt
    for B1 in eobj3:
        try:
            B1.configure(text = 'NEXT')
        except TclError:
            pass
    for q1 in eobj2:
        try:
            q1.configure(state = 'normal')
        except TclError:
            pass
    if list != []:
        r1 = random.choice(list)
        ans.append(r1)
        ni = r1.decode('shift-jis')
        strip = ni.strip(".txt")
        for L1 in eobj1:
            try:
                L1.configure(text = strip)
            except TclError:
                pass
        B1.configure(text = 'NEXT', command = shori)
        list.remove(r1)
    else:
        times = 0
        for score in scorec:
            score==score
        for L1 in eobj1:
            try:
                L1.configure(text = 'Test is finished')
            except TclError:
                pass
        q1.configure(state = 'disabled')
        B1.configure(state = 'disabled')
        Label(w4, text = 'Your total score is %d' % score).pack()
        Button(w4, text = 'OK', command = w4.destroy).pack()
        scorec.append(times)
        st1.set('')
def exam():
    global w4
    if w4 is None or not w4.winfo_exists():
        w4 = Toplevel()
        Label(w4, text = u'卒業試験').pack()
        L1 = Label(w4, text = '')
        L1.pack()
        eobj1.append(L1)
        q1 = Entry(w4, textvariable = st1, state = 'disabled')
        q1.pack()
        eobj2.append(q1)
        B1 = Button(w4, text = 'START', command = ten)
        B1.pack()
        eobj3.append(B1)
        ol = os.listdir("%s\\words" % curd)
        for i in ol:
            list.append(i)
    else:
        w4.deiconify()
cnt = 0
cntc = []
cntc.append(cnt)
score = 0
scorec = []
scorec.append(score)
ans = []
eobj1 = []
eobj2 = []
eobj3 = []
eobj4 = []
list = []
m0 = Menu(root)
root.configure(menu = m0)
m1 = Menu(m0, tearoff = False)
m2 = Menu(m0, tearoff = False)
m0.add_cascade(label = u'ファイル', under = 0, menu = m1)
m1.add_command(label = u'新規作成', command = newword)
m1.add_command(label = u'設定', command = setting)
m1.add_command(label = u'終了', command = sys.exit)
f1 = Frame(root)
f2 = Frame(root)
Label(root, text = u'高橋裕樹様専用の関数単語帳(ｗｗ)', font = ('Times New Roman', 18)).pack()
Label(root, text = u'使い方：登録する場合、単語と意味を入力、見る場合は単語を検索').pack()
Label(root, textvariable = con1).pack()
Label(f1, text = u'意味↓').pack(side = LEFT)
Label(f1, text = u'単語：').pack(side = LEFT)
Entry(f1, textvariable = tango).pack(side = LEFT)
Button(f1, text = u'単語を登録する', command = savetango).pack(side = LEFT)
Button(f1, text = u'単語の一覧', command = wordlist).pack(side = LEFT)
Button(f1, text = u'保存した単語を見る', command = seeword).pack(side = LEFT)
Button(f1, text = 'Examination', command = exam).pack(side = LEFT)
Label(f2, text = u'覚えるべきキーワード：').pack(side = LEFT)
Entry(f2, textvariable = st2, width = 75).pack(side = RIGHT)
t0 = ScrolledText(root)
f1.pack()
f2.pack()
t0.pack()
root.mainloop()
