from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
from PIL import Image
import pytesseract

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def hit_button(button):
    pyautogui.keyDown(button)
    time.sleep(0.1)
    pyautogui.keyUp(button)

def attack():
    hit_button('f1')
    time.sleep(10)

def take_screenshot(screenshot_file):
    print("Waiting...")
    keyboard.wait('h')

    mouse_x, mouse_y = pyautogui.position()

    screenshot_width = 200
    screenshot_height = 20

    left = mouse_x - screenshot_width // 2
    top = mouse_y - screenshot_height // 2

    screenshot = pyautogui.screenshot(region=(left, top, screenshot_width, screenshot_height))
    screenshot.save(screenshot_file)
    print("Mob has been saved to ", screenshot_file)

def start(screenshot_file):
    time.sleep(2)
    print("THE PROGRAM IS RUNNING, screenshot is in", screenshot_file)
    while not keyboard.is_pressed('esc'):
        try:
            if pyautogui.locateOnScreen(screenshot_file) is not None:
                print("Image found")
                attack()
                time.sleep(5)
        except pyautogui.ImageNotFoundException:
            print("Image not found")
            hit_button('\t')
    print("EXITING")
    exit(0)

def locate_on_screen(screenshot_file):
    res = pyautogui.locateOnScreen(screenshot_file)
    print(res)

def main():
    screenshot_file = 'mob.png'

    print("Click on the mob HP bar and press h \n")
    take_screenshot(screenshot_file)
    start(screenshot_file)
    #locate_on_screen(screenshot_file)

main()