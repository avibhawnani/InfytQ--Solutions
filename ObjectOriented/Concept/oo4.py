#__repr__() and __str__() function :
class Car:
    def __init__(self):
        self.name="BMW"
        self.color='Blue'
    def __str__(self):
        s="Name: {} Color :{}".format(self.name,self.color)
        return s
    # def __repr__(self):
    #     return "Hello Repr"
c1=Car()
print(c1)