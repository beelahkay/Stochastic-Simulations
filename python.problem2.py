import numpy as np

N = 10000
X = np.array([])

for i in range(0,N):
    counter = 1
    while(np.random.binomial(1, 0.2) == 0):
        counter += 1
    X = np.append(X, counter)
    
print('Empirical Mean:', sum(X)/N )
print('Empirical Variance:', sum((X-(sum(X)/N))**2)/N )


# Theoretical Values for mean and variance:
# Mean = 1/p = 1/0.2 = 5
# Variance = (1-p)/p^2 = (1-0.2)/0.2^2 = 20

# The theoretical and empircal values are very close.