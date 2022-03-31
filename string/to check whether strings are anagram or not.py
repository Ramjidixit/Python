#to check whether strings are anagram or not 
a=input() 
b=input() 
if sorted(a)==sorted(b):
    print("anagram") 
else:
    print("not anagram")