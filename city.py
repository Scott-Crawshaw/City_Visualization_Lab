class City:

    def __init__(self, country, name, region, pop, lat, lng):
        self.country = country
        self.name = name
        self.region = region
        self.pop = pop
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return self.name + "," + self.pop + "," + self.lat + "," + self.lng
