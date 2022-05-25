#Stacking Along Rows
#NumPy provides a helper function: hstack() to stack along rows.
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr) 

#Stacking Along Columns
#NumPy provides a helper function: vstack()  to stack along columns
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr) 

#Stacking Along Height (depth)
#NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr) 