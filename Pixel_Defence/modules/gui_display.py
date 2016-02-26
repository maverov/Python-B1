__author__ = "William Read"
__revision__ = "02/02/2016"
__version__ = "0.1"

from tkinter.ttk import *
from tkinter import *

from PIL import Image, ImageTk, ImageGrab

from modules import image_loader,grid,sort_algorithms,search_algorithms

import os,sys,time,pickle,pygame,threading

pygame.init()
button_accept = pygame.mixer.Sound("./audio/bgs/menu_confirm_1_dry.wav")
button_deny = pygame.mixer.Sound("./audio/bgs/menu_deny_1_dry.wav")

class Window:

    def __init__(self,parent):
        '''Sets basis of Tkinter Window.'''
        self.parent = parent # Stores Tk as self, so attributes can be chaged across classes.
        
        self.size = (900,600)
        self.x = (self.parent.winfo_screenwidth()//2)-(900//2)
        self.y = (self.parent.winfo_screenheight()//2)-(600//2)
        
        self.parent.title("PIXEL TD") # Edits the title of the main window.
        self.parent.configure(background="#666666")
        self.parent.protocol("WM_DELETE_WINDOW",self.close)
        self.parent.wm_iconbitmap("./images/logo.ico") # Changes the icon of Tkinter window (removes feather).
        self.parent.geometry("%dx%d+%d+%d" % (self.size[0],self.size[1],self.x,self.y)) # Sets resolution to tuple.
        self.parent.resizable(0,0) # Prevents window from resizing.
        self.current_settings = pickle.load(open("./modules/settings.pixel","rb"))
    
    def imageList(self):
        self.images = image_loader.Images()
        
    def close(self):
        '''Closes the main window when user wants to close the program.'''
        pygame.mixer.Sound.play(button_deny)
        time.sleep(1)
        pygame.mixer.music.stop()
        sys.exit() # Closes window.

class Main(Window): # Inherits class Window.
    '''Inherits the attributes and method of "Window".'''
    __instance = 0

    def __init__(self,parent):
        '''Widgets for home menu, allows user to play, edit future games or quit.'''
        Window.__init__(self,parent) # Inherits attributes and methods from class Window.

        self.imageList()

        pygame.mixer.music.load("./audio/bgm/jelly_castle_retro_remix.wav")# Starts song in first parameter.
        pygame.mixer.music.set_volume(self.current_settings[2]/100)
        pygame.mixer.music.play(-1)

        self.frame = Frame(self.parent,bg="#666666") # Generates a frame to store widgets.
        self.frame.pack()

        # --- Widgets for Main interface. --- #
        self.title_banner_image = Image.open("./images/misc/logo.jpg")
        self.title_banner_image = self.title_banner_image.resize((600,300),Image.ANTIALIAS)
        self.title_banner_image  = ImageTk.PhotoImage(self.title_banner_image)
        
        self.title_banner = Label(self.frame, image=self.title_banner_image, font=("Fixedsys",36),
                                  bg="#666666",fg="white")
        self.title_banner.pack(pady=10)

        self.game = Button(self.frame, text="Play", font=("Fixedsys",18),bg="green",#relief=FLAT,
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


    def game_credits(self):
        '''Sets the credits for the game giving credit to online creator and resources we used.'''
        pygame.mixer.Sound.play(button_accept)
        
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
        pygame.mixer.Sound.play(button_deny)
        Main.__instance -= 1
        self.toplevel.destroy()

class Options(Window): # Inherits class Window.
    '''Inherits the attributes and method of "Window".'''

    def __init__(self,parent,main):
        '''Displays the widgets of the Options menu.'''
        pygame.mixer.Sound.play(button_accept)
        
        Window.__init__(self,parent) # Inherets the attributes and methods from class Window.
        
        self.main = main # Remebers frame binded to class so that it can be later restored.
        self.main.pack_forget() # Forgets the main_frame. (Doesn't delete just hides it.)

        self.parent.bind("<Escape>",self.main_menu) # Binds the Escape key on the parent window to method main_menu.

        self._map = StringVar(self.parent)
        find_maps = self.find_files("./images/maps")
        self._map.set(self.current_settings[0])
        
        # --- Widgets for Options interface. --- #
        self.main_frame = Frame(self.parent,bg="#666666")
        self.main_frame.pack(side=LEFT,fill=BOTH,expand=True)
    
        self.frame01 = Frame(self.main_frame,bg="#666666")
        self.frame01.pack(fill=BOTH,pady=30)

        self.frame02 = Frame(self.main_frame,bg="#666666")
        self.frame02.pack(fill=BOTH,pady=30)

        self.frame03 = Frame(self.main_frame,bg="#666666")
        self.frame03.pack(fill=BOTH,pady=30)

        self.frame04 = Frame(self.main_frame,bg="#666666")
        self.frame04.pack(fill=BOTH,pady=30)
        
        self.frame05 = Frame(self.main_frame,bg="#666666")
        self.frame05.pack(side=BOTTOM,fill=BOTH,pady=10)

        self.difficulty = Label(self.frame01, text="Difficulty: ",font=("Fixedsys",18),bg="#666666",fg="white")
        self.difficulty.pack(side=LEFT, padx=10,pady=5)

        self.easy = Button(self.frame01, text="EASY", font=("Fixedsys",18),bg="green",
                           command=lambda: self.setting_difficulty("easy"))
        self.easy.pack(side=LEFT,fill=X,expand=True,padx=5,pady=5)

        self.normal = Button(self.frame01, text="NORMAL", font=("Fixedsys",18),bg="yellow",
                             command=lambda: self.setting_difficulty("normal"))
        self.normal.pack(side=LEFT,fill=X,expand=True,padx=5,pady=5)

        self.hard = Button(self.frame01, text="HARD", font=("Fixedsys",18),bg="red",
                           command=lambda: self.setting_difficulty("hard"))
        self.hard.pack(side=LEFT,fill=X,expand=True,padx=5,pady=5)

        self.maps = Label(self.frame02, text="Map: ",font=("Fixedsys",18),bg="#666666",fg="white")
        self.maps.pack(side=LEFT,fill=X,padx=10)        

        self.map_selection = OptionMenu(self.frame02,self._map,*find_maps)
        self.map_selection.pack(side=LEFT,fill=X,expand=True,padx=10)
        
        self.map_selection.config(font=("Fixedsys",18))
        self.map_selection.nametowidget(self.map_selection.menuname).config(font=("Fixedsys",18))

        self.audio = Label(self.frame03, text="Audio: ",font=("Fixedsys",18),bg="#666666",fg="white")
        self.audio.pack(side=LEFT,fill=X,padx=10)

        self.audio_scale = Scale(self.frame03,from_=0,to=100,orient=HORIZONTAL,font=("Fixedsys",18),
                                 bg="#666666",fg="white")
        self.audio_scale.pack(side=LEFT,fill=X,expand=True,padx=10)
        self.audio_scale.set(self.current_settings[2])

        self.submit = Button(self.frame05,text="Submit",font=("Fixedsys",18),
                             command=self.submitted)
        self.submit.pack(side=LEFT,fill=X,expand=True,padx=10)

        self.submit = Button(self.frame05,text="Cancel",font=("Fixedsys",18),
                             command=self.cancel)
        self.submit.pack(side=LEFT,fill=X,expand=True,padx=10)

        self.setting_difficulty(self.current_settings[1])

        ## Thomas Starling Addition Start
        self.cheat_option = IntVar()
        self.cheat_option.set(0)
        self.maps = Label(self.frame04, text="Cheats: ",font=("Fixedsys",18),bg="#666666",fg="white")
        self.maps.pack(side=LEFT,fill=X,padx=10)
        
        self.cheat_button = Checkbutton(self.frame04, text="Activate", font=("Fixedsys",18),bg="#666666",fg="red", variable=self.cheat_option)
        self.cheat_button.pack(side=LEFT,fill=X,padx=10)
        ## End

    def find_files(self,directory):
        files = []
        for file in os.listdir(directory):
            if file.endswith(".png") or file.endswith(".gif") or file.endswith(".jpg"):
                files.append(file)
        return files

    def setting_difficulty(self,difficulty):
        self.difficulty = difficulty
        if difficulty == "easy":
            self.easy.config(bg="light green")
            self.normal.config(bg="yellow")
            self.hard.config(bg="red")

            self.n_barricades = 50
            
        elif difficulty == "normal":
            self.easy.config(bg="green")
            self.normal.config(bg="light goldenrod")
            self.hard.config(bg="red")

            self.n_barricades = 30
            
        else:
            self.easy.config(bg="green")
            self.normal.config(bg="yellow")
            self.hard.config(bg="tomato")

            self.n_barricades = 10

    def submitted(self):
        pygame.mixer.Sound.play(button_accept)
        setting_data = [self._map.get(),self.difficulty,self.audio_scale.get(),self.n_barricades, self.cheat_option.get()]
        pygame.mixer.music.set_volume(self.audio_scale.get()/100)
        settings_file = open("./modules/settings.pixel","wb")
        pickle.dump(setting_data,settings_file)
        self.main_menu()

    def cancel(self):
        pygame.mixer.Sound.play(button_deny)
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
        pygame.mixer.Sound.play(button_accept)

        for file in os.listdir("./images/game_waves"):
            os.remove("./images/game_waves/"+file)
        
        Window.__init__(self,parent) # Inherets the attributes and methods from class Window

        self.imageList()

        ## Cheat Statment
        ## Need to finish ##
        if self.cheat_option.get() == 0:
            self.health = 100
            self.money = 1000
            self.wave = 1
        else:
            self.health = 999999999
            self.money = 999999999
            self.wave = 1
        ## End

        pygame.mixer.music.stop() # Cancels all music currently playing.
        pygame.mixer.music.load("./audio/bgm/biscuits.wav")# Plays song in first parameter.
        pygame.mixer.music.set_volume(self.current_settings[2]/100)
        pygame.mixer.music.play(-1)
        
        self.main = main # Remebers frame binded to class so that it can be later restored.
        self.main.pack_forget() # Forgets the main_frame. (Doesn't delete just hides it.)

        self.parent.bind("<Escape>",self.main_menu)

        # --- Widgets for Options interface. --- #
        self.main_frame = Frame(self.parent) # Stores the frames, frame and display.
        self.main_frame.pack(fill=BOTH, expand=True)

        self.frame = Frame(self.main_frame,bg="#666666",relief=RIDGE)
        self.frame.pack(fill=Y, side=RIGHT)

        self.round_data = Frame(self.frame,bg="#666666",relief=RIDGE)
        self.round_data.pack(fill=BOTH)

        self.sort_data = Frame(self.frame,bg="#666666",relief=RIDGE)
        self.sort_data.pack(fill=BOTH)

        self.button_data = Frame(self.frame,bg="#666666",relief=RIDGE)
        self.button_data.pack(fill=BOTH)

        self.display = Frame(self.main_frame,bg="#999999")
        self.display.pack(fill=BOTH,expand=True)

        self.game_canvas = Canvas(self.display, bg="green")
        self.game_canvas.pack(fill=BOTH,expand=True,padx=5,pady=5)

        self.photo = Image.open("./images/maps/"+self.current_settings[0])
        self.photo = self.photo.resize((700,600),Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.photo)
        
        self.game_canvas.create_image(0,0,image=self.photo,anchor=NW)

        # -- Game_Option Frame -- #
        message_health = "Health: "+str(self.health)
        self.health_label = Label(self.round_data,text=message_health,font=("Fixedsys",14),
                                  bg="#666666",fg="white")
        self.health_label.pack(fill=X)

        message_money = "Money: "+str(self.money)
        self.money_label = Label(self.round_data,text=message_money,font=("Fixedsys",14),
                                 bg="#666666",fg="white")
        self.money_label.pack(fill=X)

        self.seperator = ttk.Separator(self.round_data).pack(fill=X)
                                                        
        self.round_button = Button(self.round_data, text="Start Wave "+str(self.wave), font=("Fixedsys",14),
                              command=lambda: self.wave_start())
        self.round_button.pack(fill=X,padx=5,pady=5)

        self.stats = Button(self.round_data, text="Game Stats", font=("Fixedsys",14),
                              command=lambda: Game_Overlay())
        self.stats.pack(fill=X,padx=5,pady=5)

        self.main_menu_button = Button(self.round_data, text="Main Menu", font=("Fixedsys",14),
                              command=lambda: self.main_menu())
        self.main_menu_button.pack(fill=X,padx=5,pady=5)

        self.seperator = ttk.Separator(self.round_data).pack(fill=X)

        self.sort_canvas = Canvas(self.sort_data, width=190, height=355)
        self.sort_canvas.pack(fill=Y,expand=True,padx=5,pady=5)

        self.game_grid = grid.Grid(self.game_canvas,self.sort_canvas,self.current_settings[3])

        self.seperator = ttk.Separator(self.sort_data).pack(fill=X)

        self.bubble_sort = Button(self.button_data, text="Bubble Sort", font=("Fixedsys",14),
                                  command=lambda: self.bubble(self.sort_canvas,self.game_grid.sort_grid))
        self.bubble_sort.pack(fill=X,padx=5,pady=5)

        self.quick_sort = Button(self.button_data, text="Quick Sort", font=("Fixedsys",14),
                                 command=lambda: self.quick())
        self.quick_sort.pack(fill=X,padx=5,pady=5)

    def bubble(self, canvas, sort_grid):
        sort_algorithms.BubbleSort(canvas,sort_grid)

    def quick(self):
        sort_algorithms.QuickSort()

    def move_mob(self,event=None):
        self.path = self.mob_move_route.path
        print(self.path)
        for each in self.path:
            print(each)
            colour = self.game_canvas.itemcget(self.game_grid.main_grid[(each[1],each[0])],"fill")
            if  colour == "blue" or colour == "red":
                pass
            else:
                self.game_canvas.itemconfig(self.game_grid.main_grid[(each[1],each[0])],fill="black")
                self.game_canvas.update_idletasks()
                time.sleep(0.5)

    def wave_start(self):
        self.mob_move_route = search_algorithms.Search_Path(self.game_canvas,self.game_grid.main_grid)
        self.move_mob()
##        mob_movement_thread = threading.Thread(target=self.move_mob,args=(self,))
##        mob_movement_thread.start()
##        mob_movement_thread.join()

        self.wave_end()

    def wave_end(self):
        pygame.mixer.Sound.play(button_accept)

        data = [self.parent.winfo_x(),self.parent.winfo_y()]
        
        image = ImageGrab.grab().crop((data[0]+3,data[1],data[0]+900,data[1]+627))
        image.save("./images/game_waves/wave_"+str(self.wave)+".png")
        
        wave_info = [self.health,self.money,self.wave]
        wave_data = open("./modules/wave_settings.pixel","wb")
        pickle.dump(wave_info,wave_data)

        self.wave += 1
        self.round_button.config(text="Start Wave "+str(self.wave))

    def main_menu(self, event=None):
        '''Returns the user to the main menu.'''
        pygame.mixer.Sound.play(button_deny)
        pygame.mixer.music.stop()# Cancels all current sounds being played
        pygame.mixer.music.load("./audio/bgm/jelly_castle_retro_remix.wav")# Starts song in first parameter.
        pygame.mixer.music.set_volume(self.current_settings[2]/100)
        pygame.mixer.music.play(-1)
        
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
            pygame.mixer.Sound.play(button_accept)
            
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
            
            self.table.pack(fill=BOTH,expand=True) # Force to fill space.

            Style().configure("Treeview",font=("Fixedsys",14)) # Styles the overview treeview table.
            Style().configure("Treeview.Heading",font=("Fixedsys",18))

            self.scrollbar.config(command=self.table.yview) # Sets scollbar to treeview table.

    def instance(self, event=None):
        pygame.mixer.Sound.play(button_deny)
        Game_Overlay.__instance -= 1 # Decrements private attribute __instance.
        self.overlay.destroy()

if __name__ == "__main__":
    # --- Tests above code if run --- #
    # - WARNING: The code below won't run as it is designed for security - #
    pass
