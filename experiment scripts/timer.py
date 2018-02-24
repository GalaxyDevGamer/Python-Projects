# coding:shift-jis
from Tkinter import *

class app():
    TIME = 60*3
    def __init__(self, master = None):
        timestr.set("03:00")
        l = Label(w14, textvariable = timestr)
        b1 = Button(w14, text = u'スタート', command = countdown)
        b2 = Button(w14, text = u'終了', command = w14.destroy)
        for obj, sideparam in ((l,TOP),(b1,LEFT),(b2,RIGHT)):
            obj.pack(side = sideparam)
    def countdown():
        time = time.time()
        timeleft = max(TIME-(time.time()-time), 0)
        min,sec = (timeleft) / 60, timeleft % 60
        timestr.set("%02d:%02d" % (min,sec))
        root.after(1000, countdown)
app.mainloop()
