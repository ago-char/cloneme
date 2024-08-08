class bike:
    # init is special varibale for class which is generally use to solve the problem of initialization, pretty much similar like constructor of c++, as in cpp you may or may not list variables if the variable created at the time of init are only variables
    # so total 4 attributes of bike are set here, these are the only variables which can be accessed now
    def __init__(self, gear, diskBrake, disk_brake_N, max_speed):
        self.total_gears = gear
        if diskBrake:
            self.diskBrake = True
        else:
            self.diskBrake = False
        if self.diskBrake == True:
            self.disk_brake_N = disk_brake_N
        else:
            self.disk_brake_N = disk_brake_N
        self.maximum_speed = max_speed

    def sample_features(self):
        print(self.total_gears, self.diskBrake, self.disk_brake_N, self.maximum_speed)


b1 = bike(3, True, 2, 150)
b1.sample_features()
b1.diskBrake = False  # it is not good for data security
b1.sample_features()
