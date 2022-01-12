from numba import jit
import math
import time

@jit
def hypot(x, y):
    # Implementation from https://en.wikipedia.org/wiki/Hypot
    x = abs(x);
    y = abs(y);
    t = min(x, y);
    x = max(x, y);
    t = t / x;
    return x * math.sqrt(1+t*t)



start = time.time()
print(hypot(3.0, 4.0))
end = time.time()
print('temps excution' ,end - start)


start = time.time()
print(hypot.py_func(3.0, 4.0))
end = time.time()
print('temps excution' ,end - start)


print(hypot.inspect_types())