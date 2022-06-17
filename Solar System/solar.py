# File Name: solar.py
# Author Name: Lindsey Kim
# Date: 10/20/2020
# Course: COSC 1
# Short Description: This creates and draws a system of all the planets and the sun.
#

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 10000000   # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame


def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar.update(TIMESTEP * TIME_SCALE)


# mass, x, y, vx, vy, pixel_radius, r, g, b
sun = Body(1.98892e30, 0, 0, 0, 0, 20, 1, 1, 0)   # sun
earth = Body(5.9736e24, 1.496e11, 0, 0, 29800, 6, 0, 0, 1)            # blue earth
mercury = Body(3.30e23, 5.79e10, 0, 0, 47400, 3, 1, 0.5, 0)   # mercury
venus = Body(4.87e24, 1.082e11, 0, 0, 35000, 5, 0, 1, 0)   # venus
mars = Body(6.42e23, 2.279e11, 0, 0, 24100, 4, 1, 0, 0)   # mars

solar = System([sun, earth, mercury, venus, mars])

start_graphics(main, 2400, framerate=FRAMERATE)
