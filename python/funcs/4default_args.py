# a simple rule while giving default args is that you are only allowed to set default argument if it's right args is default unless it is for last argument because it is the rightmost

# def sum(a=1,b) # error because right of 'a' i.e 'b' is non default
# def add(a,b=0,c=0) # correct because right of 'b' is 'c' which is a default argument, for 'c' there can not be default args at right because it is itself rightmost argc

"""
Here product function is defined with 3 default args,So:
if no argument is passed --> a=1,b=1,c=2
if one args is passed(which if is not keyword argument) --> a=arg1,b=1,c=1
if two args are passed(which if are not keyword argument) --> a=arg1,b=arg2,c=1
if three args are passed(which are not keyword argument) --> a=arg1,b=arg2,c=arg3
 """


# function with 3 default args
def product(a=1, b=1, c=1):
    return a * b * c


x = 5
y = 10
z = 15
print("No args :", product())
print(x, "Only :", product(x))
print(x, "and", y, ": ", product(x, y))
print(x, ",", y, ", and", z, ": ", product(x, y, z))
print("..............\n")
