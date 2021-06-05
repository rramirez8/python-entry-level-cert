#! /usr/bin/python

name = input("What is your name? ")
color = input("What is your favorite color? ")
age = input("How old are you today? ")

#print the old fashioned way
print("The old way")
print(name, end=" ")
print("is " + str(age) + " years old", end=" ")
print("and loves the color " + color + ".")

# print using the separator 
print("The better way")
print(name, "is", age, "years old and loves the color", color, sep=" " )
# the default separator is a single space " "