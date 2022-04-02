#Inner Class
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.Laptop()
    def show(self):
        print('Name :',self.name,'\nRollNo. =',self.roll)
        # self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand='Apple'
            self.cpu='M1'
        def show(self):
            print(self.brand,'\n',self.cpu)
s1=Student('Avi','085')
print(s1.lap.brand)
s1.show()
s1.lap.show()
#we can also create object of laptop outside by    * l1=Student.Laptop()  *
