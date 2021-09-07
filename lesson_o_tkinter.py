##it's a python binding for command line graphical interface
#message box
#>showinfo
#>askyesno
#>askokcancel
# tkdocs.com

import tkinter as tk
from tkinter import messagebox

## show a message box without the root
#
def test_messagebox():
    #retire root window
    root = tk.Tk()
    root.withdraw()
    #on it's own would show an empty tk window
    messagebox.showinfo("Shaka", "When the walls fell")

test_messagebox()