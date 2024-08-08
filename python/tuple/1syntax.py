# tuples are ordered, indexed but immutable i.e unchangable(i.e cannot use assignment operator to assign/change particular item)
# tuple holds multiple value for 1 var seperated by comma (,)
t = "sagar", "simran", "swaita"
print(t)
print(type(t))

# parenthesis are not mandetory but good practice
t = ("smarika", "deeya", "deepu")
print(t)
print(type(t))

# use of tuple constructor
t = tuple(("puja", "pujan", "pooja"))  # notice double parenthesis
print(t)
print(type(t))

# create tuple with only one item
f = "sadikshya"  # this is string
print(f)
print(type(f))
f = ("sadikshya",)  # this is tuple
print(f)
print(type(f))

print(len(t), len(f))  # length of tuple
