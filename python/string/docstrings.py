def my_function():
    " " "Demonstrates triple double quotes docstrings and does nothing really" " "
    return None


def hello(a, b):
    """
    Doing Time Pass
    """
    return None


print("Using __doc__:")
print(my_function.__doc__)
input()
print("Using help:")
help(my_function)

# print(hello.__doc__)
# help(hello)
