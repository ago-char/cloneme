# method that is inside the class but actually does not care about any object or class itself meaning require nothing to access but need to define using decorator @staticmethod
class school:
    name = "National Crush School"
    location = "Ithari-07,Sunsari,Nepal"
    owner = "Anjana Subedi"
    founder = "Smarika Nepal"
    inverstors = ["Yunisha Karki", "Deepika Pokheral", "Deepa Subedi"]

    def __init__(self):
        self.studentNumber = 900
        self.Level = "Secondary"
        self.teacherNumber = 50
        self.Medium = ("English", "Nepali")

    def getTotalStudents(self):
        return self.studentNumber

    def getTotalTeachers(self):
        return self.teacherNumber

    @classmethod
    def getInfo(cls):
        print(
            f"School Name = {cls.name}\nLocation = {cls.location}\nOwner = {cls.owner}\nFounder = {cls.founder}\nInverstors = {cls.inverstors}"
        )

    @staticmethod
    def infoSchool():
        print("Class = school")


c1 = school()
# call instance method
print(c1.getTotalStudents())
# call class method
school.getInfo()
# use obj to all static method
c1.infoSchool()
# use class name to call static method
school.infoSchool()
