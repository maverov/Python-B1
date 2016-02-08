import time

class BubbleSort:

    def __init__(self,canvas,sort_grid):
        self.canvas = canvas
        self.sort_grid = sort_grid
        
        colour_list = []
        for i in range(5):
            fill_colour = canvas.itemcget(sort_grid[(i,0)],"fill")
            if fill_colour == "red":
                colour_list.append(1)
            elif fill_colour == "blue":
                colour_list.append(2)
            else:
                colour_list.append(0)

        for i in range(0,len(colour_list)):
            for j in range(0, len(colour_list)-1):
                if colour_list[j]>colour_list[j+1]:
                    x = colour_list[j]
                    colour_list[j]=colour_list[j+1]
                    colour_list[j+1]=x

                self.fill_square(colour_list[j],j)
                self.fill_square(colour_list[j+1],j+1)
                self.canvas.update_idletasks()
                time.sleep(0.1)

    def fill_square(self,colour,j):
        if colour == 1:
            self.canvas.itemconfig(self.sort_grid[(j,0)],fill="red")
        elif colour == 2:
            self.canvas.itemconfig(self.sort_grid[(j,0)],fill="blue")
        else:
            self.canvas.itemconfig(self.sort_grid[(j,0)],fill="")

class QuickSort:

    def __init__(self):
        print("TEST")
