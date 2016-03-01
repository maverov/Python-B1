import subprocess
import numpy as np
from PIL import Image

rate = 1
outf = 'test.avi'

cmdstring = ('ffmpeg.exe',
             '-y',
             '-r', '%d' % rate,
             '-f','image2pipe',
             '-vcodec', 'mjpeg',
             '-i', 'pipe:', 
             '-vcodec', 'libxvid',
             outf
             )
p = subprocess.Popen(cmdstring, stdin=subprocess.PIPE, shell=False)

for i in range(10):
    im = Image.fromarray(np.uint8(np.random.randn(100,100)))
    p.stdin.write(im.tostring('jpeg','L'))
    #p.communicate(im.tostring('jpeg','L'))

p.stdin.close()
