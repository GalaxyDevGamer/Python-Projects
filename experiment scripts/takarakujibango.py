# coding:shift-jis
from Tkinter import *
import random
loto6 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43']
loto7 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37']
numbers3 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers4 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
miniloto = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
root = Tk()
cnt = 0
cntc = []
cntc.append(cnt)
num = []
nums = ''
chose = IntVar()
def sentaku():
    if chose.get() == 1:
        n = 7
        l = loto7
    elif chose.get() == 2:
        n = 6
        l = loto6
    elif chose.get() == 3:
        n = 3
        l = numbers3
    elif chose.get() == 4:
        n = 4
        l = numbers4
    elif chose.get() == 5:
        n = 5
        l = miniloto
    else:
        pass
    for cnt in cntc:
        cnt==cnt
    if l != []:
        if n > cnt:
            r1 = random.choice(l)
            num.append(r1)
            cnt+=1
            cntc.append(cnt)
            sentaku()
        else:
            nums = num
            L1.configure(text = nums)
            cnt = 0
            cntc.append(cnt)
            if len(num) == n:
                del num[:]
    else:
        pass
Label(root, text = u'宝くじ番号生成機').pack()
Label(root, text = u'くじの種類を選択:').pack()
Radiobutton(root, text = 'LOTO 7', variable = chose, value = 1).pack()
Radiobutton(root, text = 'LOTO 6', variable = chose, value = 2).pack()
Radiobutton(root, text = 'NUMBERS 3', variable = chose, value = 3).pack()
Radiobutton(root, text = 'NUMBERS 4', variable = chose, value = 4).pack()
Radiobutton(root, text = 'MINI LOTO', variable = chose, value = 5).pack()
Button(root, text = u'生成', command = sentaku).pack()
Label(root, text = u'結果:').pack(side = LEFT)
L1 = Label(root, text = '')
L1.pack(side = RIGHT)
root.mainloop()
