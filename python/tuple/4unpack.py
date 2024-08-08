# the creation of tuple is known as tuple packing
f = "apple", "mango", "banana"
print(f)

# the extration of tuple is known as tuple unpacking
(red, green, yellow) = f
print(red, green, yellow)

# number of variables much match number of items, the following cases there are 2 var but 3 values inside f i.e ERROR
# (r, g) = f
# print(r, g)

# if number of vars are less than num of items in tuple astick(*) is usually used at last list of vars to denote rest of the items should be assigned in form of list
f = "mango", "banana", "apple", "cherry", "pomeganate"
green, yellow, *red = f
print(green, yellow, red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
f = "banana", "mango", "grapes", "guava", "watermelon", "apple"
yellow, *green, red = f
print(yellow, green, red)

# unpacking works on list too
l = list([1, 5, 7, 9, 11])
x, y, *z = l
print(x, y, z)
