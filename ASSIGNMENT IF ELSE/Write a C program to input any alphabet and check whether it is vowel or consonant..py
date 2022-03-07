#Write a C program to input any alphabet and check whether it is vowel or consonant. 
chr=str(input("Enter the alphabet:"))
if(chr=='a' or chr=='A' or chr=='e' or chr=='E' or chr=='i' or chr=='I' or chr=='o' or chr=='O' or chr=='u' or chr=='U'):
    print("The given alphabet is vowel.")
else:
    print("The given alphabet is consonant.")