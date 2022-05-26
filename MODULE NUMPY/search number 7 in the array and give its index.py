#search number 7 in the array and give its index
import numpy as np 
a=np.array([1,2,3,4,5,7,6,7,8])
x=np.where(a==7)
print(x)


#search using searchsorted()
import numpy as np 
a=np.array([1,2,3,4,5,7,6,7,8])
x=np.searchsorted(a,7)
print(x)