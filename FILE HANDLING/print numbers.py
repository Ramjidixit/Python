"""wap to write the numbers from 50 to 500 to the fle a.txt.all the numbers
should be one space separated."""


f=open("a.txt","w")
for i in range(50,501,1):
    f.write(str(i)+" ")
f.close()
