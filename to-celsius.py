#! /usr/bin/python

# get input from user
temp = float(input("What temp in fahrenheit would you like to convert to celsius? "))
celsius = (temp - 32) * 5 / 9

# print out results
print(temp, "F is", round(celsius,2), "C")