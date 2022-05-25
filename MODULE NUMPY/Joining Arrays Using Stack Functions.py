"""Joining Arrays Using Stack Functions
Stacking is same as concatenation, the only difference is
that stacking is done along a new axis.
We can concatenate two 1-D arrays along the second axis which 
would result in putting them one over the other, ie. stacking.
We pass a sequence of arrays that we want to join to the stack() 
method along with the axis. If axis is not explicitly passed it is taken as 0."""
import numpy as np 
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(np.stack((a,b),axis=1))
"""output:
[[1 5]
 [2 6]
 [3 7]
 [4 8]]
