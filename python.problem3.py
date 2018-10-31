import numpy as np
import math

np.random.seed(50)
counter = 0

def f(x):
    return math.tan((x*math.pi)/2) 
    
for i in range(10000):
    U = np.random.uniform(0,1)
    if f(U) > 2:
        counter += 1

prob = counter / 10000
prob