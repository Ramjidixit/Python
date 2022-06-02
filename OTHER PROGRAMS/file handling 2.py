"""there is a file name 'file1.txt' with some content.read file from user and crete two new file
that as file2.txt which contain only alphabet and  and file3.txt whiich contain only numbers."""
f=open("file1.txt","w")
f.write("""ramlaal,1,8,6,9,radhika,rajeev,raju""")
f.close()
g=open("file1.txt","r")
h=open("file2.txt","w")
j=open("file3.txt","w")
x=g.read()
if(x==char):
     h.write(char)
else:
    j.write()
g.close()
h.close()
j.close()
