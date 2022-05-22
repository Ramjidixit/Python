""" create a new file
use the open () method with any one of the following parameters:
"x"-create -will create a file ,returns an error if file exist
"a"-append-will create a file if the specified file does not exist
"w"-write-will create a file if the file does not exist"""
f=open("raju.txt","x")
#delete a file
import os
os.remove("raju.txt")

#check if file exist
import os
if os.path.exists("raju.txt"):
    os.remove("raju.txt")
else:
    print("The file does not exist ")
