#wap which explain indexerror
list=["raj","rahul","rajeev","raju"]
n=int(input("Enter the index error:"))
try:
    print(list[n])
except IndexError:
    print("out of range.")
