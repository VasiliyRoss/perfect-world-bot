import win32api, win32con
import time
import pyautogui
import keyboard


def locate_on_screen(screenshot_file, confidence):
    location = pyautogui.locateOnScreen(screenshot_file, grayscale=False, confidence=confidence)
    return location


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


def left_click(x, y) -> None:
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def hold_key(key, timer) -> None:
    keyboard.press(key)
    time.sleep(timer)
    keyboard.release(key)

def left_click_with_alt(x, y) -> None:
    keyboard.press('alt')
    time.sleep(0.5)
    left_click(x, y)
    time.sleep(0.5)
    keyboard.release('alt')



