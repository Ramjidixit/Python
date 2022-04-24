#Write a program to enter names of employees and their salaries as input and store them in a dictionary.
n=int(input("Enter the number of total employees:"))
c=dict()
count=1
while(count<n+1):
    a=input("enter the name of employee:")
    b=int(input("Enter the salary:"))
    c[a]=b
    count+=1
print(c)
    