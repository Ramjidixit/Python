"""Program to find the number of currency notes of each type (Rs. 2000, Rs. 500 and Rs. 100),
	when the total number of currency notes counted altogether is minimum and there must be at
	least a 100 rupee note dispensed. The amount to be withdrawn is to be entered by the user."""
	
a=int(input("enter the amount withdrawn :"))
b=a//2000
#b is the no of notes of 2000
c=a-(b*2000)
d=(c-100)//500
#d is the notes of 500
e=c-(d*500)
f=e//100
#f is the number of notes of 100
print("2000=",b)
print("500=",d)
print("100=",f)