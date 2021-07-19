from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
#import sys


class File():
    def newFile(self, *args):
        self.filename = "Untitled"
        self.text.delete(0.0, END)

    def saveFile(self, *args):
        try:
            t = self.text.get(0.0, END)
            f = open(self.filename, 'w')
            f.write(t)
            f.close()
        except:
            self.saveAs()

    def saveAs(self, *args):
        #args for keypress event    
        f = asksaveasfile(mode='w', defaultextension='.txt')
        t = self.text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            pass

    def openFile(self, *args):
        import os
        f = askopenfile(defaultextension=".txt", 
                                      filetypes=[("All Files","*.*"), 
                                        ("Text Documents","*.txt")])
        if not f:
            self.filename = None
        else:
            self.filename = f.name
            self.readFile(f)

    def readFile(self, f):
        t = f.read()
        self.text.delete(0.0, END)
        self.text.insert(0.0, t)
        self.root.title(os.path.basename(self.filename) + " - PyPad PRO")

    def quit(self, *args):
        entry = askyesno(title="Quit", message="Are you sure you want to quit?")
        if entry == True:
            self.root.destroy()

    def __init__(self, text, root):
        self.filename = None
        self.text = text
        self.root = root


def main(root, text, menubar, file_path):
    filemenu = Menu(menubar, tearoff=False)
    objFile = File(text, root)
    if file_path:
        objFile.filename = file_path
        with open(file_path, "r") as f:
            objFile.readFile(f)

    filemenu.add_command(label="New", command=objFile.newFile, accelerator="Ctrl+N")
    filemenu.add_command(label="Open", command=objFile.openFile, accelerator="Ctrl+O")
    filemenu.add_command(label="Save", command=objFile.saveFile, accelerator="Ctrl+S")
    filemenu.add_command(label="Save As...", command=objFile.saveAs, accelerator="Ctrl+Shift+S")
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=objFile.quit, accelerator="Ctrl+D")
    menubar.add_cascade(label="File", menu=filemenu)
    
    root.bind("<Control-s>", objFile.saveFile)
    root.bind("<Control-o>", objFile.openFile)
    root.bind("<Control-d>", objFile.quit)
    root.bind("<Control-n>", objFile.newFile)
    root.bind("<Control-Shift-S>", objFile.saveAs)
    
    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'PyPad.pyw'")
