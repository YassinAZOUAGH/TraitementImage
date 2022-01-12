import math  # Note that for the CUDA target, we need to use the scalar functions from the math module, not NumPy
from numba import vectorize
import numpy as np
from numba import cuda
import time


from numba import vectorize
import numpy as np

@vectorize(['float32(float32, float32)'], target='cuda')
def add_ufunc(x, y):
    return x + y

n = 100000
x = np.arange(n).astype(np.float32)
y = 2 * x

n_device = cuda.to_device(n)
x_device = cuda.to_device(x)
y_device = cuda.to_device(y)

print(n_device.dtype)
print(x_device)
print(x_device.shape)
print(x_device.dtype)
