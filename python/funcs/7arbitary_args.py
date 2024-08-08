# If you do not know how many arguments that will be passed into your function, add a astick(*) before the parameter name in the function definition. This way the function will receive a tuple of arguments, and can access the items accordingly:


def fun(*args):
    print("Total args passed =", len(args))
    print(args)


fun("a", "e", "i", "o", "u")
fun(1, 5, 9, 43, 55, 34, 56, 66)
fun(["smarika", "nepal", "sukrabare"], 20, 4.5)

# Note: arbitary argument is often referred as *args in python deocumentation
