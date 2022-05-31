"""difference between list and tuple 
SR.NO   	LIST	                                                          TUPLE
1	Lists are mutable                                           	Tuples are immutable
2	Implication of iterations is Time-consuming	            The implication of iterations is comparatively Faster
3	The list is better for performing operations, such as insertion and deletionself.	Tuple data type is appropriate for accessing the elements
4	Lists consume more memory	            Tuple consume less memory as compared to the list
5	Lists have several built-in methods	                        Tuple does not have many built-in methods.
6	The unexpected changes and errors are more likely to occur          	In tuple, it is hard to take place.
"""

score=[30,1,2,1,0]
print(score.index(1))  #output-1
print(score.count(1))  #2
print(len(score)) #5
print(max(score)) #30
print(min(score)) #0
print(sum(score)) #34
