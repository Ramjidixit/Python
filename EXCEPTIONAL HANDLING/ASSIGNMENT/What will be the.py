#1. What will be the output?
def fun():
 try:
   print("Hello")
   return 1
 finally:
   print("DONE")
fun()
print("Hi")

"""output:
    Hello
    DONE
    hi"""
