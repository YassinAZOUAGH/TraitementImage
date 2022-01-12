import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from numba import cuda

image = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')

@cuda.jit(device=True)
def julia(x, y, max_iters):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Julia
    set given a fixed number of iterations.
    """
    i = 0
    c = complex(-0.8, 0.156)
    a = complex(x,y)
    for i in range(max_iters):
        a = a*a + c
        if (a.real*a.real + a.imag*a.imag) > 1000:
            return 0
    return 255

threadsperblock = 16
xblocks = (image.shape[1] + (threadsperblock - 1)) // threadsperblock
yblocks = (image.shape[0] + (threadsperblock - 1)) // threadsperblock

x, y = cuda.grid(2)