#Write a C program to check whether a year is leap year or not. 
a=int(input("Enter the year:"))
if(a%400==0 or a%100!=0 and a%4==0):
    print("The given year is a leap year.")
    
else:
    print("The given year is not a leap year.")