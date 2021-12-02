from math import *
from operator import mul, sub


def dot(v1, v2):
    return sum(map(mul, v1, v2))


def subtract(v1, v2):
    return tuple(map(sub, v1, v2))


def length(vector):
    return sqrt(sum(list(map(lambda x: x * x, vector))))


def add(v1, v2):
    return tuple(map(sum, zip(v1, v2)))


def scale(scalar, vector):
    return tuple([c * scalar for c in vector])


def to_polar(x, y):
    rho = sqrt(x**2 + y**2)
    phi = atan2(y, x)
    return (rho, phi)


def to_cartesian(rho, phi):
    x = rho * cos(phi)
    y = rho * sin(phi)
    return (x, y)


def cross(u, v):
    ux, uy, uz = u
    vx, vy, vz = v
    return (uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)
