#Require to install images2gif
#Place pictures on the same folder ( for this code)
#Install python-imaging instead of PIL

from images2gif import writeGif
from PIL import Image
import os

file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))
#['animationframa.png', 'animationframb.png', 'animationframc.png', ...] "

images = [Image.open(fn) for fn in file_names]

size = (640,480)
for im in images:
    im.thumbnail(size, Image.ANTIALIAS)

print writeGif.__doc__

filename = "tweet.GIF"
writeGif(filename, images, duration=0.5)

