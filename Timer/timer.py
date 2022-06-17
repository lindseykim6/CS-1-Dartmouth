# File Name: timer.py
# Author Name: Lindsey Kim
# Date: 10/14/2020
# Course: COSC 1
# Short Description: This is a timer class that creates a timer object that counts down from a certain time
#

from counter import *


class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(24, hours, 2)  # makes a counter object for hours in a day
        self.minutes = Counter(60, minutes, 2)  # makes a counter object for minutes in a day
        self.seconds = Counter(60, seconds, 2)  # makes a counter object for seconds in a day

    def __str__(self):
        # returns a string in the format hh:mm:ss
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    def tick(self):
        if self.seconds.tick():  # if seconds are at 00
            if self.minutes.tick():  # if minutes are at 00
                self.hours.tick()  # when hours are at 00

    def is_zero(self):
        # returns true if time is at 00:00:00
        if self.hours.get_value() == 0:
            if self.minutes.get_value() == 0:
                if self.seconds.get_value() == 0:
                    return True
