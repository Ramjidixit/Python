"""wap to enter the value of n and then create the following dictionary
{1:1,2:4,3:9,.............}"""

n=int(input("Enter the value of n:"))
e={}
for i in range(1,n+1):
    e[i]=i**2
print(e)