"""Program to input the centre of a circle, radius of the circle and an arbitrary point P(x,y) 
and determine whether the point is inside the circle, on the circle or outside the circle."""
x=int(input("Enter the first  coordinate of centre of the circle:"))
y=int(input("Enter the second coordinate of centre of the circle:"))
r=int(input("Enter the radius of the circle:"))
a=x+r 
b=y+r 
p1=int(input("Enter the x coordinate of arbitrary point:"))
p2=int(input("Enter the y coordinate of arbitrary point:"))
if(p1<a and p2<b):
    print("The point is inside the circle.")
elif(p1==a and p2==b):
    print("The point is on the circle.")
else:
    print("The poit is outside the circle.")