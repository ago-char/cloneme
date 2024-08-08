# accessing values of dict 
# create dictionary 
mydict={
    "quickNap":10,
    "jhutti_cut":"impossible_short",
    "kadak":"unbelievable",
    "cricket":["ABD","MSD","BOSS"]
}

# use of values method for class dict, resulting list will be of class: <class 'dict_values> 
x=mydict.values()
print(x)
print(type(x))

# use of items method for class dict, result list of key:value will be of <class <'dict_items'>
x=mydict.items()
print(x)
print(type(x))

x=list(mydict.items())
print(x[0][1])