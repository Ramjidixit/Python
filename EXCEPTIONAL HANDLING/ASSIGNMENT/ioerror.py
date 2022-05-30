#wap which explainn IOError
f=open("rrrr.txt","r")
try:
    f.write("This show a magic.")
except IOError:
    print("please check properly")
