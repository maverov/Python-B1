from tkinter import *
from tkinter.ttk import *

class Grid:
    def __init__(self,canvas):
        self.canvas = canvas

        self.rows = 100
        self.columns = 100
        self.cellwidth = 31
        self.cellheight = 31

        #Create grid
        self.rect = {}
        for column in range(22):
            for row in range(19):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, tags="rect")
