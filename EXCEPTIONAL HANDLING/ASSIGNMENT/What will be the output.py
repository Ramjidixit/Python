#What will be the output?
def fun():
 for i in range(5):
  try:
   if i==0:
    print("Hello")
    break
  finally:
   print("DONE")
fun()
print("Hi")

"""output:
   Hello
   DONE
   hi"""