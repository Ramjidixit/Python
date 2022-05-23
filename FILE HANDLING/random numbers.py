"""wap to write the n random numbers between 100 to 200 to the file c.txt.
all the numbers should be one space separated."""
import random
f=open("c.txt","w")
n=int(input("Enter the n:"))
for i in range(n):
    f.write(str(random.randint(100,200))+" ")
f.close()
    
