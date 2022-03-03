cp=eval(input("Enter the cost price:"))
sp=eval(input("enter the selling price:"))
if(sp>cp):
        profit=sp-cp
        print("the profit made= ",profit)
else:
        loss=cp-sp
        print("the loss made= ",loss)