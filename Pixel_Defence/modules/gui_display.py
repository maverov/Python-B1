__author__ = "William Read"
__revision__ = "02/02/2016"
__version__ = "0.1"

from tkinter.ttk import *
from tkinter import *

from PIL import Image, ImageTk, ImageGrab

from modules import image_loader,grid,sort_algorithms,search_algorithms,entities, cheat_menu

import os,sys,time,pickle,pygame,queue,threading

pygame.init()
button_accept = pygame.mixer.Sound("./audio/bgs/menu_confirm_1_dry.wav")
button_deny = pygame.mixer.Sound("./audio/bgs/menu_deny_1_dry.wav")

####################################################################################################################################
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
        
        self.title_banner = Label(self.frame, image=self.title_banner_image,
                                  bg="#666666",fg="white")
        self.title_banner.pack(pady=10)

        ##Cristian Ghita Tutorial button
        
        self.tutorial_button = Button(self.frame, text="Begin tutorial", font=("Fixedsys",18),
                                      command=lambda: Tutorial_Window(self.parent,self.frame))
        self.tutorial_button.pack(fill=X,pady=3)

        ##End

        self.game = Button(self.frame, text="Play", font=("Fixedsys",18),bg="green",#relief=FLAT,
                           command=lambda: Game_Window(self.parent,self.frame))
        self.game.pack(pady=3, fill=X)

        self.options = Button(self.frame, text="Options", font=("Fixedsys",18),bg="sky blue",
                              command=lambda: Options(self.parent,self.frame))
        self.options.pack(pady=3, fill=X)

        self.quit = Button(self.frame, text="Quit", font=("Fixedsys",18),bg="red",
                           command=self.close)
        self.quit.pack(pady=3, fill=X)

        self.info = Button(self.frame, bitmap="info", font=("Fixedsys",18),
                           command=self.game_credits)
        self.info.pack(pady=3, fill=X)

        #Revert constant back
        constant_data = open("./modules/constants.pixel","w")
        constant_data.write("50\n")
        constant_data.write("100\n")
        constant_data.write("0.03")
        #End

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

###################################################################################################################################
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
        self.frame01.pack(fill=BOTH,pady=25)

        self.frame02 = Frame(self.main_frame,bg="#666666")
        self.frame02.pack(fill=BOTH,pady=25)

        self.frame03 = Frame(self.main_frame,bg="#666666")
        self.frame03.pack(fill=BOTH,pady=25)

        self.frame04 = Frame(self.main_frame,bg="#666666")
        self.frame04.pack(fill=BOTH,pady=25)

        self.frame06 = Frame(self.main_frame,bg="#666666")
        self.frame06.pack(fill=BOTH,pady=25)
        
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

        ##Tom Starling Cheat button
        self.cheat_option = IntVar()
        self.cheat_label = Label(self.frame04, text="Cheats: ",font=("Fixedsys",18),bg="#666666",fg="white")
        self.cheat_label.pack(side=LEFT,fill=X,padx=10)
        
        self.cheat_button = Checkbutton(self.frame04, text="Activate", font=("Fixedsys",18),bg="#666666",fg="red",
                                        variable=self.cheat_option, command=lambda: self.cheat_menu(self.cheat_option))
        self.cheat_button.pack(side=LEFT,fill=X,padx=10)
        
    def cheat_menu(self, state):
        if state.get() == 1:
            cheat_menu.Cheat_Menu()
            #print("ON")
        else:
            pass
            #print("OFF")
        ##End

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
        setting_data = [self._map.get(),self.difficulty,self.audio_scale.get(),self.n_barricades]
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

####################################################################################################################################
class Game_Constants():

     def __init__(self):
         constant_data = open("./modules/constants.pixel","r")
         constant_info = []

         for line in constant_data:
            constant_info.append(line)

         self.health = int(constant_info[0]) # Health
         self.money = int(constant_info[1]) #Money
         self.speed = float(constant_info[2]) #Play speed
