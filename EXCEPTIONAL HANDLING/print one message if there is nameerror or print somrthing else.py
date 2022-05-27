#print one message if there is nameerror or print somrthing else.
try:
    print(x)
except NameError:
    print("x is not defined .")
except:
    print("Something is wrong.")
