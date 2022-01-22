import os
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(480, 170))
        self.master.title('Check Files')
        self.master.config(bg='grey95')

        self.lblTop = Entry(self.master, text='', width=27, font=('Helvetica', 16), fg='black', bg='white')
        self.lblTop.grid(row=1, columnspan=4, padx=(120,0), pady=(45,0), sticky='E')
       
        self.lblBottom = Entry(self.master, text='', width=27, font=('Helvetica', 16), fg='black', bg='white')
        self.lblBottom.grid(row=2, columnspan=4, padx=(120,0), pady=(7,0), sticky='E')

       

        selfbtnBrowse = Button(self.master, text='Browse...', width=12, height=1, command=lambda: chooseFile(self))
        selfbtnBrowse.grid(row=1, column=0, padx=(7,7), pady=(45,0), sticky=W)
        
        selfbtnBrowse = Button(self.master, text='Browse...', width=12, height=1, command=lambda: chooseFile(self))
        selfbtnBrowse.grid(row=2, column=0, padx=(7,7), pady=(7,0), sticky=W)

        selfbtnCheck = Button(self.master, text='Check for files...', width=12, height=2)
        selfbtnCheck.grid(row=3, column=0, padx=(7,7), pady=(10,7), sticky=SW)

        selfbtnClose = Button(self.master, text='Close Program', width=14, height=2, command=lambda: closeProgram(self))
        selfbtnClose.grid(row=3, column=3, padx=(7,1), pady=(10,7), sticky=SE)



def chooseFile(self):
    name = fd.askdirectory()
    Path = name
    print(Path)
    
       
    


def closeProgram(self):
    if messagebox.askokcancel("Close program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def onSelect(self,event):
    varList = event.widget
    select = varList.curselection() [0]
    value = varList.get(select)
    conn = sqlite3.connect('')
    with conn:
        cursor = conn.cursor()
        cursor.execute()

     



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
        
