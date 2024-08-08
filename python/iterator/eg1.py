"""Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:"""

s = "shyam"


myiter = s.__iter__()

print(type(myiter))

print(next(myiter))
print(next(myiter))

# now this iteraotr contains __next__ function within it which will help getting next obj from iterable
print(myiter.__next__())


"""
Note that:
    s.__iter__() ==> iter(s)
    myiter.__next__() ==> next(myiter)
"""
