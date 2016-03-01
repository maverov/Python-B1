__author__ = "William Read"
__revision__ = "01/03/2016 07:35:44"
__version__ = "1.0"

# -- Imports directed for tkinter calls within program -- #
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo,showwarning

# -- PIL Module used for image manipulation -- #
from PIL import Image, ImageGrab

# -- Custom Module files from generate_defaults.py and -- #
# -- video_capture.py -- #
from generate_defaults import *
from video_capture import *

# -- Import base modules: os, sys and uuid (for unique id's) -- #
import os, sys, uuid

class Main:
    '''Class to define the main tkinter window.'''

    def __init__(self, parent):
        '''
Defines layout of window and attributes that the window holds. Contains initialisation
of the Video and Image Class instances, as well as finding the initial settings as
previously used.
'''
        self.root = parent # Takes passed through parent and globalises within class.
        self.root.title("Minority Screen Capture") # Defines the systems title.
        self.root.geometry("%dx%d" % (500,300)) # Sets the initial size of the window.
        self.root.minsize(width=400,height=250) # Sets minimum window size.
        self.root.maxsize(width=500,height=300) # Sets maximum window size.
        self.root.attributes("-topmost",1) # Forces window to be above over active windows.
        self.root.wm_iconbitmap("./icon.ico") # Sets the icon of this program as the one at the defined location.

        self.notebook = Notebook(self.root) # Sets up the notebook.
        self.page1 = Frame(self.notebook) # Defines the pages that are within the previously defined notebook.
        self.page2 = Frame(self.notebook)
        self.page3 = Frame(self.notebook)
        self.notebook.add(self.page1, text="Images") # Defines names to previously defined titles.
        self.notebook.add(self.page2, text="Videos")
        self.notebook.add(self.page3, text="About")
        self.notebook.pack(fill=BOTH, expand=True) # Places the notebook into the defined frame.

        self.style = Style() # Creates a custom style all the widgets follow.
        self.style.configure(".",font=("Fixedsys",16)) # Forces all the widgets to have Fixedsys as it's font.

        file = open("settings.txt","r") # Open settings.txt to be read.
        doc = file.readlines() # Read the file.
        settings = [] # Define array called settings.
        for line in doc: # For each line that is stored within the document.
            try:
                line = line.split("=") # Split by the "=" within the string.
                settings.append(line[1].replace("\n","")) # Add to the settings list the value excluding the return.
            except: # Skip blank lines within text file.
                pass
        file.close() # Close opened file.

        Image(self.page1,settings,self.root) # Call class passing values for the page, settings and the main root.
        Video(self.page2,settings,self.root)
        About(self.page3) # Call class that only passes the page.

