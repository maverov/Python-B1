__author__ = "William Read"
__revision__ = "01/02/2016"

from tkinter.ttk import *
from tkinter import *
import sys

from modules import * # Imports all modules in the modules folder.

class App:
    '''Run this program to start the Game.
Security against user opening files unwantedly'''

    def __init__(self):
        root = Tk()
        gui_display.Main(root) # Runs the class in the module
        root.mainloop() # Keeps program in mainloop (callback).


if __name__ == "__main__":
    sys.exit(App()) # Makes sure Application safely closes.
