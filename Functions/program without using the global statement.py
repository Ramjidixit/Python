#Write a program without using the global statement.
a=20
def demo():
    a=30
    print("The value of a is=",a)
demo()
print("The value of a is=",a)