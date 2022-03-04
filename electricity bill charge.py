#To calculate electricity bill
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