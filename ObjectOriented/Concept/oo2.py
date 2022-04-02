#Types of methods : 1. Instance Methods 2. Class Methods  3. Static Methods
class Students:
    school='MMS'                               #class Variable/Static Variable

    def __init__(self,m1,m2,m3):                #Constructor
        self.m1=m1
        self.m2 = m2                            #Instance Variable
        self.m3 = m3

    def get_m1(self):                           #Accessors
        return self.m1

    def set_m1(self,f):                         #Mutators
        self.m1=f

    def avg(self):                              #Instance Methods
        return (self.m1+self.m2+self.m3)/3

    @classmethod                                #Decorators- Class Decorator
    def getSchool(cls):                              #class Methods
        return cls.school

    @staticmethod                                #static Decorator
    def info():                                 #static Method
        print('This is Student Template')



s1=Students(34,56,78)
print(Students.getSchool())