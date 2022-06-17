# File Name: drawing.py
# Author Name: Lindsey Kim
# Date: 9/17/2020
# Course: COSC 1
# Short Description: This creates an illustration inspired by the book, Don't Let the Pigeon
# Drive the Bus by Mo Willems.
# I found the font for this drawing on
# http://jonathansoma.com/lede/data-studio/matplotlib/list-all-fonts-available-in-matplotlib-plus-samples/
#

from cs1lib import *


def set_fill_blue():
    set_fill_color(0.57, 0.94, 1)


def set_fill_white():
    set_fill_color(1, 1, 1)


def set_fill_black():
    set_fill_color(0, 0, 0)


def set_fill_orange():
    set_fill_color(1, 0.5, 0)


def set_fill_background_color():
    set_fill_color(1, 0.76, 0.45)


def make_background_orange():   # sets a light orange background
    set_clear_color(1, 0.76, 0.45)
    clear()


head_center_x = 150
head_center_y = 200


def draw_pigeon_head():
    # draws the orange beak of the pigeon
    set_fill_orange()
    draw_triangle(130, 200, 120, 205, 135, 210)
    draw_line(122, 206, 135, 205)  # draws the line that separates the beak

    # draws the head of the pigeon
    set_fill_blue()
    draw_circle(head_center_x, head_center_y, 20)

    # draws the eye of the pigeon
    set_fill_white()
    draw_circle(head_center_x, head_center_y, 10)
    set_fill_black()
    draw_circle(head_center_x+5, head_center_y, 5)


def draw_pigeon_legs():
    enable_stroke()

    top_of_leg_y = 305
    top_of_feet_y = 335
    bottom_of_feet_y = 345
    left_side_x = 175
    right_side_x = 195

    # left side
    draw_line(left_side_x, top_of_leg_y, left_side_x, bottom_of_feet_y)
    draw_line(left_side_x, top_of_feet_y, left_side_x-7, bottom_of_feet_y)
    draw_line(left_side_x, top_of_feet_y, left_side_x+7, bottom_of_feet_y)

    # right side
    draw_line(right_side_x, top_of_leg_y, right_side_x, bottom_of_feet_y)
    draw_line(right_side_x, top_of_feet_y, right_side_x-7, bottom_of_feet_y)
    draw_line(right_side_x, top_of_feet_y, right_side_x+7, bottom_of_feet_y)


def draw_pigeon_body():
    # draws the body
    set_fill_blue()
    draw_ellipse(185, 280, 50, 30)

    # shapes the body by covering part of the ellipse
    disable_stroke()
    set_fill_background_color()
    draw_rectangle(161, 247, 100, 20)
    enable_stroke()

    # adds the upper outline of body
    enable_stroke()
    draw_line(160, 267, 230, 267)


def draw_pigeon_neck():
    # draws the main neck
    set_fill_blue()
    draw_rectangle(head_center_x-10, head_center_y+18, 20, 49)

    # draws the white collar on the neck
    set_fill_white()
    draw_rectangle(head_center_x-10, head_center_y+30, 20, 10)

    # gets rid of the extra line
    disable_stroke()
    set_fill_blue()
    draw_rectangle(head_center_x-9, 260, 18, 10)
    enable_stroke()


def draw_pigeon_wing():
    set_fill_blue()
    draw_ellipse(190, 283, 30, 13)

    # covers half of the ellipse to create the wing
    disable_stroke()
    draw_rectangle(160, 269, 60, 13)

    # draws the upper part of the wing
    enable_stroke()
    draw_line(200, 280, 220, 283)


def draw_text_bubble():
    # creates the dialogue text bubble
    set_fill_white()
    disable_stroke()
    draw_triangle(250, 100, 400, 310, 300, 100)  # the appendage to the dialogue bubble
    draw_ellipse(200, 90, 150, 60)

    # writes the title of the book
    enable_stroke()
    set_font("Courier New")
    set_font_size(20)
    draw_text("Don't Let the Pigeon", 90, 90)
    draw_text("Drive the Bus!", 120, 110)


def pigeon_book_drawing():
    make_background_orange()

    draw_pigeon_legs()

    draw_pigeon_body()

    draw_pigeon_neck()

    draw_pigeon_head()

    draw_pigeon_wing()

    draw_text_bubble()

    set_font_size(10)
    draw_text("Drawing Programmed by Lindsey Kim (Inspired by the book)", 20, 380)


start_graphics(pigeon_book_drawing)
