#Write a program to count the number of times a character appears in a given string.
str=input("Enter the string:")
d={}
for ch in str:
    if ch in d:
        d[ch]+=1 
    else:
        d[ch]=1 
for key in d:
    print(key,":",d[key])