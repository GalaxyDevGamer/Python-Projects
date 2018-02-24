#coding:utf-8
from Tkinter import *
import codecs
root = Tk()
st = StringVar()
line = u'宇宙飛行士'
def tes():
    w = codecs.open(u'テストファイル.dat', 'a', 'shift-jis')
    w.write(u'宇宙飛行士')
    w.close()
    f = codecs.open(u'テストファイル.dat', 'r', 'shift-jis')
    for i in f:
        i==i
        print i
    st.set(i)
    Label(root, textvariable = st).pack()
tes()
root.mainloop()
