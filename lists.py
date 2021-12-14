#! /usr/bin/python
# lists are for squares because they are represented by square brackets[]
print('lists are for squares because they are represented by square brackets[]')
mylist = [1,2,3,4,5]
print(mylist)

# does not have to be of a certain type, can store mixed types
print('does not have to be of a certain type, can store mixed types')
other_list = ['a',1,1.0,False]

# reference individual elements in a list using index, zero based
print('reference individual elements in a list using index, zero based')
mylist[0]
mylist[3]
#mylist[6]

# len function works on list also
print('len function works on list also')
len(mylist)

# slicing also works on lists as it does on strings
print('slicing also works on lists as it does on strings')
mylist[0:2]
mylist[1:]
mylist[::-1]
mylist[::2]

# modify the list in place
print('modify the list in place')
mylist[0] = 'a'
print(mylist)

# you can concat lists and append to lists
print('you can concat lists and append to lists')
print(mylist + [8,9,10])

mylist += [8,9,10]
print(mylist)

# you can assign a new list to a subset of items in the existing list
print('you can assign a new list to a subset of items in the existing list')
mylist[1:3] = ['b','c']
print(mylist)

# doesnt have to match the size
print('doesnt have to match the size')
mylist[3:5] = ['d','e','f']

# you can remove the contents by replacing with a blank list
print('you can remove the contents by replacing with a blank list')
mylist = ['a','b','c','d',5,6,7]
print(mylist)
mylist[4:] = []
print(mylist)

# you can remove an item in a list using the del STATEMENT not function
print('you can remove an item in a list using the del STATEMENT not function')
del mylist[0]
print(mylist)



