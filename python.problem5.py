import numpy as np

pi = np.array([1, 0, 0])

P = np.array([[0.5, 0.3, 0.2],
              [0.4, 0.6, 0],
              [0.1, 0.9, 0]])

for i in range(10000):
    pi = np.matmul(pi, P)

print('Simulated Result =', pi)

# Which corresponds to the theoretical stationary matrix [ 5/12 1/2 1/12]