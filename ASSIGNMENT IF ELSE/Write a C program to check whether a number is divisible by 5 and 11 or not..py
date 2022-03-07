#Write a C program to check whether a number is divisible by 5 and 11 or not. 
a=int(input("Enter the number:"))
if(a%5==0 and a%11==0):
    print("The given number is divisible by 5 and 11")
else:
    print("Not divisible.")