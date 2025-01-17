# Scott Crawshaw
# 2/25/19
# city.py
# Submission for lab 3


class City:

    def __init__(self, country, name, region, pop, lat, lng):
        self.country = country
        self.name = name
        self.region = region
        self.pop = int(pop)
        self.lat = float(lat)
        self.lng = float(lng)

    def __str__(self):
        return self.name + "," + str(self.pop) + "," + str(self.lat) + "," + str(self.lng)
