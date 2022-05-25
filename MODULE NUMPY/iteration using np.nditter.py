"""iteration using np.nditter--The function nditer() is a helping function 
that can be used from very basic to very advanced iterations.""" 
import numpy as np 
arr=np.array([[1,2,3],[4,5,6]])
for x in np.nditer(arr):
    print(x)
    
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in np.nditer(arr):
    print(x)