from tkinter.ttk import *
from tkinter import *
import sys

from modules import *

class App:

    def __init__(self):
        root = Tk()
        gui_display.Main(root)
        root.mainloop()


if __name__ == "__main__":
    sys.exit(App())
