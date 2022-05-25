#creating dimension according to user by giving ndmin function
import numpy as np 
arr=np.array([1,2,3,4,5], ndmin=5)
print(arr)
print("Number of dimensions:",arr.ndim)