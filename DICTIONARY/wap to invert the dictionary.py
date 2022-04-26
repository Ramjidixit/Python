"""wap to invert the dictionary:
{"aman":"EMP1","jay":"EMP2","madhav":"EMP3"}"""

s={"aman":"EMP1","jay":"EMP2","madhav":"EMP3"}
d={}
for i in s:
    d[s[i]]=i 
print(d)