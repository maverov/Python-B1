__author__ = "William Read"
__revision__ = "01/02/2016"

from tkinter.ttk import *
from tkinter import *

import sys
    
class Window:

    def __init__(self,parent):
        '''Sets basis of Tkinter Window.'''
        self.parent = parent
        self.parent.title("PIXEL DEFENCE")
        self.parent.geometry("%dx%d" % (900,600))
        self.parent.resizable(0,0)

    def close(self):
        '''Closes the main window when user wants to close the program.'''
        sys.exit()

class Main(Window):
    '''Inherits the attributes and method of "Window".'''

    def __init__(self,parent):
        '''Widgets for home menu, allows user to play, edit future games or quit.'''
        Window.__init__(self,parent)

        self.frame = Frame(self.parent)
        self.frame.pack()

        self.label = Label(self.frame, text="PIXEL DEFENCE", font=("Ariel",24))
        self.label.pack(padx=5, pady=100)

        self.game = Button(self.frame, text="Play", font=("Ariel",18),
                           command=lambda: Game_Window(self.parent,self.frame))
        self.game.pack(padx=5, pady=10, fill=X)

        self.options = Button(self.frame, text="Options", font=("Ariel",18),
                              command=lambda: Options(self.parent,self.frame))
        self.options.pack(padx=5, pady=10, fill=X)

        self.quit = Button(self.frame, text="Quit", font=("Ariel",18),command=self.close)
        self.quit.pack(padx=5, pady=10, fill=X)
        

class Options(Window):
    '''Inherits the attributes and method of "Window".'''

    def __init__(self,parent,main):
        '''Displays the widgets of the Options menu.'''
        Window.__init__(self,parent)
        
        self.main = main
        self.main.pack_forget()

        self.parent.bind("<Escape>",self.main_menu)

        self.frame = Frame(self.parent,bg="#666666")
        self.frame.pack(fill=BOTH)

    def main_menu(self, event=None):
        '''Returns the user to the main menu.'''
        self.parent.unbind("<Escape>")
        self.frame.destroy()
        self.main.pack()

class Game_Window(Window):
    '''Inherits the attributes and method of "Window".'''

    def __init__(self,parent,main):
        '''Displays all the widgets for the main Tower Defence Game.'''
        Window.__init__(self,parent)
        
        self.main = main
        self.main.pack_forget()

        self.parent.bind("<Escape>",self.main_menu)

        self.main_frame = Frame(self.parent)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.frame = Frame(self.main_frame,bg="#666666")
        self.frame.pack(fill=Y, side=RIGHT)

        self.display = Frame(self.main_frame,bg="#999999")
        self.display.pack(fill=BOTH,expand=True)

        self.canvas = Canvas(self.display, bg="green")
        self.canvas.pack(fill=BOTH,expand=True,padx=5,pady=5)

        self.display = Button(self.frame, text="Game Stats", font=("Ariel",14),
                              command=lambda: Game_Overlay())
        self.display.pack(padx=5,pady=5)

    def main_menu(self, event=None):
        '''Returns the user to the main menu.'''
        self.main_frame.destroy()
        self.parent.unbind("<Escape>")
        self.main.pack()

class Game_Overlay:
    '''Inherits the attributes and method of "Window".'''

    def __init__(self):
        '''Displays toplevel widget displaying user scores.'''
        self.overlay = Toplevel()
        self.overlay.geometry("500x300")
        pass

if __name__ == "__main__":
    root = Tk()
    Main(root)
    root.mainloop()
