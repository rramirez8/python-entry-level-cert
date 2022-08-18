#for and while can have an else

#while example
count = 1
while count <= 4:
    print("the count is: ",count)
    count += 1
else:
    print("this is the else of the while")

# for example
# only use else in a for if you are using a break.
colors = ["red","pink","blue","orange","green"]
for color in colors:
    if color == "orange":
        print("Orange is in the list")
        break
else:
    print("Orange is not in the list")

