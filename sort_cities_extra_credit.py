# Scott Crawshaw
# 2/25/19
# sort_cities_extra_credit.py
# Extra credit for Lab 3. Same as sort_cities, but only sort by pop, and outputs complete city info

from city import City
from quicksort import sort


def compare_pop(a, b):
    return a.pop >= b.pop


def write_file(file_name, objects):
    file = open(file_name, "w")

    for obj in objects:
        file.write(obj.country + "," + obj.name + "," + obj.region + "," + str(obj.pop) + ","
                   + str(obj.lat) + "," + str(obj.lng) + "\n")

    file.close()


def load_cities(file_name):
    cities = []
    file = open(file_name, "r")

    # creates cities based on data in world_cities.txt
    for line in file:
        line = line.strip()
        values = line.split(",")
        city = City(values[0], values[1], values[2], values[3], values[4], values[5])
        cities.append(city)

    file.close()

    return cities


cities = load_cities("world_cities.txt")

sort(cities, compare_pop)
write_file("cities_population_extra_credit.txt", cities)
