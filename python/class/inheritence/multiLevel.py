# such inheritence where B inherits A, C inherits B and so on. This can be called as single inhertence at multi level or perhaps at hierarchical level
class A:
    def featureA(self):
        print("Feature of A")

    def feat(self):
        print("FeatA")


class B(A):
    def featureB(self):
        print("Feature of B")

    def feat(self):
        print("FeatB")


class C(B):
    def featureC(self):
        print("Feature of C")

    def feat(self):
        print("FeatC")


c1 = C()
c1.featureA()
c1.featureB()
c1.featureC()
c1.feat()
