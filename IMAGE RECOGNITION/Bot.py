import random
import time

import keyboard
import pyautogui
import win32api
import win32con
from pyautogui import *


# Tile 1 X: 590 Y: 450 RGB: (0, 0, 0)
# Tile 2 X: 685 Y: 450 RGB: (0, 0, 0)
# Tile 3 X: 780 Y: 450 RGB: (0, 0, 0)
# Tile 4 X: 865 Y: 450 RGB: (0, 0, 0)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed('q'):

    if pyautogui.pixel(581, 400)[0] == 0:
        click(581, 400)
    if pyautogui.pixel(685, 400)[0] == 0:
        click(685, 400)
    if pyautogui.pixel(780, 400)[0] == 0:
        click(780, 400)
    if pyautogui.pixel(865, 400)[0] == 0:
        click(865, 400)
