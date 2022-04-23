#basic dictionary functions 
s={"raj":89,"rahim":78,"raju":12}
print(s.keys())          #print only keys
print(s.values())            #print only values  
 
#creating a dictionary from name and value pairs
t=dict(zip(("name","age","mobile "),("ramlaal",89,7897399137)))
print(t)

#adding elements to a dictionary
s["ansh"]=85   
print(s)     
print("ansh" in s.keys())
