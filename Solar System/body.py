# File Name: body.py
# Author Name: Lindsey Kim
# Date: 10/20/2020
# Course: COSC 1
# Short Description: This is a class to create an object for a body in a solar system (sun, moon, etc.)
#

from cs1lib import *


class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass  # mass of body

        # x and y coordinates of the body where x=0 and y=0 is the center
        self.x = x
        self.y = y

        self.vx = vx  # horizontal velocity of the body
        self.vy = vy  # vertical velocity of the body

        self.pixel_radius = pixel_radius  # the radius of the body in pixels

        # (r, g, b) make up the color of the body
        self.r = r
        self.g = g
        self.b = b

    def update_position(self, timestep):
        self.x = self.x + (self.vx * timestep)
        self.y = self.y - (self.vy * timestep)

    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx + (ax * timestep)
        self.vy = self.vy + (ay * timestep)

    def draw(self, cx, cy, pixels_per_meter):  # draws the body
        cx = cx + (self.x * pixels_per_meter)
        cy = cy + (self.y * pixels_per_meter)
        set_fill_color(self.r, self.g, self.b)
        draw_circle(cx, cy, self.pixel_radius)
