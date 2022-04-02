dic = {1001: 25575.0, 1002: 15500.0}


class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = 0
        self.__age = None
        self.__course_id = None
        self.__fees = None

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def get_age(self):
        return self.__age

    def get_course_id(self):
        return self.__course_id

    def get_fees(self):
        return self.__fees

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_marks(self, marks):
        self.__marks = marks

    def set_age(self, age):
        self.__age = age

    def validate_marks(self):
        if self.__marks >= 0 and self.__marks <= 100:
            return True
        else:
            return False

    def validate_age(self):
        if self.__age > 20:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            if self.__marks >= 65:
                return True
            else:
                return False
        else:
            return False

    def choose_course(self, course_id):
        if course_id in dic.keys():
            self.__course_id=course_id
            self.__fees=dic.get(course_id)
            if self.__marks > 85:
                self.__fees = self.__fees - ((25 * self.__fees) / 100)
            return True

        else:
            return False


maddy = Student()
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(65)
if (maddy.check_qualification()):
    print("Student has qualified")
    if (maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")