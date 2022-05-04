"""Suppose there are two dictionaries called boys and girls containing
names as keys and ages as values. Write a program to merge the two
dictionaries into a third dictionary."""
boys={"raj":78,"rajeev":85,"rohit":56}
girls={"radhika":56,"rohini":63,"palak":23}
a=print({**boys,**girls})
b=print({**girls,**boys})