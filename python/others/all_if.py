# using if condition
num = int(input("Enter a number: "))
if num > 0:
    print("Number: ", num, "is greater than 0.")

# using if else
if num == 0:
    print("Number: ", num, "is 0.")
else:
    print("Number: ", num, "is non-zero.")

# using elif

if num < 0:
    print("Number: ", num, "is NEGATIVE.")
elif num > 0:
    print("Number: ", num, "is POSITIVE.")
else:
    print("Number: ", num, "is ZERO.")


# using nested elif/ifelse
num = 18
if num < 0:
    print("Number is negative.")
elif num > 0:
    if num <= 10:
        print("Number is between 1-10.")
    elif num <= 20:
        print("Number is between 10-20.")
    else:
        print("Number is greater than 20.")
else:
    print("Number is 0.")
