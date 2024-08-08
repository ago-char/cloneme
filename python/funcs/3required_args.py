# required args are those args in func which are mandetory to pass while function call, so that function can be called


# In the following function 'product' all 'a','b',and 'c' are required arguments because none of them were defined as default argc, so this function need all 3 parameters to get passed in order to execute
def product(a, b, c):
    return a * b * c


# p = product(3, 5)  # wrong because no. of required argcs is 3
p = product(3, 5, 7)  # correct as it matches no. of req args i.e 3
print(p)
