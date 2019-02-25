from cs1lib import *
from city import City

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 360

LNG_TO_PIXELS = 2
LAT_TO_PIXELS = 2

MARKER_WIDTH = 4
MARKER_HEIGHT = 4


def load_cities(cities_list):
    file = open("cities_population.txt", "r")
    for line in file:
        line = line.strip()
        values = line.split(",")
        city = City(None, values[0], None, values[1], values[2], values[3])
        cities_list.append(city)


def draw_map():
    clear()
    draw_image(img, 0, 0)

    disable_stroke()
    set_fill_color(1,0,0)

    for i in range(50):
        draw_rectangle((WINDOW_WIDTH/2) + cities[i].lng * LNG_TO_PIXELS - MARKER_WIDTH/2,
                       (WINDOW_HEIGHT/2) - cities[i].lat * LAT_TO_PIXELS - MARKER_HEIGHT/2, MARKER_WIDTH, MARKER_HEIGHT)


cities = []
load_cities(cities)

img = load_image("world.png")
start_graphics(draw_map, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
