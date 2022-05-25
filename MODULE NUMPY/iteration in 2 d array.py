#iteration in 2 d array 
import numpy as np 
arr=np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)    #output is matrix
    
#iterate on every scalar value in 2 d array 
import numpy as np 
arr=np.array([[1,2,3],[4,5,6]])
for x in arr:
    for y in x:
        print(y)     #output is every single element 