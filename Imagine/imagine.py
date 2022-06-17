# File Name: imagine.py
# Author Name: Lindsey Kim and CS1 @ Dartmouth
# Date: 10/7/2020
# Course: COSC 1
# Short Description: This flips the cardinal's image and adds a new background
#

from cs1lib import load_image, draw_image, start_graphics


# sets the color of pixel at location x, y to have color r, g, b
#  I have written this function for you (djb).
def set_pixel(image, x, y, r, g, b):
    image.set_pixel(x, y, r, g, b)


# gets the color of pixel at location x, y, returning a list containing
#  3 floating point r, g, b values of the color in that order.
#  I have written this function for you (djb).
def get_pixel(image, x, y):
    return list(image.get_pixel(x, y))


# draw the image on the screen. I have written for you (djb)
def display_image():
    draw_image(img, 0, 0)


# swap the colors of pixels x1, y1 and x2, y2:
def swap_pixels(image, x1, y1, x2, y2):
    color_one = get_pixel(image, x1, y1)
    color_two = get_pixel(image, x2, y2)
    set_pixel(image, x2, y2, color_one[0], color_one[1], color_one[2])
    set_pixel(image, x1, y1, color_two[0], color_two[1], color_two[2])
    pass


# flip a single row of the image horizontally. The row to flip is given
#   by the parameter row_y, and the width of the image is given
#   by the parameter width. You should make use of the function
#   swap_pixels.
def flip_row(image, row_y, width):
    for i in range(0, width//2):
        swap_pixels(image, i, row_y, width - 1 - i, row_y)
    pass


# Flip the image horizontally. For the example, this will cause
#  the cardinal to face right. You should make use of the function flip_row.
def flip_horizontal(image, width, height):
    for i in range(0, height):
        flip_row(image, i, width)
    pass


# Replace all green pixels with pixels from the background image
def virtual_background(image, background, width, height):
    for x in range(0, width):
        for y in range(0, height):
            image_pixel = get_pixel(image, x, y)  # the current pixel of the image
            if image_pixel[1] >= 0.5:
                background_pixel = get_pixel(background, x, y)  # the corresponding pixel of the background image
                set_pixel(image, x, y, background_pixel[0], background_pixel[1], background_pixel[2])
    pass
    # loop over all x, y values of pixels in the image.
    # for each x, y value, replace the pixel in
    #  image with a pixel from the background if the current
    #  pixel has a green value > .5.


img_cardinal = load_image("cardinal.jpg")
img_baker = load_image("SnowyBaker.jpg")

img = img_cardinal

# Test code. You might want to remove one or both of these lines
#  temporarily so you can test your functions one at a time, but don't
#  forget to put them back in.
flip_horizontal(img, 400, 400)
virtual_background(img, img_baker, 400, 400)

start_graphics(display_image)
