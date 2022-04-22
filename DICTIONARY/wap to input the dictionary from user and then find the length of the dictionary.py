"""wap to input the dictionary from user and then find the length of the dictionary"""

#(a)using len() function
d=eval(input("Enter the dictionary:"))
c=len(d)  #len only count number of keys
print("The length of the given dictionary is:",c)

#(b)without using len() function
counter=0
for i in d:
    counter=counter+1 
print(counter)