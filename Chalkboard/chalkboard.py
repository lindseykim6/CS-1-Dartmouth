# File Name: chalkboard.py
# Author Name: Lindsey Kim
# Date: 9/28/2020
# Course: COSC 1
# Short Description: This creates a chalkboard with five colors.
#


from cs1lib import *


old_x = 0  # old x position of the cursor
old_y = 0  # old x position of the cursor
new_x = 0  # new x position of the cursor
new_y = 0  # new y position of the cursor
drawn = False  # variable for whether or not the cursor is clicked
first_frame = True  # variable for whether or not it is the first frame or not
pressed_r = False  # variable for whether or not r is pressed
pressed_g = False  # variable for whether or not g is pressed
pressed_y = False  # variable for whether or not y is pressed
pressed_b = False  # variable for whether or not b is pressed


# sets the first background as black
def background():
    global first_frame
    if first_frame:
        set_clear_color(0, 0, 0)
        clear()
    first_frame = False


# changes the global variable of the color to true based on the key pressed (key press)
def change_color(key):
    global pressed_r, pressed_g, pressed_b, pressed_y
    if key == "r":
        pressed_r = True
    elif key == "g":
        pressed_g = True
    elif key == "b":
        pressed_b = True
    elif key == "y":
        pressed_y = True


# changes the global variable of the color to False based on the key pressed (key release)
def key_up(key):
    global pressed_r, pressed_g, pressed_b, pressed_y
    if key == "r":
        pressed_r = False
    elif key == "g":
        pressed_g = False
    elif key == "b":
        pressed_b = False
    elif key == "y":
        pressed_y = False


# changes the color based on the key pressed
def stroke():
    global pressed_y, pressed_r, pressed_g, pressed_b
    if pressed_y:
        set_stroke_color(1, 1, 0)  # yellow
    elif pressed_b:
        set_stroke_color(0, 0, 1)  # blue
    elif pressed_g:
        set_stroke_color(0, 1, 0)  # green
    elif pressed_r:
        set_stroke_color(1, 0, 0)  # red
    else:
        set_stroke_color(1, 1, 1)  # black
        set_stroke_width(2)  # width is 2 pixels


def clicked(mx, my):
    global old_x, old_y, drawn
    drawn = True
    old_x = mx
    old_y = my


def released(mx, my):
    global drawn
    drawn = False


def movement(mx, my):
    global new_x, new_y
    new_x = mx
    new_y = my


# draws the line
def chalk():
    if drawn:
        draw_line(old_x, old_y, new_x, new_y)


# updates the old x and the old y
def update_old():
    global old_x, old_y
    old_x = new_x
    old_y = new_y


def main():
    background()
    stroke()
    chalk()
    update_old()


start_graphics(main, 1, mouse_press=clicked, mouse_release=released, mouse_move=movement,
               key_press=change_color, key_release=key_up)
