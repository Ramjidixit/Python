#find the indexes where the even value is present in array 
import numpy as np 
a=np.array([1,2,3,4,5,6,7,8,9,10,11,25,86,96,45])
x=np.where(a%2==0)
print(x)
#it gives the different positions at where the even value is present 
