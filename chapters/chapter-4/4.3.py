# Exercise 4.3 — Mini Project
#
# What happens to the teapot when you scale every
# vector by a scalar between 0 and 1? What happens when you scale it by a factor
# of –1?

from appendix.teapot import load_triangles
from appendix.draw_model import draw_model
from helpers import *

teapot = load_triangles()

# decreases the size of the teapot
scaled_by_half = polygon_map(scale_by(.5), teapot)

# flips the teapot upside down
scaled_by_minus_one = polygon_map(translate_by(-1), teapot)
