#Getting some elements out of an existing array and creating a new array out of them is called filtering
#Create an array from the elements on index 0 and 2
import numpy as np
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr) #only print those values for which value is true