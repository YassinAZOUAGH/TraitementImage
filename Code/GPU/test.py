


import numpy as np
from numba import jit


@jit(nopython=True)
def ex1(x, y, out):
    for i in range(x.shape[0]):
        out[i] = x[i] + y[i]
in1 = np.arange(10, dtype=np.float64)
in2 = 2 * in1 + 1
out = np.empty_like(in1)
print('in1:', in1)
print('in2:', in2)
ex1(in1, in2, out)
print('out:', out)