class Image:

    def __init__(self, page, settings, parent):
        '''
Sets up widgets that will be displayed on the Image tab of the notebook and define constants
that would be used within methods created by the call of this class.
'''
        self.page = page
        self.settings = settings
        self.parent = parent
        self.filters = ["None","None","BLUR","CONTOUR","DETAIL","EDGE_ENHANCE",
                        "EDGE_ENHANCE_MORE","EMBOSS","FIND_EDGES",
                        "SMOOTH","SMOOTH_MORE","SHARPEN"]
        self.bindings = ["<F1>","<F1>","<F2>","<F3>","<F4>","<F5>","<F6>","<F7>",
                         "<F8>","<F9>","<F10>","<F11>","<F12>"]
        
        self.frame_01 = Frame(self.page)
        self.frame_01.pack(fill=BOTH)

        self.frame_02 = Frame(self.page)
        self.frame_02.pack(fill=BOTH)

        self.frame_03 = Frame(self.page)
        self.frame_03.pack(fill=BOTH)

        self.frame_04 = Frame(self.page)
        self.frame_04.pack(fill=BOTH)

        self.frame_05 = Frame(self.page)
        self.frame_05.pack(side=BOTTOM,fill=BOTH)

        # -- Define tkVariables -- #
        self.location = StringVar()
        self.filter = StringVar()
        self.screen = BooleanVar()
        self.binding = StringVar()

         # -- Frame 01 Widgets -- #
        self.label_01 = Label(self.frame_01,text="SAVE LOCATION: ")
        self.label_01.pack(side=LEFT,fill=X,expand=True)

        self.entry_01 = Entry(self.frame_01,textvariable=self.location, state=DISABLED)
        self.entry_01.pack(side=LEFT,fill=X,expand=True)
        
        self.location.set(self.settings[0])

        self.button_01 = Button(self.frame_01,text="...",width=3,command=lambda: self.select_location())
        self.button_01.pack(side=LEFT)

        # -- Frame 02 Widgets -- #
        self.label_02 = Label(self.frame_02,text="FILTER: ")
        self.label_02.pack(side=LEFT,fill=X,expand=True)

        self.filter_selection = OptionMenu(self.frame_02,self.filter,*self.filters)
        self.filter_selection.pack(side=LEFT,fill=X,expand=True)

        self.filter.set(self.settings[1])

        # -- Frame 03 Widgets -- #
        self.label_03 = Label(self.frame_03,text="GAME WINDOW ONLY: ")
        self.label_03.pack(side=LEFT,fill=X,expand=True)

        self.checkbutton = Checkbutton(self.frame_03, variable=self.screen)
        self.checkbutton.pack(side=LEFT,fill=X,expand=True)

        self.screen.set(self.settings[2])

        # -- Frame 04 Widgets -- #
        self.label_04 = Label(self.frame_04,text="KEY TO CAPTURE: ")
        self.label_04.pack(side=LEFT,fill=X,expand=True)

        self.binding_selection = OptionMenu(self.frame_04,self.binding,*self.bindings)
        self.binding_selection.pack(side=LEFT,fill=X,expand=True)
        
        self.binding.set(self.settings[3])

        # -- Frame 05 Widgets -- #
        self.button_02 = Button(self.frame_05,text="SUBMIT",command=lambda: self.submit())
        self.button_02.pack(side=LEFT,fill=X,expand=True)

        self.button_03 = Button(self.frame_05,text="CLOSE",command=lambda: self.close())
        self.button_03.pack(side=LEFT,fill=X,expand=True)

        self.parent.bind(self.settings[3],self.capture)

    def capture(self, event=None):
        '''
Captures the image based of the user defined settings, and adjusts the outputed image
as a result of this manipulation.
'''
        image = ImageGrab.grab() # Takes a screenshot of the screen using the pillow module.
        if self.filter.get() != None:
            pass
        else:
            # -- IF statements to determine correct opperation to act as the filter. -- #
            if self.filter.get() == "BLUR":
                image = image.filter(ImageFilter.BLUR)
            elif self.filter.get() == "CONTOUR":
                image = image.filter(ImageFilter.CONTOUR)
            elif self.filter.get() == "DETAIL":
                image = image.filter(ImageFilter.DETAIL)
            elif self.filter.get() == "EDGE_ENHANCE":
                image = image.filter(ImageFilter.EDGE_ENHANCE)
            elif self.filter.get() == "EMBOSS":
                image = image.filter(ImageFilter.EMBOSS)
            elif self.filter.get() == "FIND_EDGES":
                image = image.filter(ImageFilter.FIND_EDGES)
            elif self.filter.get() == "SMOOTH":
                image = image.filter(ImageFilter.SMOOTH)
            elif self.filter.get() == "SMOOTH_MORE":
                image = image.filter(ImageFilter.SMOOTH_MORE)
            elif self.filter.get() == "SHARPEN":
                image = image.filter(ImageFilter.SHARPEN)
        try:
            file_name = uuid.uuid4() # Create a unique code value to use as the file name.
            image.save(self.location.get()+"/"+str(file_name)+".jpg","JPEG") # Save generated image.
            showinfo("Image","Screenshot has been captured") # Display messagebox informing user it has been saved.
        except:
            showwarning("Image","Problem whilst taking screenshot.")# Display message warning user of problem.
        
    def select_location(self):
        '''
Opens up an askdirectory window to retrieve user desired save location for images.
'''
        location = askdirectory(initialdir=self.location.get())
        if location == "":
            location = "./images"
        self.location.set(location)                           

    def submit(self):
        '''
Saves settings that have been updated on the image page to the settings.txt so they remain on next
boot ready for the users next use of the program.
'''
        new_settings = [self.location.get(), self.filter.get(), self.screen.get(), self.binding.get()] # Stores new setting values within an array.

        # -- Find Old Settings -- #
        file = open("settings.txt","r") # Open settings file in read-mode.
        doc = file.readlines() # Read all lines in the file and store in array at doc.
        file.close() # Close file.

        # -- Create file with update settings -- #
        with open("temp_settings.txt","w") as file: # While opening temp_settings.txt as file.
            file.write("IMAGE_SAVE_LOCATION="+self.location.get()+"\n") # Write new setting.
            file.write("FILTER="+self.filter.get()+"\n")
            file.write("SET_IMAGE_CAPTURE="+str(self.screen.get())+"\n")
            file.write("SET_IMAGE_BIND="+self.binding.get()+"\n")
            for i in range(4,8): # Remaining are set for video settings.
                file.write(doc[i]) # Write that line in the doc file to the file.

        # -- Remove old settings and rename updated settings file. -- #
        os.remove("./settings.txt") # Delete settings.txt
        os.rename("./temp_settings.txt","./settings.txt") # Rename temp_settings.txt to settings.txt
        showinfo("Updated","Settings have been updated.") # Display info to say data has been updated.

        # -- Rebind the screenshot key -- #
        self.parent.unbind(self.settings[3])
        self.parent.bind(new_settings[3],self.capture)
            
    def close(self):
        '''
Closes the program.
'''
        sys.exit()

