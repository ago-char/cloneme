"""
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first (occurance) element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value 
reverse()	Reverses the order of the list
sort()	Sorts the list (always use key function)
"""

# As we have already use all of those let me use count once
# just generating random list of 1,2,3
l = [x % 4 for x in range(100, 0, -1) if x > 22 and x % 4 != 0]
print("\nOur List 'l' :\n")
print(l)
print("\n'1' in list :", l.count(1), "times.")
print("\n'2' in list :", l.count(2), "times.")
print("\n'3' in list :", l.count(3), "times.")
