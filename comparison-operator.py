#! /usr/bin/python

print("1 < 2")
print(1 < 2)

print("2 > 1")
print(2 > 1)

print("2 < 1")
print(2 < 1)

print("a > b")
print('a' > 'b')

print("a < b")
print('a' < 'b')

print(ord('a'))
print(ord('A'))
print(ord('A') < ord('a'))

print("1 == 1")
print(1 == 1)

# == comparison operator can compare str to int
print("'a' == 1")
print('a' == 1)

print("'a' == 'a'")
print('a' == 'a')

print("1 != 1")
print(1 != 1)

print("2 != 1")
print(2 != 1)

# identity operator compares to see if its the same object, the is operator
# integers are immutable
print("1 is 1")
print(1 is 1)

print("1 is 1.0")
print(1 is 1.0)

# string are also immutable
print("'a' is 'a'")
print('a' is 'a')

print("'a' is not 'a'")
print('a' is not 'a')

# you can print the id of an object such as a str or int
print("id('a')")
print(id('a'))

print("id(1)")
print(id(1))

# lists are NOT immutable so . . .
print("[] is []")
print([] is [])