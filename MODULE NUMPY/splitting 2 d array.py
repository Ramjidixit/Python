#splitting 2 d array 
import numpy as np 
a=np.array([[1,2],[3,4],[6,7],[8,9]])
b=np.array_split(a,3)
print(b)