# constructor is actually init which provides shape to the class
class house:
    # init constructor
    # this will set some defaults, this will provide the model of the class 'house' about what attributs will be on the house, the variables named inside init are actually the properties or overview of the 'house' or class 'house'
    def __init__(self):
        self.rooms = 4
        self.passage = False
        self.Trust = False
        self.Area = 1000  # in sq.ft
        self.LowerBalcony = 100  # in sq.ft
        self.height = 12  # in m

    # instance method to print the model
    def model(self):
        print(
            self.rooms,
            self.passage,
            self.Trust,
            self.Area,
            self.LowerBalcony,
            self.height,
        )


h1 = house()
house.model(h1)
