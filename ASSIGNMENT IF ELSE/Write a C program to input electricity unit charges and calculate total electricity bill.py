"""Write a C program to input electricity unit charges and calculate total electricity bill according to the 
	given condition: 
	For first 50 units Rs. 0.50/unit 
	For next 100 units Rs. 0.75/unit 
	For next 100 units Rs. 1.20/unit 
	For unit above 250 Rs. 1.50/unit """
	
u=int(input("enter the unit expand:"))
if(u<50):
    print("the total electricity charge is =",u*0.50)
elif(u<150):
    v=u-50
    print("charge=",(25+(v*0.75)))
elif(u<250):
    v=u-150
    print("charge=",(100+(v*1.20)))
else:
    v=u-250
    print("charge=",(220+(v*1.50)))
    
