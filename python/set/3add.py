# Once a set is created, you cannot change its items, but you can add new items.
f = {"apple", "mango", "orange", "banana"}
print(f)

# add new fruits using add method
f.add("litchi")
print(f)

# add any iterable i.e string,list,set,tuple using update method, as update takes any iterable not just set
mylist = ["graves", "guava"]
f.update(mylist)
print(f)
mytuple = "strawberry", "blueberry"
f.update(mytuple)
print(f)
