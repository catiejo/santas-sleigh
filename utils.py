import math
from point import Point

def haversine_distance(start, end):
    print("{} {}, {} {}".format(start.lat, start.long, end.lat, end.long))

p1 = Point(1, 2)
p2 = Point(3, 4)
haversine_distance(p1, p2)
