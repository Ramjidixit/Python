"""Program to find the number of currency notes of each type (Rs. 2000, Rs. 500 and Rs. 100),
	when the total number of currency notes counted altogether is minimum and there must be at
	least a 100 rupee note dispensed. The amount to be withdrawn is to be entered by the user."""
	
a=int(input("enter the amount withdrawn :"))
if a<500:
    print("the number of notes required is of 100=",a//100)
elif(a==500):
    print("the number of notes requires is of 500 which is =1")
elif(500<a<2000):
    if(500<a<1000):
        print("the no of notes of 500=1 and the 100 rupee note=",(a-500)//100)
    elif(a==1000):
        print("two notes of 500 require.")
    elif(1000<a<1500):
        print(" the number of notes of 500=2 and the 100 rupee note= ",((a-1000)//100))
    elif(a==1500):
        print("three notes of 500 require.")
    elif(1500<a<2000):
        print("the no of notes of 500=3 and the 100 rupee note=",(a-1500)//100)
    else:
        print(" a single note of 2000 require.")
if(a>2000):
    x=a//2000
    y=(a-(2000*x))//500
    z=(a-((2000*x)+(500*y)))//100
    print("The no of notes of 2000=",x,".The no of notes of 500=",y,"The number of notes of 100=",z)