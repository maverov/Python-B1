__author__ = "William Read"
__revision__ = "02/02/2016"
__version__ = "0.1"

from tkinter.ttk import *
from tkinter import *

from modules import image_loader

import sys,time,winsound,pickle,sqlite3
    
class Window:

    def __init__(self,parent):
        '''Sets basis of Tkinter Window.'''
        self.parent = parent # Stores Tk as self, so attributes can be chaged across classes.

        self.images = image_loader.Images()
        
        self.parent.title("PIXEL TD") # Edits the title of the main window.
        self.parent.protocol("WM_DELETE_WINDOW",self.close)
        self.parent.wm_iconbitmap("./images/logo.ico") # Changes the icon of Tkinter window (removes feather).
        self.parent.geometry("%dx%d" % (900,600)) # Sets resolution to tuple.
        self.parent.resizable(0,0) # Prevents window from resizing.

    def close(self):
        '''Closes the main window when user wants to close the program.'''
        winsound.PlaySound(None,winsound.SND_PURGE)
        sys.exit() # Closes window.

class Main(Window): # Inherits class Window.
    '''Inherits the attributes and method of "Window".'''
    __instance = 0

    def __init__(self,parent):
        '''Widgets for home menu, allows user to play, edit future games or quit.'''
        Window.__init__(self,parent) # Inherits attributes and methods from class Window.

        winsound.PlaySound(None,winsound.SND_PURGE) # Cancels all current sounds being played.
        winsound.PlaySound("./audio/bgm/jelly_castle_retro_remix.wav",winsound.SND_LOOP|winsound.SND_ASYNC) # Starts song in first parameter.

        self.frame = Frame(self.parent) # Generates a frame to store widgets.
        self.frame.pack()

        # --- Widgets for Main interface. --- #
##        current_background = self.images.demo[0]
##        self.background = Label(self.parent, image=current_background)
##        self.background.current_background = current_background
##        self.background.place(x=0,y=0)
        
        self.title_banner = Label(self.frame, text="PIXEL TD", font=("Fixedsys",36))
        self.title_banner.pack(pady=100)

        self.game = Button(self.frame, text="Play", font=("Fixedsys",18),bg="green",
                           command=lambda: Game_Window(self.parent,self.frame))
        self.game.pack(pady=10, fill=X)

        self.options = Button(self.frame, text="Options", font=("Fixedsys",18),bg="sky blue",
                              command=lambda: Options(self.parent,self.frame))
        self.options.pack(pady=10, fill=X)

        self.quit = Button(self.frame, text="Quit", font=("Fixedsys",18),bg="red",
                           command=self.close)
        self.quit.pack(pady=10, fill=X)

        self.info = Button(self.frame, bitmap="info", font=("Fixedsys",18),
                           command=self.game_credits)
        self.info.pack(pady=10, fill=X)

