# importing the necessary modules
import tkinter as tk
from tkinter import *
import webbrowser as wb


root = tk.Tk()

# creating a variable from the user's input
text_var=tk.StringVar()

# creating the GUI, its styling, and the entry bar 
e = tk.Entry(root, textvariable=text_var, width=50, font=('helvetica',10,'normal'))
e.pack()
e.insert(0, "")


# creating the function to get the user's input
def Submit():
    msg = text_var.get()
    print(msg)
# this will open a file for the website and insert the input to the page
    f = open("basic_site.html", "w")
    f.write(msg)
    f.close()
    url = "/Programs/Python/Python310/basic_site.html"
    wb.open_new(url)


# creating the button for the user's input 
submit_button = tk.Button(root, text="Submit", command = Submit)
submit_button.pack()




root.mainloop()

