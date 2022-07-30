colors = ["red","blue","orange","green","yellow"]
uppercase_colors = []
for color in colors:
    uppercase_colors.append(color.upper())
print("The uppercase colors are: ")
print(uppercase_colors)

colors2 = ["red","blue","orange","green","yellow"]
uppercase_colors2 = [color.upper() for color in colors]

print("The uppercase colors 2 are: ")
print(uppercase_colors2)

