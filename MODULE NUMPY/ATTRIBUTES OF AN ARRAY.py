#ATTRIBUTES OF AN ARRAY 
#1.ndim--the ndim attribute represents the number of dimensions or axes of the array
import numpy as np
a=np.array([1,2,3,4])
b=np.array([[1,2],[3,4]])
print(a.ndim)  #output--1
print(b.ndim)  #output--2

"""2.shape--the shape attribute give the shape of the array if shape attribute is used i one 
one d array,then it will return the number of elements in the form of tuple.if its used in 2 d array 
then it will return a tuple havng first column as row and second column as column."""
a=np.array([1,2,3,4])
b=np.array([[1,2],[3,4]])
print(a.shape)  #output--(4,)
print(b.shape)  #output--(2,2)

"""3. dtype-- return data type of an array"""
a=np.array([1,2,3,4])
b=np.array([[1,2],[3,4]])
print(a.dtype)  #output--int64
print(b.dtype)   #output--int64

#4. reshape--used to change the shape of an array
a=np.array([1,2,3,4])
a=a.reshape(2,2)  #convert in 2 d array
print(a)  #output--[[1 2]
                   # [3 4]]"""
                    
"""5. flatten()--the flatten method is useful to return a copy of the array into one dimensions"""
a=np.array([1,2,3,4])
a=a.reshape(2,2)  #convert in 2 d array
print(a)
a=a.flatten()
print(a)  #output--[1 2 3 4]

"""6.eye function--the eye function cretes two dimension and fills the diagonal element as one 
and rest element as zero."""
import numpy as np 
b=np.array([1,2,8,9,6,7,8,5,2,1,4,7])
b=eye(3)
print(b)
