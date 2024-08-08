# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change. Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

mydict={
    "quickNap":10,
    "jhutti_cut":"impossible_short",
    "kadak":"unbelievable",
    "cricket":["ABD","MSD","BOSS"]
}

# the reason behind when you print dict it will be printed in the order of insertion is that it is ordered, when it was not ordered,any key:value pair could be displayd first and so on 

# create a dictionary using dict constructor 
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
print(mydict)
print(mydict["cricket"][0])

# accesing dict key:val using index 
keys=list(mydict) # first convert keys of dict to list
print(keys[0],":",mydict[keys[0]]) # print key:val pair i.e of first index which is always 0th