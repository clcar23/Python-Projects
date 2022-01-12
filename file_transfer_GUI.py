#this will show how to move new/updated files only from folder to folder
#import all the necessary modules
import os
import os.path
import shutil
from datetime import datetime, timedelta
import tkinter

from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import *


#creating the tkinter window
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.geometry("500x300")
        self.master.title('Move updated files')
        self.master.config(bg='grey93')
#creating buttons, entry boxs, adding in functionality
        self.txtSource = Entry(self.master, width=30,  text=folderPathStart, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtSource.grid(row=1, column=1, padx=(5, 5), pady=(5, 5))
        self.btnSource = Button(self.master, text='From', width=10, height=2, command=chooseFile)
        self.btnSource.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky='W')

        self.txtDestination = Entry(self.master, width=30, text=folderPathEnd, font=('Helvetica', 16), fg='black', bg='lightblue')
        self.txtDestination.grid(row=2, column=1, padx=(5, 5), pady=(5, 5))
        self.btnDestination = Button(self.master, text='To', width=10, height=2, command=moveFile)
        self.btnDestination.grid(row=2, column=0, padx=(5, 5), pady=(5, 5), sticky='SW')

        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=moveFiles)
        self.btnSubmit.grid(row=3, column=1, padx=(5, 5), pady=(10, 0))

#creating a function for the first button that chooses the folder with files to be moved
def chooseFile():
    name = tkinter.filedialog.askdirectory()
    folderPathStart.set(name)

#creating a function for the second button that chooses the folder for the files to be moved to
def moveFile():
    name = tkinter.filedialog.askdirectory()
    folderPathEnd.set(name)


#the function that moves the files
def moveFiles():
    # create the source object
    source = folderPathStart.get()

    # create the destination object
    destination = folderPathEnd.get()

    source_files = os.listdir(source)

    # getting the current time for comparison
    cur_time = datetime.now()
    print("current time" + str(cur_time))

    for i in source_files:
        file_path = os.path.join(source, i)
        # changing the time until the past 24 hours
        past_24hrs = cur_time - timedelta(hours=24)
        # getting the modification date of the files
        mod_date_in_sec = os.path.getmtime(file_path)
        # converting the time from seconds into days
        recent_update_files = datetime.fromtimestamp(mod_date_in_sec)
        if past_24hrs < recent_update_files:
            shutil.move(source + '/' + i, destination)
            print(i + "File transfer successful!")
        else:
            print("No recent updates to files.")



if __name__ == "__main__":
    root = Tk()
    folderPathStart = StringVar()
    folderPathEnd = StringVar()
    App = ParentWindow(root)
    root.mainloop()


