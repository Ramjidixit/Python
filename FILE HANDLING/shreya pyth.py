# write an existing file
f=open("shreya.txt","a")  #"a"=append-will append to the end of the file
f.write("\nshe is completing her graduation in 2024")
f.close
#open and read the file after appendiung:
f=open("shreya.txt","r")
print(f.read())

#TO OVERWRITE ANY FILE USE W
f=open("shreya.txt","w")   #w method will overwrite any content
f.write("I met her in college 30years ago")
f.close()
#open and read the file after the appending:
f=open("shreya.txt","r")
print(f.read())
