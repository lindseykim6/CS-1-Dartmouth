# File Name: string_art.py
# Author Name: Lindsey Kim
# Date: 9/17/2020
# Course: COSC 1
# Short Description: This creates a work of string art that changes colors from blue to green.
#

from cs1lib import *


def make_background_black():
    set_clear_color(0, 0, 0)
    clear()


def string_art(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, strings):
    f = 0  # f is the fraction of the stick length that the position increments by
    set_stroke_color(1, 0, 0)  # colors the stick red
    set_stroke_width(3)
    draw_line(ax1, ay1, ax2, ay2)  # draws stick a
    draw_line(bx1, by1, bx2, by2)  # draws stick b

    while f <= 1:
        set_stroke_width(1)
        set_stroke_color(0, f, (1.0-f))  # gradually changes the color from blue to green as f increases
        draw_line(ax1 + f * (ax2 - ax1), ay1 + f * (ay2 - ay1), bx1 + (1.0 - f) * (bx2 - bx1),
                  by1 + (1.0 - f) * (by2 - by1))  # draws strings along the stick
        f = f + 1.0 / (strings - 1)  # increases the length down the stick by an increment


def main():
    make_background_black()
    string_art(25, 50, 50, 200, 350, 180, 200, 350, 25)


start_graphics(main)
