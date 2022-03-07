#Write a C program to input month number and print number of days in that month. 
a=int(input("Enter the month number:"))
if(a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12):
    print("Number of days=31")
elif(a==4 or a==6 or a==9 or a==11):
    print("Number of days=30")
else:
    print("Number of days=28 or 29")