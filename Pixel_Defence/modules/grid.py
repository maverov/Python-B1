__author__ = "Tom Starling, William Read"
__revision__ = "08/02/2016"
__version__ = "1.0"

from tkinter import *
from tkinter.ttk import *

from modules import sort_algorithms

import random

class Grid:
    def __init__(self,canvas01,canvas02):
        self.canvas01 = canvas01
        self.canvas02 = canvas02

        self.main_grid = self.generate_grid(self.canvas01,100,100,31,31,22,19,"")
        self.sort_grid = self.generate_grid(self.canvas02,300,300,200,72,1,5,"black")

        self.canvas01.itemconfig(self.main_grid[(0,random.randint(0,21))],fill="red")
        self.canvas01.itemconfig(self.main_grid[(18,random.randint(0,21))],fill="blue")

        self.canvas02.itemconfig(self.sort_grid[(0,0)],fill="blue")
        self.canvas02.itemconfig(self.sort_grid[(1,0)],fill="red")
        self.canvas02.itemconfig(self.sort_grid[(2,0)],fill="red")
        self.canvas02.itemconfig(self.sort_grid[(3,0)],fill="blue")

    #Create Grid on Main Display
    def generate_grid(self,canvas,rows,columns,cellwidth,cellheight,n_columns,n_rows,borders):
        self.rect = {}
        for column in range(n_columns):
            for row in range(n_rows):
                x1 = column*cellwidth
                y1 = row * cellheight
                x2 = x1 + cellwidth
                y2 = y1 + cellheight
                self.rect[(row,column)] = canvas.create_rectangle(x1,y1,x2,y2,outline=borders,tags="self.rect")

        return self.rect

        
