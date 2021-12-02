# Exercise 4.1
#
# Implement a translate_by function (referred to in section 4.1.2), taking a
# translation vector as input and returning a translation function as output.

from appendix.vectors import *
from appendix.teapot import load_triangles
from appendix.draw_model import draw_model


def translate_by(n):
    def fn(v):
        return add(n, v)
    return fn


tris = load_triangles()
translated = [map(translate_by((1, 1, 1)), v) for v in tris]

draw_model(translated)