####################################################################################################################################
class Tutorial_Window(Window):
    def __init__(self,parent,main):
        pygame.mixer.Sound.play(button_accept)

        if os.path.isfile("./modules/wave_settings.pixel"): # Check is file exsists
            os.remove("./modules/wave_settings.pixel") #Remove wave_settings file
        else:
            wave_data = open("./modules/wave_settings.pixel","w")

        sort_speed = open("./modules/sort_speed.pixel","w")
        sort_speed.write(str(0.03))

        self.tower_list = ['red','blue','green','yellow','purple','brown']
        self.tower_cost_list = [50,100,250,500,750,5]
        
        Window.__init__(self,parent) # Inherets the attributes and methods from class Window

        self.imageList()
        initial_data = Game_Constants()

        self.inst = 0
        
        self.health = initial_data.health
        self.money = initial_data.money
        self.wave = 'Tutorial'

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
        self.sort_data_left = Frame(self.sort_data, bg="#666666",relief=RIDGE)
        self.sort_data_left.pack(fill=BOTH)
        self.sort_data_right = Frame(self.sort_data, bg="#666666",relief=RIDGE)
        self.sort_data_right.pack(fill=BOTH)

        self.button_data = Frame(self.frame,bg="#666666",relief=RIDGE)
        self.button_data.pack(fill=BOTH)

        self.tower_d1 = Frame(self.button_data,bg="#666666",relief = RIDGE)
        self.tower_d2 = Frame(self.button_data,bg="#666666",relief = RIDGE)
        self.tower_d3 = Frame(self.button_data, bg="#666666", relief=RIDGE)
        self.tower_d3.pack(side=BOTTOM,fill=BOTH)
        self.tower_d2.pack(side=BOTTOM,fill=BOTH)
        self.tower_d1.pack(side=BOTTOM,fill=BOTH)

        self.display = Frame(self.main_frame,bg="#666666")
        self.display.pack(fill=BOTH,expand=True)
        self.display_bottom = Frame(self.display,bg="#666666")
        self.display_bottom.pack(side=BOTTOM)
        self.display_bottom_l = Frame(self.display_bottom,bg="#666666")
        self.display_bottom_l.pack(side=LEFT)
        self.display_bottom_r = Frame(self.display_bottom,bg="#666666")
        self.display_bottom_r.pack(side=RIGHT)

        self.game_canvas = Canvas(self.display, bg="black")
        self.game_canvas.pack(fill=BOTH,expand=True,padx=5,pady=5)
        self.next_button = Button(self.display_bottom_r, text="Next",font=("Fixedsys",16),width=15,
                                  bg="white", command=lambda: self.instruction('next'))
        self.next_button.pack(side=BOTTOM,padx=10,pady=2)
        self.back_button = Button(self.display_bottom_l, text="Back",font=("Fixedsys",16),width=15,
                                  state = DISABLED,bg="#d1d1d1",command=lambda:self.instruction('back'))
        self.back_button.pack(side=BOTTOM,padx=10,pady=2)

        self.photo = Image.open("./images/maps/"+self.current_settings[0])
        self.photo = self.photo.resize((700,600),Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.photo)
        
        self.game_canvas.create_image(0,0,image=self.photo,anchor=NW)

        self.textTutorial = self.game_canvas.create_text(333,250,text='--------------------------------\nThe main idea of the game is to\nkill the monsters that will try to reach\nyour town entrance. In order to do that\nyou have to place towers that will\nfire at them. Towers will cost money\nand you can unlock new towers\n by collecting dropped parts from the killed monsters.\nYou can also build barricades\nto make the monsters have a longer path\nso your turrets will have more time to\nkill them.\n--------------------------------',
                                                         font=("Fixedsys",16),justify=CENTER)
        self.text1 = self.game_canvas.create_text(128,20,text="", font=("Fixedsys",16))
        self.text2 = self.game_canvas.create_text(570,540,text="", font=("Fixedsys",16))
        self.text3 = self.game_canvas.create_text(560,65,text="",font=("Fixedsys",16))
        self.text4 = self.game_canvas.create_text(495,99,text="",font=("Fixedsys",16),justify=CENTER)
        self.text5 = self.game_canvas.create_text(455,390,text="",font=("Fixedsys",16),justify=CENTER)
        self.text6 = self.game_canvas.create_text(465,460,text="",font=("Fixedsys",16),justify=CENTER)
        self.text7 = self.game_canvas.create_text(340,250,text="",font=("Fixedsys",25),justify=CENTER)
        self.text8 = self.game_canvas.create_text(345,350,text="",font=("Fixedsys",16),justify=CENTER)

        # -- Game_Option Frame -- #
        message_health = "Health: "+str(self.health)
        self.health_label = Label(self.round_data,text=message_health,font=("Fixedsys",14),
                                  bg="#666666",fg="white")
        self.health_label.pack(fill=X)

        self.message_money = "Money: "+str(self.money)
        self.money_label = Label(self.round_data,text=self.message_money,font=("Fixedsys",14),
                                 bg="#666666",fg="white")
        self.money_label.pack(fill=X)

        self.seperator = ttk.Separator(self.round_data).pack(fill=X)
                                                        
        self.round_button = Button(self.round_data, text="Start Wave "+str(self.wave), font=("Fixedsys",14),
                              command=lambda: self.wave_start(),state=DISABLED)
        self.round_button.pack(fill=X,padx=5,pady=5)

        self.stats = Button(self.round_data, text="Game Stats", font=("Fixedsys",14),
                              command=lambda: Game_Overlay(),state=DISABLED)
        self.stats.pack(fill=X,padx=5,pady=5)

        self.main_menu_button = Button(self.round_data, text="Main Menu", font=("Fixedsys",14),
                              command=lambda: self.main_menu())
        self.main_menu_button.pack(fill=X,padx=5,pady=5)

        self.seperator = ttk.Separator(self.round_data).pack(fill=X)

        self.sort_canvas = Canvas(self.sort_data_left, width=90, height=170)
        self.sort_canvas.pack(padx=25,pady=5)

        self.game_grid = grid.Grid(self.game_canvas,self.sort_canvas,self.current_settings[3],True)

        self.bubble_sort = Button(self.sort_data_right, text="Bubble Sort", font=("Fixedsys",14),
                                  state=DISABLED,command=lambda: self.bubble(self.sort_canvas,self.game_grid.sort_grid))
        self.bubble_sort.pack(fill=X,padx=5,pady=5)

        self.quick_sort = Button(self.sort_data_right, text="Sort Options", font=("Fixedsys",14),
                                 state=DISABLED,command=lambda: self.s_options())
        self.quick_sort.pack(fill=X, padx=5, pady=5)

        self.separator = ttk.Separator(self.sort_data).pack(side=BOTTOM,fill=X)

        self.turret1 = Button(self.tower_d1, text="T1\n"+str(self.tower_cost_list[0]), font=("Fixedsys",14),width=8,height=3,
                              state=DISABLED,command=lambda: self.set_ID(0))
        self.turret1.pack(side=LEFT,padx=15,pady=3)
        
        self.turret2 = Button(self.tower_d1, text="T2\n"+str(self.tower_cost_list[1]), font=("Fixedsys",14),width=8,height=3,
                              state=DISABLED,command=lambda: self.set_ID(1))
        self.turret2.pack(side=RIGHT,padx=15,pady=3)
        self.turret3 = Button(self.tower_d2, text="T3\n"+str(self.tower_cost_list[2]), font=("Fixedsys",14),width=8,height=3,
                              state=DISABLED,command=lambda: self.set_ID(2))
        self.turret3.pack(side=LEFT,padx=15,pady=3)
        self.turret4 = Button(self.tower_d2, text="T4\n"+str(self.tower_cost_list[3]), font=("Fixedsys",14),width=8,height=3,
                              state=DISABLED,command=lambda: self.set_ID(3))
        self.turret4.pack(side=RIGHT,padx=15,pady=3)
        self.turret5 = Button(self.tower_d3, text="T5\n"+str(self.tower_cost_list[4]), font=("Fixedsys",14),height=3,width=8,
                              state=DISABLED,command=lambda: self.set_ID(4))
        self.turret5.pack(side=LEFT,padx=15,pady=3)
        self.barricade6 = Button(self.tower_d3, text="Ba\n"+str(self.tower_cost_list[5]), font=("Fixedsys",14),height=3,width=8,
                                 state=DISABLED,command=lambda: self.set_ID(5))
        self.barricade6.pack(side=RIGHT,padx=15,pady=3)

    def instruction(self, order):
        if order == 'next':
            self.inst += 1
        elif order == 'back' and self.inst-1>=0:
            self.inst -= 1
        if self.inst > 0:
            self.back_button.config(state = NORMAL, bg='white')
        else:
            self.back_button.config(state=DISABLED, bg='#d1d1d1')
        if self.inst <7:
            self.next_button.config(state=NORMAL,bg='white')
        else:
            self.next_button.config(state=DISABLED,bg='#d1d1d1')
        if self.inst == 0:
            self.game_canvas.itemconfig(self.text1,text='')
            self.game_canvas.itemconfig(self.textTutorial, text='--------------------------------\nThe main idea of the game is to\nkill the monsters that will try to reach\nyour town entrance. In order to do that\nyou have to place towers that will\nfire at them. Towers will cost money\nand you can unlock new towers\n by collecting dropped parts from the killed monsters.\nYou can also build barricades\nto make the monsters have a longer path\nso your turrets will have more time to\nkill them.\n--------------------------------')
        elif self.inst == 1:
            self.game_canvas.itemconfig(self.text1,text="<-- This is where the\n   monsters will spawn")
            self.game_canvas.itemconfig(self.textTutorial,text="")
            self.game_canvas.itemconfig(self.text2,text="")
        elif self.inst == 2:
            self.game_canvas.itemconfig(self.text1,text='')
            self.game_canvas.itemconfig(self.text2,text="This is where they\n  will head to  -->")
            self.round_button.config(state=DISABLED,bg='#F0F0ED')
            self.game_canvas.itemconfig(self.text3,text='')
        elif self.inst == 3:
            self.game_canvas.itemconfig(self.text2,text='')
            self.game_canvas.itemconfig(self.text3,text="This button will send the -->\n  next wave of monsters\n        Test it!")
            self.stats.config(state=DISABLED,bg='#F0F0ED')
            self.round_button.config(state=NORMAL,bg='green')
            self.game_canvas.itemconfig(self.text4,text='')
        elif self.inst == 4:
            self.game_canvas.itemconfig(self.text3,text='')
            self.game_canvas.itemconfig(self.text4,text="Your stats will get recorded after each -->\nwave. You can visualise them here ")
            self.round_button.config(state=DISABLED,bg='#F0F0ED')
            self.bubble_sort.config(state=DISABLED,bg='#F0F0ED')
            self.quick_sort.config(bg='#F0F0ED')
            self.stats.config(state=NORMAL,bg='green')
            self.game_canvas.itemconfig(self.text5,text='')
        elif self.inst == 5:
            self.stats.config(state=DISABLED,bg='#F0F0ED')
            self.game_canvas.itemconfig(self.text4,text='')
            self.game_canvas.itemconfig(self.text6,text='')
            self.bubble_sort.config(state=NORMAL,bg='green')
            self.quick_sort.config(bg='green')
            self.turret1.config(state=DISABLED,bg='#F0F0ED')
            self.turret2.config(bg='#F0F0ED')
            self.turret3.config(bg='#F0F0ED')
            self.turret4.config(bg='#F0F0ED')
            self.turret5.config(bg='#F0F0ED')
            self.barricade6.config(state=DISABLED,bg='#F0F0ED')
            self.game_canvas.itemconfig(self.text5,text="When you kill monsters there are chances to drop  -->\ntower parts. These tower parts if\nsorted can unlock you a new tower to construct.\nYou can edit the sort in terms of speed and orientation.\nSort options are available only in the main game.")
        elif self.inst == 6:
            self.bubble_sort.config(state=DISABLED,bg='#F0F0ED')
            self.quick_sort.config(bg='#F0F0ED')
            self.game_canvas.itemconfig(self.text6,text='This is the building menu. In order to build\nsomething you have to select a tile then press\n the desired button. You can build barricades -->\nthat monsters will have to avoid.\nSelect a tile and build something.')
            self.game_canvas.itemconfig(self.text5,text='')
            self.turret1.config(state=NORMAL,bg='green')
            self.turret2.config(bg='green')
            self.turret3.config(bg='green')
            self.turret4.config(bg='green')
            self.turret5.config(bg='green')
            self.barricade6.config(state=NORMAL,bg='green')
            self.game_canvas.itemconfig(self.text7,text='')
            self.game_canvas.itemconfig(self.text8,text='')
            self.main_menu_button.config(bg='#F0F0ED')
        elif self.inst == 7:
            self.turret1.config(state=DISABLED,bg='#F0F0ED')
            self.turret2.config(bg='#F0F0ED')
            self.turret3.config(bg='#F0F0ED')
            self.turret4.config(bg='#F0F0ED')
            self.turret5.config(bg='#F0F0ED')
            self.barricade6.config(state=DISABLED,bg='#F0F0ED')
            self.game_canvas.itemconfig(self.text6,text='')
            self.game_canvas.itemconfig(self.text7,text="You've finished\nthe tutorial!\nGood job!\nGL & HF")
            self.game_canvas.itemconfig(self.text8,text="Press 'Main Menu' button to exit the tutorial.")
            self.main_menu_button.config(bg='green')
            

    def set_ID(self, ID):
        self.last_button = ID
        print(self.tower_list[self.last_button]+" tower placed on: ")
        print(self.game_grid.last_barricade)
        if self.money-self.tower_cost_list[self.last_button] >= 0:
            self.game_grid.canvas01.itemconfig(self.game_grid.main_grid[self.game_grid.last_barricade]
                                           ,fill=self.tower_list[self.last_button])
            self.money -= self.tower_cost_list[self.last_button]
            self.money_label.config(text="Money: "+str(self.money))
            self.money_label.pack(fill=X)

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

    def wave_start(self):
        pygame.mixer.Sound.play(button_accept)
        self.round_button.config(state=DISABLED)
        self.next_button.config(state=DISABLED)
        self.back_button.config(state=DISABLED)
        self.round_button.update()
        
        self.no_mobs = (1*4)
        if 1 % 20 == 0:
            self.no_mobs = 1
        if self.no_mobs > 100:
            self.no_mobs == 100
            
        self.mob_move_route = search_algorithms.Search_Path(self.game_canvas,self.game_grid.main_grid)
        self.mob_move_route = self.mob_move_route.path

        self.move_mobs_stop = threading.Event()
        
        self.move_mobs = threading.Thread(target=self.animate_wave)
        self.move_mobs.start()

        self.queue = queue.Queue()
        Thread_Tasks(self.queue).start()

        self.parent.after(100,self.queue_processes)

        self.wave_end()

    def animate_wave(self):
        self.path = self.mob_move_route
        self.path_length = 0
        for i in range(self.no_mobs):
            for each in self.path:
                self.path_length += 1
                try:
                    self.previous = self.mob_move_route[self.path_length-2]
                except:
                    break
                colour = self.game_canvas.itemcget(self.game_grid.main_grid[(each[1],each[0])],"fill")
                previous_colour = self.game_canvas.itemcget(self.game_grid.main_grid[(self.previous[1],self.previous[0])],"fill")
                
                if  colour == "blue" or colour == "red":
                    if colour == "blue":
                        self.health -= 10
                        self.back_button.config(state=NORMAL)
                        self.next_button.config(state=NORMAL)
                        self.game_grid.canvas01.itemconfig(self.game_grid.main_grid[(17,21)],fill="blue")
                        if self.health <= 0:
                            self.gameover()
                        self.game_canvas.itemconfig(self.game_grid.main_grid[(self.previous[1],self.previous[0])],fill="")
                        self.health_label.config(text="Health: "+str(self.health))
                        self.game_canvas.update_idletasks()
                else:
                    if previous_colour != "red":
                        self.game_canvas.itemconfig(self.game_grid.main_grid[(self.previous[1],self.previous[0])],fill="")
                    self.game_canvas.itemconfig(self.game_grid.main_grid[(each[1],each[0])],fill="black")
                    self.game_canvas.update_idletasks()
            
                initial_data = Game_Constants() #Connect to class
                self.speed = initial_data.speed # Allow changable value for cheat manu
                time.sleep(0.07)

    def wave_end(self):
        self.move_mobs_stop.set()
        data = [self.parent.winfo_x(),self.parent.winfo_y()]
        
        wave_info = [self.wave,self.health,self.money]
        wave_data = open("./modules/wave_settings.pixel","a")
        wave_data.write(str(wave_info)+"\n")

    def bubble(self, canvas, sort_grid):
        sort_algorithms.BubbleSort(canvas,sort_grid)

    def queue_processes(self):
        try:
            pass
        except queue.Empty:
            self.parent.after(100,self.queue_processing)


