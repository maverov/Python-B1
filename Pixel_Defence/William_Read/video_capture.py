__author__ = "William Read"
__revision__ = "01/03/2016 07:35:28"
__version__ = "1.0"

# -- Imports directed for tkinter calls within program -- #
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo

# -- Import base modules: subprocess, numpy, queue, uuid, threading, time. -- #
import subprocess, numpy, queue, uuid, threading, time

# -- PIL Module used for image manipulation -- #
from PIL import Image, ImageGrab

class Video_Capture:

    def __init__(self, data):
        '''Captures visuals from Desktop screen using the FFMPEG API'''
        if data.montage.get() == False:
            self.frame_rate = 10
        else:
            self.frame_rate = 60
            
        out_file = data.location.get()+"/"+str(uuid.uuid4())+".avi" # Creates the name and location the result video is stored.
        ffmpeg_location = "./ffmpeg/bin/ffmpeg.exe" # Sets the location of the ffmpeg.exe file.
        command_string = (ffmpeg_location, "-y",
                          "-r", "%d" % self.frame_rate,
                          "-f", "image2pipe",
                          "-vcodec", "mjpeg",
                          "-i", "pipe:",
                          "-vcodec", "libxvid",
                          out_file) # Stores the command that will be run through CMD to boot.

        self.process = subprocess.Popen(command_string,stdin=subprocess.PIPE,shell=False) # Runs the command_string that has been defined.

        # -- Sets up the Toplevel window which allows the user to record.
        self.toplevel = Toplevel()
        self.toplevel.attributes("-topmost",True) # Forces window to appear above all other active windows.
        self.toplevel.title("Minority Screen Capture")
        self.toplevel.wm_iconbitmap("./icon.ico")

        # -- Defines initial constants. -- #
        self.record = False
        self.time = "0"
        
        self.record_stop_button = Button(self.toplevel,text="Record",
                                    command=lambda: self.film_screen())
        self.record_stop_button.pack(side=LEFT)

        self.timer = Label(self.toplevel,text="Time Elapsed: "+self.time)
        self.timer.pack(side=LEFT)

        self.toplevel.mainloop()
    
    def film_screen(self):
        '''
Sets the value of if the file is being currently being recorded and sets the threads that are being used, as well
as update the button to show the user that that the system is being recorded.
'''
        self.record = not self.record
        if self.record == True:
            self.record_stop_button.config(text="Recording")
            self.record_stop_button.update()
            
            self.record_thread_stop = threading.Event() # Creates factory new objects
            self.timer_thread_stop = threading.Event()  
            
            self.record_thread = threading.Thread(target=self.capture_screen) # Initialises target and arguements for record_thread.
            self.timer_thread = threading.Thread(target=self.timer_algorithm) # Initialises target and arguements for timer_thread.
            
            self.record_thread.start() # Starts the record_thread routine
            self.timer_thread.start() # Starts the timer_thread routine
            
            self.queue = queue.Queue() # Initialises active Queue.
            Thread_Tasks(self.queue).start() # Starts all the values within a queue in defined in the class Thread_Tasks
            self.toplevel.after(100,self.queue_processing) # Checks the queue processing every 100ms
        else:
            self.record_thread_stop.set() # Stops record_thread.
            self.timer_thread_stop.set() # Stops timer_thread.
            self.process.stdin.close() # Closes the process input PIPE that has been opened.
            self.toplevel.destroy() # Destroys the Toplevel Window.
            showinfo("Video","Video has successfully captured.") # Display info window to let user know video has been saved.

    def queue_processing(self):
        try:
            pass # Events relative to key presses on the GUI placed in here.
        except queue.Empty:
            self.toplevel.after(100,self.queue_processing) # Prevents hang when Queue is empty.
    
    def capture_screen(self):
        '''
Creates grabs of the images of the screen creates a raw string value of the data. Then passes this value back to
be stored as a new frame in the process.
'''
        while self.record: # While the user hasn't stopped the recording.
            try:
                image = ImageGrab.grab() # Take the image.
                data = image.tostring("jpeg","RGB") # Convert the frame from a jpeg to a string using "RGB" values.
                self.process.stdin.write(data) # Returns process standard input and writes out the value.
            except:
                pass # Skips a frame if there is an issue with the conversion.

    def timer_algorithm(self):
        '''
Performs a counter which increases by one after each second, allowing the user to know how long the video being
stored currently is.
'''
        counter = 0 # Initialise the counter as 0.
        while self.record: # While the user hasn't stopped recording.
            self.time = str(counter) # Sets the value of the timer as a string.
            self.timer.config(text="Time Elapsed: "+self.time) # Update value of the label.
            self.timer.update_idletasks()
            time.sleep(1) # Pauses the program for 1 second.
            counter += 1 # Increase counter by 1.

class Thread_Tasks(threading.Thread):
    '''Inherit all attributes from the class Thread from module threading.'''
    
    def __init__(self,queue_data):
        '''Initialise a thread using all values within the queue.'''
        threading.Thread.__init__(self)
        self.queue = queue_data #Sets all events from callback to be stored in the class.

if __name__ == "__main__":
    pass
