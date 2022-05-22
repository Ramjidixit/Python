#Change data type from float to integer by using 'i' as parameter value:
#using astype function 
import numpy as np 
a=np.array([1.1,1.2,1.8,3.2,5.6])
print(a.dtype)
b=a.astype("i")
print(b.dtype)

#change data type from float to bool
import numpy as np 
a=np.array([1.1,1.2,1.8,3.2,5.6])
print(a.dtype)
b=a.astype("bool")
print(b.dtype)