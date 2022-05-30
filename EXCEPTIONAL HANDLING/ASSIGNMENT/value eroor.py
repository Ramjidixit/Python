#wap which explain Valueerror
a=int(input("Enter the number:"))
try:
    if(a<0):
        raise ValueError
    else:
        print(a)
except ValueError:
    print("please check your number and enter positive one.")
