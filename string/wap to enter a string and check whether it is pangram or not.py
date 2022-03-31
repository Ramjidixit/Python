"""wap to enter a string and check whether it is pangram or not"""
a=input()
b="abcdefghijklmnopqrstuvwxyz"
c=0
for i in b:
    if i in a:
        c=c+1 
if c==26:
    print("pangram ")
else:
    print("not pangram")