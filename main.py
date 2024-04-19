"""
This is a main module for the program.
Author: Vasiliy
Date: 2022-04-20
Version: 1.0
License: MIT
"""

import keyboard
from utils import take_screenshot, start


def main() -> None:
    print("Click on the mob HP bar and press h \n")
    screenshot_file = take_screenshot()
    while not keyboard.is_pressed('q'):
        if keyboard.is_pressed('q'):
            break
        start(screenshot_file)


if __name__ == '__main__':
    main()
