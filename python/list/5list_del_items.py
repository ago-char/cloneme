list1 = ["apple", "mango", "orange"]
print(list1)
# delete at specified index using pop method
list1.pop(1)
print(list1, "\n...........................................\n")

list1 = ["banana", "pear", "pineapple"]
print(list1)
# delete at last index with no argc in pop
list1.pop()
print(list1, "\n...........................................\n")

list1 = ["apple", "mango", "orange", "banana", "pear", "mango"]
print(list1)
# delete specific element using remove method, if multiple occurence are present, delete first one
list1.remove("mango")
print(list1, "\n...........................................\n")

list1 = ["graves", "guava", "litchi", "watermelon"]
print(list1)
# delete at specified index using del keyword
del list1[1]
print(list1, "\n...........................................\n")

list1 = ["watermelon", "strawberry", "avocado", "pineapple"]
print(list1)
# clear entire list but not delete completely i.e list exists but has no elements on it i.e empty list using clear method
list1.clear()
print(list1, "\n...........................................\n")

list1 = ["apple", "mango", "orange", "graves", "guava"]
print(list1)
# delete entire list using del keyword meaning list will get destroyed, you can no print now it will throw ValueError
del list1
# remove/comment following line to discard error
# print("\nReady For Error :")
# print(list1, "\n...........................................\n")
