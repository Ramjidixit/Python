#BASICS FUNCTIONS OF DICTIONARY

b={"raj":"9559851102","ramesh":"9636521232"}
b["riya"]="7897399137"      #add new key value pair
print(b)
b["raj"]=9645758525        #modify value for a key
print(b)
del(b["ramesh"])      #delete a key value pair
print(b)
#if you use del(b) it will delete the dictionary object and during runtime it shows error.
print(len(b))    # len return number of key value pairs
print(max(b))    # max return maximum key value
print(min(b))    #min returns minimum key value
print("raju" in b)  #return true if raju is present in b 
print("raju" not in b)  #return true if raju is not present in b 
print(type(b))  #check the type of dictionary
