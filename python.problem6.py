import numpy as np


N1 = [0] * 1000
N2 = [0] * 1000

for i in range(1000):
    counter1 = 0
    counter2 = 0
    y = np.random.exponential(0.5, 50)
    x = np.cumsum(y)
    
    while x[counter1] < 1 and counter1 < 50:
        counter1 = counter1 + 1
    while x[counter2] < 2 and counter2 < 50:
        counter2 = counter2 + 1
    
    N1[i] = N1[i] + (counter1)
    N2[i] = N2[i] + (counter2)

product = [0] * 1000

for i in range(1000):
    product[i] = N1[i] * N2[i]

answer = sum(product) / 1000
print('Emprical Expectation:',answer)

# The empirical expectation is close to the theoretical value of 10.