###########################################################################################################################
class Game_Window(Window): # Inherits class Window.
    '''Inherits the attributes and method of "Window".'''

    def __init__(self,parent,main):
        '''Displays all the widgets for the main Tower Defence Game.'''
        pygame.mixer.Sound.play(button_accept)

        if os.path.isfile("./modules/wave_settings.pixel"): # Check is file exsists
            os.remove("./modules/wave_settings.pixel") #Remove wave_settings file
        else:
            wave_data = open("./modules/wave_settings.pixel","w") # Create file

        sort_speed = open("./modules/sort_speed.pixel","w")
        sort_speed.write(str(0.03))

        self.tower_list = ['red','blue','green','yellow','purple','brown']
        self.tower_cost_list = [50,100,250,500,750,5]
        
        Window.__init__(self,parent) # Inherets the attributes and methods from class Window

        self.imageList()
        initial_data = Game_Constants()
        
        self.health = initial_data.health
        self.money = initial_data.money
        self.wave = 1

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
        self.sort_data_left = Frame(self.sort_data, bg="#666666",relief=RIDGE)
        self.sort_data_left.pack(fill=BOTH)
        self.sort_data_right = Frame(self.sort_data, bg="#666666",relief=RIDGE)
        self.sort_data_right.pack(fill=BOTH)

        self.button_data = Frame(self.frame,bg="#666666",relief=RIDGE)
        self.button_data.pack(fill=BOTH)

        self.tower_d1 = Frame(self.button_data,bg="#666666",relief = RIDGE)
        self.tower_d2 = Frame(self.button_data,bg="#666666",relief = RIDGE)
        self.tower_d3 = Frame(self.button_data, bg="#666666", relief=RIDGE)
        self.tower_d3.pack(side=BOTTOM,fill=BOTH)
        self.tower_d2.pack(side=BOTTOM,fill=BOTH)
        self.tower_d1.pack(side=BOTTOM,fill=BOTH)

        self.display = Frame(self.main_frame,bg="#999999")
        self.display.pack(fill=BOTH,expand=True)

        self.game_canvas = Canvas(self.display, bg="black")
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

        self.message_money = "Money: "+str(self.money)
        self.money_label = Label(self.round_data,text=self.message_money,font=("Fixedsys",14),
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

        self.sort_canvas = Canvas(self.sort_data_left, width=90, height=170)
        self.sort_canvas.pack(padx=25,pady=5)

        self.bubble_sort = Button(self.sort_data_right, text="Bubble Sort", font=("Fixedsys",14),
                                  command=lambda: self.bubble(self.sort_canvas,self.game_grid.sort_grid))
        self.bubble_sort.pack(fill=X,padx=5,pady=5)

        self.sort_options = Button(self.sort_data_right, text="Sort Options", font=("Fixedsys",14),
                                 command=lambda: self.s_options())
        self.sort_options.pack(fill=X, padx=5, pady=5)

        self.game_grid = grid.Grid(self.game_canvas,self.sort_canvas,self.current_settings[3],False)

        self.separator = ttk.Separator(self.sort_data).pack(side=BOTTOM,fill=X)

        self.turret1 = Button(self.tower_d1, text="T1\n"+str(self.tower_cost_list[0]), font=("Fixedsys",14),width=8,height=3,
                              command=lambda: self.set_ID(0))
        self.turret1.pack(side=LEFT,padx=15,pady=3)
        
        self.turret2 = Button(self.tower_d1, text="T2\n"+str(self.tower_cost_list[1]), font=("Fixedsys",14),width=8,height=3,
                              command=lambda: self.set_ID(1))
        self.turret2.pack(side=RIGHT,padx=15,pady=3)
        #self.turret2.config(state=DISABLED)
        self.turret3 = Button(self.tower_d2, text="T3\n"+str(self.tower_cost_list[2]), font=("Fixedsys",14),width=8,height=3,
                              command=lambda: self.set_ID(2))
        self.turret3.pack(side=LEFT,padx=15,pady=3)
        #.turret3.config(state=DISABLED)
        self.turret4 = Button(self.tower_d2, text="T4\n"+str(self.tower_cost_list[3]), font=("Fixedsys",14),width=8,height=3,
                              command=lambda: self.set_ID(3))
        self.turret4.pack(side=RIGHT,padx=15,pady=3)
        #self.turret4.config(state=DISABLED)
        self.turret5 = Button(self.tower_d3, text="T5\n"+str(self.tower_cost_list[4]), font=("Fixedsys",14),height=3,width=8,
                              command=lambda: self.set_ID(4))
        self.turret5.pack(side=LEFT,padx=15,pady=3)
        #self.turret5.config(state=DISABLED)
        self.barricade6 = Button(self.tower_d3, text="Ba\n"+str(self.tower_cost_list[5]), font=("Fixedsys",14),height=3,width=8,
                                 command=lambda: self.set_ID(5))
        self.barricade6.pack(side=RIGHT,padx=15,pady=3)

        self.start = time.time()

    def set_ID(self, ID):
        try:
            self.error_label.pack_forget()
            self.last_button = ID
            #print(self.tower_list[self.last_button]+" tower placed on: ")
            #print(self.game_grid.last_barricade)
            if self.money-self.tower_cost_list[self.last_button] >= 0:
                self.game_grid.canvas01.itemconfig(self.game_grid.main_grid[self.game_grid.last_barricade]
                                               ,fill=self.tower_list[self.last_button])
                self.money -= self.tower_cost_list[self.last_button]
                self.money_label.config(text="Money: "+str(self.money))
                self.money_label.pack(fill=X)
        except:
            self.error_label = Label(self.game_canvas,text="Please select a location to place a tower first",font=("Fixedsys",16), bg="white",fg="red")
            self.error_label.pack()
            
    def bubble(self, canvas, sort_grid):
        sort_algorithms.BubbleSort(canvas,sort_grid)

    def s_options(self):
        sort_algorithms.sort_options()

    def wave_start(self):
        pygame.mixer.Sound.play(button_accept)
        self.round_button.config(state=DISABLED)
        self.round_button.update()
        
        self.no_mobs = (self.wave*4)
        if self.wave % 20 == 0:
            self.no_mobs = 1
        if self.no_mobs > 100:
            self.no_mobs == 100
            
        self.mob_move_route = search_algorithms.Search_Path(self.game_canvas,self.game_grid.main_grid)
        self.mob_move_route = self.mob_move_route.path

        self.move_mobs_stop = threading.Event()
        
        self.move_mobs = threading.Thread(target=self.animate_wave)
        self.move_mobs.start()

        self.queue = queue.Queue()
        Thread_Tasks(self.queue).start()
        
        self.parent.after(100,self.queue_processes)


        self.wave += 1
        self.wave_end()        

    def wave_end(self):
        self.move_mobs_stop.set()
        data = [self.parent.winfo_x(),self.parent.winfo_y()]
        
        wave_info = [(self.wave - 1),self.health,self.money]
        wave_data = open("./modules/wave_settings.pixel","a")
        wave_data.write(str(wave_info)+"\n")

        self.round_button.config(text="Start Wave "+str(self.wave))
        self.round_button.config(state=NORMAL)
        self.round_button.update()

    def gameover(self):
        self.move_mobs_stop.set()
        self.game_canvas.delete(ALL)
        self.game_canvas.create_text(300,300,text="GAME OVER",fill="white",font=("Fixedsys",30))
        self.game_canvas.update()
        
        end = time.time()
        time_spent = "You survived: " + str(round(end - self.start, 1)) + " seconds! " + str(self.wave) + " waves."
        self.time_label = Label(self.game_canvas,text=time_spent,font=("Fixedsys",18))
        self.time_label.pack()
        
        time.sleep(5)
        self.main_menu()

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

    def queue_processes(self):
        try:
            pass
        except queue.Empty:
            self.parent.after(100,self.queue_processing)
            

    def animate_wave(self):
        self.path = self.mob_move_route
        self.path_length = 0
        for i in range(self.no_mobs):
            for each in self.path:
                self.path_length += 1
                try:
                    self.previous = self.mob_move_route[self.path_length-2]
                except:
                    break
                colour = self.game_canvas.itemcget(self.game_grid.main_grid[(each[1],each[0])],"fill")
                previous_colour = self.game_canvas.itemcget(self.game_grid.main_grid[(self.previous[1],self.previous[0])],"fill")
                
                if  colour == "blue" or colour == "red":
                    if colour == "blue":
                        self.health -= 10
                        if self.health <= 0:
                            self.gameover()
                        self.game_canvas.itemconfig(self.game_grid.main_grid[(self.previous[1],self.previous[0])],fill="")
                        self.health_label.config(text="Health: "+str(self.health))
                        self.game_canvas.update_idletasks()
                else:
                    if previous_colour != "red":
                        self.game_canvas.itemconfig(self.game_grid.main_grid[(self.previous[1],self.previous[0])],fill="")
                    self.game_canvas.itemconfig(self.game_grid.main_grid[(each[1],each[0])],fill="black")
                    self.game_canvas.update_idletasks()

                initial_data = Game_Constants() #Connect to class
                self.speed = initial_data.speed # Allow changable value for cheat manu
                time.sleep(self.speed)
            
###################################################################################################################################
class Thread_Tasks(threading.Thread):

    def __init__(self,queue_data):
        threading.Thread.__init__(self)
        self.queue = queue_data
        
###################################################################################################################################
class Game_Overlay(Game_Window):
    '''Inherits the attributes and method of "Window".'''
    __instance = 0

    def __init__(self):
        '''Displays toplevel widget displaying user scores.'''
        
        wave_data = open("./modules/wave_settings.pixel","r")
        wave_info = []

        #####Access to constants
        initial_data = Game_Constants()
        self.health = initial_data.health
        self.money = initial_data.money
        self.speed = initial_data.speed
        ####End

        for line in wave_data:
            wave_info.append(line)
            #print(wave_info)
        
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

            ##Insert Data
            for i in wave_info:
                i = i.replace("[","")
                i = i.replace("]","")
                i = i.split(",")
                self.table.insert("", -1, values=(i[0],i[2],i[1]))
            ##End

    def instance(self, event=None):
        pygame.mixer.Sound.play(button_deny)
        Game_Overlay.__instance -= 1 # Decrements private attribute __instance.
        self.overlay.destroy()

if __name__ == "__main__":
    # --- Tests above code if run --- #
    # - WARNING: The code below won't run as it is designed for security - #
    pass
