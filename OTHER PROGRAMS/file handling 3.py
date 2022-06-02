"""there are two file a and b .write a program to cretae a new file "c.txt"
that store lines alternatively.if content of any line finish then just copy the
content of another line"""
f=open("a.txt","r")
g=open("b.txt","r")
h=open("c.txt","w")
x=f.readlines()
y=g.readlines()
for i in range(0,len(x)):
    for j in range(0,len(y)):
        k=f.readline()
        h.write(k)
        l=g.readline()
        h.write(l)
f.close
g.close()
h.close()
