#! /usr/bin/python

# lesson in immutability
mystr = "testing"
print(mystr)
print(mystr.capitalize())
print(id(mystr))
print(id("testing"))

otherstr = "testing"
print(id(mystr) == id(otherstr))


