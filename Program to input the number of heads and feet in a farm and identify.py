"""Program to input the number of heads and feet in a farm and identify the number of chickens and goats in the farm.
For example, if there are 340 heads and 1,060 feet, there are 150 chickens and 190 goats."""

h=int(input("Enter the total number of heads:"))
f=int(input("Enter the total number of feet:"))
y=(f-(2*h))/2
x=((4*h)-f)/2
print("The total number of chicken=",x,"and total number of goat=",y)