#! /usr/bin/python

# setting a binary value
print("setting a to binary 2")
a = 0b10
print (a)

# bitwise compliment operator
# will take the value you pass it and multiply by negative 1 then subtract one
# so 2 will become a -3
print("bitwise compliment operator on 2, ~2")
print(~2)

# bitwise operators AND, OR, XOR, NOT
# set some variables
print("set a to binary 1001")
print("set b to binary 1100")
a = 0b1001
b = 0b1100
print(a)
print(b)

print("lets try OR with | ") # should be 1101
print(bin(a | b))

print("lets try AND with & ") # should be 1000
print(bin(a & b))

print("lets try XOR with ^ ") # should be 0101, xclusive OR only true if they are different both 1 or both 0 yields a 0
print(bin(a ^ b))

# shift operators move the decimal to the left or right
# counter intuitive >> moves to the left, << moves to the right
print("lets try shifting the decimal to the left using >>")
print(bin(a >> 2)) # should be 10

print("lets try shifting the decimal to the right using <<")
print(bin(a << 2)) # should be 100100