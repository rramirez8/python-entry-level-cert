#! /usr/bin/python
# tuples are immutable, cant be changed
point = (2.0,3.0)
print(point)

# add a 3rd point
point3d = point + (4.0,)
print(point3d)

# break up tuple into diffent variables
x,y,z = point3d

print(x)
print(y)
print(z)

# tuples vs lists
# tuples dont change so if it is static use a tuple, it can be unpacked

# create my list
mylist = [1,2,3]
print(mylist)

# create tuble
mytuple = (mylist,1)
print(mytuple)

# create other list
otherlist = [1,2,mytuple]
print(otherlist)

# add 1 to mylist
mylist.append(1)
print(mylist)
print(mytuple)
print(otherlist)
