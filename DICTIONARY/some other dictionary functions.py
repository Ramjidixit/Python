#some other dictionary functions

s={"raj":89,"rahim":78,"raju":12,"anshul":48}
print(len(s))    #to measure length
print(s.get("raj"))   #to get the value of any keys
print(s.items())   #to print the items of dictionary
print(s.values())    #to print values
print(s.keys())   #to print keys

a=dict.fromkeys([1,2,3,4,5],10) #associate values
print(a) 
#output-{1:10,2:10,3:10,4:10,5:10}
b=dict.fromkeys([1,2,3,4,5],(6,7,8))
print(b)
#output-{1:(6,7,8),2:(6,7,8),3:(6,7,8),4:(6,7,8),5:(6,7,8)

#setdefault() function to insert a new key value pair
s.setdefault("anshi",85)
print(s)
s["anshi"]=23
print(s)

c=s.popitem() #delete the last item
print(c)

l=sorted(s)  #sort according to ascii value
print(l)
p=sorted(s,reverse=True)  #sort in reverse order
print(p)
print(sorted (s.values())) #to sort the value in ascending order
print(sorted(s.items()))  #sort according to key value
print(min(s)) #print minimum key means having minimum ascii value
print(max(s))
# if the values of keys are numeric and want to add use sum() function 