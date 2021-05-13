from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con

while 1:
    area = pyautogui.screenshot(region=(680,820,560,70))
    area.save(r"D:\WORK\UDINUS\ProjectPY\ImageRecognition\Bar.png")
    if pyautogui.locateOnScreen('Tomat.png',region=(920,640,156,94), confidence = 0.8) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
