from tkinter.ttk import *
from tkinter import *
from PIL import *
from generate_defaults import *

import os, sys

class Main:

    def __init__(self):
        self.root = Tk()
        self.root.title("SYSTEM 19 - MAIL")
        self.root.geometry("%dx%d" % (600,400))
        self.root.attributes("-topmost",1)
        self.root.wm_iconbitmap("./icon.ico")

        self.notebook = Notebook(self.root)
        self.page1 = Frame(self.notebook)
        self.page2 = Frame(self.notebook)
        self.notebook.add(self.page1, text="Images")
        self.notebook.add(self.page2, text="Videos")
        self.notebook.pack(fill=BOTH, expand=True)

        self.style = ttk.Style()
        self.style.configure(".",font=("Fixedsys",16))

class Image:

    def __init__(self):
        pass

class Video:

    def __init__(self):
        pass


if __name__ == "__main__":
    if os.path.isfile("./settings.txt") == False:
        Generate_Defaults()        
    sys.exit(Main())
