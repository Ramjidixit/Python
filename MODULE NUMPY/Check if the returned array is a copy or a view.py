#Check if the returned array is a copy or a view
import numpy as np 
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a.reshape(6,2).base)
#The example above returns the original array, so it is a view.