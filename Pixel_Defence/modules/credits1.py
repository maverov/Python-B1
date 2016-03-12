###############################################################################
# Hristiyan Maverov's Individual Feature
# Interactive Credits Program


import sys
from tkinter import *
from tkinter import messagebox
import webbrowser




class GameCredits:
    def __init__(self):

        
        #Main Window
        master = Tk()
        self.master=master
        self.master.geometry("800x600")
        self.master["bg"] = "#00A3A7"
        self.master.wm_iconbitmap("Icon.ico")

        #File Menu
        menu = Menu(self.master)
        self.master.config(menu=menu)
        subMenu = Menu(menu)


        
        menu.add_cascade(label="Info", menu=subMenu)
        subMenu.add_command(label="About", command=self.menuOptions)
        subMenu.add_command(label="Visit my website!", command=self.hristiyanWeb)
        subMenu.add_command(label="Sound effects", command=self.soundCredits)
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=master.destroy)

        #Edit Menu
        editMenu = Menu(menu)
        menu.add_cascade(label="Click here!", menu=editMenu)
        editMenu.add_command(label="Easter Egg", command=self.easterEgg)
        
        self.master = master
        master.title("PixelTD - Credits")
        self.banner = PhotoImage(file="pixelbanner.gif")
        self.creditsBanner = Label(self.master, image=self.banner, borderwidth="0")
        self.creditsBanner.pack()
        self.label = Label(self.master, text="Game Credits", fg="#00A3A7", font="Helvetica, 22")
        self.label.pack(padx=10, pady=10)


        self.button1 = Button(self.master, text="Hristiyan Maverov", fg="#999900", command=self.credits1)
        self.button1.pack(padx=2, pady=2)
        self.button1.bind("<Button-1>", self.hristiyanWeb)
        
        self.button2 = Button(self.master, text="William Read", fg="red", command=self.credits3)
        self.button2.pack(padx=2, pady=2)
        self.button2.bind("<Button-1>", self.williamWeb)
        
        self.button3 = Button(self.master, text="Cristian Ghita", fg="green", command=self.credits2)
        self.button3.pack(padx=2, pady=2)
        self.button3.bind("<Button-1>", self.cristianWeb)
        
        self.button4 = Button(self.master, text="Thomas Starling", fg="blue", command=self.credits4)
        self.button4.pack(padx=2, pady=2)
        self.button4.bind("<Button-1>", self.thomasWeb)
        
        self.close_button = Button(self.master, text="Close", command=master.destroy)
        self.close_button.place(x=10, y=10)

        # ***** Status Bar *****
        self.statusBar = Label(self.master,text="Hristiyan Maverov's Individual Game Feature (Interactive Credits)", bd=1, relief=SUNKEN, anchor=W)
        self.statusBar.pack(side=BOTTOM, fill=X)

        self.master.mainloop()


    def credits1(self):
        self.label = Label(self.master, text="Hristiyan Maverov, 20, Interactive Credits Feature", font="Helvetica, 17", bg="#00A3A7")
        self.label.pack(padx=7, pady=7)
        self.label.after(4000, self.clear_label)
        
    def credits2(self):
        self.label = Label(self.master, text="Cristian Ghita, 19, Tutorial Feature, gcristian96.wordpress.com", font="Helvetica, 17", bg="#00A3A7")
        self.label.pack(padx=7, pady=7)
        self.label.after(4000, self.clear_label)

    def credits3(self):
        self.label = Label(self.master, text="William Read, 20, Screen Capture Feature, www.williamread.weebly.com", font="Helvetica, 17", bg="#00A3A7")
        self.label.pack(padx=7, pady=7)
        self.label.after(4000, self.clear_label)

    def credits4(self):
        self.label = Label(self.master, text="Thomas Starling, 19, Cheat Menu, thomas-starling.weebly.com", font="Helvetica, 17", bg="#00A3A7")
        self.label.pack(padx=7, pady=7)
        self.label.after(4000, self.clear_label)

#    def easterEgg(self):
#        webbrowser.open_new(r"file://easteregg.py")

    def clear_label(self):
        self.label.destroy()
        

    def menuOptions(self):
        messagebox.showinfo(title="What is this?", message="Welcome to the credits page for our Pixel Tower Defense game. This program is developer by Hristiyan Maverov as part of the CS ALL Project.")
        return

    def hristiyanWeb(self,event):
        webbrowser.open_new(r"http://www.google.com")

    def williamWeb(self,event):
        webbrowser.open_new(r"http://www.williamread.weebly.com")
        
    def thomasWeb(self,event):
        webbrowser.open_new(r"http://www.thomas-starling.weebly.com")

    def cristianWeb(self,event):
        webbrowser.open_new(r"http://www.gcristian96.wordpress.com")

    def soundCredits(self):
        messagebox.showinfo(title="Thanks to...", message="Special Thanks to Evan King for the use of his Royalty Free Music. Evan King Audio - https://www.youtube.com/user/EvanKingAudio")
        return

    def easterEgg(self,event):
        pass




GameCredits()



