from time import sleep
from key import *
from pynput.keyboard import Key, Controller


keyboard = Controller()

keyboard.press(windowkey) 
keyboard.release(windowkey)
sleep(0.6)
keyboard.type(cmd)
sleep(0.6)
keyboard.press(enter) 
keyboard.release(enter)
sleep(1.3)
keyboard.type("shutdown /s")
sleep(0.6)
keyboard.press(enter) 
keyboard.release(enter)