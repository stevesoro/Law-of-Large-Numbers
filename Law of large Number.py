# importing library and the normal distribution function
import numpy as np
from numpy.random import randn

# setting a list for the quantity of random numbers to be generated
N = [10, 100, 1000, 10000, 100000, 1000000]

# iterating to generate the sets of random numbers and the estimate of the average of those between -1 and 1 for each case
for i in N:
    counter = 0  # Resetting counter for each value of N
    for j in randn(i):
        if j > -1 and j < 1:
            counter += 1
    print(f"For N = {i}, result = {counter / i}")
    
# After running the code, we see that, as N grows, the average converges to 0.68.
