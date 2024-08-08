# in multiple inheritence, one child can have 2 or more parents
class p1:
    def __init__(self) -> None:
        print("p1 init")

    def displayHello(self):
        print("Printing Hello from parent1..........")
        print("Hello")


class p2:
    def __init__(self) -> None:
        print("p2 init")

    def displayHello(self):
        print("Printing Hello from parent2..........")
        print("Hello")


class child(p1, p2):
    # Rule1
    # if no init is defined, init of parent will run but which parent ? Look at the () the order is left to right, here (p1,p2) means p1 first and then only p2. so init of p1 will run if it has else p2
    def __init__(self) -> None:
        # super is use to invoke parent class but which ? Remember Rule1
        super().__init__()
        print("INIT OF child")

        # Rule1 is not only for init but for all methods

    def info(self):
        print("I am info in child")


c1 = child()
c1.info()
c1.displayHello()
