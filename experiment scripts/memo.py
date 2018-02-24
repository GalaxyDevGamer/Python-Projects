#! /usr/bin/env python
# -*- coding: shift_jis -*-
import Tkinter as Tk
import ScrolledText as S
import tkFileDialog as D
import os
      
class Frame(Tk.Frame):  
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title(os.name=='posix' and 'untitled' or u'����')
        self.file_name=None
        ### Menu
        menu_bar = Tk.Menu(self, tearoff=0)
        # File
        menu_file = Tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=u"�t�@�C��(F)", menu=menu_file,  underline=5)
        menu_file.add_command(label=u"�V�K�쐬(N)", command=self.new_memo, underline=5, accelerator = 'Ctrl-N')
        menu_file.add_command(label=u"�J��(O)", command=self.open_memo, underline=3, accelerator = 'Ctrl-O')
        menu_file.add_command(label=u"�ۑ�(S)", command=self.save_memo, underline=3, accelerator = 'Ctrl-S')
        menu_file.add_command(label=u"���O�����ĕۑ�(A)", command=self.saveas_memo, underline=9)
        menu_file.add_separator()
        menu_file.add_command(label=u"�I��(Q)", command=self.exit, underline=3 , accelerator = 'Ctrl-Q')
        # Edit
        menu_edit = Tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=u'�ҏW(E)', menu=menu_edit, underline=3)
        menu_edit.add_command(label=u'�S�Ă�I��(A)', command=self.select_all, underline=6, accelerator = 'Ctrl-A')
        menu_edit.add_command(label=u'�؂���(X)', command=self.cut, underline=5,
                              accelerator = os.name=='posix' and 'Ctrl-W' or 'Ctrl-X')
        menu_edit.add_command(label=u'�R�s�[(C)', command=self.copy, underline=4,
                              accelerator = os.name=='posix' and 'Alt-W' or 'Ctrl-C')
        menu_edit.add_command(label=u'�y�[�X�g(V)', command=self.paste, underline=5,                                    accelerator = os.name=='posix' and 'Ctrl-Y' or 'Ctrl-V')
        menu_edit.add_command(label=u'�J�[�\���̂���s���폜', command=self.delete_line, accelerator = 'Shift-Del')
     # short-cuts
        self.master.bind('<Control-KeyPress-o>', self.open_memo)
        self.master.bind('<Control-KeyPress-s>', self.save_memo)
        self.master.bind('<Control-KeyPress-q>', self.exit)
        self.master.bind('<Control-KeyPress-a>', self.select_all)
        self.master.bind('<Shift-KeyPress-Delete>', self.delete_line)
        self.master.bind('<Double-Button-1>', self.delete_line)
        if os.name == 'posix':
            self.master.bind('<Alt-KeyPress-w>', self.copy)
     
        # add menu bar
        try:
            self.master.config(menu=menu_bar)     # this required to show the menu bar
        except AttributeError:
            self.master.Tk.call(master, "config", "-menu", menu_bar)
     
     
        self.txt = S.ScrolledText(self, font=('Helvetica', '10'))
        self.txt.pack(fill=Tk.BOTH, expand=1)
        self.txt.focus_set()
     
     
    def new_memo(self, event=None):
        self.file_name=None
        self.master.title(os.name=='posix' and 'untitled' or u'����')
        self.txt.delete('1.0', Tk.END)
     
     
    def open_memo(self, event=None):
        fname = D.askopenfilename(filetypes =[('text files', '*.txt'), ('all files', '*.*')])
                                        
        if fname:
            self.txt.delete('1.0', Tk.END)
            f=file(fname)
            self.txt.insert(Tk.END, f.read().decode('shift_jis'))  ## decode is required to show data
            f.close()
            self.file_name = fname
            self.master.title(fname)
     
     
    def save(self, f):
        f.write(self.txt.get('1.0', Tk.END).encode('shift_jis')) ## encode is required to write data
        f.close()
                 
    def save_memo(self, event=None):
        if self.file_name:
            self.save(file(self.file_name, 'w'))
        else:
            self.saveas_memo()
     
    def saveas_memo(self):
        fname = D.asksaveasfilename(filetypes =[('text files', '*.txt')])
        if fname:
            self.save(file(fname, 'w'))
            self.file_name=fname
            self.master.title(fname)
     
     
    def select_all(self, event=None):
        self.txt.tag_add(Tk.SEL, '1.0', Tk.END+'-1c')
        self.txt.mark_set(Tk.INSERT, '1.0')
        self.txt.see(Tk.INSERT)
     
    def cut(self, event=None):
        if self.txt.tag_ranges(Tk.SEL):
            self.copy()
            self.txt.delete(Tk.SEL_FIRST, Tk.SEL_LAST)
     
    def copy(self, event=None): 
        if self.txt.tag_ranges(Tk.SEL): 
            text = self.txt.get(Tk.SEL_FIRST, Tk.SEL_LAST)  
            self.clipboard_clear()              
            self.clipboard_append(text)
     
    def paste(self, event=None):
        text = self.selection_get(selection='CLIPBOARD')
        if text:
            self.txt.insert(Tk.INSERT, text)
            self.txt.tag_remove(Tk.SEL, '1.0', Tk.END) 
            self.txt.see(Tk.INSERT)
     
    def delete_line(self, event=None):
        self.txt.delete(Tk.INSERT + " linestart", Tk.INSERT + " lineend")
             
    def exit(self, event=None):
        self.master.destroy()
     
     
if __name__ == '__main__':
    f = Frame()
    f.pack()
    f.mainloop()
