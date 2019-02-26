# Scott Crawshaw
# 2/25/19
# visualize_america.py
# Extra credit submission for Lab 3. Visualizes just american cities.

from cs1lib import *
from city import City
from time import time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 421

LNG_TO_PIXELS = 13.78691  # multiplier
LAT_TO_PIXELS = 18.345  # multiplier

MARKER_RADIUS = 3

MAX_DISPLAY_RANGE = 50  # number of cities to display
PAUSE_SECONDS = 0.01  # number of seconds to pause between cities


def load_cities(cities_list):
    # load cities from the sorted by population file

    file = open("cities_population_extra_credit.txt", "r")
    for line in file:
        line = line.strip()
        values = line.split(",")
        if values[0] == "us" and values[2] != "AK" and values[2] != "HI" and values[2] != "PR":
            city = City(values[0], values[1], values[2], values[3], values[4], values[5])
            cities_list.append(city)
    file.close()


def pressed(x, y):
    print(x, y)


def increase_display_range():
    # if PAUSE_TIME has passed, display one more city

    global display_range, old_time

    if time() - old_time >= PAUSE_SECONDS:
        display_range += 1
        old_time = time()


def draw_map():
    global display_range

    clear()
    draw_image(img, 0, 0)

    set_fill_color(1, 0, 0)

    if display_range < MAX_DISPLAY_RANGE:
        increase_display_range()

    for i in range(display_range):
        draw_circle((124.732978 + cities[i].lng) * LNG_TO_PIXELS,
                    (49.269979-cities[i].lat) * LAT_TO_PIXELS, MARKER_RADIUS)
        draw_text(cities[i].name, (124.732978 + cities[i].lng) * LNG_TO_PIXELS, (49.269979-cities[i].lat) * LAT_TO_PIXELS)


cities = []
load_cities(cities)

display_range = 0  # keeps track of how many cities we are displaying
old_time = 0  # used to delay displaying new cities

img = load_image("america_flat.png")
start_graphics(draw_map, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, mouse_press=pressed)
