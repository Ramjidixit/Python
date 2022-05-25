"""Enumerate on following 1D arrays elements--Enumeration means mentioning 
sequence number of somethings one by one.Sometimeswe require corresponding index of 
the element while iterating, the ndenumerate() method can be used for those usecases."""
import numpy as np
arr=np.array([1,2,3,4,5])
for idx,x in np.ndenumerate(arr):
    print(idx,x)
"""output=
(0,)1 
(1,)2
(2,)3
(3,)4
(4,)5"""

