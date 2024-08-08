n1 = 12
n2 = 33

# while you do something with operator, remember behind the curtain it is calling some method for that particular type or class. Here 'a' and 'b' are of type <int>. So it is calling __add__() function or method for class int
n3 = n1 + n2


class cmplx:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __add__(self, another):
        temp = cmplx()
        temp.a = self.a + another.a
        temp.b = self.b + another.b
        return temp

    def __str__(self):
        string = str()
        if self.b >= 0:
            string = f"{self.a}i+{self.b}j"
        else:
            string = f"{self.a}i{self.b}j"
        return string

    def getRealPart(self):
        return self.a

    def getImaginaryPart(self):
        return self.b

    def displayNumber(self):
        if self.b >= 0:
            print(f"{self.a}i+{self.b}j")
        else:
            print(f"{self.a}i{self.b}j")


c1 = cmplx(8, -3)
c2 = cmplx(99, 33)
c3 = cmplx(-7, 34)

# but you can not add c1 and c2 or any of this cmplx type because type <cmplx> does not have __add__() method within, let's make one
# c4 = c1 + c2  # error

# now that it has __add__() method which will be invoked when you write '+'
c4 = c1 + c2  # implicitly it is c4=c1.__add__(c2)
c4.displayNumber()

# try using add method
c5 = c2.__add__(c3)
c5.displayNumber()

# when you print some obj, unseen part is that it is actually calling __str__ method so if you do it print(a) or print(a.__str__()), it is same.
a = "sargam"
print(a.__str__())
print(a)

# but it is not same for cmplx coz no __str__ is defined so
# either print(c1)
# or print(c1.__str__()) both wrong

# making it right creating __str__ function now
print(c1)
print(c1.__str__())
