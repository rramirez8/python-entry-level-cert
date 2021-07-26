#! /usr/bin/python

# create at list
mylist = [1,2,3]

# append to the list
mylist.append(4)
print(mylist)

# insert in the middle of the list
mylist.insert(0, 'a')
print(mylist)

# get value of specific index
mylist = [1,2,3]
print(mylist)
print(mylist.index(1))

# using in to ask the question
print(4 in mylist)
print(4 not in mylist)

# use sorted method
mylist = [1,3,4,8,2]
print(mylist)
print(sorted(mylist))

# use reverse on list then change back to list
print(list(reversed(mylist)))

# use them all together
print(list(reversed(sorted(mylist))))