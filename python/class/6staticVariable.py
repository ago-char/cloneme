# static variable are class varibale, meaning they do not require any obj, they will remain same for any object for the class, but the value may differ, meaning they are  created just once but can hold multiple value


class car:
    # static variable are defined outside class
    name = "Tesla"
    series = "T334"

    def __init__(self, model=2020, max_speed=200, gear=5) -> None:
        # thse are instance variable
        self.model = model
        self.max_speed = max_speed
        self.gear = gear

    def displayConfig(self):
        print(
            f"Name = {self.name} and Series = {self.series}\nModel = {self.model}, Maximum Speed = {self.max_speed}, Top Gear = {self.gear}"
        )


c1 = car()
c2 = car()
c3 = car()
# you can access static varibales
print(c1.name, c2.name, c3.name)
# you can change value of static varibale for an object, this wil not change for another
c1.name = "sagar"
print(c1.name, c2.name, c3.name)
# to change static variable value for all obj(except to which it is explicitly modified, in this case it will change name for c2 and c3 but not for c1 as name for c1 is explicitly modified at line numberr 27) use class instead of obj
car.name = "Marcedes"
print(c1.name, c2.name, c3.name)
