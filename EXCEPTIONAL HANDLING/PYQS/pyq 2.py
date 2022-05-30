"""write an exceptional handling program in python that asks the user to 
enter a number greater than 100 and print it,otherwise explicitly raise an 
exception"""
try:
    a=int(input("Enter the number grater than 100:"))
    if(a>100):
        print(a)
    else:
        raise ValueError
except ValueError:
    print("Check number again.")