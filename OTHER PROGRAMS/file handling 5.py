"""create a file name "info.txt" that stores n random numbers in seaparate line.
after that read the content of file and print average."""
import random

n=int(input("Enter the number of numbers:"))
l=int(input("Enter the last number:")
f=open("info.txt","w")
for i in range(n):
    f.write(str(random.randint(0,l))+" ")

f.close()


