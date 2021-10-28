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

    v = np.median(image)

    upper, im = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    lower = 0.5*upper

    canned = cv2.Canny(im, lower, upper)
    
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.3, 200, param1=90, param2=60)
    circles2 = cv2.HoughCircles(canned, cv2.HOUGH_GRADIENT, 1.3, 350, param1=90, param2=60)
    circles3 = cv2.HoughCircles(canned, cv2.HOUGH_GRADIENT, 1.4, 350, param1=90, param2=60)

    if r == 255 and g == 255 and b == 255:

        click(590, 830)
        time.sleep(1)

        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
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

        time.sleep(1)
