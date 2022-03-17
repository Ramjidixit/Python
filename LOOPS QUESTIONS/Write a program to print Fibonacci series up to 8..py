#Write a program to print Fibonacci series up to 8.

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the number of terms:"))
print(a,end=" ")
print(b,end=" ")
for i in range(c+1):
    s=a+b 
    a=b 
    b=s 
    print(s,end=" ")
    