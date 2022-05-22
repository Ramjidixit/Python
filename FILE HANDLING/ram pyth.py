#opening file 
f=open("ram.txt","r")
print(f.read())

#read only parts of the file-by default read() mrthod returns the whole text,but you can also
# specify how many characters you want to print
f=open("ram.txt","r")
print(f.read(5))
print(f.readline()) #read one line using readline()
#to print two line of any text give command two times
f=open("ram.txt","r")
print(f.readline())
print(f.readline())

#print line by line using loop:
f=open("ram.txt","r")
for x in f:
    print(x)


#close files
f=open("ram.txt","r")
print(f.readline())
f.close()
