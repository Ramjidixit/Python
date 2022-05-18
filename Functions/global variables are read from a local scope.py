#Write a program where global variables are read from a local scope.
def demo():
    print(s)
s="I love my India"
demo()

"""Before calling the function Demo(), the variable ‘s’ is defined as a string, “I Love
my india”. However, the body of the function Demo() contains only one statement print(s) statement.
As there is no local variable ‘s’ defined within the function Demo(), the print(s) statement uses the
value from the global variable. Hence, the output of the above program will be ‘I Love my india’."""