'''Design a program in python to display the number of days left in the current year (2022), 
when today’s date is entered by the user in format of your choice.'''

m=int(input("Enter the current month number:"))
d=int(input("Enter the today's date:"))
if(m==1):
    print("Number of days left=",365-(0+d))
if(m==2):
    print("Number of days left=",365-(31+d))
if(m==3):
    print("Number of days left=",365-(59+d))
if(m==4):
    print("Number of days left=",365-(90+d))
if(m==5):
    print("Number of days left=",365-(120+d))
if(m==6):
    print("Number of days left=",365-(151+d))
if(m==7):
    print("Number of days left=",365-(181+d))
if(m==8):
    print("Number of days left=",365-(212+d))
if(m==9):
    print("Number of days left=",365-(243+d))
if(m==10):
    print("Number of days left=",365-(273+d))
if(m==11):
    print("Number of days left=",365-(304+d))
if(m==12):
    print("Number of days left=",365-(334+d))


