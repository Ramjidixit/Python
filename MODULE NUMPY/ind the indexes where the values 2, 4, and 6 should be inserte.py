#Find the indexes where the values 2, 4, and 6 should be inserted
import numpy as np 
a=np.array([1,2,3,4,5,6,7,8,9])
x=np.searchsorted(a,[2,4,6])
print(x)