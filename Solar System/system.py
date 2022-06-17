# File Name: system.py
# Author Name: Lindsey Kim
# Date: 10/20/2020
# Course: COSC 1
# Short Description: This is a class to create a solar system with a group of bodies.
#
import math

GRAVITATIONAL_CONSTANT = 6.67384e-11


class System:
    def __init__(self, body_list):
        self.body_list = body_list  # a list of bodies in the given solar system

    def compute_acceleration(self, n):
        ax = 0  # x component of acceleration
        ay = 0  # y component of acceleration
        for index in range(len(self.body_list)):
            if index != n:  # skips over the current body who's acceleration is being calculated
                dx = self.body_list[index].x - self.body_list[n].x  # distance between the x of the two bodies
                dy = self.body_list[n].y - self.body_list[index].y  # distance between the y of the two bodies
                r = math.sqrt((dx*dx)+(dy*dy))  # distance between the two bodies
                # acceleration due to the body of given index
                acceleration = GRAVITATIONAL_CONSTANT * self.body_list[index].mass / (r*r)
                i_ax = acceleration * dx / r  # acceleration in x direction due to the body of given index
                i_ay = acceleration * dy / r  # acceleration in y direction due to the body of given index
                ax += i_ax  # ax is the total acceleration in the x direction due to all other bodies
                ay += i_ay  # ay is the total acceleration in the y direction due to all other bodies
        return (ax, ay)

    def update(self, timestep):  # updates the position and velocity of each body
        for n in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(n)  # updates the velocity based on the computed acceleration
            self.body_list[n].update_velocity(ax, ay, timestep)
            self.body_list[n].update_position(timestep)

    def draw(self, cx, cy, pixels_per_meter):
        for i in range(len(self.body_list)):
            self.body_list[i].draw(cx, cy, pixels_per_meter)
