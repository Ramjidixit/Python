#Program to input two numbers and subtract the smaller number from the greater number.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    print("Difference=",a-b)
else:
    print("Difference=",b-a)