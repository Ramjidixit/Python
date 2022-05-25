#Join two 2-D arrays along rows
import numpy as np 
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,11,12]])
arr=np.concatenate((a,b),axis=1)
print(arr)
#it concatenate only first row of first with first row of second matrix and second row of first with second row of second.