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

turned_on = False
buy_upgrades_turned_on = False

def click_cookie():
    global turned_on
    start = time.time()
    while(1):
        if turned_on:
            pyautogui.click(264, 468, 2)

def buy_buildings():
    while(1):
        if False:
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
def buy_upgrades():
    while(1):
        if buy_upgrades_turned_on:
            pyautogui.click(1581, 219)
def on_press(key):
    try:
        print('{0}'.format(
            key.char))
    except AttributeError:
        print('{0}'.format(
            key))

def on_release(key):
    global turned_on
    global buy_upgrades_turned_on
    if key == keyboard.Key.space:
        turned_on = not turned_on

    try:
        if key.char == 'z':
            buy_upgrades_turned_on = not buy_upgrades_turned_on
    except AttributeError:
        pass

    if key == keyboard.Key.esc:
        # Stop listener
        sys.exit()

# Spin up clicking threads.
_thread.start_new_thread(click_cookie, ())
_thread.start_new_thread(buy_buildings, ())
_thread.start_new_thread(buy_upgrades, ())


# Collect events until released

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()