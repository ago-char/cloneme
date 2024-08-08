# any() is a built-in Python function that returns True if at least one element of an iterable (such as a list, tuple, or any other iterable object) evaluates to True. If all elements evaluate to False or if the iterable is empty, any() returns False.

# Example 1
list1 = [False, True, False, False]
print(any(list1))  # Output: True, because at least one element (True) is True

# Example 2
list2 = [0, "", None, False]
print(any(list2))  # Output: False, because all elements are false

# Example 3
list3 = [0, "", None, False, True]
print(any(list3))  # Output: True, because at least one element (True) is True
