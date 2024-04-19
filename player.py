import time
import pyautogui


def hit_button(button) -> None:
    pyautogui.keyDown(button)
    time.sleep(0.1)
    pyautogui.keyUp(button)


def attack(delay) -> None:
    hit_button('f1')
    time.sleep(delay)


def find_enemy(screenshot_file) -> None:
    enemy = "seeking"
    while enemy == "seeking":
        try:
            if pyautogui.locateOnScreen(screenshot_file) is not None:
                print("Enemy found")
                enemy = "found"
        except pyautogui.ImageNotFoundException:
            print("Enemy not found")
            hit_button('\t')
            time.sleep(0.5)
