import numpy
import csv

class Point:
    def __init__(self, latitude, longitude):
        self.lat = numpy.deg2rad(latitude)
        self.long = numpy.deg2rad(longitude)

class Gift:
    def __init__(self, id, point, weight):
        self.id = id
        self.pt = point
        self.w = weight

# points are already in radians
def haversine_distance(start, end):
    r = 6371 #km
    sin_of_lats = numpy.sin((end.lat - start.lat) / 2.0) ** 2
    sin_of_longs = numpy.sin((end.long - start.long) / 2.0) ** 2
    cos_product = numpy.cos(start.lat) * numpy.cos(end.lat)
    inner_portion = numpy.sqrt(sin_of_lats + (cos_product * sin_of_longs))
    distance = 2 * r * numpy.arcsin(inner_portion)
    return distance

# num_gifts is the number of gifts to get since the file is really big
def parse_gifts(**kwargs):
    gifts = []
    with open('gifts.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        i = kwargs.get('num_gifts', float('inf'))
        for row in reader:
            if (i == 0):
                return gifts
            else:
                i -= 1
            coord = Point(float(row['Latitude']), float(row['Longitude']))
            gifts.append(Gift(int(row['GiftId']), coord, float(row['Weight'])))
    return gifts
