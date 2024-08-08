"""
Syntax of function
def func_name([parameter[s]]):
    statement[s]
"""


# a simple function to print sum of 2 numbers, this is func definition
def sum(a, b):
    print("Sum of", a, "and", b, "is", a + b)


x = int(input("First Number : "))
y = int(input("Second Number : "))

# this is function call
sum(x, y)

print("End......")
