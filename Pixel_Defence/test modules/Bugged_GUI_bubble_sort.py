import sys
import time
from tkinter import *

class Gui:
    def __init__(self,root):
        
        self.root = root

        self.sort_list = []

        #blue = 3 , red = 1, green = 2

        self.x = 0
        self.x2 = 50
        
        self.place = Canvas(root, width=300,height=60, bg="white")
        self.place.pack()

        self.button2 = Button(self.root, text='Blue', command=lambda a=3 : self.add_blue(a))
        self.button2.pack(side=LEFT)
        self.button3 = Button(self.root, text='Red', command=lambda a=1 : self.add_red(a))
        self.button3.pack(side=LEFT)
        self.button4 = Button(self.root,text='Green', command=lambda a=2 : self.add_green(a))
        self.button4.pack(side=LEFT)
        
        self.button = Button(self.root, text='Sort', command=lambda : self.BubbleSort(self.sort_list))
        self.button.pack()
        self.place.pack()
        
    def add_blue(self, val):
        self.place.create_rectangle(self.x,0,self.x2,50, fill="blue")
        self.place.pack()
        self.x += 60
        self.x2 += 60
        self.sort_list.append(val)

    def add_red(self, val):
        self.red = self.place.create_rectangle(self.x,0,self.x2,50, fill="red")
        self.place.pack()
        self.x += 60
        self.x2 += 60
        self.sort_list.append(val)

    def add_green(self, val):
        self.green = self.place.create_rectangle(self.x,0,self.x2,50, fill="green")
        self.place.pack()
        self.x += 60
        self.x2 += 60
        self.sort_list.append(val)

##    def sort(self, val):
##        print(self.sort_list)
##        self.BubbleSort(self.sort_list)

    def BubbleSort(self, mylist):
        print(mylist)
        for i in range(0,len(mylist)):
            for j in range(0, len(mylist)-1):
                if mylist[j]>mylist[j+1]:
                    x = mylist[j]
                    mylist[j]=mylist[j+1]
                    mylist[j+1]=x

                    print(mylist)

                    sort_x = j*60
                    sort_x1 = 50+j*60

                    sort_x01 = (j+1)*60
                    sort_x02 = 50+((j+1)*60)
                    
                    if mylist[j] == 1:
                        self.red = self.place.create_rectangle(sort_x,0,sort_x1,0, fill='red')
                    elif mylist[j] == 2:
                        self.green = self.place.create_rectangle(sort_x, 0, sort_x1, fill='green')
                    elif mylist[j] == 3:
                        self.blue = self.place.create_rectangle(sort_x, 0, sort_x1, fill='blue')

                    if mylist[j+1] == 1:
                        self.red = self.place.create_rectangle(sort_x01,0,sort_x02,0, fill='red')
                    elif mylist[j+1] == 2:
                        self.green = self.place.create_rectangle(sort_x01, 0, sort_x02, fill='green')
                    elif mylist[j+1] == 3:
                        self.blue = self.place.create_rectangle(sort_x01, 0, sort_x02, fill='blue')

                    self.place.pack()
                    time.sleep(2)
                    
        print(mylist)
        print('Done sorting')


def main():
    root = Tk()
    gui = Gui(root)
    root.mainloop()

if __name__ == '__main__':
    sys.exit(main())
