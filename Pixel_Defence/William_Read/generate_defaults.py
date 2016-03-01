__author__ = "William Read"
__revision__ = "01/03/2016 07:36:18"
__version__ = "1.0"

class Generate_Defaults:

    def __init__(self):
        '''
Generates a default settings.txt file if it doesn't exist allowing the
program to function normally.
'''
        file = open("settings.txt","w") # Opens settings.txt
        file.write("""IMAGE_SAVE_LOCATION=./images
FILTER=None
SET_IMAGE_CAPTURE=False
SET_IMAGE_BIND=<F8>
VIDEO_SAVE_LOCATION=./videos
CAPTURE_AUDIO=False
SET_VIDEO_BIND=<F9>
MONTAGE_MODE=False
            """) # Writes data in the file.
        file.close() # Closes the file.

# -- Code is run if this is the main file. -- #
if __name__ == "__main__":
    Generate_Defaults() # Calls the Class Generate_Defaults.
