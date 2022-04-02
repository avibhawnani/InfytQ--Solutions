#Inheritance : Single level , Multi Level , Multiple , Hybrid
class A:
    def __init__(self):
        print("In A init")

    def feat1(self):
        print("In Feature1 A")
    def feat2(self):
        print("In Feature2 A")

class B:
    def __init__(self):
        print("In B init")

    def feat2(self):
        print("In Feature2 B")

    def feat4(self):
        print("In Feature4 B")

class C (A,B):
    def __init__(self):
        super().__init__()                          #calling parent class constructor .  A init is called because of MRO (Method Resolution Order)
        print("in C init")
c1=C()
print(c1.feat2())




