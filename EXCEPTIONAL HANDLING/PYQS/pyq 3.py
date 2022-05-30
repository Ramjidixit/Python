"""how exceptional handling is done in python
    Exceptions are raised when the program is syntactically correct, 
    but the code resulted in an error.
    This error does not stop the execution of the program,
    however, it changes the normal flow of the program.

how we can raise an exception in python

As a Python developer you can choose to throw an exception if a condition occurs.
To throw (or raise) an exception, use the raise keyword.
Example
Raise an error and stop the program if x is lower than 0:
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

The raise keyword is used to raise an exception.
You can define what kind of error to raise, and the text to print to the user."""