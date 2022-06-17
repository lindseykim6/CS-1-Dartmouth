# File Name: visualize_cities.py
# Author Name: Lindsey Kim
# Date: 11/2/2020
# Course: COSC 1
# Short Description: This sorts the list by using partitions
#

from cs1lib import *
from sort_cities import *

WINDOW_WIDTH = 720
WINDOW_LENGTH = 360
CENTER_X = WINDOW_WIDTH/2
CENTER_Y = WINDOW_LENGTH/2
MARKER_WIDTH = 8

img = load_image("world.png")
in_file = open("world_cities.txt", "r")

counter = 0  # allows for drawing the markers one at a time

map_list = get_city_list()  # list of cities
sort_population()  # sorts based on population


def draw_map():
    global counter
    set_fill_color(1, 0, 0)  # colors markers red
    draw_image(img, 0, 0)  # draws the map picture

    for i in range(0, counter):
        new_x = map_list[i].get_longitude()
        new_y = map_list[i].get_latitude()
        # draws the marker at the given longitude and latitude (multiplies by 2 to fit)
        draw_rectangle(CENTER_X + (2*new_x), CENTER_Y - (2*new_y), MARKER_WIDTH, MARKER_WIDTH)

    if counter < 48:  # allows for drawing the markers one at a time
        counter += 1


start_graphics(draw_map, framerate=5, width=WINDOW_WIDTH, height=WINDOW_LENGTH)
