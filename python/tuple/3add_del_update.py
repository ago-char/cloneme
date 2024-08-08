fruits = "watermellon", "strawberry", "avocado"
# since tuple does not support assignment, the only way to change tuple after creation is append another tuple to that tuple
fruits += ("apple",)
print(fruits)

# however there is a secondary way via list
# first convert tuple to list
f_list = list(fruits)
# do anything in list you want and convert it back to tuple
f_list.insert(0, "litchi")  # insertion
f_list.remove("watermellon")  # deletion
f_list.append("mango")  # adding/appending
# convert back
fruits = tuple(f_list)
print(fruits)

# you can not clear tuple but you can convert it to list and clear list and convert it back to tuple
f_list = list(fruits)
print(f_list)
f_list.clear()
fruits = tuple(f_list)

# however you can entirely delete tuple using del keyword
del fruits
# print(fruits) # ERROR uncomment to check
