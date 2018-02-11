from PIL import ImageGrab
from PIL import ImageOps
import os
import time
from numpy import *
import win32api, win32con
import vlc

warTarget = (1877, 376, 1886, 385)
corporation = (1877, 464, 1886, 473)
alliance = (1877, 486, 1886, 495)
excellent_Standing = (1877, 508, 1886, 517)
good_Standing = (1877, 530, 1886, 539)
minus5_standing = (1877, 574, 1886, 583)
killright_Standing = (1877, 640, 1886, 649)
terrible_Standing = (1877, 662, 1886, 671)
bad_standing = (1877, 684, 1886, 693)
bellowzero_standing = (1877, 728, 1886, 737)
neutral_standing = (1877, 750, 1886, 759)
neutral_doublecheck = (1877, 794, 1886, 803)

def grab(box):
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print(a)
    return a

def main():
    pass

if __name__ == '__main__':
    main()
