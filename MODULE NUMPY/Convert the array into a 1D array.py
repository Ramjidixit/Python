"""Convert the array into a 1D array----Flattening array means converting 
a multidimensional array into a 1D array. We can use reshape(-1) to do this."""
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr) 