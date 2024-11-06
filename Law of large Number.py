# importing library and the normal distribution function
import numpy as np
import numpy as numpy
from numpy.random import randn

# setting parameters where N is the quantity of random numbers
N = 1000000
counter = 0

# iterating to generate the N random numbers
for j in randn(N):
    if j > -1 and j < 1:
        counter = counter + 1
print(counter/N)

# Will improve by using a list for N = [100, 1000, 10000, 100000, 1000000] and printing E(X) simultaneously for all N
