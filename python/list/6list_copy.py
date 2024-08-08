l = ["Smarika", 20, "SukraBare", 4.5]
# simple assignment operater will do copy. but the problem with this is 'x' will only be the reference of 'l' meaning that any changes on 'l' (only by using list state changing methods i.e list methods/functions) will be reflected in 'x'
x = l
# use list function to convert list 'l' to list 'y'
y = list(l)
# copy list 'l' to 'z' using copy method for <class 'list'>
z = l.copy()
print(type(l), type(x), type(y), type(z))
print(l, x, y, z)

# changes in 'l' affecting 'x'
l.insert(1, "Nepal")
print(l, x)

# Additional information: Count the occurance of element 'e' using count method as such : list.count(element)
