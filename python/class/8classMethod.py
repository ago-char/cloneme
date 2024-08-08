# class method in py can be recognized by 2 keyword. 'cls'(first argument, this can be any name but it will refer to class, you can not use self) is used instead of 'self' and to say py, this is class method the decorator i.e @classmethod is used


class car:
    # static variable are defined outside class
    name = "Tesla"
    series = "T334"

    def __init__(self, model=2020, max_speed=200, gear=5) -> None:
        # thse are instance variable
        self.model = model
        self.max_speed = max_speed
        self.gear = gear

    # following is instance method
    def displayConfig(self):
        print(
            f"Name = {self.name} and Series = {self.series}\nModel = {self.model}, Maximum Speed = {self.max_speed}, Top Gear = {self.gear}"
        )

    # an obj of class car will call this method to get its model
    def getModel(self):
        return self.model

    @classmethod
    def changeName(cls, newName):
        cls.name = newName


c1 = car()
c2 = car()
c2.name = "BMW"
c3 = car()
print(c1.name, c2.name, c3.name)
# you can call using class name, first argc will be class name 'car' of type 'class'
car.changeName("ElonMusk")  # this is right
print(c1.name, c2.name, c3.name)
# you can not call using obj
# c1.changeName("FirstCAR") # this is wrong
