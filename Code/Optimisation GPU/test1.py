from numba import vectorize
import numpy as np
import timeit

@vectorize(['float32(float32, float32)'], target='cuda')
def add_ufunc(x, y):
    return x + y


x = 2
y = 2 * x

print(add_ufunc(x, y))