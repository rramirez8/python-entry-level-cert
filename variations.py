message = input("Please enter a message: ")

print("lower:", message.lower())
print("upper:", message.upper())
print("title:", message.title())
print("capitalize:", message.capitalize())

words = message.split()
print("Words:", words)

sorted_words = sorted(words)

print("Words sorted alphabetically")
print(sorted_words)


print("First alphabetic word")
print(sorted_words[0])

print("Last alphabetic word")
print(sorted_words[-1])

