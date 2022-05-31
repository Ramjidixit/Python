"""list comprehnsion-List comprehension offers a shorter syntax when you want to 
create a new list based on the values of an existing list."""
#print the new list with items starting with s 
a=["sanjana",'aarti','shreya','sweety','sachin','pohu','kuhu','sarthak']
new=[]
new1=[]
for x in a:
    if "s" in x:
        new.append(x)
print(new)

for x in a:
    if "s" not in x: #to print other than starting with s 
        new1.append(x)
print(new1)

newlist = [x.upper() for x in a] #to convert every letter to upper 
print(newlist)

r=['hello' for x in a]  #to convert every element to hello 
print(r)

