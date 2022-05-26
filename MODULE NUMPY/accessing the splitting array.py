#accessing the splitting array 
import numpy as np 
a=np.array([1,2,3,4,5,6])
b=np.array_split(a,3)
print(b[0])
print(b[1])
print(b[2])
