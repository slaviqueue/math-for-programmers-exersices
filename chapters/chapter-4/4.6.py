# Exercise 4.7
#
# Write a curry2(f) function that takes a Python function f(x,y)
# with two arguments and returns a curried version. For instance, once you write
# g = curry2(f), the two expressions f(x,y) and g(x)(y) should return the same
# result.

def curry(f):
    def f1(arg1):
        def f2(arg2):
            return f(arg1, arg2)
        return f2
    return f1


def sum_two_numbers(a, b):
    return a + b


curried_sum_two_numbers = curry(sum_two_numbers)

print(curried_sum_two_numbers(2)(2))  # 4
