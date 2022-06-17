# File Name: load_graph.py
# Author Name: Lindsey Kim
# Date: 11/14/2020
# Course: COSC 1
# Short Description: This writes a function that parses through all the lines in a file and creates a dictionary
# that holds the vertex name as the key and a reference to the vertex object as its value
#

from vertex import *


def load_graph(filename):
    vertex_dictionary = {}  # the dictionary that holds the vertex name and a reference to the vertex object
    in_file = open(filename, "r")
    for line in in_file:
        # for each line, splits the information into the name, adjacent vertices, and coordinates
        vertex_information = line.split(";")
        coordinates = vertex_information[2].split(",")  # splits the coordinates into x and y
        # adds the info to a new vertex object
        new_vertex = Vertex(vertex_information[0], coordinates[0].strip(), coordinates[1].strip())
        # adds the vertex and its name into the dictionary
        vertex_dictionary[vertex_information[0]] = new_vertex
    in_file.close()

    in_file = open(filename, "r")
    for line in in_file:
        # for each line, splits the information into the name, adjacent vertices, and coordinates
        vertex_information = line.split(";")
        name = vertex_information[0]
        # grabs the vertices that are adjacent to the current vertex and puts it in a list
        adjacency_list = vertex_information[1].split(",")
        for item in adjacency_list:
            # adds each vertex that is adjacent into the current vertex's adjacency list
            current_vertex = vertex_dictionary[name]
            current_vertex.adjacency_list.append(vertex_dictionary[item.strip()])

    return vertex_dictionary


load_graph("dartmouth_graph.txt")