#extend list-to add element from another list 
a=['arm','raju','raghav','raghvendra','rajshree']
b=['raju','ragini','ratinder']
a.extend(b) #to add elements of b to a 
print(a)
b.extend(a) #to add element of a to b 
print(b)

#we can also add tuple to list 
c=("kavya",'shreya')
a.extend(c) #same method is also apply here as for adding list to list 
print(a)
