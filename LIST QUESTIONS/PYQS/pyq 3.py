"""write down four methods of list in python.how do you create a list for a 2 d matrix with 
three rows and four columns and four elements with value 0

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
"""

#what is the output?
matrix=[]
matrix.append(3*[1])
matrix.append(3*[1])
matrix.append(3*[1])
matrix[0][0]=2
print(matrix)
#output-[[2,1,1],[1,1,1],[1,1,1]]
