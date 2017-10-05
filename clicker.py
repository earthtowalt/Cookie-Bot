"""
An extremely simple bot that plays cookie clicker on an assumed 1080p resolution monitor with cookie clicker open in a full web browser.
To use, go to this page http://orteil.dashnet.org/cookieclicker/ in full screen and start the program.

Controls:
Z: Clicks the cookie.
X: Buys new buildings.
C: Buys Upgrades
ESC: Closes out of the program.

These keys can be pressed from any location on your OS and are recognized using the same tech that is used for key loggers.
"""

import pyautogui
import time
import sys
from pynput import keyboard
import _thread

flags = {}
flags["buy upgrades"] = False
flags["click cookie"] = False
flags["buy buildings"] = False

def click_cookie():
    global flags
    while(True):
        if flags['click cookie']:
            pyautogui.click(264, 468, 2)
            time.sleep(0.00002)

def buy_buildings():
    global flags
    while(True):
        if flags['buy buildings']:
            pyautogui.click(1736, 354)
            pyautogui.click(1643, 427)
            pyautogui.click(1734, 507)
            pyautogui.click(1750, 562)
            pyautogui.click(1750, 630)
            pyautogui.click(1659, 715)
            pyautogui.click(1736, 808)
            pyautogui.click(1716, 853)
            pyautogui.click(1752, 946)
            pyautogui.click(1701, 999)
            time.sleep(5)
def buy_upgrades():
    while(True):
        if flags['buy upgrades']:
            pyautogui.click(1581, 219)
            time.sleep(5)
def on_press(key):
    try:
        print('{0}'.format(
            key.char))
    except AttributeError:
        print('{0}'.format(
            key))

def on_release(key):
    global flags

    try:
        if key.char == 'z':
            flags['click cookie'] = not flags['click cookie']
        if key.char == 'x':
            flags['buy buildings'] = not flags['buy buildings']
        if key.char == 'c':
            flags['buy upgrades'] = not flags['buy upgrades']
    except AttributeError:
        pass

    # Stop listener
    if key == keyboard.Key.esc:
        
        sys.exit()



if __name__ == "__main__":
    # Spin up clicking threads.
    _thread.start_new_thread(click_cookie, ())
    _thread.start_new_thread(buy_buildings, ())
    _thread.start_new_thread(buy_upgrades, ())


    # Collect events until released

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()