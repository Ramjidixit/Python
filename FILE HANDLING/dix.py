f=open("di.txt","w")
str="hello"
f.write(str)
f.close()
f=open("di.txt","r")
str=f.read()
print(str)
f.close()


f=open("di.txt","a+")
f.seek(1,0)
str=" world"
f.write(str)
f.seek(0,0)
str1=f.read()
print(str1)
f.close()


