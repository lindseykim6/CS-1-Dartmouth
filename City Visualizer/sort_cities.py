# File Name: sort_cities.py
# Author Name: Lindsey Kim
# Date: 11/2/2020
# Course: COSC 1
# Short Description: This sorts the list by using partitions
#

from quicksort import *
from city import *

city_list = []  # city_list is a list of all the cities in world_cities.txt


def compare_latitude(a, b):  # compares latitude and returns true if a's latitude is smaller or equal to b's latitude
    return a.latitude <= b.latitude


def compare_population(a, b):  # compares population and returns true if a's population is bigger than b's population
    return a.population >= b.population


def compare_alpha(a, b):  # compares name and returns true if a's name comes before b's name lexically
    return a.name.lower() <= b.name.lower()


# takes the output from world_cities.txt and processes it
def process_file():
    for line in in_file:  # processes each line in world_cities.txt
        t = line.strip()  # strips the new line from each line in world_cities.txt
        sections = t.split(",")  # splits the line with a comma delimiter and creates an array filled with each section
        # creates a city object with each split from the array that was created
        city = City(sections[0], sections[1], sections[2], sections[3], sections[4], sections[5])
        city_list.append(city)  # appends the city to the city_list


def get_city_list():
    return city_list


def sort_alphabetically():
    sort(city_list, compare_alpha)  # sorts in alphabetical order


def sort_population():
    sort(city_list, compare_population)   # sorts population from biggest to smallest


def sort_latitude():
    sort(city_list, compare_latitude)   # sorts from smaller latitude to bigger


# writes the output in cities_out.txt
def write_file():
    for index in range(len(city_list)):  # for each city in city list, it adds the string of the city in cities_out.txt
        # adds the string of the city with a new line if it is not the last city in the list
        if index != len(city_list)-1:
            out_file.write(str(city_list[index]) + "\n")
        # if it is the last city, add it without a new line
        else:
            out_file.write(str(city_list[index]))


in_file = open("world_cities.txt", "r")
process_file()  # processes world_cities.txt

out_file = open("cities_alpha.txt", "w")
sort_alphabetically()
write_file()  # writes in cities_alpha.txt
out_file.close()  # closes cities_alpha.txt

out_file = open("cities_population.txt", "w")
sort_population()
write_file()  # writes in cities_population.txt
out_file.close()  # closes cities_population.txt

out_file = open("cities_latitude.txt", "w")
sort_latitude()
write_file()  # writes in cities_latitude.txt
out_file.close()  # closes cities_out.txt

in_file.close()  # closes world_cities.txt
