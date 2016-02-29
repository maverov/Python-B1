#Thomas Starling Addition - Cheat Menu
###################################################################################################################################
from tkinter import *
from tkinter.ttk import *
import pygame

class Cheat_Menu:

    __instance = 0
    
    def __init__(self):

        self.button_accept = pygame.mixer.Sound("./audio/bgs/menu_confirm_1_dry.wav")
        self.button_deny = pygame.mixer.Sound("./audio/bgs/menu_deny_1_dry.wav")
        
        if Cheat_Menu.__instance > 0: # Prevents more than one overlay opening at anytime.
            pass
        else:
            Cheat_Menu.__instance += 1 # Increments private attribute __instance.
            pygame.mixer.Sound.play(self.button_accept)
            
            self.overlay = Toplevel()
            self.overlay.title("Cheat Menu")
            self.overlay.geometry("500x300")
            self.overlay.wm_iconbitmap("./images/logo.ico")
            self.overlay.protocol("WM_DELETE_WINDOW",self.instance) # Sets event to when window is being closed.

            #Layout            
            self.main_frame = Frame(self.overlay,bg="#666666")
            self.main_frame.pack(side=LEFT,fill=BOTH,expand=True)
    
            self.frame01 = Frame(self.main_frame,bg="#666666")
            self.frame01.pack(fill=BOTH,pady=30)

            self.frame02 = Frame(self.main_frame,bg="#666666")
            self.frame02.pack(fill=BOTH,pady=30)

            self.frame03 = Frame(self.main_frame,bg="#666666")
            self.frame03.pack(fill=BOTH,pady=30)

            #Attributes
            self.cheat_label = Label(self.frame01, text="Cheats: ",font=("Fixedsys",18),bg="#666666",fg="white")
            self.cheat_label.pack(side=LEFT,fill=X,padx=10)

    def instance(self, event=None):
        pygame.mixer.Sound.play(self.button_deny)
        Cheat_Menu.__instance -= 1 # Decrements private attribute __instance.
        self.overlay.destroy()
        
###################################################################################################################################
