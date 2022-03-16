"""Big Bazaar specifies its customers into three categories as Bronze, Silver and Gold. If the shopping amount 
is greater than 25000, the category is GOLD. If the shopping amount is between 10000 and 25000, the 
category is SILVER, otherwise the category is BRONZE. The discount offered for GOLD customers is 20% of the 
shopping amount, for SILVER customers is 10% of the shopping amount and 5% otherwise. Design a program in python 
that asks the user to input the total shopping amount, outputs the category and amount to be paid."""

b=int(input("Enter the total shopping amount:"))
if(b>=25000):
    print("Hey, your category is Gold.")
    a=b-((b*20)/100)
    print("Amount to be paid=",a)
elif(10000<b<25000):
    print("Hey, your category is Silver.")
    a=b-((b*10)/100)
    print("Amount to be paid=",a)
else:
    print("Hey, your category is Bronze.")
    a=b-((b*5)/100)
    print("Amount to be paid=",a)