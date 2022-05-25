#Print the value of the base attribute to check if an array owns it's data or not
import numpy as np 
arr=np.array([100,85,69,74,23,56,84,71])
x=arr.copy()
y=arr.view()
print(x.base)
print(y.base)
"""Every NumPy array has the attribute base that returns None if the array owns the data.
Otherwise, the base  attribute refers to the original object. """