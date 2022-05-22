#calculating size of file with and without using blanck lines.
f=open("data.txt","r")
str1=" "
size=0
tsize=0
while str1:
    str1=f.readline()
    tsize=tsize+len(str1)
    size=size+len(str1.strip())
print("Total size:",tsize)
print("size after removing all EOL and blanck lines:",size)
f.close()
