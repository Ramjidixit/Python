#Check if the number entered is prime or not.
n=int(input("Enter the number:"))
x=n 
for i in range(2,n):
    if n%i==0:
        flag=0
        break
    else:
        flag=1 
if(flag==0):
    print("Number is not prime.")
else:
    print("Number is prime.")