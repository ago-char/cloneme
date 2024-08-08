# set, like tuple can store multiple values in single var but the difference is
# set is unordered i.e any item can appear while operation
# set is unindexed
# duplicates not allowed

# use braces while creating set
vowels = {"a", "e", "i", "o", "u"}
print(type(vowels))
print(vowels)  # can display in any order, does not depend on order of insertion
# print(vowels[1]) # set is unindexed

# duplicate not allowed so ignored
animals = {"zebra", "lion", "tiger", "lion"}
print(len(animals))  # will be 3 as "lion" is twice
print(animals)  # display "lion" only once

# use of set constructor
s1 = set({"sagar", "simran", "sweata"})  # set creation
s2 = set((1, 2))  # tuple conversion
print(type(s1), s1, type(s2), s2)

x = {
    False,
    0,
    1,
    True,
}  # as False is evaluated as 0 and True as 1 they will be considered same.
print(
    x
)  # Any combination of True/1 and False/0, insertion order may be given preference (but as set is not ordered data structure, you can not certainly tell what is comming)
