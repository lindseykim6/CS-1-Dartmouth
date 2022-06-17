# solar.py
# Example for CS 1 Lab Assignment 2.
# db, thc; 2011-2016

from cs1lib import *
from extra_credit_system import System
from extra_credit_body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 1000000   # real seconds per simulation second
PIXELS_PER_METER = 8 / 1e10  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame


def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar.update(TIMESTEP * TIME_SCALE)


# mass, x, y, vx, vy, filename
sun = Body(1.98892e30, 0, 0, 0, 0, "sun.png")   # sun
earth = Body(5.9736e24, 1.496e11, 0, 0, 29800, "earth.png")            # blue earth
mercury = Body(3.30e23, 5.79e10, 0, 0, 47400, "mercury.png")   # mercury
venus = Body(4.87e24, 1.082e11, 0, 0, 35000, "venus.png")  # venus
mars = Body(6.42e23, 2.279e11, 0, 0, 24100, "mars.png")   # mars

solar = System([sun, earth, mercury, venus, mars])

start_graphics(main, 2400, framerate=FRAMERATE)