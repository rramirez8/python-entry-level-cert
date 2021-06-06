#! /usr/bin/python

#prompt user for a message
message = input("Hey you, whats your message? ")

print("First character", message[0])
print("Last character", message[-1])
print("Middle character", message[int(len(message) / 2)])
print("Even index characters", message[0::2])
print("Odd index characters", message[1::2])
print("String in reverse", message[::-1])
