from appendix.vectors import *


def translate_by(n):
    def fn(v):
        return add(n, v)
    return fn


def scale_by(n):
    def fn(v):
        return scale(n, v)
    return fn


def polygon_map(fn, polys):
    return [[fn(vertex) for vertex in poly] for poly in polys]


def compose(*fns):
    def composition(input):
        state = input

        for fn in reversed(fns):
            state = fn(state)

        return state

    return composition
