#counting size of file in bytes and count number of lines
f=open("data.txt","r")
str=f.read()
size=len(str)
print("size of file in bytes:",size)
f.close()
f=open("data.txt","r")
str=f.readlines()
lines=len(str)
print("No. of lines:",lines)
f.close()