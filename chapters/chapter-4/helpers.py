from appendix.vectors import *


def translate_by(n):
    def fn(v):
        return add(n, v)
    return fn


def polygon_map(fn, polys):
    return [[fn(vertex) for vertex in poly] for poly in polys]
