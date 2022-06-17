# File Name: adventure.py
# Author Name: Lindsey Kim
# Date: 11/9/2020
# Course: COSC 1
# Short Description: This analyzes story.txt and plays the story, allowing the user to input their own choices for it.
#

# This is a class that creates a vertex object to represent a choice in the story
class Vertex:
    def __init__(self, adjacency_list, data):
        self.adjacency_list = adjacency_list  # the list of all vertices that are adjacent to the vertex itself
        self.data = data  # the text of the current vertex

    # checks if there are any adjacent vertices and returns True if there are none
    def is_empty(self):
        if len(self.adjacency_list) == 0:
            return True


def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


def load_story(filename):

    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

            # print("vertex " + vertex_name)
            # print(" adjacent:  " + str(adjacent_vertices))
            # print(" text:  " + text)

            vertex_dict[vertex_name] = Vertex(adjacent_vertices, text)   # adds a vertex object to the vertex dictionary

    file.close()

    return vertex_dict


# runs through the adventure and allows the user to pick their own choices
def play_game():
    next_vertex = "START"  # starts with START
    end = False # determines if the story is over

    while not end:
        # if the next vertex has no other options, print the text for it and ends the story
        if story_dict[next_vertex].is_empty():
            print(story_dict[next_vertex].data)
            end = True

        # if the next vertex has options, print the text for it and ask the user for input to determine the next vertex
        else:
            print(story_dict[next_vertex].data)  # prints the text for this vertex
            val = input("Enter your input: ")
            index = ord(val) - ord('a')  # determines what the index of the next vertex will be based on the user input
            next_vertex = story_dict[next_vertex].adjacency_list[index]  # updates next_vertex to be the new vertex


story_dict = load_story("story.txt")  # opens the story that I wrote
play_game()
