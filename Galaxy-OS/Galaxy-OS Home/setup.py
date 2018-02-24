# coding:shift-jis
from Tkinter import *
import Crypto.Cipher.DES
root = Tk()
i1 = IntVar()
enckey2 = Crypto.Cipher.DES.new("kudoukey", Crypto.Cipher.DES.MODE_ECB)
ek1 = 'activate'
dousa = 'ugoitaze'
ugoku = enckey2.encrypt(dousa)
eke = enckey2.encrypt(ek1)

def write():
    if i1.get() == 1:
        f = open('License.dat', 'w')
        f.write(eke)
        f.close()
        root.destroy()
    if i1.get() == 2:
        f = open('License.dat', 'w')
        f.write(ugoku)
        f.close()
        root.destroy()
Radiobutton(root, text = 'activate', variable = i1, value = 1).pack()
Radiobutton(root, text = 'ugoitaze', variable = i1, value = 2).pack()
Button(root, text = 'OK', command = write).pack()
root,mainloop()
