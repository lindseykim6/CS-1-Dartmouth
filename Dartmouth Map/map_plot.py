# File Name: map_plot.py
# Author Name: Lindsey Kim
# Date: 11/14/2020
# Course: COSC 1
# Short Description: This creates a plot of the Dartmouth map
#
from bfs import *

WIDTH = 1012  # width of the window
HEIGHT = 811  # height of the window
RADIUS = 8

vertex_dictionary = load_graph("dartmouth_graph.txt")  # loads the graph of dartmouth into a dictionary
start_vertex=None
goal_vertex=None


def draw_map():
    dartmouth_map = load_image("dartmouth_map.png")  # loads the map image
    draw_image(dartmouth_map, 0, 0)  # draws map


def draw_graph():
    for vertex in vertex_dictionary:
        vertex_dictionary[vertex].draw_vertex(0, 0, 1)  # draws all the vertices in the graph
        vertex_dictionary[vertex].draw_adjacent(0, 0, 1)  # draws all the edges in the graph


def select_vertices():
    global start_vertex, goal_vertex
    # if the vertex is in bounds and the mouse is pressed, this is the start vertex
    if is_mouse_pressed():
        for vertex in vertex_dictionary:
            if vertex_dictionary[vertex].in_bounds(mouse_x(), mouse_y()):
                start_vertex = vertex_dictionary[vertex]
    # if the vertex is in bounds and the mouse is not pressed, this is the goal vertex
    else:
        for vertex in vertex_dictionary:
            if vertex_dictionary[vertex].in_bounds(mouse_x(), mouse_y()):
                goal_vertex = vertex_dictionary[vertex]


def bfs():
    if start_vertex is not None and goal_vertex is not None:  # checks if there is a start and goal vertex
        # performs a breath first search from the start to goal vertex
        search = breadth_first_search(start_vertex, goal_vertex)
        for i in range(len(search)-1):
            search[i].draw_vertex(1, 0, 0) # draws the vertices up until the last one
            search[i].draw_edge(search[i+1], 1, 0, 0)  # draws the edges between all vertices
        search[len(search)-1].draw_vertex(1, 0, 0)  # draws the last vertex


def draw():
    draw_map()
    draw_graph()
    select_vertices()
    bfs()


start_graphics(draw, framerate=300, width=WIDTH, height=HEIGHT)
