#Convert the following 1-D array with 12 elements into a 2-D array
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x=arr.reshape(4,3)
print(x)

y=arr.reshape(3,4)
print(y)