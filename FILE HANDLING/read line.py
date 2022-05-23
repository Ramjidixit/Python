"""wap to copy all lines of one file (f.txt) to the other file (g.txt) .
copy only those lines which are starting with 172."""
f=open("f.txt","r")
g=open("g.txt","w")
for i in f.readlines():
    if i.startswith("172"):
        g.write(i)
f.close()
g.close()
