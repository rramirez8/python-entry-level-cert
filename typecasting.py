#! /usr/bin/python

print("cast int 1 to float 1.0")
print("using float function")
print(float(1))

print("cast float 1.6 to int 1")
print("using int function, note it will trunc decimal")
print(int(1.6))

print("cast 1 to string")
print(str(1))

print("cast 1.0 to string")
print(str(1.0))

print("cast boolean false to string")
print(str(False))

print("cast string to int, float")
print(int('1'))
print(float('1.6'))

print("cast int,float,str to boolean")
print(bool(1)) #returns boolean
print(bool(1.0))#returns boolean
print(bool('hello'))#returns boolean
print(bool(0)) #returns boolean
print(bool(0.0))#returns boolean
print(bool(''))#returns boolean

print("boolean opertors can be applied to different types")
print("this" and "that") # returns "that"
print("this" and 0) # returns 0
# works with or and not
# and returns first false value or last value
# or returns first true value or last value
# not returns opposite boolean value