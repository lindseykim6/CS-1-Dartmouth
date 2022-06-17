# File Name: bfs.py
# Author Name: Lindsey Kim
# Date: 11/14/2020
# Course: COSC 1
# Short Description: This creates a breadth first search
#

from collections import deque
from load_graph import *


def breadth_first_search(start_vertex, goal_vertex):
    backpointer_dict = {}  # has a dictionary of all the backpointers
    q = deque()  # deque of all vertices
    q.append(start_vertex)  # starts with the start vertex
    while len(q) != 0:  # ends when the q is empty
        current_vertex = q.popleft()  # sets the current vertex to the vertex that has been there longest

        for adjacent in current_vertex.adjacency_list:
            if adjacent not in backpointer_dict:
                q.append(adjacent)  # adds an adjacent vertex to the deque if it hasn't been visited
                backpointer_dict[adjacent] = current_vertex  # sets the backpointer of the adjacent vertex to the vertex

            if adjacent == goal_vertex:  # returns the search list when it reaches the goal vertex
                search = [goal_vertex]

                while start_vertex != goal_vertex:
                    goal_vertex = backpointer_dict[goal_vertex]
                    search.append(goal_vertex)  # keeps adding the backpointers until it reaches the start vertex

                return search


vertex_dictionary = load_graph("dartmouth_graph.txt")