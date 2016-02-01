__author__ = "William Read"
__revision__ = "01/02/2016"

from tkinter.ttk import *
from tkinter import *

import sys
    
class Window:

    def __init__(self,parent):
        '''Sets basis of Tkinter Window.'''
        self.parent = parent # Stores Tk as self, so attributes can be chaged across classes.
        self.parent.title("PIXEL TD") # Edits the title of the main window.
        self.parent.wm_iconbitmap("./images/logo.ico") # Changes the icon of Tkinter window (removes feather).
        self.parent.geometry("%dx%d" % (900,600)) # Sets resolution to tuple.
        self.parent.resizable(0,0) # Prevents window from resizing.


    def close(self):
        '''Closes the main window when user wants to close the program.'''
        sys.exit() # Closes window.

class Main(Window): # Inherits class Window.
    '''Inherits the attributes and method of "Window".'''

    def __init__(self,parent):
        '''Widgets for home menu, allows user to play, edit future games or quit.'''
        Window.__init__(self,parent) # Inherits attributes and methods from class Window.

        self.frame = Frame(self.parent) # Generates a frame to store widgets.
        self.frame.pack()

        # --- Widgets for Main interface. --- #
        self.label = Label(self.frame, text="PIXEL TD", font=("Fixedsys",36))
        self.label.pack(pady=100)

        self.game = Button(self.frame, text="Play", font=("Fixedsys",18),bg="green",
                           command=lambda: Game_Window(self.parent,self.frame))
        self.game.pack(pady=10, fill=X)

        self.options = Button(self.frame, text="Options", font=("Fixedsys",18),bg="sky blue",
                              command=lambda: Options(self.parent,self.frame))
        self.options.pack(pady=10, fill=X)

        self.quit = Button(self.frame, text="Quit", font=("Fixedsys",18),bg="red",
                           command=self.close)
        self.quit.pack(pady=10, fill=X)
        

class Options(Window): # Inherits class Window.
    '''Inherits the attributes and method of "Window".'''

    def __init__(self,parent,main):
        '''Displays the widgets of the Options menu.'''
        Window.__init__(self,parent) # Inherets the attributes and methods from class Window.
        
        self.main = main # Remebers frame binded to class so that it can be later restored.
        self.main.pack_forget() # Forgets the main_frame. (Doesn't delete just hides it.)

        self.parent.bind("<Escape>",self.main_menu) # Binds the Escape key on the parent window to method main_menu.

        self.map = StringVar(self.parent)
        self.map.set("test1")
        
        # --- Widgets for Options interface. --- #
        self.frame01 = Frame(self.parent,bg="#666666")
        self.frame01.pack(fill=BOTH)

        self.frame02 = Frame(self.parent,bg="#666666")
        self.frame02.pack(fill=BOTH)

        self.difficulty = Label(self.frame01, text="Difficulty: ",font=("Fixedsys",18),bg="#666666",fg="white")
        self.difficulty.pack(side=LEFT, padx=10,pady=5)

        self.easy = Button(self.frame01, text="EASY", font=("Fixedsys",18),bg="green")
        self.easy.pack(side=LEFT,fill=X,padx=5,pady=5)

        self.normal = Button(self.frame01, text="NORMAL", font=("Fixedsys",18),bg="yellow")
        self.normal.pack(side=LEFT,fill=X,padx=5,pady=5)

        self.hard = Button(self.frame01, text="HARD", font=("Fixedsys",18),bg="red")
        self.hard.pack(side=LEFT,fill=X,padx=5,pady=5)

        self.maps = Label(self.frame02, text="Map: ",font=("Fixedsys",18),bg="#666666",fg="white")
        self.maps.pack(side=LEFT,fill=X,padx=10)

        self.map_selection = OptionMenu(self.frame02,self.map,"test1","test2","test3","test4")
        self.map_selection.pack(side=LEFT,fill=X,padx=10)

        self.submit = Button(self.frame02,text="Submit",font=("Fixedsys",18),
                             command=self.submitted)
        self.submit.pack(side=LEFT,fill=X,padx=10)

    def submitted(self):
        print(self.map.get())

    def main_menu(self, event=None):
        '''Returns the user to the main menu.'''
        self.parent.unbind("<Escape>") # Removes the event binded to Escape key on parent window.
        self.frame.destroy() # Deletes Frame, and all widgets belonging to it.
        self.main.pack() # Restores hidden window.

class Game_Window(Window): # Inherits class Window.
    '''Inherits the attributes and method of "Window".'''

    def __init__(self,parent,main):
        '''Displays all the widgets for the main Tower Defence Game.'''
        Window.__init__(self,parent) # Inherets the attributes and methods from class Window
        
        self.main = main # Remebers frame binded to class so that it can be later restored.
        self.main.pack_forget() # Forgets the main_frame. (Doesn't delete just hides it.)

        self.parent.bind("<Escape>",self.main_menu)

        # --- Widgets for Options interface. --- #
        self.main_frame = Frame(self.parent) # Stores the frames, frame and display.
        self.main_frame.pack(fill=BOTH, expand=True)

        self.frame = Frame(self.main_frame,bg="#666666")
        self.frame.pack(fill=Y, side=RIGHT)

        self.display = Frame(self.main_frame,bg="#999999")
        self.display.pack(fill=BOTH,expand=True)

        self.canvas = Canvas(self.display, bg="green")
        self.canvas.pack(fill=BOTH,expand=True,padx=5,pady=5)

        self.display = Button(self.frame, text="Game Stats", font=("Fixedsys",18),
                              command=lambda: Game_Overlay())
        self.display.pack(padx=5,pady=5)

    def main_menu(self, event=None):
        '''Returns the user to the main menu.'''
        self.main_frame.destroy()
        self.parent.unbind("<Escape>")
        self.main.pack()

class Game_Overlay:
    '''Inherits the attributes and method of "Window".'''
    __instance = 0

    def __init__(self):
        '''Displays toplevel widget displaying user scores.'''
        if Game_Overlay.__instance > 0: # Prevents more than one overlay opening at anytime.
            pass
        else:
            Game_Overlay.__instance += 1 # Increments private attribute __instance.
            self.overlay = Toplevel()
            self.overlay.geometry("500x300")
            self.overlay.protocol("WM_DELETE_WINDOW",self.instance)

            self.table = ttk.Treeview(self.overlay) # Grid Styled widget to display data.
            self.table.pack()

    def instance(self, event=None):
        Game_Overlay.__instance -= 1 # Decrements private attribute __instance.
        self.overlay.destroy()

if __name__ == "__main__":
    # --- Tests above code if run --- #
    # - WARNING: May crash if intergrated as hosted from boot folder. Only Test Code below. - #
    root = Tk()
    Main(root)
    root.mainloop()
