#Thomas Starling Addition - Cheat Menu
###################################################################################################################################
from tkinter import *
from tkinter.ttk import *
import pygame
import sqlite3

#from modules import gui_display

class Cheat_Menu:
    
    __instance = 0
    
    def __init__(self):

        self.button_accept = pygame.mixer.Sound("./audio/bgs/menu_confirm_1_dry.wav")
        self.button_deny = pygame.mixer.Sound("./audio/bgs/menu_deny_1_dry.wav")

        #Layout & Window
        if Cheat_Menu.__instance > 0: # Prevents more than one overlay opening at anytime.
            pass
        else:
            Cheat_Menu.__instance += 1 # Increments private attribute __instance.
            pygame.mixer.Sound.play(self.button_accept)
            
            self.overlay = Toplevel()
            self.overlay.title("Cheat Menu")
            self.overlay.resizable(0,0)
            self.overlay.geometry("350x240")
            self.overlay.wm_iconbitmap("./images/logo.ico")
            self.overlay.protocol("WM_DELETE_WINDOW",self.instance) # Sets event to when window is being closed.

            #Attributes
            self.frame01 = Frame(self.overlay)
            self.frame01.pack(fill=BOTH)

            self.frame02 = Frame(self.overlay)
            self.frame02.pack(fill=BOTH, pady=5)

            self.frame03 = Frame(self.overlay)
            self.frame03.pack(fill=BOTH, pady=5)

            self.frame04 = Frame(self.overlay)
            self.frame04.pack(fill=BOTH, pady=5)

            self.frame05 = Frame(self.overlay)
            self.frame05.pack(fill=BOTH, pady=5)

            self.frame06 = Frame(self.overlay)
            self.frame06.pack(fill=BOTH, pady=5)

            self.cheats = Label(self.frame01, text="Cheat Menu!",font=("Fixedsys",18))
            self.cheats.pack(side=LEFT, fill=X,expand=True,padx=10)
            
            self.cheat_healthmoney = Label(self.frame02, text="Unlimited Health and Money:",font=("Fixedsys",16))
            self.cheat_healthmoney.pack(side=LEFT, fill=X,expand=True,padx=10)

            var1 = BooleanVar()
            var1.set(False)
            self.unlimited_toggle_button = Checkbutton(self.frame02, text='Cheat OFF', variable=var1,
                                                    command=lambda : self.unlimited_toggle(var1))
            self.unlimited_toggle_button.pack(side=LEFT, fill=X,expand=True,padx=10)

            self.speed_hack = Label(self.frame03, text="Speed Hack: ",font=("Fixedsys",16))
            self.speed_hack.pack(side=LEFT, fill=X,expand=True,padx=10)

            self.speed_scale = Scale(self.frame03,from_=1.00,to=0.01,orient=HORIZONTAL)
            self.speed_scale.pack(side=LEFT,fill=X,expand=True,padx=10)
            self.speed_scale.set(0.03)

            self.speed_set = Button(self.frame03, text="Set", command=lambda: self.set_speed())
            self.speed_set.pack(side=LEFT,fill=X,expand=True,padx=5,pady=5)

            self.cheat_instant = Label(self.frame04, text="Unlock All Towers:         ",font=("Fixedsys",16))
            self.cheat_instant.pack(side=LEFT, fill=X,expand=True,padx=10)

            var2 = BooleanVar()
            var2.set(False)
            self.instant_toggle_button = Checkbutton(self.frame04, text='Cheat OFF', variable=var2,
                                                    command=lambda : self.unlock_towers(var2))
            self.instant_toggle_button.pack(side=LEFT, fill=X,expand=True,padx=10)


            self.cheat_low_health = Label(self.frame05, text="Enimies have low health:",font=("Fixedsys",16))
            self.cheat_low_health.pack(side=LEFT, fill=X,expand=True,padx=10)
            
            self.low = Button(self.frame05, text="Activate", command=lambda: self.low_health())
            self.low.pack(side=LEFT,fill=X,expand=True,padx=5,pady=5)

            self.cheat_overpower = Label(self.frame06, text="Over powered turrets:",font=("Fixedsys",16))
            self.cheat_overpower.pack(side=LEFT, fill=X,expand=True,padx=10)
            
            self.power = Button(self.frame06, text="Activate", command=lambda: self.over_power())
            self.power.pack(side=LEFT,fill=X,expand=True,padx=5,pady=5)

    def unlimited_toggle(self, state):
        if state.get() == 1:
            self.unlimited_toggle_button.config(text="Cheat ON")
            message = messagebox.showinfo("Activated", "Cheat Activated, If You Are Currently in Game, Main Menu to Apply Cheat")
            self.unlimited_toggle_button.state(["disabled"])

            constant_data = open("./modules/constants.pixel","w")
            constant_data.write("99999999\n")
            constant_data.write("99999999\n")
            constant_data.write(str(self.speed_scale.get()))
            #print("ON")
        else:
            pass
            #print("OFF")

    def set_speed(self):
        constant_data = open("./modules/constants.pixel","r")
        tmplist = []
        
        for line in constant_data:
            tmplist.append(line)
            
        health = tmplist[0]
        money = tmplist[1]
        speed = self.speed_scale.get()
            
        constant_data = open("./modules/constants.pixel","w")
        constant_data.write(str(health))
        constant_data.write(str(money))
        constant_data.write(str(speed))
        #print(self.speed_scale.get())

    def unlock_towers(self, state):
        if state.get() == 1:
            self.instant_toggle_button.config(text="Cheat ON")
            message = messagebox.showinfo("Activated", "Cheat Activated, If You Are Currently in Game, Main Menu to Apply Cheat")
            self.instant_toggle_button.state(["disabled"])
            print("Need to implement")
            #print("ON")
        else:
            pass
            #print("OFF")

    def low_health(self, event=None):
        ''' Connect to database, modify values on the mobs making
        thier health very low'''
        message = messagebox.showinfo("Activated", "Cheat Activated, If You Are Currently in Game, Main Menu to Apply Cheat")
        print("Need to implement")

    def over_power(self, event=None):
        '''Connect to database and edit value in turret for power'''
        message = messagebox.showinfo("Activated", "Cheat Activated, If You Are Currently in Game, Main Menu to Apply Cheat")
        print("Need to implement")

    def instance(self, event=None):
        pygame.mixer.Sound.play(self.button_deny)
        Cheat_Menu.__instance -= 1 # Decrements private attribute __instance.
        self.overlay.destroy()
        
###################################################################################################################################
