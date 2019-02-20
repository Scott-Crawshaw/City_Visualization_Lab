# Scott Crawshaw
# 2/20/19
# checkpoint.py
# Submission for lab 3 checkpoint

from city import City

cities = []
file_name = "world_cities.txt"
file = open(file_name, "r")

# creates cities based on data in world_cities.txt
for line in file:
    line = line.strip()
    values = line.split(",")
    city = City(values[0], values[1], values[2], values[3], values[4], values[5])
    cities.append(city)

file.close()

# write city information to cities_out.txt
file_name = "cities_out.txt"
file = open(file_name, "w")

for city in cities:
    file.write(str(city) + "\n")

file.close()
