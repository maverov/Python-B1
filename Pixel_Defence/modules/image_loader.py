__author__ = "William Read"
__revision__ = "02/02/2016"
__version__ = "0.1"

from tkinter.ttk import *
from tkinter import *

class Images:

    def __init__(self):

        self.demo = []
        location = 0
        while True:
            try:
                self.demo.append(PhotoImage(file="./images/demo.gif",format="gif -index "+str(location)))
                location += 1
            except:
                break
            
        self.demo_frames = len(self.demo)
        
if __name__ == "__main__":
    Images()
