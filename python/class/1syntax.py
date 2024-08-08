class bike:
    def sample_features(self):
        print("150cc, Double Disk, Tubeless Tyre")


# define variable that is of type bike
b1 = bike()
# verify the type
print(type(b1))
# call the sample features
bike.sample_features(b1)
# can be called as such too
b1.sample_features()  # this will ultimately be represented as: bike.sample_features(b1)
