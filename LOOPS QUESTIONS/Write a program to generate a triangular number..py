#Write a program to generate a triangular number.
n=int(input("Enter a number:"))
sum=0
for i in range(n,0,-1):
    sum=sum+i 
    i=i+1
print("Triangular number of ",n,"is=",sum)
