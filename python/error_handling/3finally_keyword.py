# finally exists on try-except block. try must be followed by either except or finally or both
# only one of try or except will get evaluated. Regardless of any block being executed, finally block always run

x = 5
try:
    print("I am try block. I run because 'x' exists and its value : ", x)
except NameError:
    print("Perhaps 'x' does not exist")
except:
    print("Maybe Value in 'x' is unprintable!")
finally:
    print("Regardless of anything. I am finally block and I must run..")

"""
use of finally:
1. closing the file after use 
2. opening/closing the connection regardless of func return 
"""

# finally does not seem worthy without function, because even if you write outside the try-except block, the same work can be done regardless of any of try-except block is evaluated. But maybe if you have to do same task time and again you may need to write too often this will produce long line of code. so, we will use function. In function even if function returns, it must run


def fun(x):
    try:
        if x > 0:
            return 1
        if x < 0:
            return -1
        if x == 0:
            return 0
    except:
        print("Maybe 'x' is not type 'int'...")
        return -2
    finally:
        print("I don't care....You have reached to 'finally' block.")


print(fun(5))
print(fun("string"))
