#splitting the array 
import numpy as np 
arr=np.array([1,2,3,4,5,6])
c=np.array_split(arr,3)
print(c)
#output-[array([1,2]),array([3,4]),array([5,6])]