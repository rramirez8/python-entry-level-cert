#! /usr/bin/python
ages = {'kevin':59,'alex':29,'bob':40}
print(ages)

# print items from dict
print(ages['kevin'])

# add entry to dict
ages['kayla'] = 21
print(ages)

# update kevin to 60
ages['kevin'] = 60
print(ages)

# delete an entry
del ages['kevin']
print(ages)

# we can us in and not in on dicts
print('kevin' in ages)
print('kevin' not in ages)

# multiple ways to create a dict

# using dict() funct/class, probably the constrctor
weights = dict(kevin=160,bob=240,kayla=135)
print(weights)

# using dict() with tuples
colors = dict([('kevin','blue'),('bob','green'),('kayla','red')])
print(colors)

# dict.keys gets a list of the keys - must be cast to list
# dict.values gets a list of items - must be cast to list
# dict.items gets a list of tuples for each key/value pair - must be cast to list
ages = {'kevin':61, 'bob':79}
print(ages)
print(list(dict.keys(ages)))
print(list(dict.values(ages)))
print(list(dict.items(ages)))
