import numpy as np

N = 10000
x = list()
y = list()

np.random.seed(420)

for i in range(N):
    U = np.random.uniform(0,1)
    
    if U < 0.25:
        x.append(1)
        y.append(0)
    
    elif U < 0.50:
        x.append(0)
        y.append(1)
    
    elif U < 0.75:
        x.append(-1)
        y.append(0)
        
    else:
        x.append(0)
        y.append(-1)

print("Cov", np.cov(x,y))

# In the top right and bottom left outputs, the covariance
# of x and y is given. This simulated, empircal value
# is very close to zero.

# Theoretical value:
# Cov(x,y) = E[xy] - E[x] * E[y]
# E[xy] = 1*0*0.25 + 0*1*0.25 + (-1)*0*0.25 + 0*(-1)*0.25 = 0
# E[x] = 1*0.25 + 0*0.50 + (-1)*0.25 = 0
# E[y] = 1*0.25 + 0*0.50 + (-1)*0.25 = 0
# Cov(x,y) = 0

# Therefore, the empirical covariance is very close to the
# theoretical value for covariance.