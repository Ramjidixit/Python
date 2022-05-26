#Split the 2-D array into three 2-D arrays along rows
import numpy as np 
a=np.array([[1,2],[3,4],[5,6],[7,8]])
b=np.array_split(a,3,axis=1)
print(b)