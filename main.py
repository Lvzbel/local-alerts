from PIL import ImageGrab
from PIL import ImageOps
import os
import time
from numpy import *
import vlc

"""
Hard coded coordinates, for now this cords will be unique to my UI setup and monitor resolution which is 1440p
The Following cords being store are:
*Main Client Local = mainLocal
*Scout Overlay Local = scoutLocal
*D-Scan Signatures = scanCord
"""
# D-Scan Coordinates:
scanCord = [(2156, 894), (2156, 916), (2156, 938), (2156, 960), (2156, 982), (2156, 1004),
            (2156, 1026), (2156, 1048), (2156, 1070), (2156, 1092), (2156, 1114), (2156, 1136),
            (2156, 1158), (2156, 1180), (2156, 1202), (2156, 1224), (2156, 1246), (2156, 1268),
            (2156, 1290), (2156, 1312), (2156, 1334), (2156, 1356), (2156, 1378)]

# Main Client Local Coordinates:
homeLocal = (1629, 671, 1846, 1048)

# Scout Overlay Local Coordinates:
scoutLocal = (1858, 624, 2139, 1119)

# Testing Coords
testLocal = (229, 690, 422, 1043)

home_alert = os.getcwd() + r'''\audio\home_alert.mp3'''
scout_alert = os.getcwd() + r'''\audio\scout_alert.mp3'''
welcome_message = os.getcwd() + r'''\audio\welcome.mp3'''


def screenGrab():
    im = ImageGrab.grab()
    im.save(os.getcwd() + '//full_snap__' +str(int(time.time())) + '.png', 'PNG')
    return im

def grab(box):
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print(a)
    return a


def d_scan_check(cord, img):
    """
    This function will iterate through all 23 different possible signatures
    :param cord: Position of the pixel check example: scanCord.scan_001
    :param img: Screenshot taken by screenGrab
    :return: If a new signature is detected (color: (225, 0, 0)it will return 1
    """
    unknow_sig = (225, 0, 0)
    aler_sig = 0
    for num in range(0, 23):
        color = img.getpixel(cord[num])
        #print(color)
        if color == unknow_sig:
            aler_sig += 1
    return aler_sig

def playAudio(file):
    p = vlc.MediaPlayer(file)
    p.play()
    time.sleep(2)



def main():
    while True:
        # time.sleep(5)
        # screenShot = screenGrab()
        # new_sig_alert = d_scan_check(scanCord, screenShot)
        # if new_sig_alert == 1:
        #     print("ALERT NEW SIGNATURE HAS SPAWNED")
        # else:
        #     print("nothing found")
        # break
        p = vlc.MediaPlayer(welcome_message)
        p.play()
        time.sleep(12)
        old_local_home = grab(homeLocal)
        old_local_scout = grab(scoutLocal)
        while True:
            #Scout Lookout loop
            new_local_scout = grab(scoutLocal)
            if old_local_scout != new_local_scout:
                playAudio(scout_alert)
                # print('Scout')
                #print(old_local_scout)
                #print(new_local_scout)
                old_local_scout = new_local_scout
                pass

            #Home System Local Loop
            new_local_home = grab(homeLocal)
            if old_local_home != new_local_home:
                playAudio(home_alert)
                # print('Home')
                # print(old_local_home)
                # print(new_local_home)
                old_local_home = new_local_home
                pass


if __name__ == '__main__':
    main()
