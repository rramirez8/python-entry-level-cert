name = input("What is your name ")

if len(name) >= 6:
    print("Your name is long")
elif len(name) == 5:
    print("Your name is 5 chars long")
elif len(name) >= 4:
    print("your name is 4 or more chars")
else:
    print("your name is short")


