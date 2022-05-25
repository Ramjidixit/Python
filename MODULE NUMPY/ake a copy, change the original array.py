#Make a copy, change the original array, and display both arrays:
import numpy as np 
arr=np.array([1,2,3,4,5,6,7,8,9])
x=arr.copy()
arr[0]=25
print(x)
print(arr)