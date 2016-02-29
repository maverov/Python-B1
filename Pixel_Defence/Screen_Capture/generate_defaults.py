class Generate_Defaults:

    def __init__(self):
        file = open("settings.txt","a")
        file.write("""IMAGE_SAVE_LOCATION=./images
FILTER=None
SET_IMAGE_CAPTURE=False
SET_IMAGE_BIND=<F8>
VIDEO_SAVE_LOCATION=./videos
CAPTURE_AUDIO=False
SET_VIDEO_BIND=<F9>
            """)
        file.close()

if __name__ == "__main__":
    pass
