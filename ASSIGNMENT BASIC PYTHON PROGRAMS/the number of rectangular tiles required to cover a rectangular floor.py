""". Program that calculates the number of rectangular tiles required to cover a rectangular floor if
	the dimensions of the floor and the dimensions of a tile are entered by the user."""
	
a=int(input("enter the length of floor:"))
b=int(input("enter the breadth of floor:"))
c=int(input("enter the length of tile:"))
d=int(input("enter the breadth of tile:"))
x=((a*b)//(c*d))
print("the number of rectangular tiles required to cover a rectangular floor=",x)
