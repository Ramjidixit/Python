#find the indexes where the value 7 should be inserted, starting from the right


import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

import numpy as np 
a=np.array([2,3,7,8])
x=np.searchsorted(a, 7, side='right')
print(x)