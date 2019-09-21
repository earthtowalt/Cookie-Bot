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
import sys, os
from pynput import keyboard
import _thread

flags = {}
flags["buy things"] = False
flags["click cookie"] = False


def click_cookie():
    global flags
    while(True):
        if flags['click cookie']:
            pyautogui.click(-1636, 157, 50)
            time.sleep(0.1)

def buy_things():
	global flags
	while(True):
		time.sleep(3)
		if flags['buy things']:
			pyautogui.click(-291,-76, 4) # upgrade
			time.sleep(1)
			pyautogui.click(-185,572,4)
			time.sleep(.1)
			pyautogui.click(-185,500,4)
			time.sleep(.1)
			'''
			## balanced
			time.sleep(.1)
			pyautogui.click(-185,410,4)
			time.sleep(.1)
			pyautogui.click(-185,350,4)
			time.sleep(.1)
			pyautogui.click(-185,285,4)
			time.sleep(.1)
			pyautogui.click(-185,220,4)
			time.sleep(.1)
			pyautogui.click(-185,150,4)
			time.sleep(.1)
			pyautogui.click(-185,90,4)
			time.sleep(.1)
			pyautogui.click(-185,30,4)
			time.sleep(.1)
		'''
		time.sleep(60 * 10)
def on_press(key):
	pass 
	'''
    try:
        print('{0}'.format(
            key.char))
    except AttributeError:
        print('{0}'.format(
            key))'''

def on_release(key):
	global flags

	try:
		if key.char == 'c':
			flags['click cookie'] = not flags['click cookie']
		if key.char == 'b':
			flags['buy things'] = not flags['buy things']
		if key.char == 'c' or key.char == 'b':
			os.system('cls')
			print('clicking cookies: ' + str(flags['click cookie']))
			print('buying things: ' + str(flags['buy things']))
			
	except AttributeError:
		pass

	# Stop listener
	if key == keyboard.Key.esc:
		sys.exit()



if __name__ == "__main__":
    # Spin up clicking threads.
    _thread.start_new_thread(click_cookie, ())
    _thread.start_new_thread(buy_things, ())


    # Collect events until released

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()