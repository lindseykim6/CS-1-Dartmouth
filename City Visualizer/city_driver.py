# File Name: city_driver.py
# Author Name: Lindsey Kim
# Date: 10/28/2020
# Course: COSC 1
# Short Description: This takes the text from world_cities.txt and inputs it into a new text file called cities_out.txt
#

from city import *

in_file = open("world_cities.txt", "r")
out_file = open("cities_out.txt", "w")

city_list = []  # city_list is a list of all the cities in world_cities.txt


# takes the output from world_cities.txt and processes it
def process_file():
    for line in in_file:  # processes each line in world_cities.txt
        t = line.strip()  # strips the new line from each line in world_cities.txt
        sections = t.split(",")  # splits the line with a comma delimiter and creates an array filled with each section
        # creates a city object with each split from the array that was created
        city = City(sections[0], sections[1], sections[2], sections[3], sections[4], sections[5])
        city_list.append(city)  # appends the city to the city_list


# writes the output in cities_out.txt
def write_file():
    for index in range(len(city_list)):  # for each city in city list, it adds the string of the city in cities_out.txt
        # adds the string of the city with a new line if it is not the last city in the list
        if index != len(city_list)-1:
            out_file.write(str(city_list[index]) + "\n")
        # if it is the last city, add it without a new line
        else:
            out_file.write(str(city_list[index]))


process_file()
write_file()

in_file.close()  # closes world_cities.txt
out_file.close()  # closes cities_out.txt
