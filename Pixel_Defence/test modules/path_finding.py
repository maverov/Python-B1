################################################################################
#
# path_finding
# Thomas Starling
# 
################################################################################
import tkinter as tk
import random

class path_finding(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        #Create canvas
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=600, height=600, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 100
        self.columns = 100
        self.cellwidth = 30
        self.cellheight = 30

        #Create grid
        self.rect = {}
        for column in range(20):
            for row in range(20):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="white", tags="rect")

        start = self.canvas.create_rectangle(0, 0, 90, 100, fill="red")
        finish = self.canvas.create_rectangle(100, 200, 90, 100, fill="green")
        
        #Create map variables
        START_COLOUR = "red"
        FINISH_COLOUR = "green"
        BARACADE_COLOUR = "brown"
        
    def path_finder(self):
        #Create sets
        openList = []
        closedList = []
        path = []

        #Finish Off Code HERE

if __name__ == "__main__":
    root = path_finding()
    root.mainloop()
