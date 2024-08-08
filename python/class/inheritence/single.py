# in single inheritence, child will have only one parent
class parent:
    def __init__(self) -> None:
        print("INIT of parent class")

    def info(self):
        print("This is info inside parent")


class child(parent):
    def __init__(self) -> None:
        print("INIT of child class")

    def info(self):
        print("This is Info inside child class")


p1 = parent()
c1 = child()

# c1 has 2 version of info first it will look at own class if found execute it, if not search in parent class and execute else raiseError
c1.info()
