"""there are 10 students in a class.wap to print the names that coccur in another file
more than  one time.the file name will be given by user and all the new names
should be written in another file"""
f=open("student.txt","r")
g=open("new.txt","w")
x=f.read()
if(x==x):
    g.write(x)
f.close()
g.close()
