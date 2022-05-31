#sorting of list 
a=["radhika",'rani','geeta','seeta','billo','meena']
a.sort() #to sort alphabetically 
print(a)

b=[78,52,96,36,45,21,36,78,96,52,36,41,94]
b.sort() #to sort numeriaclly in ascending order
print(b)
b.sort(reverse=True) #to sort in descending order
print(b)

"""case insertive sort-By default the sort() method is case sensitive, 
resulting in all capital letters being sorted before lower case letters"""
c=['Banana',"rahul","Ram","mango"]
c.sort()
print(c)
#to rverse it we use inbuilt function 
c.sort(key=str.lower)
print(c)

#reversing of a list 
d=['Banana',"rahul","Ram","mango"]
d.reverse()
print(d)