##    def home_animation(self):
##        while True:
##            for i in self.images.demo:
##                time.sleep(0.1)
##                current_background = i
##                self.background.config(image=current_background)
##                self.background.current_background = current_background
##                
##            current_background = self.images.demo[0]
##            self.background.config(image=current_background)
##            self.background.current_background = current_background

    def game_credits(self):
        '''Sets the credits for the game giving credit to online creator and resources we used.'''
        
        data = """
Special Thanks to Evan King for the use of his
Royalty Free Music.

Evan King Audio - https://www.youtube.com/user/EvanKingAudio
"""
        if Main.__instance > 0:
            pass
        else:
            Main.__instance += 1
            self.toplevel = Toplevel()
            self.toplevel.title("CREDITS")
            self.toplevel.wm_iconbitmap("./images/logo.ico")
            self.toplevel.protocol("WM_DELETE_WINDOW", self.remove_level)
            
            self.label = Label(self.toplevel, text=data, font=("Fixedsys",14))
            self.label.pack()

    def remove_level(self):
        '''Makes sure only one instance of the Credits window is open at anytime.'''
        Main.__instance -= 1
        self.toplevel.destroy()

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
        self.main_frame = Frame(self.parent,bg="#666666")
        self.main_frame.pack(side=LEFT,fill=BOTH,expand=True)
    
        self.frame01 = Frame(self.main_frame,bg="#666666")
        self.frame01.pack(fill=BOTH,pady=10)

        self.frame02 = Frame(self.main_frame,bg="#666666")
        self.frame02.pack(fill=BOTH,pady=10)

        self.frame03 = Frame(self.main_frame,bg="#666666")
        self.frame03.pack(fill=BOTH,pady=10)

        self.frame04 = Frame(self.main_frame,bg="#666666")
        self.frame04.pack(side=BOTTOM,fill=BOTH,pady=10)

        self.difficulty = Label(self.frame01, text="Difficulty: ",font=("Fixedsys",18),bg="#666666",fg="white")
        self.difficulty.pack(side=LEFT, padx=10,pady=5)

        self.easy = Button(self.frame01, text="EASY", font=("Fixedsys",18),bg="green")
        self.easy.pack(side=LEFT,fill=X,expand=True,padx=5,pady=5)

        self.normal = Button(self.frame01, text="NORMAL", font=("Fixedsys",18),bg="yellow")
        self.normal.pack(side=LEFT,fill=X,expand=True,padx=5,pady=5)

        self.hard = Button(self.frame01, text="HARD", font=("Fixedsys",18),bg="red")
        self.hard.pack(side=LEFT,fill=X,expand=True,padx=5,pady=5)

        self.maps = Label(self.frame02, text="Map: ",font=("Fixedsys",18),bg="#666666",fg="white")
        self.maps.pack(side=LEFT,fill=X,padx=10)

        self.map_selection = OptionMenu(self.frame02,self.map,"test1","test2","test3","test4")
        self.map_selection.pack(side=LEFT,fill=X,padx=10)
        
        self.map_selection.config(font=("Fixedsys",18))
        self.map_selection.nametowidget(self.map_selection.menuname).config(font=("Fixedsys",18))

        self.audio = Label(self.frame03, text="Audio: ",font=("Fixedsys",18),bg="#666666",fg="white")
        self.audio.pack(side=LEFT,fill=X,padx=10)

        self.audio_scale = Scale(self.frame03,from_=0,to=100,orient=HORIZONTAL,font=("Fixedsys",18),
                                 bg="#666666",fg="white")
        self.audio_scale.pack(side=LEFT,fill=X,expand=True,padx=10)

        self.submit = Button(self.frame04,text="Submit",font=("Fixedsys",18),
                             command=self.submitted)
        self.submit.pack(side=LEFT,fill=X,padx=10)

    def submitted(self):
        print(self.map.get())
        self.main_menu()

    def main_menu(self, event=None):
        '''Returns the user to the main menu.'''
        self.parent.unbind("<Escape>") # Removes the event binded to Escape key on parent window.
        self.main_frame.destroy() # Deletes Frame, and all widgets belonging to it.
        self.main.pack() # Restores hidden window.

class Game_Window(Window): # Inherits class Window.
    '''Inherits the attributes and method of "Window".'''

    def __init__(self,parent,main):
        '''Displays all the widgets for the main Tower Defence Game.'''
        Window.__init__(self,parent) # Inherets the attributes and methods from class Window

        winsound.PlaySound(None,winsound.SND_PURGE) # Cancels all music currently playing.
        winsound.PlaySound("./audio/bgm/biscuits.wav",winsound.SND_LOOP|winsound.SND_ASYNC)# Plays song in first parameter.
        
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

        # --- Canvas Display Options Below. --- #
        pass
        

    def main_menu(self, event=None):
        '''Returns the user to the main menu.'''
        winsound.PlaySound(None,winsound.SND_PURGE)# Cancels all music currently playing.
        winsound.PlaySound("./audio/bgm/jelly_castle_retro_remix.wav",winsound.SND_LOOP|winsound.SND_ASYNC)# Plays song in first parameter.
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
            self.overlay.wm_iconbitmap("./images/logo.ico")
            self.overlay.protocol("WM_DELETE_WINDOW",self.instance) # Sets event to when window is being closed.

            self.scrollbar = Scrollbar(self.overlay) # Set scrollbar of the widget.
            self.scrollbar.pack(side=RIGHT,fill=Y)
            
            self.table = Treeview(self.overlay,yscrollcommand=self.scrollbar.set)# Grid Styled widget to display data.
            self.table["show"] = "headings" # Hides column '0'
            self.table["columns"] = ("first","second","third") # Tags the columns in the table.

            self.table.column("first",width=150,minwidth=50) # Sets min stretch of the tables in the widget.
            self.table.column("second",width=150,minwidth=50)
            self.table.column("third",width=150,minwidth=50)

            self.table.heading("first",text="Round") # Set names of widgets in the table
            self.table.heading("second",text="Money")
            self.table.heading("third",text="Health")

            self.table.tag_configure("ttk")
            
            self.table.pack(expand=True) # Force to fill space.

            Style().configure("Treeview",font=("Fixedsys",14)) # Styles the overview treeview table.
            Style().configure("Treeview.Heading",font=("Fixedsys",18))

            self.scrollbar.config(command=self.table.yview) # Sets scollbar to treeview table.

    def instance(self, event=None):
        Game_Overlay.__instance -= 1 # Decrements private attribute __instance.
        self.overlay.destroy()

if __name__ == "__main__":
    # --- Tests above code if run --- #
    # - WARNING: The code below won't run as it is designed for security - #
    pass
##    root = Tk()
##    Main(root)
##    root.mainloop()
