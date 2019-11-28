from .fibonacci import fib
import math


def dummy_math_function(x):
    if x == 0:
        return 0
    p = math.pi * x
    tot = (p * fib(x)) / (x / 2)
    return tot
