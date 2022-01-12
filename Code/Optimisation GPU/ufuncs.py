import timeit
import numpy as np

from numba import vectorize

@vectorize(['int64(int64, int64)'], target='cuda')
def add_ufunc(x, y):
    return x + y


int('a+b:\n', add_ufunc(10, 2))
print()
