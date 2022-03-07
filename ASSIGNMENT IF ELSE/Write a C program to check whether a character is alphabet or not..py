#Write a C program to check whether a character is alphabet or not. 
chr=str(input("Input the character:"))
a=ord(chr)

if(97<=a<=122 or 65<=a<=90):
    print("The given character is alphabet.")
else:
    print("The given character is not a alphabet.")