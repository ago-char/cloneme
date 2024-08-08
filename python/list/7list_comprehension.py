# the concept of list comprehension will help creating new list in very easy and convinient way
# syntax:
# newlist = [ <expression> for <item> in <iterable> [if condition == True] ]
# the <expression> is one which will be appended in newlist
# for eg: you are given to create list of numbers which are exactly divisible by 4 which are greater than 0 not exceeding 100
newlist = []
for x in range(1, 101):
    if not x % 4:
        newlist.append(x)
print(newlist)

# let's do the same with list comprehension (one liner)
anotherlist = [x for x in range(1, 101) if not x % 4]
print(anotherlist)

# ok this seems fun but not much difference in effort wise, suppose you are given to create new list from existing list of Friends whose name does not have 't' letter
frns = ["Smarika", "Teena", "Nikita", "Prajita", "Niruta"]
newlist.clear()
for f in frns:
    if "t" not in f and "T" not in f:
        newlist.append(f)
print(newlist)

# using list comprehension you can do that in one line
anotherlist = [f for f in frns if "t" not in f and "T" not in f]
print(anotherlist)
