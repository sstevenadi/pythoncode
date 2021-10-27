import time
import keyboard
import win32api
import win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

time.sleep(2)

while keyboard.is_pressed("q") == False:

    for i in range(4):
        time.sleep(0.2)
        click(960, 390)

    time.sleep(0.2)
    click(920, 885)

    time.sleep(0.2)
    click(960, 390)

    time.sleep(0.2)
    click(835, 880)
