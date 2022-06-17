# File Name: counter_driver.py
# Author Name: Lindsey Kim
# Date: 10/14/2020
# Course: COSC 1
# Short Description: This tests the counter class
#

from counter import *


# This counts down the numbers from a certain number
def string_test(counter):
    for i in range(0, 100):
        print("Testing __str__ function...")
        print("Iteration " + str(i+1) + ": " + str(counter))
        print("")
        print("Testing get value function...")
        print("Iteration " + str(i + 1) + ": " + str(counter.get_value()))
        print("")
        counter.tick()  # tests tick


counter_one = Counter(60, 5, 3)
string_test(counter_one)

counter_two = Counter(60, 60, 3)
string_test(counter_two)
