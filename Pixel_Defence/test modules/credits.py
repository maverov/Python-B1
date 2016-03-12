###############################################################################
# Hristiyan Maverov's Individual Feature
# Interactive Credits Program


import sys
from tkinter import *
from tkinter import messagebox
import webbrowser
from pygame import mixer



def menuOptions():
    messagebox.showinfo(title="What is this?", message="Welcome to the credits page for our Pixel Tower Defense game. This program is developer by Hristiyan Maverov as part of the CS ALL Project.")
    return

def hristiyanWeb(event):
    webbrowser.open_new(r"http://www.google.com")

def williamWeb(event):
    webbrowser.open_new(r"http://www.williamread.weebly.com")
    
def thomasWeb(event):
    webbrowser.open_new(r"http://www.thomas-starling.weebly.com")

def cristianWeb(event):
    webbrowser.open_new(r"http://www.gcristian96.wordpress.com")

def soundCredits():
    messagebox.showinfo(title="Thanks to...", message="Special Thanks to Evan King for the use of his Royalty Free Music. Evan King Audio - https://www.youtube.com/user/EvanKingAudio")
    return

def easterEgg(event):
    pass

class GameCredits:
    def __init__(self, master):
        
        self.master = master
        master.title("PixelTD - Credits")
        self.banner = PhotoImage(file="pixelbanner.gif")
        self.creditsBanner = Label(root, image=self.banner, borderwidth="0")
        self.creditsBanner.pack()
        self.label = Label(master, text="Game Credits", fg="#00A3A7", font="Helvetica, 22")
        self.label.pack(padx=10, pady=10)


        self.button1 = Button(master, text="Hristiyan Maverov", fg="#999900", command=self.credits1)
        self.button1.pack(padx=2, pady=2)
        self.button1.bind("<Button-1>", hristiyanWeb)
        
        self.button2 = Button(master, text="William Read", fg="red", command=self.credits3)
        self.button2.pack(padx=2, pady=2)
        self.button2.bind("<Button-1>", williamWeb)
        
        self.button3 = Button(master, text="Cristian Ghita", fg="green", command=self.credits2)
        self.button3.pack(padx=2, pady=2)
        self.button3.bind("<Button-1>", cristianWeb)
        
        self.button4 = Button(master, text="Thomas Starling", fg="blue", command=self.credits4)
        self.button4.pack(padx=2, pady=2)
        self.button4.bind("<Button-1>", thomasWeb)
        
        self.close_button = Button(master, text="Close", command=root.destroy)
        self.close_button.place(x=10, y=10)

        # ***** Status Bar *****
        self.statusBar = Label(root,text="Hristiyan Maverov's Individual Game Feature (Interactive Credits)", bd=1, relief=SUNKEN, anchor=W)
        self.statusBar.pack(side=BOTTOM, fill=X)

    def credits1(self):
        self.label = Label(root, text="Hristiyan Maverov, 20, Interactive Credits Feature", font="Helvetica, 17", bg="#00A3A7")
        self.label.pack(padx=7, pady=7)
        self.label.after(4000, self.clear_label)
        
    def credits2(self):
        self.label = Label(root, text="Cristian Ghita, 19, Tutorial Feature, gcristian96.wordpress.com", font="Helvetica, 17", bg="#00A3A7")
        self.label.pack(padx=7, pady=7)
        self.label.after(4000, self.clear_label)

    def credits3(self):
        self.label = Label(root, text="William Read, 20, Screen Capture Feature, www.williamread.weebly.com", font="Helvetica, 17", bg="#00A3A7")
        self.label.pack(padx=7, pady=7)
        self.label.after(4000, self.clear_label)

    def credits4(self):
        self.label = Label(root, text="Thomas Starling, 19, Cheat Menu, thomas-starling.weebly.com", font="Helvetica, 17", bg="#00A3A7")
        self.label.pack(padx=7, pady=7)
        self.label.after(4000, self.clear_label)

#    def easterEgg(self):
#        webbrowser.open_new(r"file://easteregg.py")

    def clear_label(self):
        self.label.destroy()


#Main Window
root = Tk()
root.geometry("800x600")
root["bg"] = "#00A3A7"
root.wm_iconbitmap("Icon.ico")
my_gui = GameCredits(root)

#File Menu
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="Info", menu=subMenu)
subMenu.add_command(label="About", command=menuOptions)
subMenu.add_command(label="Visit my website!", command=hristiyanWeb)
subMenu.add_command(label="Sound effects", command=soundCredits)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)

#Edit Menu
editMenu = Menu(menu)
menu.add_cascade(label="Click here!", menu=editMenu)
editMenu.add_command(label="Easter Egg", command=easterEgg)

#Audio
mixer.init()
mixer.music.load('jelly_castle_retro_remix.wav')
mixer.music.play()

root.mainloop()

