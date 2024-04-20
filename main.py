"""
This is a main module for the program.
Author: Vasiliy
Date: 2024-04-20
Version: 0.0.1
"""
import time
import math
import keyboard
from utils import take_screenshot
from player import fight, go_to_start


def main() -> None:
    print("Click on the mob HP bar and press h \n")
    target = take_screenshot()
    n = 1
    print("Enter time in seconds for attack sequence(e.g 60)\n")
    attack_timer = int(input())
    while not keyboard.is_pressed('q'):
        start_time = math.ceil(time.time())
        end_time = start_time
        while end_time - start_time <= attack_timer:
            if keyboard.is_pressed('q'):
                exit(0)
            fight(target, n)
            end_time = math.ceil(time.time())
            n += 1
            print(end_time - start_time)
        go_to_start()


if __name__ == '__main__':
    main()
