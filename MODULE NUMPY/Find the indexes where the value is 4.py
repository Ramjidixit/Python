#Find the indexes where the value is 4
import numpy as np 
a=np.array([1,2,3,4,4,5,4])
x=np.where(a==4)
print(x)
#it give the indexes where the value of array is equal to 4