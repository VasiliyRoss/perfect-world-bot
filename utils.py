import win32api, win32con
import time
import pyautogui
import keyboard
from player import attack, find_enemy


def locate_on_screen(screenshot_file):
    res = pyautogui.locateOnScreen(screenshot_file)
    print(res)


def take_screenshot() -> str:
    print("Waiting...")
    keyboard.wait('h')
    screenshot_file = 'mob.png'

    mouse_x, mouse_y = pyautogui.position()

    screenshot_width = 200
    screenshot_height = 20

    left = mouse_x - screenshot_width // 2
    top = mouse_y - screenshot_height // 2

    screenshot = pyautogui.screenshot(region=(left, top, screenshot_width, screenshot_height))
    screenshot.save(screenshot_file)
    print("Mob has been saved to ", screenshot_file)
    return screenshot_file


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def start(screenshot_file):
    attack(3)
    find_enemy(screenshot_file)
