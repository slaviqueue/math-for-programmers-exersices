# Exercise 4.4
#
# First apply translate1left to the teapot and then apply scale2.
# How is the result different from the opposite order of composition? Why?

from helpers import *
from appendix.teapot import load_triangles
from appendix.draw_model import draw_model

scale2 = scale_by(1.1)
translate1left = translate_by((.5, 0.5, 0.5))

scale_then_translate = compose(scale2, translate1left)
translate_then_scale = compose(translate1left, scale2)

# draw_model(polygon_map(scale_then_translate, load_triangles()))
# draw_model(polygon_map(translate_then_scale, load_triangles()))

# if translation happens first, scaling will affect the model more
