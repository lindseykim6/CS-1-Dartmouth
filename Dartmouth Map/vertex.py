# File Name: vertex.py
# Author Name: Lindsey Kim
# Date: 11/14/2020
# Course: COSC 1
# Short Description: This creates a class for a vertex object with a name, coordinates, and adjacent vertices
#
from cs1lib import *

RADIUS = 8  # radius of the vertex
WIDTH = 3  # width of the edge


class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)  # x coordinate
        self.y = int(y)  # y coordinate
        self.adjacency_list = []  # list of all vertices that are adjacent to this vertex

    def __str__(self):
        # creates a string version of the names of the vertices in the adjacency list
        adjacency_list_string = self.adjacency_list[0].name  # starting vertex so that there is no comma
        for i in range(1, len(self.adjacency_list)):
            adjacency_list_string += ", " + self.adjacency_list[i].name   # adds the rest to the string

        # returns in the form of name; Location: x, y; Adjacent vertices: adjacency_list_string
        return self.name + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent vertices: " + \
            adjacency_list_string

    def draw_vertex(self, r, g, b):  # draws the vertex in the color r, g, b
        set_stroke_color(r, g, b)
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, RADIUS)

    def draw_edge(self, vertex, r, g, b):  # draws an edge between this vertex and another in the color r, g, b
        set_stroke_width(WIDTH)  # sets the width of the stroke to width
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, vertex.x, vertex.y)

    def draw_adjacent(self, r, g, b):  # draws an edge with this vertex and all the adjacent vertices
        set_stroke_width(WIDTH)  # sets the width of the stroke to width
        set_stroke_color(r, g, b)  # sets the color of the edge to r, g, b
        for item in self.adjacency_list:
            draw_line(self.x, self.y, item.x, item.y)

    def in_bounds(self, x, y):  # checks if (x,y) is within a vertex and returns true if it is
        if self.x - RADIUS <= x <= self.x + RADIUS:  # checks if it is within the range in the x direction
            if self.y - RADIUS <= y <= self.y + RADIUS:  # checks if it is within the range in the y direction
                return True
