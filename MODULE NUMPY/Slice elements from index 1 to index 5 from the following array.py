#Slice elements from index 1 to index 5 from the following array:
import numpy as np 
a=np.array([1,5,8,9,7,8,9,6,5,2,4])
print(a[1:5])

#Slice elements from index 4 to the end of the array:
import numpy as np 
b=np.array([8,9,6,7,5,2,4,6,9,8,2,3,7,8])
print(b[4:]) 

#Slice elements from the beginning to index 4 (not included):
import numpy as np 
c=np.array([8,9,7,5,6,4,1,8,9,5,3])
print(c[:4])