# import only onlyInt and scanInt functions from integer
from integer import onlyInt, scanInt

# use this if you want to import all functions use *
# from integer import *
from math import pow

# num = onlyInt.keepAskingInt("num: ", True)
onlyInt()
x = scanInt("Enter a number to find square of : ")
print(pow(x, 2))
