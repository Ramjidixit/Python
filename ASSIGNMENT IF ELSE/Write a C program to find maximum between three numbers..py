#Write a C program to find maximum between three numbers. 
x=int(input("enter the number:"))
y=int(input("enter the number:"))
z=int(input("enter the number:"))
if x>y:
    if y>z:
        print(x,"is greater than",y,"and",z)
else:
        print(x,"is less than",y,"and",z)
