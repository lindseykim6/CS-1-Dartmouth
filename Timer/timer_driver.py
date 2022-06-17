# File Name: timer_driver.py
# Author Name: Lindsey Kim
# Date: 10/14/2020
# Course: COSC 1
# Short Description: This tests the timer class by counting down from 1:30:00
#

from timer import *


# This counts down the time from the given timer object until it reaches 00:00:00
def timer_tester(timer):
    while not timer.is_zero():
        print(timer)
        timer.tick()  # ticks the time by 1
    print(timer)  # prints the time 00:00:00


# creates a timer object
timer_one = Timer(1, 30, 00)


timer_tester(timer_one)
