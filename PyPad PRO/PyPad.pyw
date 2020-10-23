from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from tkinter.font import Font
import file_menu
import edit_menu
import format_menu
import help_menu

class PyPadPRO():
    def __init__(self):
        root = Tk()

        root.title("Untitled - PyPad PRO")
        root.geometry("300x250+300+300")
        root.minsize(width=400, height=400)

        text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
        text.pack(fill=Y, expand=1)

        text.focus_set()

        menubar = Menu(root, tearoff=False)



        photo = PhotoImage(file = "PyPad.png")
        root.iconphoto(False, photo)
        file_menu.main(root, text, menubar)
        edit_menu.main(root, text, menubar)
        format_menu.main(root, text, menubar)
        help_menu.main(root, text, menubar)
        root.mainloop()

app = PyPadPRO()
