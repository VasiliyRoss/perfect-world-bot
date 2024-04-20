import time
import keyboard
import pyautogui
from utils import locate_on_screen, hold_key, left_click_with_alt, left_click


def hit_button(button) -> None:
    pyautogui.keyDown(button)
    time.sleep(0.1)
    pyautogui.keyUp(button)


def attack(delay) -> None:
    hit_button('f1')
    time.sleep(delay)


def loot(i) -> None:
    for i in range(i):
        hit_button('f2')
        time.sleep(0.7)


def find_enemy(screenshot_file) -> None:
    target_status = "seeking"
    while target_status == "seeking":
        try:
            if pyautogui.locateOnScreen(screenshot_file) is not None:
                target_status = "found"
        except pyautogui.ImageNotFoundException:
            hit_button('\t')
            time.sleep(0.5)
        print("Enemy", target_status)
        if keyboard.is_pressed('q'):
            exit(0)


def drink_potion() -> None:
    hit_button('f3')


def fight(screenshot_file, n) -> None:
    find_enemy(screenshot_file)
    for i in range(6):
        attack(1)
    loot(4)
    if n % 3 == 0:
        drink_potion()
    if n % 10 == 0:
        go_to_start()


def fly() -> None:
    hit_button('f4')


def take_safe_height() -> None:
    hold_key('space', 20)


def open_map() -> None:
    hit_button('m')
    time.sleep(0.5)


def set_route(x, y) -> None:
    left_click_with_alt(x, y)
    time.sleep(0.5)


def go_to_start() -> None:
    open_map()
    destination = locate_on_screen('public/map_start.png', 0.3)
    set_route(destination[0], destination[1]+30)
    open_map()


if __name__ == '__main__':
    time.sleep(2)
    go_to_start()
