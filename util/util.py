import os
from PyQt4.QtGui import *

def load_image(name):
    load_string = os.path.join('res/img', name)
    if os.path.isfile(load_string):
        return QImage(load_string)
    else:
        print "Error loading image"
