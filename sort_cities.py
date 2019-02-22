from city import City
from quicksort import sort


def compare_names(a, b):
    return a.name.lower() <= b.name.lower()


def compare_pop(a, b):
    return a.pop >= b.pop


def compare_lat(a, b):
    return a.lat <= b.lat


def write_file(file_name, objects):
    file = open(file_name, "w")

    for obj in objects:
        file.write(str(obj) + "\n")

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

sort(cities, compare_names)
write_file("cities_alpha.txt", cities)

sort(cities, compare_pop)
write_file("cities_population.txt", cities)

sort(cities, compare_lat)
write_file("cities_latitude.txt", cities)
