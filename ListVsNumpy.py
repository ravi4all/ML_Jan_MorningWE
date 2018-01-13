import numpy as np
import time

SIZE = 100000000

list_1 = range(SIZE)
list_2 = range(SIZE)

# start = time.time()
#
# for x,y in zip(list_1, list_2):
#     result = x+y
#
# end = time.time()
# print("Total Time By list",end-start)

start = time.time()

arr_1 = np.arange(SIZE)
arr_2 = np.arange(SIZE)

arr_result = arr_1 + arr_2

end = time.time()

print("Total time by numpy array",end-start)