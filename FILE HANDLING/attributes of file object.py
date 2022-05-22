#attributes of file object
f=open("rajeev.txt","w")
print("Name of the file:",f.name)  #f.name-name of the file
print("closed or not:",f.closed)   #f.closed-returns true if the file is closed,false otherwise
print("Opening mode:",f.mode)   #f.mode-return access mode with which file was opened 
print("Softsapce flag:,f.softspace")  #return 0 if space is explicitly required with rpint,1 otherwise
