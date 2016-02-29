__author__ = "Tom Starling, William Read"
__revision__ = "17/02/2016"
__version__ = "1.0"

from tkinter import *
from tkinter.ttk import *

from modules import sort_algorithms
from modules import search_algorithms

import random

class Grid:
    def __init__(self,canvas01,canvas02,n_barricades):
        self.canvas01 = canvas01
        self.canvas02 = canvas02
        self.n_barricades = n_barricades

        self.main_grid = self.generate_grid(self.canvas01,100,100,31,31,22,19,"",True)
        self.sort_grid = self.generate_grid(self.canvas02,300,300,200,72,1,5,"black",False)

        self.canvas01.itemconfig(self.main_grid[(0,0)],fill="red")
        self.canvas01.itemconfig(self.main_grid[(18,21)],fill="blue")

        self.canvas02.itemconfig(self.sort_grid[(0,0)],fill="blue")
        self.canvas02.itemconfig(self.sort_grid[(1,0)],fill="red")
        self.canvas02.itemconfig(self.sort_grid[(2,0)],fill="red")
        self.canvas02.itemconfig(self.sort_grid[(3,0)],fill="blue")

    #Create Grid on Main Display
    def generate_grid(self,canvas,rows,columns,cellwidth,cellheight,n_columns,n_rows,borders,add_event):
        self.rect = {}
        for column in range(n_columns):
            for row in range(n_rows):
                x1 = column*cellwidth
                y1 = row * cellheight
                x2 = x1 + cellwidth
                y2 = y1 + cellheight
                self.rect[(row,column)] = canvas.create_rectangle(x1,y1,x2,y2,outline=borders,tags="self.rect")
                if add_event == True:
                    canvas.tag_bind(self.rect[(row,column)],"<ButtonPress-1>",lambda event, tile=(row,column): self.print_click(tile,event))

        if add_event == True:           
            for i in range(self.n_barricades):
                location_x = random.randint(0,18)
                location_y = random.randint(0,21)
                if canvas.itemcget(self.rect[(location_x,location_y)],"fill")=="red" or canvas.itemcget(self.rect[(location_x,location_y)],"fill")=="blue":
                    pass
                else:
                    canvas.itemconfig(self.rect[(location_x,location_y)],fill="brown")
                    canvas.update_idletasks()
        
        return self.rect

    def print_click(self,tile,event):
        last_barricade = (tile[0],tile[1])
        self.canvas01.itemconfig(self.main_grid[(tile[0],tile[1])],fill="brown")
        # Save last click into wave_settings.pixel - use to prevent None Error.
