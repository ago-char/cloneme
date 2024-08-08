# let me light up why 'self' is required
class house:
    # # this is init without self, you can not initilise and variable, the purpose of init is to set properties for class, so if there will not be any kind of variable how to store the properties of class. Well if the only intention of init is to print something then you can do without passing anything to it but again you can not call it with obj
    # def __init__() -> None:
    #     area = 1000
    #     rooms = 6
    #     isTrustPresent = False
    #     isLowerBalcony = True

    # init just doing printing stuff.. very rare and not more useful
    # def __init__():
    #     print("I am init\n")

    # this is init with self
    def __init__(self) -> None:
        self.area = 1000
        self.rooms = 6
        self.isTrustPresent = False
        self.isLowerBalcony = True


# if you just wanna print stuff
# house.__init__()
# create 'h1' the obj for class 'house'
h1 = house()
