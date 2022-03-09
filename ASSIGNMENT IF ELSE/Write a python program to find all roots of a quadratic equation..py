#Write a C program to find all roots of a quadratic equation. 
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
r=((-b)+(((b*b)-(4*a*c))**0.5))/(2*a)
d=((-b)-(((b*b)-(4*a*c))**0.5))/(2*a)
print("Root =",r,"and ",d)