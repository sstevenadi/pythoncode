from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('Clicker.png',region=(975,380,450,375), confidence = 0.75) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
