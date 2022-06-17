# File Name: vertex.py
# Author Name: Lindsey Kim
# Date: 11/9/2020
# Course: COSC 1
# Short Description: This is a class to create a vertex object to represent a choice in the story
#

class Vertex:
    def __init__(self, adjacency_list, data):
        self.adjacency_list = adjacency_list  # the list of all vertices that are adjacent to the vertex itself
        self.data = data  # the text of the current vertex

    # checks if there are any adjacent vertices and returns True if there are none
    def is_empty(self):
        if len(self.adjacency_list) == 0:
            return True
