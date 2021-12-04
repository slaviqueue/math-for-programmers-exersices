# Exercise 4.9
#
# Write a function stretch_x(scalar,vector) that scales the target
# vector by the given factor but only in the x direction. Also write a curried
# version stretch_x_by so that stretch_x_by(scalar)(vector) returns the same
# result.

def stretch_x(scalar, vector):
    x, y, z = vector
    return (x*scalar, y, z)


def stretch_x_by(scalar):
    def fn(vector):
        return stretch_x(scalar, vector)
    return fn


v = (2, 3, 4)
stretched = stretch_x(2, v)
assert(stretched == (4, 3, 4))

stretched_curried = stretch_x_by(2)(v)
assert(stretched_curried == (4, 3, 4))
