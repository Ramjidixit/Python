#Write a program to traverse every second character of a string using the for loop.

s="ILOVEGLA"
for ch in range(0,len(s),2):
    print(s[ch],end=" ")