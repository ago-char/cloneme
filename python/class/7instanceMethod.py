# instance method is method for instance or obj, which require object to get called and do it job. It uses self keyword to refer the caller obj
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


c1 = car()
# # you can not use class only to call instance method
# print(car.getModel())
# you have to pass object even if you call using clsas name
print(car.getModel(c1))
# so better call using object
print(c1.getModel())
