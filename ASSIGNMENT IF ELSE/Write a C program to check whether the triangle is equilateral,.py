#Write a C program to check whether the triangle is equilateral, isosceles or scalene triangle. 

a=int(input("Enter the first side of triangle:"))
b=int(input("Enter the second side of triangle:"))
c=int(input("Enter the third side of triangle:"))
if(a<=b+c or b<=a+c or c<=a+b):
    if(a==b==c):
        print("The triangle is equilateral.")
    elif(a==b or b==c or c==a):
        print("The traingle is isosceles.")
    else:
        print("The traingle is scalene.")
else:
        print("triangle is not valid.")