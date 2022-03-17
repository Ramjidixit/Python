#Read the string “Hello World” from the user. Make use of continue keyword and remove space.
str1=str(input("Please Enter the String: "))
print(" Entered String is : ", str1)
print("After Removing Spaces, the String becomes:")
for i in str1:
    if i==" ":
        continue
    print(i, end="")