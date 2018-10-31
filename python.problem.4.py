import numpy as np

counter = 0
N = 10000

for i in range(N):
    X = np.random.uniform(0,1)
    Y = np.random.uniform(0,1)
    counter = X + Y + counter

value = counter / N
print('Calculated value:',value)

# The theoretical value is 1.
# The calculated value and the theoretical value are very close.