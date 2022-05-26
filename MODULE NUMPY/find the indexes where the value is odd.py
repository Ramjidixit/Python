#find the indexes where the value is odd 
import numpy as np 
a=np.array([1,2,3,4,5,6,7,8,9,25,6,366,74,52])
x=np.where(a%2==1)
print(x)