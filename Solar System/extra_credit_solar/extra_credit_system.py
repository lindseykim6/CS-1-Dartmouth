# File Name: system.py
# Author Name: Lindsey Kim
# Date: 10/20/2020
# Course: COSC 1
# Short Description: This is a class to create a solar system with a group of bodies
#
import math

GRAVITATIONAL_CONSTANT = 6.67384e-11


class System:
    def __init__(self, body_list):
        self.body_list = body_list  # a list of bodies in the given solar system

    def compute_acceleration(self, n):
        ax = 0
        ay = 0
        for index in range(len(self.body_list)):
            if index != n:
                dx = self.body_list[index].x - self.body_list[n].x
                dy = self.body_list[n].y - self.body_list[index].y
                r = math.sqrt((dx*dx)+(dy*dy))
                acceleration = GRAVITATIONAL_CONSTANT * self.body_list[index].mass / (r*r)
                i_ax = acceleration * dx / r
                i_ay = acceleration * dy / r
                ax += i_ax
                ay += i_ay
        return (ax, ay)

    def update(self, timestep):  # updates the position and velocity of each body
        for n in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(n)  # updates the velocity based on the computed acceleration
            self.body_list[n].update_velocity(ax, ay, timestep)
            self.body_list[n].update_position(timestep)

    def draw(self, cx, cy, pixels_per_meter):
        for i in range(len(self.body_list)):
            self.body_list[i].draw(cx, cy, pixels_per_meter)
