"""wap to copy the content of one file (a.txt) to the other file (e.txt)."""
f=open("d.txt","r")
s=f.read()
f.close()

g=open("e.txt","w")
g.write(s)
g.close()
