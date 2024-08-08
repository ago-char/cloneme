# remove,discard,pop,clear,del
animals = {"tiger", "cow", "buffalo", "lion", "rhino", "deer", "goat"}
print(animals)

# use remove method to delete specific item, as remove method raises error it item is not find better use with if clause
if "goat" in animals:
    animals.remove("goat")
    print("'goat' is removed")
else:
    print("'goat' is not in set.")
print(animals)

# get rid of if else using discard method as it does not throw error even if item not found, but this also can be drawback as you will not know if given item is removed or not. use if statement as per your requirement
animals.discard("sheep")

# use pop method to remove random item, pop will return what it removes so it is easy to know what happens
x = {""}  # set of size 1, if x={} it would have been empty dict
print(type(x), len(x))
y = x.pop()
print(type(y))
y = animals.pop()
print(y)
print(animals)
