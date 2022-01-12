from numba import jit, cuda
import numpy as np


TILE_DIM = 32
BLOCK_ROWS = 8

@cuda.jit
def transpose(a_in, a_out):
    x = cuda.blockIdx.x * TILE_DIM + cuda.threadIdx.x
    y = cuda.blockIdx.y * TILE_DIM + cuda.threadIdx.y

    for j in range(0, TILE_DIM, BLOCK_ROWS):
        a_out[x, y + j] = a_in[y + j, x]

size = 1024
a_in = cuda.to_device(np.arange(size*size, dtype=np.int32).reshape((size, size)))
a_out = cuda.device_array_like(a_in)

print(a_in.copy_to_host())