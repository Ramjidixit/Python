#opening file ,closing file and writing text
def main():
    a=open("raj.txt","w")   #open a file in write mode
    a.write("Hello\n")
    a.write("Welcome to gla")
    a.close() #closing a file 
main() #call to main function


#--------------writing something to a file-----------


#write numbers from 1 to 20 to the file rajeev.txt
def main():
    a=open("rajeev.txt","w")    #open file in write mode
    for x in range(1,21): #iterate from 1 to 20
        x=str(x)   #convert number to string
        a.write(x)    #write number to output file
        a.write(" ")   #space to separate numbers
    a.close()  #close file
main()



#generate 50random numbers within a range 500 to 1000 and write them  to file anshul.txt
from random import randint    #import random module
f=open("anshull.txt","w")   #open file in write mode
for x in range(51): #iterate for 50 times
    x=randint(500,1000)       #generate one random number
    x=str(x) #convert number to string
    f.write(x+" ") #write number to output file
f.close() #finish writing close the file

#-------reading text from a file------------


#write a program to read the content of file ram.txt using the read() method
f=open("ram.txt","r")   #open file in read mode in which data is already present
text=f.read()
print(text)
"""output:
========= RESTART: C:/Users/rajpu/Desktop/New folder (2)/hiiiiiii.py ==========
welcome
to the world of galamour
aur btao kya hall chaaal hai 
theek ho tum        this text was already presnt there """
#alterante method for this question
a=open("ram.txt","r")
for line in a:
    print(line)


#reading numbers from from a file

#write a program to read the content of the file ggg.py
f=open("ggg.txt","r") #open file in read mode
num=f.read()  #return entire of the file as string
print(num)
print(type(num))  #check the type of num


#write a program to read the contents of a file grades.txt and calculate the total marks and percentage obtained by a student.
a=open("grades.txt")
n=int(a.readline()) #read first line of file
print("Total number of students:",n)
for i in range(n):
    print("student #",i+1,":",end=" ")
    allgrades=(a.readline().split())
    print(allgrades)
    sum=0
    for j in range(len(allgrades)):
        sum=sum+int(allgrades[j])
        per=float((sum/500)*100)
    print("Total=",sum,"\npercentage=",per)
    print("\n")
