

# import packages
import time
import numpy as np
np.random.seed(21)
# initialize variable
num = 10000

# initialize lists
l1, l2 = [i for i in range(num)], [i+2 for i in range(num)]

# initialize arrays
a1, a2 = np.array(l1), np.array(l2)

# start time
start_list = time.time()

# element-wise addition for both lists
sum_lists = [i+j for i, j in zip(l1, l2)]

# stop time
stop_list = time.time()

# display time
print(stop_list - start_list)


# start time
start_array = time.time()

# element-wise addition for both arrays
sum_arrays = a1 + a2

# stop time
stop_array = time.time()

# display time
print(stop_array - start_array)