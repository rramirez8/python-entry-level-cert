# this is all the python training from cloud guru

# -------- functions ---------
def hw(name):
    print(name, 'says Hello Everyone')

def do_dict_stuffs():
    # create dict
    ages = {'Kevin':59,'Alex':29,'Bob':40}
    print(ages)
    
    # get value using key
    print(ages['Kevin'])
    
    # add new entry
    ages['Kayla'] = 21
    print(ages)
    
    # update entry
    ages['Kevin'] = 60
    print(ages)
    
    # delete entry
    del ages['Kevin']
    print(ages)
    
    # use in function
    print('Kevin' in ages)
    print('Alex' in ages)
    
    # create dictionaries in different ways
    # use dict function
    weights = dict(kevin=160, bob=240, kayla=135)
    print(weights)
    # pass in a list of tuples to dict function
    colors = dict([('kevin','blue'),('bob','green'),('kayla','red')])
    print(colors)

    
# -------- main ----------
if __name__ == "__main__":
    hw('Richard')
    do_dict_stuffs()
    
    