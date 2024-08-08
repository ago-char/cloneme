# index and count method for tuple
t = 1, 2, 9, 11, 23, 1

# index() return index for particular value (first occurance)
value = 11
if value in t:
    print(value, "lies in index", t.index(value), "in tuple 't'.\n")
else:
    print(value, "is not in tuple 't'.\n")

# count() return no. of times value is found in tuple
value = 111
if value in t:
    print(value, "occurs", t.count(value), "times in tuple 't'.\n")
else:
    print(value, "is not in tuple 't'.\n")
