#creating array using numpy and checking class 
import numpy as np 
a=np.array([1,2,3,4,5,6,7,8,9,10])
print(a)
print(type(a))

"""To create an ndarray, we can pass a list, tuple or any array-like 
object into the array() method, and it will be converted into an ndarray:"""
b=np.array((1,8,9,6,7,4,5))
print(b)
print(type(b))
