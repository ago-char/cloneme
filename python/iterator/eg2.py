"""
default color combination for variables were:
forgback #D4D4D4#1E1E1E
"""

# s = "rams"
# myiter = s.__iter__()
# print(myiter.__next__)


class myNum:
    def __init__(self):
        self.a = 1

    def __iter__(self):
        return self

    def __next__(self):
        var, self.a = self.a, self.a + 1
        return var


num = myNum()
myiter = num.__iter__()
print(num.__next__())
num.a = 5
print(num.__next__())
print(num.__next__())
