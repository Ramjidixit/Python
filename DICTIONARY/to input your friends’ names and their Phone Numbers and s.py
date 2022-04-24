"""Write a program to input your friends’ names and their Phone Numbers and store them in the
dictionary as the key-value pair. Perform the following operations on the dictionary:
a) Display the name and phone number of all your friends
b) Add a new key-value pair in this dictionary and display the modified dictionary
c) Delete a particular friend from the dictionary
d) Modify the phone number of an existing friend
e) Check if a friend is present in the dictionary or not
f) Display the dictionary in sorted order of names"""
n=int(input("Enter the total number of friends:"))
count=1 
d={}
#a
while(count<=n):
    e=input("Enter the name of friend:")
    m=int(input("Enter the mobilr number of friend:"))
    d[e]=m
    count+=1 
print(d)
#b 
d["shyam"]=8963254512
print(d)
#c 
c=input("Enter the  field which u want to delete:")
p=d.pop(c)
print(d)
#d 
g=input("Enter the name of friend which you want to modify:")
f=int(input("Enter the new phone number:"))
d[g]=f 
print(d)
#e 
x=input("Enter the field which u want to check whether its present or not :")
print(x in d)
#f 
z=sorted(d)
print("dictionary in sorted order:",z)