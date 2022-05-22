#step slicing
import numpy as np 
a=np.array([1,8,9,6,5,7,5,1,4,6,3,5])
#Return every other element from index 1 to index 5:
print(a[1:5:2])
#Return every other element from the entire array:
print(a[::2])