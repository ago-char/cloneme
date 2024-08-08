# variable inside init are instance variable, as they require instance of object to get accessed, modified, they are called instance variblae
class car:
    def __init__(self, model, max_speed, gear) -> None:
        # thse are instance variable
        self.model = model
        self.max_speed = max_speed
        self.gear = gear

    def displayConfig(self):
        print(
            f"Model = {self.model}, Maximum Speed = {self.max_speed}, Top Gear = {self.gear}"
        )


c1 = car(2020, 200, 5)
c1.displayConfig()
# instance variable can be accessed with instance of obj
c1.model = 2022
c1.gear = 6
c1.displayConfig()
