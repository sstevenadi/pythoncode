import pyautogui
import time

time.sleep(2)

im1 = pyautogui.screenshot(region=(930,425,400,350))
im1.save(r"./Area.png")