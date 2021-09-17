import time

import cv2
import keyboard
import numpy as np
import pyautogui as py2
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


time.sleep(2)

while keyboard.is_pressed('q') == False:

    im1 = py2.screenshot(region=(955, 425, 400, 300))
    im1.save(r"./Area.png")

    white = py2.screenshot(region=(475, 810, 5, 5))
    r, g, b = white.getpixel((1, 1))

    image = cv2.imread('Area.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canned = cv2.Canny(image, 100, 100)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.3, 200, param1=90, param2=100)
    circles2 = cv2.HoughCircles(canned, cv2.HOUGH_GRADIENT, 1.4, 350, param1=90, param2=98)


    if r == 255 and g == 255 and b == 255:

        click(590, 830)
        time.sleep(1)

        if circles is not None:

            circles = np.round(circles[0, :]).astype("int")

            for (x, y, r) in circles:
                print(x, y, r)
                click(x + 955, y + 425)
                break

        elif circles2 is not None:

            circles2 = np.round(circles2[0, :]).astype("int")

            for (x, y, r) in circles2:
                print(x, y, r)
                click(x + 955, y + 425)
                break

        time.sleep(1)

    else:

        if circles is not None:

            circles = np.round(circles[0, :]).astype("int")

            for (x, y, r) in circles:
                print(x, y, r)
                click(x + 955, y + 425)
                break

        elif circles2 is not None:

            circles2 = np.round(circles2[0, :]).astype("int")

            for (x, y, r) in circles2:
                print(x, y, r)
                click(x + 955, y + 425)
                break

        time.sleep(1)
