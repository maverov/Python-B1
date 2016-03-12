from tkinter import *
from random import *



def jump(event):
    app.hello_b.place(relx=random(),rely=random())

class App:
    def __init__(self,master):
        frame = Frame(master)
        master.geometry("160x160")
        master.title("My first program!")
        frame.pack()

        self.hello_b = Button(master,text="Quit",command=sys.exit)
        self.hello_b.bind("<Enter>",jump)
        self.hello_b.pack()




root = Tk()

app = App(root)

root.mainloop()
