"""wap to write the numbers from 50 to 500 to the file b.txt.all the numbers should come in
different lines."""
f=open("b.txt","w")
for i in range(50,501,1):
    f.write(str(i)+"\n")
f.close()
