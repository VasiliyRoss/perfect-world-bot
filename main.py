"""
This is a main module for the program.
Author: Vasiliy
Date: 2024-04-20
Version: 0.0.1
"""

import keyboard
from utils import take_screenshot
from player import fight


def main() -> None:
    print("Click on the mob HP bar and press h \n")
    target = take_screenshot()
    n = 0
    while not keyboard.is_pressed('q'):
        if keyboard.is_pressed('q'):
            break
        fight(target, n)
        n += 1


if __name__ == '__main__':
    main()
