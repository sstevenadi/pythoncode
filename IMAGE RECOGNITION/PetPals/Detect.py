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

hsv = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
gray = cv2.cvtColor(hsv, cv2.COLOR_RGB2GRAY)

v = np.median(image)

upper, thresh_im = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
lower = 0.5*upper

canned = cv2.Canny(thresh_im, lower, upper)
# canned = cv2.Canny(image, 100, 0)

# cv2.imshow("canny", canned)
# cv2.imshow('abu',gray)
# cv2.waitKey(0)

# detect circles in the image
circles = cv2.HoughCircles(canned, cv2.HOUGH_GRADIENT, 1.4, 350, param1=50, param2=50)
# ensure at least some circles were found
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")
    # loop over the (x, y) coordinates and radius of the q
    for (x, y, r) in circles:
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    # show the output image
    cv2.imshow("output", np.hstack([output]))
cv2.imshow("gray", gray)
cv2.imshow("can", canned)
cv2.imshow("hsv", hsv)
print(circles)
cv2.waitKey(0)
