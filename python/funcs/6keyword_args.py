# function with 2 default args and 1 required argument
def product(a, b=1, c=1):
    return a * b * c


"""
positional args refer to the place and order of argument, if you look at the function above, you will see:
1st arg is the positional arg for 'a'
2nd is for 'b'
3rd is for 'c'
You can not change this order (unless you pass keyword argument)
If you wish to change this order you have to pass keyword argument but remember you can not pass any positional argument after you pass keyword argument coz keyword argument is for certain variable in funcion, mind one thing that while providing keyword argument you need to know variable name of the function definition, you can not pass keyword argument without knowing it.
"""

# simple order i.e positional argument
print(product(8, 8, 10))

# if you want to pass 'b' first then: you simply can't here in this case because no. of required argument is 1, well providing 'b' argument will match that requirement but the required argument is positional argument for 'a', so you can't
# print(product(b=32)) # ERROR

# pass 'c' before 'b': 1st is for 'a' which is mandetory, 2nd goes for 'c' as keyword argument, you can omit 3rd argument (in this case if omitted the default value of 'b' will be evaluated)
print(product(12, c=2))

# if you wanna pass 2nd as 'c' and 3rd as 'b', both will be keyword argument because 3rd is the positional arg for 'c' which is already passed at 2nd and remember the rule that you are not allowd to pass positional arg after keyword arg
print(product(14, c=2, b=10))