class Video:

    def __init__(self, page, settings, parent):
        '''
Sets up widgets that will be displayed on the Video tab of the notebook and define constants
that would be used within methods created by the call of this class.
'''
        self.page = page
        self.settings = settings
        self.parent = parent
        self.bindings = ["<F1>","<F1>","<F2>","<F3>","<F4>","<F5>","<F6>","<F7>",
                         "<F8>","<F9>","<F10>","<F11>","<F12>"]

        self.frame_01 = Frame(self.page)
        self.frame_01.pack(fill=BOTH)

        self.frame_02 = Frame(self.page)
        self.frame_02.pack(fill=BOTH)

        self.frame_03 = Frame(self.page)
        self.frame_03.pack(fill=BOTH)

        self.frame_04 = Frame(self.page)
        self.frame_04.pack(fill=BOTH)

        self.frame_05 = Frame(self.page)
        self.frame_05.pack(side=BOTTOM,fill=BOTH)

        # -- Define tkVariables -- #
        self.location = StringVar()
        self.screen = BooleanVar()
        self.binding = StringVar()
        self.montage = BooleanVar()

        # -- Frame 01 Widgets -- #
        self.label01 = Label(self.frame_01,text="SAVE LOCATION: ")
        self.label01.pack(side=LEFT,fill=X,expand=True)

        self.entry01 = Entry(self.frame_01,textvariable=self.location, state=DISABLED)
        self.entry01.pack(side=LEFT,fill=X,expand=True)

        self.location.set(self.settings[4])

        self.button_01 = Button(self.frame_01,text="...",width=3,command=lambda: self.select_location())
        self.button_01.pack(side=LEFT)

        # -- Frame 02 Widgets -- #
        self.label_02 = Label(self.frame_02,text="CAPTURE AUDIO: ")
        self.label_02.pack(side=LEFT,fill=X,expand=True)

        self.checkbutton_01 = Checkbutton(self.frame_02, variable=self.screen)
        self.checkbutton_01.pack(side=LEFT,fill=X,expand=True)

        self.screen.set(settings[5])

        # -- Frame 03 Widgets -- #
        self.label03 = Label(self.frame_03,text="KEY TO CAPTURE: ")
        self.label03.pack(side=LEFT,fill=X,expand=True)

        self.binding_selection = OptionMenu(self.frame_03,self.binding,*self.bindings)
        self.binding_selection.pack(side=LEFT,fill=X,expand=True)
        
        self.binding.set(self.settings[6])

        # -- Frame 04 Widgets -- #
        self.label_04 = Label(self.frame_04,text="MONTAGE MODE: ")
        self.label_04.pack(side=LEFT,fill=X,expand=True)

        self.checkbutton_02 = Checkbutton(self.frame_04, variable=self.montage)
        self.checkbutton_02.pack(side=LEFT,fill=X,expand=True)

        self.screen.set(settings[7])

        # -- Frame 05 Widgets -- #
        self.button_03 = Button(self.frame_05,text="SUBMIT",command=lambda: self.submit())
        self.button_03.pack(side=LEFT,fill=X,expand=True)

        self.button_04 = Button(self.frame_05,text="CLOSE",command=lambda: self.close())
        self.button_04.pack(side=LEFT,fill=X,expand=True)

        self.parent.bind(self.settings[6],self.capture)

    def capture(self, event=None):
        '''
Runs the video capture threaded module and traps any acceptions.
'''
        try:
            Video_Capture(self) # Calls Video_Capture Class and runs containing program.
        except:
            showwarning("Video","Issue when creating video.") # Runs this if error occurs during video capture.
    
    def select_location(self):
        '''
Opens up an askdirectory window to retrieve user desired save location for videos.
'''
        location = askdirectory(initialdir=self.location.get()) # Store location of searched file.
        if location == "": # Resets to default if no directory is selected.
            location = "./videos"
        self.location.set(location) 

    def submit(self):
        '''
Saves settings that have been updated on the video page to the settings.txt so they remain on next
boot ready for the users next use of the program.
'''
        new_settings = [self.location.get(), self.screen.get(), self.binding.get()]

        file = open("settings.txt","r")
        doc = file.readlines()
        file.close()

        with open("temp_settings.txt","w") as file:
            for i in range(4):
                file.write(doc[i])
            file.write("VIDEO_SAVE_LOCATION="+self.location.get()+"\n")
            file.write("CAPTURE_AUDIO="+str(self.screen.get())+"\n")
            file.write("SET_IMAGE_BIND="+self.binding.get()+"\n")
            file.write("MONTAGE_MODE="+str(self.montage.get())+"\n")

        os.remove("./settings.txt")
        os.rename("./temp_settings.txt","./settings.txt")

        showinfo("Updated","Settings have been updated.")
        
        self.parent.unbind(self.settings[6])
        self.parent.bind(new_settings[2],self.capture)
    
    def close(self):
        '''
Closes the program.
'''
        sys.exit()

class About:

    def __init__(self, page):
        '''
Displays the widgets on the about page used to show what version of the program is running,
the author and thanks to author of extra program.
'''
        self.page = page
        
        self.credits_frame = Frame(self.page)
        self.credits_frame.pack(pady=10)

        self.author = Label(self.credits_frame, text="Author: William Read")
        self.author.pack(pady=10)

        self.special_thanks = Label(self.credits_frame,
                                    text="""
Special Thanks: FFMPEG - https://www.ffmpeg.org/
         for video codec API systems.
""")
        self.special_thanks.pack(pady=10)

        self.version = Label(self.credits_frame, text="Version: 1.0")
        self.version.pack(pady=10)
        
        self.copyright = Label(self.credits_frame, text="Copyright ©2016")
        self.copyright.pack(pady=10)


# -- Code Run if this file is run first -- #
if __name__ == "__main__":
    if os.path.isfile("./settings.txt") == False: # Checks to see if settings.txt exists.
        Generate_Defaults() # Runs if settings.txt doesn't exist.
    parent = Tk() # Set up Tk class and define as instance parent.
    Main(parent) # Call the class Main.
    parent.mainloop() # Set a callback function on the parent instance.
