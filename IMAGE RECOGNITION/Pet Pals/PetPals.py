# Location 475,275,950,550

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

# Area Click 975,380,450,375
# Egg 232,216,184 Loc 560,830,765,75 (1282,852)
# Border 480,860
# Item 600,860

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    


while keyboard.is_pressed('q') == False:
    area = pyautogui.screenshot(region=(975,380,450,375))
    
    white = pyautogui.screenshot(region=(480,840,40,40))
    white.save(r"D:\WORK\UDINUS\ProjectPY\ImageRecognition\Pet Pals\White.png")
    
    r1,g1,b1 = white.getpixel((5,5))

    width, height = area.size

    if r1 == 255 and g1 == 255 and b1 == 255:
        print ("I see it")
        click(600,850)
        time.sleep(0.25)
        for x in range (0,width,5):
            for y in range(0,height,5):
                r,g,b = area.getpixel((x,y))
                if r in (5,range(170,255)):
                    click(x+975, y+380)
                    time.sleep(0.25)
                    break
                if b in (5,range(170,255)):
                    click(x+975, y+380)
                    time.sleep(0.25)
                    break
                if g in (5,range(170,255)):
                    click(x+975, y+380)
                    time.sleep(0.25)
                    break
    else:
        print ("Not see it")
        for x in range (0,width,5):
            for y in range(0,height,5):
                r,g,b = area.getpixel((x,y))
                if r in (5,range(170,255)):
                    click(x+975, y+380)
                    time.sleep(0.25)
                    break
                if b in (5,range(170,255)):
                    click(x+975, y+380)
                    time.sleep(0.25)
                    break
                if g in (5,range(170,255)):
                    click(x+975, y+380)
                    time.sleep(0.25)
                    break
