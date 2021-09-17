import time

import cv2
import pyautogui as py2
import numpy as np
import PIL

time.sleep(3)

# area = py2.screenshot()
# area.save(r"D:\WORK\UDINUS\ProjectPY\PetPals\Area.png")

image = cv2.imread('Area.png')
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canned = cv2.Canny(image, 100, 100)
# canned = cv2.Canny(image, 100, 0)

# cv2.imshow("canny", canned)
# cv2.imshow('abu',gray)
# cv2.waitKey(0)

# detect circles in the image
circles = cv2.HoughCircles(canned, cv2.HOUGH_GRADIENT, 1.4, 350, param1=90, param2=98)
# ensure at least some circles were found
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")
    # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    # show the output image
    cv2.imshow("output", np.hstack([output]))
    print(circles)
    cv2.waitKey(0)
