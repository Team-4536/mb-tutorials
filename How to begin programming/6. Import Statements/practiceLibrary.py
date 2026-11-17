from math import sin, radians

BEST_ANGLE: float = 31 # degrees

def degSin(degrees: float):
    rads: float = radians(degrees)
    return sin(rads)