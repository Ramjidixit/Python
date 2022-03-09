"""Write a C program to input basic salary of an employee and calculate its Gross salary according to 
	following: 
	Basic Salary <= 10000 : HRA = 20%, DA = 80% 
	Basic Salary <= 20000 : HRA = 25%, DA = 90% 
	Basic Salary >20000 : HRA = 30%, DA = 95% """

b=int(input("Enter the basic salary:"))
if(b<=10000):
    print("Gross salary=",b+((20*b)/100)+((80*b)/100))
elif(b<=20000):
    print("Gross salary=",b+((25*b)/100)+((90*b)/100))
else:
    print("Gross salary=",b+((30*b)/100)+((95*b)/100))