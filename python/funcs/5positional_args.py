# function with 2 default args and 1 required argument
def product(a, b=1, c=1):
    return a * b * c


"""
positional args refer to the place and order of argument, if you look at the function above, you will see:
1st arg is the positional arg for 'a'
2nd is for 'b'
3rd is for 'c'
You can not change this order (unless you pass keyword argument)
"""

# here 1st arg 7 is for 'a', 2nd arg 8 is for 'b' and 10 is for 'c'
print(product(7, 8, 10))

# here 1st arg 12 is for 'a', 2nd arg 14 is for 'b' and 3rd is not passed as it is not mandetory, default argc will be used. However 2nd was also not mandetory
print(product(12, 14))

# here 1st arg is for 'a' , 2nd and 3rd will take default arg
print(product(88))
