import numpy as np

x = ([])

for i in range(100):
    Nt = np.random.poisson(730)
    Z = np.random.exponential(1/(2.3), Nt)
    x = np.append(x, sum(Z))

y = sorted(x)

value = y[89] # 90th element to get confidence level of 90%

print('Simulated Value at Risk:', value)

# This value is relatively close to the theoretical value,
# The theoretical value is 339.