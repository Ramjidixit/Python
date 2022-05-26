#Use the hsplit() method to split the 2-D array into three 2-D arrays along rows
import numpy as np 
a=np.array([[1,2,3],[3,4,5],[5,6,7]])
b=np.hsplit(a,3)
print(b)