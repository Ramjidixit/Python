"""Program to find whether a triangle is scalene, isosceles, right angled or invalid when the sides of
	the triangle are entered by the user."""
	
a=int(input("enter the first side of triangle:"))
b=int(input("enter the second side of triangle:"))
c=int(input("enter the third side of triangle:"))
if(a==b or b==c or c==a):
    print("The triangle is isosceles.")
elif((a==((b**2)+(c**2))**0.5) or (b==((a**2)+(c**2))**0.5) or (c==((b**2)+(a**2))**0.5)):
    print("The triangle is right angled triangle")
elif(a+b<c or b+c<a or a+c<b):
    print("The triangle is invalid.")
else:
    print("the triangle is scalene")