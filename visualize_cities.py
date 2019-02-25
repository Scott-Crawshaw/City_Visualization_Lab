# Scott Crawshaw
# 2/25/19
# visualize_cities.py
# Submission for Lab 3

from cs1lib import *
from city import City
from time import time

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 360

LNG_TO_PIXELS = 2  # multiplier
LAT_TO_PIXELS = 2  # multiplier

MARKER_WIDTH = 4
MARKER_HEIGHT = 4

MAX_DISPLAY_RANGE = 50  # number of cities to display
PAUSE_SECONDS = 1  # number of seconds to pause between cities


def load_cities(cities_list):
    # load cities from the sorted by population file

    file = open("cities_population.txt", "r")
    for line in file:
        line = line.strip()
        values = line.split(",")
        city = City(None, values[0], None, values[1], values[2], values[3])
        cities_list.append(city)


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

    disable_stroke()
    set_fill_color(1, 0, 0)

    if display_range < MAX_DISPLAY_RANGE:
        increase_display_range()

    for i in range(display_range):
        draw_rectangle((WINDOW_WIDTH/2) + cities[i].lng * LNG_TO_PIXELS - MARKER_WIDTH/2,
                       (WINDOW_HEIGHT/2) - cities[i].lat * LAT_TO_PIXELS - MARKER_HEIGHT/2, MARKER_WIDTH, MARKER_HEIGHT)


cities = []
load_cities(cities)

display_range = 0  # keeps track of how many cities we are displaying
old_time = 0  # used to delay displaying new cities

img = load_image("world.png")
start_graphics(draw_map, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
