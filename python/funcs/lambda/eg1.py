# lambda is function in python without name
# syntax for python lambda expression/function
# lambda argument[s]:expression
x = lambda a, b: a + b  # lambda function assigned to 'x'
print(type(x))  # type will be <class 'function'>
print(
    x(1, 5)
)  # now it can be called with 'x', as it takes 2 args mentioned above, 2 args are passed
y = x  # now same function is referred by y
print(x is y)  # check if 'x' and 'y' are referring to same obj
print(y(6, 9))  # as y is now same as x you can call lambda using 'y'

# Note: You can have multiple arguments in python lambda but the expression is only one
