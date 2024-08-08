# syntax of list (are created inside big brackets)
list1 = ["sagar", "shreya", "simran"]

# list can be created using list constructor, notice double braces
list2 = list((1, 5, 7, 0))

# list are ordered meaning that order does not change, it will be printed and manipulated on the order of insertion
print("List1 :", list1, "\nList2 :", list2)

# list are indexed starting from 0. as they are indexed duplicates are allowed and even differenct data types are allowd
list3 = ["SmarikaNepal", 20, "Sukrabare", 4.5, 20]  # 20 is at 1 and 4 index
print("List3 :", list3)

# type of list is <class 'list'> i.e From Python's perspective, lists are defined as objects with the data type 'list'
print("Type of List1, List2, and List3 :", type(list1))

# length of list
print("Length of list1 is :", len(list1))

# The list is changeable (can use assignment operator too which is not in case of tuple infact), meaning that we can change, add, and remove items in a list after it has been created. We will see this in next chapters.
