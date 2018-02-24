from Tkinter import *
from tkCommonDialog import Dialog
root = Tk()
st = StringVar()
def showdir(root):
    Label(textvariable = st).pack()
class DirSelectDlg(Dialog):
    command = "tk_chooseDirectory"
    showdir(root)
openfiledir = DirSelectDlg(Dialog).show()
DirselectDlg(Dialog)
st.set(openfiledir)
root.mainloop()

