# defining a function

# takes radius of a circle as a float 
# prints area of circle with radius 
# returns nothing 

import math


def radiusFunction():
    radius = input("give me a radius as a float: ")
    radius = float(radius)
    area = math.pi * (radius ** 2)
    print("the area of a circle with", radius, "radius is", area)

radiusFunction()