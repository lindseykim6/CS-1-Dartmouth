# File Name: counter.py
# Author Name: Lindsey Kim
# Date: 10/14/2020
# Course: COSC 1
# Short Description: This is a counter class that creates a counter object that counts down from a certain number from a
# limit
#

class Counter:
    def __init__(self, limit, initial=0, min_digits=1):
        self.limit = limit
        if 0 <= initial <= (limit-1):  # makes the value the initial if it is between 0 and the limit
            self.value = initial
        else:
            print("ERROR")
            self.value = (limit-1)
        self.min_digits = min_digits  # makes the value the limit-1 if it is out of bounds

    def get_value(self):
        return self.value

    def __str__(self):
        # returns a string with the right amount of digits
        return '0'*(self.min_digits-len(str(self.value)))+str(self.value)

    def tick(self):
        if self.value > 0:
            self.value -= 1
            return False
        else:
            self.value = self.limit-1
            return True
