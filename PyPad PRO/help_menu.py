from tkinter import *
from tkinter.messagebox import *
import sys


class Help():
    def about(root):
        
        showinfo(title="PyPad PRO", message="A Light(er)weight fully-featured Notepad written purely in Python 3.x.\n(c) 2020 Samuel Cheng")


def main(root, text, menubar):

    help = Help()

    helpMenu = Menu(menubar, tearoff=False)
    helpMenu.add_command(label="About", command=help.about)
    menubar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'PyPad.py'")
