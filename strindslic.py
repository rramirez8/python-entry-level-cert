#! /usr/bin/python

# this exercise is about indexing and slicing strings using [] square brackets for indexing 0 based
mystr = "testing"
print("Indexing")
print(mystr)
print(mystr[0])
print(mystr[len(mystr)-1])
# if you use and index that is too big for a string then you will get and index out of range error

# you can use negative indexing to start from the end of the string
print(mystr[-1])
print(mystr[-2])

# in order to slice up a string, you use a range [0:2], start at index 0 and return upto but not including index 2
print("Slicing")
print(mystr[0:4])
print(mystr[3:5])
print("Print from index 3 to end of string")
print(mystr[3:])

# if you step by 2 you get every other char
print(mystr[0::2])

# you can reverse the string with a negative 1 step value 
print(mystr[::-1])
