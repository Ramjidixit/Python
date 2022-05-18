#Write a program using the global statement
a = 20
def Display():
 global a
 a = 30
print(" The value of a in function:",a)
Display()
print("The value of an outside function:’,a)

"""The program demonstrates the use of the global keyword. The global keyword has
been used before the name of the variable to change the value of the local variable. Since the value
of the global variable is changed within the function, the value of ‘a’ outside the function will be
the most recent value of ‘a’."""