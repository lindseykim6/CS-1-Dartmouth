# File Name: body.py
# Author Name: Lindsey Kim
# Date: 10/20/2020
# Course: COSC 1
# Short Description: This is a class to create an object for a body in a solar system (sun, moon, etc.)
#

from cs1lib import *


class Body:
    def __init__(self, mass, x, y, vx, vy, filename):
        self.mass = mass  # mass of body

        # x and y coordinates of the body where x=0 and y=0 is the center
        self.x = x
        self.y = y

        self.vx = vx  # horizontal velocity of the body
        self.vy = vy  # vertical velocity of the body

        self.image = load_image(filename)

    def update_position(self, timestep):
        self.x = self.x + (self.vx * timestep)
        self.y = self.y - (self.vy * timestep)

    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx + (ax * timestep)
        self.vy = self.vy + (ay * timestep)

    def draw(self, cx, cy, pixels_per_meter):  # draws the body
        cx = cx + (self.x * pixels_per_meter)
        cy = cy + (self.y * pixels_per_meter)
        draw_image(self.image, cx, cy, self.image.width()/2, self.image.height()/2)
