#basic functions and comparison

p={"amit":9559889697,"raj":7896356252}
q={"amit":9559889697,"raj":7896356252}
r={"amit":9559889697,"raj":7896356252}
print(p)
print(p["amit"]) #dispaly value associated with amit
p["jhon"]=8963522585   #add new element
print(p)
del p["raj"]   #delete key raj
print(p)

print(r==q) #return true if condition is true else false 
