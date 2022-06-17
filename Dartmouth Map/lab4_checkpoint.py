# File Name: lab4_checkpoint.py
# Author Name: Lindsey Kim
# Date: 11/14/2020
# Course: COSC 1
# Short Description: This checks that load_graph works.
#
from load_graph import load_graph

vertex_dict = load_graph("dartmouth_graph.txt")

out_file = open("vertices.txt", "w")
for vertex in vertex_dict:
    out_file.write(str(vertex_dict[vertex]) + "\n")  # writes the string version of each vertex
out_file.close()