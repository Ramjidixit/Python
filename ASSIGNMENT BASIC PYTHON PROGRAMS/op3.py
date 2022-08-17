"""Write a program to calculate simple interest (SI). Read the principle, rate of interest and number
of years from the user."""
p=int(input("Enter the principle amount:"))
r=int(input("Enter the rate of interest:"))
t=int(input("Enter the number of years:"))
print("principle amount=",p)
print("Rate of interst=",r)
print("Number of years=",t)
si=p*r*t/100
print("Simple interst=",si)
