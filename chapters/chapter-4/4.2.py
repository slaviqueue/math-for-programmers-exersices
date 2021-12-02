# Exercise 4.2
#
# Render the teapot translated by 20 units in the negative z direction.
# What does the resulting image look like?

# Exercise 4.1
#
# Implement a translate_by function (referred to in section 4.1.2), taking a
# translation vector as input and returning a translation function as output.

from appendix.teapot import load_triangles
from appendix.draw_model import draw_model
from helpers import *


tris = load_triangles()
translated = polygon_map(translate_by((0, 0, -20)), tris)

draw_model(translated)
