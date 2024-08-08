# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition. This way the function will receive a dictionary of arguments, and can access the items accordingly:


def fun(**kargs):
    print("\n    Key Value Pairs\n.........................\n")
    for key, value in kargs.items():
        print(key, "----->", value)


# fun(1, 3, 5, 6, 2, 2) # can not call like this because it taks no positional value all keyword value are taken
# pass argument as key=value pair and they will be interpreted as dictionay like we have read that the dictinary is key:value pair in previous chapters
fun(Fname="Smarika", Lname="Nepal", Age=20, Height=4.5, Home="Sukrabare")
