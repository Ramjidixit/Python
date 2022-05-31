#join list 
a=[1,2,3,4,5]
b=["ram","radhika","raju","ragini","ratan"]
c=a+b #method 1 to join
print(c)
for x in b: #mehod 2 to join 
    a.append(x)
print(a)

a.extend(b) #method 3 to join 
print(a)
