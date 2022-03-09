"""A man has certain number of apples.
	If he picks them in a group of 7, he can pick all of them.
	If he picks them in a group of 6, 1 apple is left behind.
	If he picks them in a group of 5, 1 apple is left behind.
	If he picks them in a group of 4, 1 apple is left behind.
	If he picks them in a group of 3, 1 apple is left behind.
	If he picks them in a group of 2, 1 apple is left behind.
	Write a program that identifies the minimum number of apples he has."""

a=int(input("Enter the number of apples:"))
if(a%7==0):
    if(a%6==1):
        if(a%5==1):
            if(a%4==1):
                if(a%3==1):
                    if(a%2==1):
                        print("No of apple is valid which is equal to =",a)
else:
    print("Invalid number of apples.")
