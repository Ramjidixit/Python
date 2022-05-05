#write a python program to get the maximum and minimum value in a dictionary.
d={"rahim":78,"raj":56,"shreya":99}
p=max(d,key=d.get)
print("The highest value =",p,"which is equal to",d[p])
q=min(d,key=d.get)
print("The minimum value=",q,"which is equal to",d[q])