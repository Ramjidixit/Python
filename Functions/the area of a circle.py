"""Write a program to calculate the area of a circle using the formula:
Area of Circle = pi*(r)^2
Declare the default parameter value of pi as 3.14 and radius as 1."""

def area(pi=3.14,r=1):
    area=pi*r*r 
    print("radius=",r)
    print("The area of the circle is:",area)
area()
area(r=4)
area(r=6)