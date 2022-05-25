#Make a view, change the original array, and display both arrays
import numpy as np 
arr=np.array([12,45,63,96,85,45,25,36,48])
x=arr.view()
arr[0]=100
print(x)
print(arr)
#The view SHOULD be affected by the changes made to the original array.