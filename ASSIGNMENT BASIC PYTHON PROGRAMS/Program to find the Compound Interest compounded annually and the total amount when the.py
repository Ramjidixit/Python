"""Program to find the Compound Interest compounded annually and the total amount when the
	Principal, Rate of Interest and Time are entered by the user."""
	
p=int(input("enter the principle amount:"))
r=eval(input("enter the rate of interest:"))
t=int(input("enter the time period:"))

A = p * (pow((1 + r / 100), t))
CI= A - p
print("Compound interest is", CI)
x=p+CI
print("the total amount=",x)
