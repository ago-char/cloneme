# use try--except if you are uncertain that some piece of code may raise some error, but even if error occured the rest of code must be evaluated and executed
x = {"Sagar"}
# you don't know what is inside 'x' but you want it to be multiply by 2, so lets use try--except
print("\n\n\nPrinting Explicit Error defined by programmer ::\n")
try:
    print(x * 2)
except:
    print(f"{type(x)} can not be multiplyed.")

print("............................................................")

print("Rather printing Implicit Error using 'Exception' class :\n")
try:
    print(x * 2)
except Exception as error:
    print(error)

print("............................................................")


print("Rather printing Implicit Error using 'BaseException' class :\n")
try:
    print(x * 2)
except BaseException as error:
    print(error)

print("............................................................")

print("This time no Error :\n")
try:
    x.add("Shivam")
    print(x)
except Exception as error:
    print(error)

print("\n\n")
