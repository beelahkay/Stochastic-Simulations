import numpy as np

counter = 0

for i in range(10000):
    position = -1
    for i in range(10):
        x = np.random.uniform(0,1)
        if x > 0.4:
            position = position + 1
        if x < 0.4:
            position = position - 1
    
    if position == -3:
        counter = counter + 1

probability = counter / 10000
print('Empirical Probability:', probability)

# This corresponds to the theoretical value of 0.1115