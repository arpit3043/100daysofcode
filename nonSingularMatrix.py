import numpy as np
# initialize array B and Identity matrix
B = np.array([[2, 0, -1],[0, 2, -1],[-1, 0, 1]])
I = np.identity(3)
m = np.array(I)*3
# calculate result
A = np.subtract(m,B)
print(A)
# Code ends here