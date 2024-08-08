# The setdefault() method returns the value of the item with the specified key. If the key does not exist, insert the key, with the specified value, see example below
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# as value for model already exists do not set model as brono
x = car.setdefault("model", "brono")

print(x)

# Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# as color key does not exist create new key:value pair as such  color:white
x = car.setdefault("color", "white")

print(x)

# form dict with specified key value pair
x = ("key1", "key2", "key3")
y = ("val1", "val2", "val3")
# only key specified so value will be None
thisdict = dict.fromkeys(x)
print(thisdict)
# keys taken from x will each have the value of 1
thisdict = dict.fromkeys(x, 1)
print(thisdict)
# key taken from x will each have the value of y
thisdict = dict.fromkeys(x, y)
print(thisdict)

# as we already have use other methods just description here

"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""
