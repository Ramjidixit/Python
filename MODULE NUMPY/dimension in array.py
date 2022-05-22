#dimension in array 
#1. 0 d array-0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
import numpy as np 
a=np.array([87])
print(a)

#2. 1 d array-containg 0 d as its elements 
import numpy as np 
b=np.array([1,2,3,4,5,6])
print(b)

#3. 2 d array-containg 1 d array as its elements
import numpy as np 
c=np.array([[1,2],[3,4]])
print(c)

#4. 3 d array-containg 2 d array as its elements
import numpy as np 
d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d)