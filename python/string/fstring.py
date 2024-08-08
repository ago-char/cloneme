# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

# f-string and variable
kids = 7
print(f"Nilam has {kids} kids.")

# f-string and modifier. A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
marks = 93.2285
print(f"Anjana scored {marks:.2f}, no doubt she is a brilient talent in the college.")

# f-string and operations
usd = 50000
print(
    f"{usd}$ is NRS {usd*133.6:.2f}"
)  # multiplication operation, multiple placeholders used


# f-string and functions
def sum(a, b):
    return a + b


x = 19
y = 10
print(f"Sum of {x} and {y} is {sum(x,y)}.")

# Note: make sure you are python version 3.6 or later
