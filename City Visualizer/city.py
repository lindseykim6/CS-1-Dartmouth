# File Name: city.py
# Author Name: Lindsey Kim
# Date: 10/28/2020
# Course: COSC 1
# Short Description: This is a class that creates a city object
#

class City:
    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.country_code = country_code
        self.name = name
        self.region = region
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    # returns a string with the name, population, latitude, and longitude of the city
    def __str__(self):
        return self.name + "," + str(self.population) + "," \
               + str(self.latitude) + "," + str(self.longitude)

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def get_population(self):
        return self.population

    def get_name(self):
        return self.name